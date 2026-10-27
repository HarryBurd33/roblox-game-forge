"""Temp-fixture tests of the offline publication validator, using stdlib only."""

import csv
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
SPEC = importlib.util.spec_from_file_location("publication_validate", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.skill = self.root / "skills" / validator.SKILL_NAME
        (self.skill / "templates").mkdir(parents=True)
        self.license = "MIT License\n\nCopyright (c) 2026 Test contributors\n\n" + validator.MIT_BODY + "\n"
        (self.root / "LICENSE").write_text(self.license)
        (self.skill / "LICENSE").write_text(self.license)
        (self.root / "README.md").write_text("# Fixture\n\n[Skill](skills/roblox-game-forge/SKILL.md)\n")
        (self.skill / "SKILL.md").write_text(
            "---\nname: roblox-game-forge\ndescription: A fixture skill for structural checks.\nlicense: MIT\n---\n\n# Fixture\n"
        )
        output = io.StringIO()
        csv.writer(output, lineterminator="\n").writerow(validator.INVENTORY_HEADER)
        (self.skill / "templates" / "asset-inventory.csv").write_text(output.getvalue())

    def assert_invalid(self, phrase):
        with self.assertRaisesRegex(ValueError, phrase):
            validator.validate(self.root)

    def test_valid_fixture(self):
        result = validator.validate(self.root)
        self.assertTrue(result["ok"])
        self.assertEqual(result["internal_links_checked"], 1)

    def test_broken_internal_link(self):
        (self.root / "README.md").write_text("[Missing](docs/missing.md)\n")
        self.assert_invalid("Broken resource link")

    def test_relative_parent_link_and_external_url(self):
        (self.root / "docs").mkdir()
        (self.root / "docs" / "guide.md").write_text("[Root](../README.md) [Web](https://example.invalid/unknown)\n")
        self.assertEqual(validator.validate(self.root)["internal_links_checked"], 2)

    def test_resource_escape_rejected(self):
        (self.root / "README.md").write_text("[Outside](../outside.md)\n")
        self.assert_invalid("escapes repository")

    def test_missing_mit_license(self):
        (self.root / "LICENSE").unlink()
        self.assert_invalid("Missing root or skill MIT")

    def test_truncated_mit_rejected(self):
        (self.root / "LICENSE").write_text("MIT License\nCopyright (c) 2026 Test\nPermission is hereby granted, truncated\n")
        self.assert_invalid("complete MIT")

    def test_license_mismatch_rejected(self):
        (self.skill / "LICENSE").write_text(self.license.replace("Test contributors", "Different contributors"))
        self.assert_invalid("texts must match")

    def test_mismatched_metadata_name(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text().replace("name: roblox-game-forge", "name: wrong-name"))
        self.assert_invalid("name must match folder")

    def test_missing_expected_folder(self):
        self.skill.rename(self.skill.with_name("wrong-folder"))
        self.assert_invalid("Missing skills")

    def test_malformed_csv_width(self):
        (self.root / "other.csv").write_text("name,status\nonly-one\n")
        self.assert_invalid("Inconsistent CSV")

    def test_inventory_sample_asset_rejected(self):
        path = self.skill / "templates" / "asset-inventory.csv"
        with path.open("a", newline="") as handle:
            csv.writer(handle).writerow(["illustrative-asset"] + [""] * (len(validator.INVENTORY_HEADER) - 1))
        self.assert_invalid("must have no asset rows")

    def test_private_file_rejected(self):
        (self.root / ".checkpoint").mkdir()
        (self.root / ".checkpoint" / "state.json").write_text("{}")
        self.assert_invalid("Private directory")

    def test_raw_response_file_rejected(self):
        (self.root / "baseline-responses.json").write_text("[]")
        self.assert_invalid("Raw model response")

    def test_git_and_cache_internals_are_not_scanned(self):
        for name in (".git", "__pycache__"):
            path = self.root / name
            path.mkdir()
            (path / "not-public").write_bytes(b"\x00\xff")
        self.assertTrue(validator.validate(self.root)["ok"])

    def test_worktree_git_pointer_is_not_scanned(self):
        (self.root / ".git").write_text("gitdir: /Users/" + "private-person/repo/worktrees/a")
        self.assertTrue(validator.validate(self.root)["ok"])

    def test_home_path_rejected(self):
        (self.root / "private.md").write_text("/Users/" + "private-person/work.txt")
        self.assert_invalid("user home path")

    def test_credential_pattern_rejected_without_echoing_value(self):
        credential = "ghp_" + "A" * 40
        (self.root / "private.md").write_text(credential)
        try:
            validator.validate(self.root)
        except ValueError as error:
            self.assertIn("credential", str(error))
            self.assertNotIn(credential, str(error))
        else:
            self.fail("Expected credential detection")

    def test_symlink_rejected(self):
        try:
            (self.root / "linked.md").symlink_to(self.root / "README.md")
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable on this platform")
        self.assert_invalid("Symlink")

    def test_reference_and_encoded_links(self):
        (self.root / "a file.md").write_text("# Content\n")
        (self.root / "README.md").write_text("[One](a%20file.md#content)\n\n[Two][ref]\n\n[ref]: <a file.md>\n")
        self.assertEqual(validator.validate(self.root)["internal_links_checked"], 2)


if __name__ == "__main__":
    unittest.main()
