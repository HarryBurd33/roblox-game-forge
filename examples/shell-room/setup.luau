-- Original disposable Studio fixture. NOT yet live-tested; see README.md.
-- Execute in the verified disposable place's Edit context. Creates only owned names.
local RunService = game:GetService("RunService")
assert(RunService:IsStudio() and not RunService:IsRunning(), "Run in Studio Edit mode")
local SSS = game:GetService("ServerScriptService")
local RS = game:GetService("ReplicatedStorage")
local SPS = game:GetService("StarterPlayer"):WaitForChild("StarterPlayerScripts")
for _, item in ipairs({{workspace, "GameForgeSmoke"}, {SSS, "GameForgeSmokeServer"},
    {RS, "GameForgeSmokeRestart"}, {SPS, "GameForgeSmokeClient"}}) do
    assert(not item[1]:FindFirstChild(item[2]), "Owned fixture name exists; inspect before replacing: " .. item[2])
end
local root = Instance.new("Folder")
root.Name = "GameForgeSmoke"
root.Parent = workspace
local function part(name, size, position, color)
    local p = Instance.new("Part")
    p.Name, p.Size, p.Position = name, size, position
    p.Color, p.Anchored = color, true
    p.Parent = root
    return p
end
part("Floor", Vector3.new(40, 1, 32), Vector3.new(0, 0, 0), Color3.fromRGB(90, 140, 150))
local spawn = Instance.new("SpawnLocation")
spawn.Name, spawn.Size, spawn.Position = "Spawn", Vector3.new(6, 1, 6), Vector3.new(0, 1, 12)
spawn.Anchored, spawn.Neutral, spawn.Parent = true, true, root
local shell = part("Shell", Vector3.new(2, 2, 2), Vector3.new(0, 2, 0), Color3.fromRGB(255, 210, 65))
shell.Shape = Enum.PartType.Ball
local boat = part("Boat", Vector3.new(5, 2, 4), Vector3.new(10, 1.5, 0), Color3.fromRGB(80, 210, 120))
local function prompt(parent, action)
    local p = Instance.new("ProximityPrompt")
    p.ActionText, p.ObjectText, p.HoldDuration = action, parent.Name, 0
    p.MaxActivationDistance, p.RequiresLineOfSight = 8, false
    p.Parent = parent
end
prompt(shell, "Collect shell")
prompt(boat, "Deposit shell")
local restart = Instance.new("RemoteEvent")
restart.Name, restart.Parent = "GameForgeSmokeRestart", RS
local server = Instance.new("Script")
server.Name = "GameForgeSmokeServer"
server.Source = [==[
local Players = game:GetService("Players")
local root = workspace:WaitForChild("GameForgeSmoke")
local restart = game:GetService("ReplicatedStorage"):WaitForChild("GameForgeSmokeRestart")
local lastReset = {}
local function reset(player)
    player:SetAttribute("ForgeCollected", false)
    player:SetAttribute("ForgeWon", false)
    player:SetAttribute("ForgeAwards", 0)
    player:SetAttribute("ForgeLastAction", "Restarted")
end
local function near(player, target)
    local char = player.Character
    local body = char and char:FindFirstChild("HumanoidRootPart")
    local humanoid = char and char:FindFirstChildOfClass("Humanoid")
    return body and humanoid and humanoid.Health > 0 and (body.Position - target.Position).Magnitude <= 12
end
local function joined(player)
    reset(player)
    player.CharacterAdded:Connect(function() reset(player) end)
end
Players.PlayerAdded:Connect(joined)
for _, player in ipairs(Players:GetPlayers()) do joined(player) end
Players.PlayerRemoving:Connect(function(player) lastReset[player] = nil end)
root.Shell.ProximityPrompt.Triggered:Connect(function(player)
    if not near(player, root.Shell) or player:GetAttribute("ForgeCollected") or player:GetAttribute("ForgeWon") then return end
    player:SetAttribute("ForgeCollected", true)
    player:SetAttribute("ForgeLastAction", "Collected")
    print("[GameForgeSmoke] collected")
end)
root.Boat.ProximityPrompt.Triggered:Connect(function(player)
    if not near(player, root.Boat) then return end
    if player:GetAttribute("ForgeWon") then
        player:SetAttribute("ForgeLastAction", "RejectedDuplicateDeposit")
        return
    end
    if not player:GetAttribute("ForgeCollected") then
        player:SetAttribute("ForgeLastAction", "RejectedEarlyDeposit")
        return
    end
    player:SetAttribute("ForgeWon", true)
    player:SetAttribute("ForgeAwards", (player:GetAttribute("ForgeAwards") or 0) + 1)
    player:SetAttribute("ForgeLastAction", "Won")
    print("[GameForgeSmoke] won")
end)
restart.OnServerEvent:Connect(function(player, action)
    if action ~= "restart" then return end
    local now = os.clock()
    if lastReset[player] and now - lastReset[player] < .25 then return end
    lastReset[player] = now
    reset(player)
    print("[GameForgeSmoke] restarted")
end)
]==]
server.Parent = SSS
local client = Instance.new("LocalScript")
client.Name = "GameForgeSmokeClient"
client.Source = [==[
local player = game:GetService("Players").LocalPlayer
local root = workspace:WaitForChild("GameForgeSmoke")
local restart = game:GetService("ReplicatedStorage"):WaitForChild("GameForgeSmokeRestart")
local gui = Instance.new("ScreenGui")
gui.Name, gui.ResetOnSpawn = "GameForgeSmokeHUD", false
local text = Instance.new("TextLabel")
text.Name, text.Size, text.Position = "Status", UDim2.new(0, 500, 0, 65), UDim2.new(.5, -250, 0, 25)
text.TextSize, text.TextWrapped = 22, true
text.BackgroundColor3, text.TextColor3 = Color3.fromRGB(20, 30, 40), Color3.new(1, 1, 1)
text.Parent = gui
local button = Instance.new("TextButton")
button.Name, button.Size, button.Position = "Restart", UDim2.new(0, 160, 0, 45), UDim2.new(.5, -80, 0, 100)
button.Text, button.TextSize, button.Parent = "Restart (R)", 20, gui
gui.Parent = player:WaitForChild("PlayerGui")
local function update()
    local collected, won = player:GetAttribute("ForgeCollected"), player:GetAttribute("ForgeWon")
    text.Text = won and "You win! Restart and complete the loop again." or collected and "Carry the shell to the green boat; press E." or "Find the gold shell; press E to collect."
    root.Shell.LocalTransparencyModifier = collected and 1 or 0
    root.Shell.ProximityPrompt.Enabled = not collected
end
player:GetAttributeChangedSignal("ForgeCollected"):Connect(update)
player:GetAttributeChangedSignal("ForgeWon"):Connect(update)
button.Activated:Connect(function() restart:FireServer("restart") end)
game:GetService("UserInputService").InputBegan:Connect(function(input, processed)
    if not processed and input.KeyCode == Enum.KeyCode.R then restart:FireServer("restart") end
end)
update()
]==]
client.Parent = SPS
print("[GameForgeSmoke] fixture prepared in Edit mode; gameplay has not been tested")
return {root = root:GetFullName(), server = server:GetFullName(), client = client:GetFullName()}
