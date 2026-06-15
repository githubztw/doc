# WPF Harness Demo — AI 会话入口（唯一信息层入口）

> 原 `CLAUDE.md` 已合并至本文件；请勿再维护重复入口。

## 项目简介

**驾驭层制品包**（本目录无 `src`/`.sln`）。目标技术栈为 **.NET 8 + Prism.WPF + WPF UI (lepoco)**；应用代码由 Agent 按 [init-agent-prompt.md](.harness/automation/init-agent-prompt.md) 从本 Harness **生成**。

## 技术栈基线（不允许擅自升级）

| 层级 | 技术 |
| :--: | :--- |
| 运行时 | .NET 8（脚手架后根目录 `global.json`，模板见 `.harness/templates/`） |
| 框架 | Prism.WPF 9.x + Prism.DryIoc |
| UI | Wpf.Ui（`lepoco/wpfui`）+ Shell 统一 `App.xaml` 资源字典 |
| 配置 | `appsettings.json` + 各模块 `module.settings.json`（Shell 合并） |
| 测试 | xUnit + NetArchTest.Rules（架构约束） |
| 格式 | `dotnet format` + EditorConfig |

## 快速导航

| 你想做什么 | 去哪里看 |
| ---------- | -------- |
| 分层与目录 | [.harness/rules/工程结构.md](.harness/rules/工程结构.md) |
| 编码与 MVVM 规范 | [.harness/rules/代码规范.md](.harness/rules/代码规范.md) |
| 开发流水线 | [.harness/rules/开发流程规范.md](.harness/rules/开发流程规范.md) |
| 领域与术语 | [.harness/wiki/领域术语.md](.harness/wiki/领域术语.md) |
| 模块与导航契约 | [.harness/wiki/业务模型.md](.harness/wiki/业务模型.md) |
| 配置合并约定 | [.harness/wiki/数据模型.md](.harness/wiki/数据模型.md) |
| 模块间契约 | [.harness/wiki/接口协议.md](.harness/wiki/接口协议.md) |
| 功能清单（JSON） | [.harness/automation/feature_list.json](.harness/automation/feature_list.json) |
| 熵管理后台任务 | [.harness/automation/cleanup-agent-prompt.md](.harness/automation/cleanup-agent-prompt.md) |
| 从 Harness 生成代码 | [.harness/automation/init-agent-prompt.md](.harness/automation/init-agent-prompt.md) |
| 校验制品完整性 | [scripts/verify.ps1](scripts/verify.ps1) |
| 驾驭方法论（仓库级） | [../Hanness.md](../Hanness.md) |

## 技能（按需加载，≤3/会话）

| 技能 | 路径 |
| :--- | :--- |
| 需求分析 | [.harness/skills/需求分析/SKILL.md](.harness/skills/需求分析/SKILL.md) |
| 编码实现 | [.harness/skills/编码实现/SKILL.md](.harness/skills/编码实现/SKILL.md) |
| 架构约束 | [.harness/skills/架构约束/SKILL.md](.harness/skills/架构约束/SKILL.md) |

## 红线（不可违反，CI / verify 会验证）

1. **分层依赖方向** — `Domain → Abstractions → Configuration → Infrastructure → Services → Modules → Shell`，禁止反向
2. **ViewModel 不依赖 View 类型** — 禁止 `using` 模块内 `Views` 命名空间
3. **业务逻辑只在 Services** — ViewModel 仅编排与 `BindableBase` 状态
4. **模块配置独立文件** — `Modules/{Name}/module.settings.json`，Shell `appsettings.json` 的 `Modules` 节点统一覆盖
5. **导航注册在 Module 内** — `RegisterTypes` + `OnInitialized` 注册区域与菜单；URI 常量在 `Abstractions/Navigation/`
6. **异步 UI** — 禁止阻塞 UI 线程（`.Result` / `.Wait()`）
7. **主题与样式走全局资源** — 禁止各 View 复制色值/字号
8. **禁止 `MessageBox.Show` 散落** — 统一 `IDialogService` / `ISnackbarService`
9. **禁止静态 Service Locator** — `Container.Resolve` 仅允许 Bootstrapper/Module 注册阶段
10. **Harness 非 trivial 变更** — 更新 `.harness/changes/{feature}/summary.md`（及 `rollback.md` 若可回滚）

## 硬性规则摘要（与架构测试对齐）

- Domain 不得引用 WPF / Prism / Wpf.Ui
- Modules 不得引用 Shell 项目
- 新增公共类型须有架构测试或单元测试；架构变更必跑 `ArchitectureTests`

## AI 会话启动（编码 Agent）

1. 确认工作目录为 `Demo/`
2. 读本文件 → 按需 `.harness/rules/`（≤3）→ `.harness/wiki/`（≤3）
3. 读取 `claude-progress.txt`、`.harness/automation/feature_list.json`
4. 若有 git：读最近提交与未完成功能
5. 实现前更新 `feature_list.json` 状态；结束后更新进度与 changes

## 提交规范

`feat:` / `fix:` / `refactor:` / `docs:` / `test:` / `chore(harness):`