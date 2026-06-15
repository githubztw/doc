# 架构约束技能

## 触发条件
新增项目引用、跨层调用、新模块落地或 CI 架构测试失败时。

## 步骤
1. 对照 [.harness/rules/工程结构.md](../../rules/工程结构.md) 确认依赖方向
2. 在 `tests/Harness.Wpf.Demo.ArchitectureTests` 补充/调整 NetArchTest 规则
3. 错误信息格式（Agent 可自修复）：
   - ❌ 什么错了
   - ✅ FIX: 具体改法
   - �� See: 文档路径

## 必跑命令
```powershell
dotnet test tests/Harness.Wpf.Demo.ArchitectureTests/Harness.Wpf.Demo.ArchitectureTests.csproj
```

## 常见违规
| 违规 | 修复 |
| :--- | :--- |
| ViewModel 引用 View | 用导航 URI + 接口 |
| Module 引用 Shell | 将共享逻辑下沉 Abstractions/Services |
| Domain 引用 WPF | 上移 DTO 或 Shell 专用模型 |