# 需求分析技能

## 触发条件
新功能、新模块或从 Harness 生成项目代码前。

## 步骤
1. 阅读 [领域术语.md](../../wiki/领域术语.md)、[业务模型.md](../../wiki/业务模型.md)
2. 将需求映射到分层：`Domain` / `Services` / `Modules.{Name}`
3. 列出导航区域、配置项（写入 `Modules` JSON 节点草案）
4. 在 `feature_list.json` 新增条目：`id`, `title`, `priority`, `status`, `acceptance`
5. 若跨模块，在 `summary.md` 记录影响面

## 输出
- 验收标准（可测试）
- 不涉及 UI 细节前先定 Service 契约（Abstractions）