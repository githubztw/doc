# Feature: [功能名称] 

## Status: 📝 Draft | 📄 Approved | 🚧 In Progress | ✅ Implemented 
## 目标 
一句话描述这个功能要解决什么问题。

## 非目标 

明确列出这次不做什么（防止 Agent 扩大范围）。 

## 技术方案 

## ### 涉及的模块 

+ domain/      : 新增 XXX 实体（@TableName）与 DTO 

+ mapper/      : 新增 XXXMapper extends BaseMapper<XXX> 

+ service/     : 新增 XXXService 业务逻辑 

+ controller/  : 新增 /api/xxx 端点 

### 数据模型变更 

```sql
 -- 如有数据库变更，写在这里（Flyway 迁移脚本路径：src/main/resources/db/migration/V_xxx.sql）
```

### API 变更 
```http 
POST /api/xxx  
Request:  { ... }  
Response: { ... }
```

## 验收标准

- 标准 1：具体的、可验证的
- 标准 2：具体的、可验证的
- 测试覆盖率 ≥ 80%



```
Agent 拿到一个功能需求后，先填写这个模板（或人工填写），审批通过后再动手写代码。这就是"明确意图"的工程化实现
```

