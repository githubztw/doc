#Requires -Version 5.1
# 制品层仓库：verify 等同于 verify-harness。完整解决方案生成后在此扩展 dotnet build/test。
& "$PSScriptRoot\verify-harness.ps1"
exit $LASTEXITCODE