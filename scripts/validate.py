#!/usr/bin/env python3
"""Offline structural checks for this repository; no model or Studio execution.

Run ``python3 scripts/validate.py [REPOSITORY_ROOT]``. Pattern-based privacy
checks catch common accidental disclosures; they cannot certify arbitrary text
or prove gameplay, model behavior, asset rights, or native skill discovery.
"""

import argparse
import csv
import io
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


SKILL_NAME = "roblox-game-forge"
INVENTORY_HEADER = [
    "asset_key", "name", "role", "status", "source_kind", "source_url_or_path",
    "creator", "roblox_asset_id", "rights_basis", "rights_checked_at",
    "cost_status", "upload_authorized", "import_format", "import_status",
    "studio_target_path", "technical_checks", "notes",
]
MIT_BODY = '''Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

PRIVATE_COMPONENTS = {
    ".checkpoint", ".forge", ".env", ".aws", ".ssh", "raw-model-output",
    "raw-model-outputs", "raw-responses", "model-responses", "raw-logs",
}
RAW_RESPONSE_NAMES = {
    "baseline-responses.json", "candidate-responses.json", "model-responses.json",
    "execution-inputs.json", "raw-model-outputs.json", "raw-model-output.json",
}
PRIVATE_TEXT = [
    ("user home path", re.compile(r"/(?:Users|home)/[^/\s`\"'<>]+")),
    ("Windows user home path", re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s`\"'<>]+")),
    ("API credential", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("GitHub credential", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("Slack credential", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{15,}\b")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _normalized(text):
    return " ".join(text.split())


def _metadata(text):
    lines = text.splitlines()
    _require(bool(lines) and lines[0] == "---", "SKILL.md needs YAML front matter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("SKILL.md front matter is not closed") from None
    fields = {}
    for line in lines[1:end]:
        match = re.match(r"^(name|description|license):\s*(.*?)\s*$", line)
        if not match:
            continue
        key, value = match.groups()
        _require(key not in fields, "Duplicate metadata field: " + key)
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except (ValueError, TypeError):
                raise ValueError("Invalid quoted metadata field: " + key) from None
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        _require(isinstance(value, str), "Metadata must contain text: " + key)
        fields[key] = value
    _require(fields.get("name") == SKILL_NAME, "Skill metadata name must match folder " + SKILL_NAME)
    _require(1 <= len(fields.get("description", "")) <= 1024,
             "Skill description must contain 1–1024 characters")
    _require(fields.get("description") not in ("|", ">", "|-", ">-"),
             "Use a single-line description for this offline metadata check")
    _require(fields.get("license") == "MIT", "Skill metadata license must be MIT")
    return fields


def _files(root):
    for directory, subdirs, filenames in os.walk(str(root), followlinks=False):
        parent = Path(directory)
        for name in list(subdirs):
            path = parent / name
            _require(not path.is_symlink(), "Symlink is not allowed: " + str(path.relative_to(root)))
            if name in {".git", "__pycache__"}:
                subdirs.remove(name)
                continue
            _require(name not in PRIVATE_COMPONENTS, "Private directory is not allowed: " + str(path.relative_to(root)))
        for name in sorted(filenames):
            if name == ".git":
                # Worktrees use a Git administrative pointer file, not a folder.
                continue
            path = parent / name
            relative = path.relative_to(root)
            _require(not path.is_symlink(), "Symlink is not allowed: " + str(relative))
            _require(not any(part in PRIVATE_COMPONENTS for part in relative.parts),
                     "Private file is not allowed: " + str(relative))
            _require(not name.startswith(".env."), "Environment file is not allowed: " + str(relative))
            _require(name not in RAW_RESPONSE_NAMES and not name.lower().startswith("raw-model-"),
                     "Raw model response file is not allowed: " + str(relative))
            _require(name not in {".DS_Store", "credentials.json", "auth.json"},
                     "Private machine file is not allowed: " + str(relative))
            yield path


def _link_targets(text):
    # Ignore fenced code examples; their illustrative links are not resources.
    cleaned = re.sub(r"(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", text)
    for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^)\n]+)\)", cleaned):
        raw = match.group(1).strip()
        yield raw[1:raw.index(">")] if raw.startswith("<") else raw.split()[0]
    for match in re.finditer(r"(?m)^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", cleaned):
        raw = match.group(1)
        yield raw[1:-1] if raw.startswith("<") else raw


def _check_links(path, root, text):
    count = 0
    for target in _link_targets(text):
        if target.startswith("#"):
            continue
        parsed = urlsplit(target)
        if parsed.scheme in {"https", "http", "mailto"} or target.startswith("//"):
            continue
        _require(not parsed.scheme and not target.startswith("/"),
                 "Unsupported/absolute resource link in " + str(path.relative_to(root)))
        local = unquote(parsed.path)
        if not local:
            continue
        destination = (path.parent / local).resolve()
        try:
            destination.relative_to(root)
        except ValueError:
            raise ValueError("Resource link escapes repository: " + str(path.relative_to(root))) from None
        _require(destination.exists(), "Broken resource link in " + str(path.relative_to(root)) + ": " + local)
        count += 1
    return count


def validate(root):
    """Return structural counts, or raise ValueError with a bounded diagnostic."""
    root = Path(root).resolve()
    _require(root.is_dir(), "Repository root does not exist")
    skill = root / "skills" / SKILL_NAME
    _require((skill / "SKILL.md").is_file(), "Missing skills/" + SKILL_NAME + "/SKILL.md")
    files = list(_files(root))
    texts = {}
    links = 0
    for path in files:
        relative = path.relative_to(root)
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            raise ValueError("Cannot inspect published text file: " + str(relative)) from None
        texts[path] = text
        for label, pattern in PRIVATE_TEXT:
            _require(not pattern.search(text), "Possible " + label + " in " + str(relative))
        if path.name == "SKILL.md":
            _require(path == skill / "SKILL.md", "Unexpected skill root: " + str(relative))
        if path.suffix.lower() == ".md":
            links += _check_links(path, root, text)
        if path.suffix.lower() == ".csv":
            try:
                rows = list(csv.reader(io.StringIO(text), strict=True))
            except csv.Error:
                raise ValueError("Malformed CSV: " + str(relative)) from None
            _require(bool(rows) and bool(rows[0]) and len(set(rows[0])) == len(rows[0]),
                     "CSV needs a unique nonempty header: " + str(relative))
            _require(all(len(row) == len(rows[0]) for row in rows),
                     "Inconsistent CSV row width: " + str(relative))
            if path.name == "asset-inventory.csv":
                _require(rows[0] == INVENTORY_HEADER, "Asset inventory header differs from template contract")
                _require(len(rows) == 1, "Public asset inventory template must have no asset rows")
    metadata = _metadata(texts[skill / "SKILL.md"])
    _require((root / "README.md") in texts, "Missing root README.md")
    license_path = root / "LICENSE"
    skill_license = skill / "LICENSE"
    _require(license_path in texts and skill_license in texts, "Missing root or skill MIT LICENSE")
    license_text = texts[license_path]
    _require(license_text.startswith("MIT License\n"), "Root LICENSE must identify MIT")
    _require(bool(re.search(r"(?m)^Copyright .+", license_text)), "MIT LICENSE needs copyright attribution")
    position = license_text.find("Permission is hereby granted,")
    _require(position >= 0 and _normalized(license_text[position:]) == _normalized(MIT_BODY),
             "Root LICENSE must contain the complete MIT text")
    _require(_normalized(license_text) == _normalized(texts[skill_license]),
             "Root and skill MIT LICENSE texts must match")
    _require((skill / "templates" / "asset-inventory.csv") in texts,
             "Missing asset inventory template")
    return {"ok": True, "scope": "offline static checks only", "skill": metadata["name"],
            "files_checked": len(files), "internal_links_checked": links}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    try:
        result = validate(args.root)
    except (ValueError, OSError) as error:
        parser.exit(1, "validation failed: " + str(error) + "\n")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
