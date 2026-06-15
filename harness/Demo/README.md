# Harness WPF Demo（仅驾驭层制品）

可拷贝的 **Harness 工程包**：约束、技能、Wiki、自动化与脚本。**不含** `src/`、`.sln` 或任何应用代码；由初始化 Agent 按规范生成（见 `.harness/automation/init-agent-prompt.md`）。

## 入口

**只读一个文件：** [AGENTS.md](AGENTS.md)

## 目录

| 路径 | 说明 |
| :--- | :--- |
| `.harness/rules/` | 工程结构、编码、流程 |
| `.harness/skills/` | 需求分析 / 编码实现 / 架构约束 |
| `.harness/wiki/` | 术语、业务、配置、接口契约 |
| `.harness/automation/` | `feature_list.json`、Init/Cleanup Agent 模板 |
| `.harness/changes/` | 变更 summary / rollback 模板 |
| `.harness/templates/` | 脚手架化时复制到根目录的 `global.json`、`Directory.Build.props` |
| `scripts/` | `init.ps1`、`verify.ps1`（制品完整性） |

## 本地

```powershell
cd Demo
.\scripts\init.ps1      # 或 .\scripts\verify.ps1
```

## 方法论

仓库根目录 [Hanness.md](../Hanness.md)。`doc/` 为早期副本，**以 `Demo/.harness` 为准**。