# 任务：Harness WPF Demo 代码库卫生清理

请执行以下检查，对每个发现的问题生成**独立**变更（或独立 PR）：

## 检查清单

1. **超长文件**：`src/`、`tests/` 下超过 300 行的 `.cs` 文件 → 拆分为更小类型或 `partial`
2. **缺失测试**：`Services` 中公共类型无对应 `*Tests` → 补充 xUnit 基础用例
3. **未使用的 using**：`dotnet format` / IDE 清理
4. **TODO/FIXME**：列出全部；超过 30 天未处理则建清理任务
5. **重复代码**：>10 行高度相似 → 提取到 `Infrastructure` 或共享 Abstractions（不违反分层）
6. **文档漂移**：`.harness/wiki` 与 `NavigationKeys`、配置键不一致 → 同步 Wiki frontmatter `last_updated`
7. **架构告警**：`dotnet test tests/Harness.Wpf.Demo.ArchitectureTests` 失败 → 先修分层再合入

## 约束

- 每个修复独立，不混在一个大提交里
- 修改后必须 `scripts/verify.ps1` 通过（或等价 `dotnet build` + `dotnet test`）
- 标题：`chore(cleanup): [具体描述]`
- **禁止**擅自升级 .NET / Prism / Wpf.Ui 主版本（见 `AGENTS.md`）
- 不确定是否安全的重构：跳过并在说明中标注原因

## 错误信息格式（自修复 Prompt）

```
❌ [什么错了]
✅ FIX: [怎么改，可含代码片段]
📖 See: [.harness/rules/xxx.md](...)
```