#Requires -Version 5.1
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

Write-Host "== Harness WPF Demo: init (制品层) ==" -ForegroundColor Cyan
Write-Host "本目录仅含驾驭层制品，不含 .sln / src 代码。" -ForegroundColor Gray
Write-Host ""
Write-Host "会话入口: AGENTS.md" -ForegroundColor Green
Write-Host "功能状态: .harness/automation/feature_list.json"
Write-Host "生成代码: 按 .harness/automation/init-agent-prompt.md 脚手架化解决方案"
Write-Host ""
Write-Host "校验制品完整性:" -ForegroundColor Yellow
& "$PSScriptRoot\verify-harness.ps1"