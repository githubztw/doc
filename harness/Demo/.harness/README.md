# 驾驭层制品（Harness）

可整体拷贝到新 WPF 项目根目录，与 `AGENTS.md` 配套使用。

| 子目录 | 作用 |
| :--- | :--- |
| `rules/` | 不可违反的结构与流程（对应 Hanness 规则层） |
| `skills/` | 按需加载的执行技能（对应技能层） |
| `wiki/` | 业务与配置契约（对应知识层） |
| `automation/` | `feature_list.json`、后台清理 Prompt |
| `changes/` | 每次非 trivial 变更的 summary / rollback |
| `templates/` | 脚手架化时复制到项目根的 `global.json`、`Directory.Build.props` |

会话入口：[../AGENTS.md](../AGENTS.md)

**本包不含** `src/`、`.sln`；生成代码见 `automation/init-agent-prompt.md`。