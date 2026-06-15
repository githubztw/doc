# 初始化 Agent（首次搭建 / 从 Harness 生成代码库）

在 **已有** `Demo/.harness` 与 `AGENTS.md` 的前提下，完成可编译、可启动的最小解决方案。

## 交付物

0. 将 `.harness/templates/global.json`、`Directory.Build.props` 复制到 `Demo/` 根目录
1. 创建 `Harness.Wpf.Demo.sln` 与 `src/`、`tests/` 各层 `.csproj` 及项目引用（见 `rules/工程结构.md`）
2. `tests/` ArchitectureTests + Services.Tests
3. 各模块 `module.settings.json` + Shell `appsettings.json`
4. 初始 git 提交（若仓库已初始化）
5. 更新 `feature_list.json`：F-001～F-005 标为 `passing`（经自测后）
6. 更新 `claude-progress.txt`

## 禁止

- 升级 .NET / Prism / Wpf.Ui 基线
- 在 View Code-Behind 写业务逻辑
- 跳过 ArchitectureTests

## 验证

```powershell
.\scripts\verify.ps1
```