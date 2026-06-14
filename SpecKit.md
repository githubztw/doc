# 1 安装

## 1.1 基础

1. 安装命令：`uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.9.5`

2. 创建项目 spec-kit_test：`specify init spec-kit_test`

3. 选择`coding agent `
   + cursor
   + claude
   + codex
   + 。。。
4. 进入`spec-kit_test`目录
5. `cursor .`进入cursor。或者`Claude .` 进入Claude

`specify self check`： 查询版本
`specify self upgrade`：更新版本


## 1.2 SDD

1. 意图驱动的开发 —— 规范先定义 "做什么"，再定义 "如何做"。
2. 使用护栏和组织原则 创建丰富的规范。
3. 多步细化 —— 而不是根据提示一次性生成代码。
4. 严重依赖 AI

## 1.3 命令

`/speckit.constitution`：创建项目的管理原则和开发指南，明确必须遵守的最高原则，指导后续开发。

+ 代码质量
+ 测试标准
+ 用户体验一致性、统一设计规范
+ 性能要求（响应时间限制、支援占用指标等）

他会修改 `specify\memory\constitution.md`文件，它相当于Claude中的`claude.md`文件或者cursor中的全局规则

```
/constitution 为 Next.js + Tailwind 项目制定：TypeScript 严格模式、统一 ESLint + Prettier（或 Biome）规则、提交前必须通过 lint 与 typecheck、所有新功能需附带单元测试与页面级 e2e 测试
```



`/speckit.specite`：命令描述你想构建的功能和目标。关注**“什么”**和**“为什么”，**而不是技术栈。即规范文档

+ 用户故事
+ 功能需求
+ 关键实体（Entities/数据模型）
+ 成功标准

**注意**

1. 不要说明任何技术细节
2. 需要检查spec.md文档，实现补充
3. 每次执行都会自动创建一个分支，说明这是一个新的需求 `feature`

```
/specify 构建一个待办事项（Todo）应用，帮助用户管理日常任务。用户可以添加、编辑、完成和删除任务。
任务应按创建时间排序，并可切换查看 "全部任务"、" 已完成任务 "、"未完成任务"。
用户应能为任务添加截止日期和优先级，应用需要在任务到期当天提醒用户。
所有任务仅存储在本地浏览器，不需要多设备同步。应用目标是提供简单直观的界面，帮助用户保持条理。
成功标准包括：用户能顺利添加和完成任务，任务列表能正确更新，且提醒功能在任务到期当天触发。
```

`/plan`：提供你的技术栈和架构选择。生成技术相关的文档

+ 技术栈（前端、后端、数据库、第三方服务）
+ 架构设计（模块划分、交互方式）
+ API 合约雏形（路径、请求 / 响应格式）
+ 数据模型设计（字段、关系）
+ 外部依赖与集成点

```
/plan 前端采用 Next.js 14（App Router 模式），结合 TailwindCSS 与 shadcn/ui 构建用户界面。应用的主要页面包括任务列表页、新建任务页和设置页。TailwindCSS 负责全局样式，shadcn/ui 提供按钮、表单、对话框等基础交互组件。前端状态管理使用 React 状态与服务器组件数据获取结合。

后端使用 Supabase 提供数据库和认证服务。数据库表设计如下：
- users 表：id, email, created_at
- todos 表：id, user_id, title, description, due_date, priority, completed, created_at, updated_at

认证由 Supabase Auth 完成，前端通过 session 获取用户信息。所有任务与用户 id 绑定。

数据获取采用 Next.js Server Actions 调用 Supabase。增删改查 todos 时，使用 Supabase 的 row-level security 策略，确保用户只能访问自己的任务。前端通过 React Server Components 获取任务列表，客户端交互（添加/编辑/完成任务）通过 form actions 或 client component 调用 API route。

性能与安全要求：
- 所有接口需启用 HTTPS，敏感信息不写入前端代码。
- 前端必须实现输入校验（zod），后端由 Supabase 约束与触发器保证数据一致性。
- 页面初始加载目标在 1.5s 内，JS 首包控制在 120KB 内。


非功能需求：
- UI 必须具备可访问性（a11y）。
- 提供简单的移动端自适应布局。
- 所有新增任务必须可设置截止日期与优先级，并在任务到期当天通过前端提醒显示。

最终交付：plan.md 会包含架构图示意、API 合约草案（如 GET /todos，POST /todos），以及 quickstart 文档说明如何在本地运行（连接 Supabase 项目并配置 .env）。
```

`/tasks`：根据你的实施计划，拆解、创建一个可执行的任务列表。

`/implement`：执行所有任务，并按照计划构建你的功能



## 1.4 说明

```
大项目建议按特性拆分多个 specs（例如 “用户管理”“支付”“报表” 各一份），而不是把全站一次塞进一个 /specify
```

优点：用一套框架对齐需求、减少遗漏

缺点：对于 spec 的要求很高 + 超级慢