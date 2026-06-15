# 回滚说明：{feature_name}

## 前置条件

- 记录回滚前 git commit / 标签（若有）

## 步骤

1. 还原代码：……
2. 还原配置：`appsettings.json` / `module.settings.json` 键……
3. 运行 `scripts/verify.ps1` 确认基线

## 数据 / 状态

Demo 无 DB 迁移；若有本地用户设置，说明是否需手动清理。