#Requires -Version 5.1
# 校验驾驭层制品完整性（无 src / .sln）
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$required = @(
    "AGENTS.md",
    "README.md",
    ".editorconfig",
    "claude-progress.txt",
    ".harness/README.md",
    ".harness/rules/工程结构.md",
    ".harness/rules/代码规范.md",
    ".harness/rules/开发流程规范.md",
    ".harness/skills/需求分析/SKILL.md",
    ".harness/skills/编码实现/SKILL.md",
    ".harness/skills/架构约束/SKILL.md",
    ".harness/automation/feature_list.json",
    ".harness/automation/cleanup-agent-prompt.md",
    ".harness/automation/init-agent-prompt.md",
    ".harness/wiki/领域术语.md",
    ".harness/wiki/业务模型.md",
    ".harness/wiki/数据模型.md",
    ".harness/wiki/接口协议.md",
    ".harness/changes/_template/summary.md",
    ".harness/changes/_template/rollback.md",
    ".harness/templates/Directory.Build.props",
    ".harness/templates/global.json",
    "scripts/init.ps1",
    "scripts/verify.ps1",
    "scripts/verify-harness.ps1"
)

$forbidden = @(
    "Harness.Wpf.Demo.sln",
    "CLAUDE.md",
    "global.json",
    "Directory.Build.props"
)

$missing = @()
foreach ($f in $required) {
    if (-not (Test-Path $f)) { $missing += $f }
}

$leftover = @()
foreach ($f in $forbidden) {
    if (Test-Path $f) { $leftover += $f }
}

if (Test-Path "src") {
    $cs = Get-ChildItem -Path "src" -Recurse -Include *.cs,*.csproj -ErrorAction SilentlyContinue
    if ($cs) { $leftover += "src/ (contains code files)" }
}

if ($missing.Count -gt 0) {
    Write-Host "Missing harness artifacts:" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host "  $_" }
    exit 1
}

if ($leftover.Count -gt 0) {
    Write-Host "Forbidden in harness-only tree:" -ForegroundColor Red
    $leftover | ForEach-Object { Write-Host "  $_" }
    exit 1
}

Write-Host "verify-harness: OK ($($required.Count) artifacts, no application code)" -ForegroundColor Green
exit 0