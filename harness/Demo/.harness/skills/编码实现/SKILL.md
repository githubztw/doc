# 编码实现技能

## 触发条件
`feature_list.json` 中某功能状态为 `in_progress` 或用户指定实现任务。

## 前置条件
- 需求分析已完成
- 已读 [工程结构.md](../../rules/工程结构.md)、[代码规范.md](../../rules/代码规范.md)（按需 ≤3 规则文件）

## WPF 编码顺序

### Step 1：Domain / Abstractions
- 实体、枚举放 `Domain`
- 服务接口、导航常量放 `Abstractions`

### Step 2：Configuration
- 新增 `XxxModuleOptions` + 绑定扩展
- 更新模块 `module.settings.json` 与 Shell `appsettings.json` 的 `Modules` 节点

### Step 3：Services
- 实现用例，注入 `ILogger<T>`
- 编写 `Services.Tests`

### Step 4：Module
- `{Name}Module.cs`：`RegisterTypes` + `OnInitialized`（菜单/区域导航）
- ViewModel → View（Prism 自动装配）

### Step 5：Shell（仅全局变更）
- 主题、新模块引用、配置合并

## 自检
- `dotnet build` / `dotnet test`
- `scripts/verify.ps1`
- 更新 `feature_list.json` 与 `.harness/changes/{feature}/summary.md`