# prompts.chat 插件完整说明文档

## 概述

**prompts.chat** 是一个为 Claude Code 提供 AI 提示词(Prompts)和智能体技能(Agent Skills)发现、检索、安装、创建和优化的 MCP 插件。它连接 prompts.chat 平台，让用户可以直接在 Claude Code 中搜索和使用社区共享的提示词模板与可复用技能。

- **官网**: https://prompts.chat
- **插件类型**: MCP Server
- **安装方式**: 通过 Claude Code 插件市场安装

---

## 一、核心功能概览

该插件提供两大功能板块，共 **10 个 MCP 工具**：

### 1. Prompt 管理（AI 提示词）

| 工具 | 功能 | 使用场景 |
|------|------|----------|
| `search_prompts` | 关键词搜索提示词 | 寻找代码审查、写作、分析等各类提示词模板 |
| `get_prompt` | 获取指定提示词详情 | 查看完整提示词内容，支持变量填充 |
| `improve_prompt` | AI 优化提示词 | 将简单提示词增强为结构化、高质量版本 |
| `save_prompt` | 保存提示词到账户 | 将自定义提示词上传到 prompts.chat 平台 |

### 2. Skill 管理（智能体技能）

| 工具 | 功能 | 使用场景 |
|------|------|----------|
| `search_skills` | 关键词搜索技能 | 发现可复用的 AI 智能体技能 |
| `get_skill` | 获取指定技能详情 | 查看技能包含的所有文件（SKILL.md、参考文档、脚本等） |
| `save_skill` | 创建新技能 | 将多文件技能保存到平台 |
| `add_file_to_skill` | 向已有技能添加文件 | 为技能补充参考文档、脚本、配置文件 |
| `remove_file_from_skill` | 从技能中移除文件 | 删除技能中不需要的文件（不可删除 SKILL.md） |
| `update_skill_file` | 更新技能中的文件 | 修改技能内的参考文档、脚本或 SKILL.md 内容 |

---

## 二、配套 Skill 命令

插件安装后在 Claude Code 中可用的自定义命令：

| 命令 | 功能 |
|------|------|
| `/prompts.chat:prompts` | 搜索和发现 AI 提示词 |
| `/prompts.chat:skills` | 搜索和发现智能体技能 |
| `/prompts.chat:skill-lookup` | 搜索、检索并安装技能到本地 `.claude/skills/` |
| `/prompts.chat:prompt-lookup` | 搜索、检索和优化提示词 |

---

## 三、详细功能说明

### 3.1 搜索提示词（`search_prompts`）

按关键词搜索 prompts.chat 平台上的公共提示词库，返回匹配的提示词列表。

**支持的过滤条件**：
- `query`：搜索关键词（必填）
- `limit`：返回数量（默认 10，最大 50）
- `type`：按内容类型过滤 — `TEXT`（文本）、`STRUCTURED`（结构化）、`IMAGE`（图像）、`VIDEO`（视频）、`AUDIO`（音频）
- `category`：按分类过滤
- `tag`：按标签过滤

**返回信息**：标题、描述、作者、分类、标签、链接

### 3.2 获取提示词（`get_prompt`）

根据 ID 获取提示词的完整内容。支持**变量模板**功能：
- 提示词可以包含 `{{variable}}` 或 `{{variable:default_value}}` 格式的占位变量
- 获取时会交互式提示用户填写变量值
- 无默认值的变量为必填项，有默认值的为可选项

### 3.3 优化提示词（`improve_prompt`）

使用 AI 将基础提示词转化为结构良好、全面的提示词。

**参数**：
- `prompt`：原始提示词文本
- `outputType`：目标内容类型 — `text`、`image`、`video`、`sound`
- `outputFormat`：输出格式 — `text`（纯文本）、`structured_json`（JSON 结构）、`structured_yaml`（YAML 结构）

**典型用途**：将一句话的模糊需求扩展为包含角色设定、输出格式、约束条件的完整提示词。

### 3.4 保存提示词（`save_prompt`）

将自定义提示词保存到 prompts.chat 个人账户（需要 API Key 认证）。

**参数**：
- `title`：标题（必填，最长 200 字符）
- `content`：内容（必填，支持 `{{variable}}` 模板语法）
- `description`：描述（可选，最长 500 字符）
- `tags`：标签数组（最多 10 个）
- `category`：分类
- `isPrivate`：是否私有（默认跟随账户设置）
- `type`：提示词类型（`TEXT`、`STRUCTURED`、`IMAGE`、`VIDEO`、`AUDIO`）
- `structuredFormat`：结构化格式（`JSON` 或 `YAML`）

### 3.5 搜索技能（`search_skills`）

按关键词搜索可复用的智能体技能。Agent Skills 是包含 SKILL.md、参考文档、脚本和配置文件的多文件组件。

**支持的过滤条件**：
- `query`：搜索关键词
- `limit`：返回数量（默认 10，最大 50）
- `category`：按分类过滤
- `tag`：按标签过滤

### 3.6 获取技能（`get_skill`）

根据 ID 获取技能的完整文件内容，包括：
- `SKILL.md`：技能的主要指令文件（必需）
- 参考文档（reference docs）
- 辅助脚本（scripts）
- 配置文件（configuration files）

获取后可安装到本地 `.claude/skills/{slug}/` 目录下使用。

### 3.7 技能文件管理

**创建技能（`save_skill`）**：
- 必须包含 `SKILL.md` 作为主文件
- 可附带参考文档、脚本、配置文件
- 支持设置标签、分类和私有性

**维护技能**：
- `add_file_to_skill`：为已有技能补充文件
- `remove_file_from_skill`：移除不需要的文件（SKILL.md 不可删除）
- `update_skill_file`：更新技能中指定文件的内容

---

## 四、使用场景

### 场景 1：寻找代码审查提示词
```
用户：帮我找一个代码审查的提示词模板
→ 使用 search_prompts(query="code review", category="coding")
→ 展示结果，用户选择后使用 get_prompt 获取完整内容
```

### 场景 2：优化自定义提示词
```
用户：我想把这个提示词变得更好
→ 使用 improve_prompt(prompt="...", outputType="text", outputFormat="text")
→ 返回增强后的结构化提示词
```

### 场景 3：发现并安装技能
```
用户：有没有自动化测试相关的技能？
→ 使用 search_skills(query="testing automation")
→ 用户选择后使用 get_skill 获取文件
→ 安装到 .claude/skills/{slug}/ 目录
```

### 场景 4：创建并分享技能
```
用户：帮我创建一个处理 CSV 文件的技能
→ 使用 save_skill 创建技能（包含 SKILL.md 和参考文档）
→ 后续可用 add_file_to_skill 补充功能
```

---

## 五、架构说明

```
prompts.chat 平台 (云端)
       │
       ▼
┌──────────────────────────────────────┐
│  prompts.chat MCP Server (插件层)     │
│  ┌────────────┐  ┌────────────────┐  │
│  │ Prompt 管理 │  │  Skill 管理    │  │
│  │ search      │  │  search        │  │
│  │ get         │  │  get           │  │
│  │ improve     │  │  save          │  │
│  │ save        │  │  add_file      │  │
│  │             │  │  remove_file   │  │
│  │             │  │  update_file   │  │
│  └────────────┘  └────────────────┘  │
└──────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│  Claude Code 本地环境                 │
│  ┌────────────┐  ┌────────────────┐  │
│  │ /prompts   │  │  /skills       │  │
│  │ /prompt-   │  │  /skill-       │  │
│  │ lookup     │  │  lookup        │  │
│  └────────────┘  └────────────────┘  │
│                                      │
│  .claude/skills/{slug}/              │
│  ├── SKILL.md                        │
│  ├── reference.md                    │
│  └── scripts/helper.py               │
└──────────────────────────────────────┘
```

---

 ┌──────────┬──────────────────────────────┬───────────────────┐
  │   类型   │             名称             │       功能        │
  ├──────────┼──────────────────────────────┼───────────────────┤
  │ Skill    │ prompts.chat:prompt-lookup   │ 搜索和发现提示词  │
  ├──────────┼──────────────────────────────┼───────────────────┤
  │ Skill    │ prompts.chat:skill-lookup    │ 搜索和安装技能    │
  ├──────────┼──────────────────────────────┼───────────────────┤
  │ Command  │ prompts.chat:prompts         │ /prompts 快捷命令 │
  ├──────────┼──────────────────────────────┼───────────────────┤
  │ Command  │ prompts.chat:skills          │ /skills 快捷命令  │
  ├──────────┼──────────────────────────────┼───────────────────┤
  │ Agent    │ prompts.chat:prompt-manager  │ 提示词管理代理    │
  ├──────────┼──────────────────────────────┼───────────────────┤
  │ Agent    │ prompts.chat:skill-manager   │ 技能管理代理      │
  ├──────────┼──────────────────────────────┼───────────────────┤
  │ MCP 工具 │ 10 个 search/get/save 等工具 │ 底层 API 调用     │
  └──────────┴──────────────────────────────┴───────────────────┘

  ├──────────┼──────────────────────────────┼───────────────────┤
  │ MCP 工具 │ 10 个 search/get/save 等工具 │ 底层 API 调用     │
  └──────────┴──────────────────────────────┴───────────────────┘
  ---
  局部删除方法

  插件是作为整体安装的，没有"官方开关"单独禁用某个 skill。但可以直接删除插件缓存中对应的 skill 目录：

  # 例如只删除 skill-lookup，保留 prompt-lookup
  rm -rf ~/.claude/plugins/cache/prompts-chat/prompts-chat/1.0.0/skills/skill-lookup

  # 同理删除 command
  rm -rf ~/.claude/plugins/cache/prompts-chat/prompts-chat/1.0.0/commands/skills.md

  # 删除 agent
  rm -rf ~/.claude/plugins/cache/prompts-chat/prompts-chat/1.0.0/agents/skill-manager.md

  注意事项：插件更新（/plugins update）可能会恢复被删除的文件，届时需要重新删除。

---
  你想删除哪些？告诉我具体名字，我直接帮你操作。

✻ Cogitated for 27s

※ recap: 你想保留 prompts.chat 插件但只删除其中部分 skill。我已经列出了它的所有组件，等你告诉我具体删哪些。 (disable recaps
  in /config)







## 六、重要提示

1. **账户要求**：搜索和获取是公开的；`save_prompt` 和 `save_skill` 需要 API Key 认证
2. **隐私控制**：保存的内容默认跟随账户设置，可显式设为私有
3. **技能结构**：每个 Skill 必须有一个 `SKILL.md` 文件，这是技能的入口和核心指令
4. **本地安装**：通过 `get_skill` 获取的技能需安装到 `.claude/skills/{slug}/` 才会被 Claude Code 识别和使用
5. **提示词变量**：提示词支持 `{{variable}}` 模板语法，获取时可交互式填充
