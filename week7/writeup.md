# Week 7 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **TODO** \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do. 


## Task 1: Add more endpoints and validations
a. Links to relevant commits/issues
> TODO

b. PR Description
> 本任务添加了以下功能：
> - 删除笔记端点 (`DELETE /notes/{note_id}`)
> - 删除行动项端点 (`DELETE /action-items/{item_id}`)
> - 获取单个行动项端点 (`GET /action-items/{item_id}`)
> - 使用 Pydantic Field 添加输入验证（标题长度限制、内容非空检查）

c. Graphite Diamond generated code review
> TODO

## Task 2: Extend extraction logic
a. Links to relevant commits/issues
> TODO

b. PR Description
> 扩展了行动项提取逻辑，支持更多关键词和模式：
> - 添加了行动相关关键词（need to, must, should, have to, want to 等）
> - 支持列表项格式识别（数字编号、项目符号）
> - 添加了去重功能，避免重复提取
> - 添加了文本清理功能，自动去除关键词前缀

c. Graphite Diamond generated code review
> TODO

## Task 3: Try adding a new model and relationships
a. Links to relevant commits/issues
> TODO

b. PR Description
> 添加了标签（Tag）模型及其与笔记和行动项的多对多关系：
> - 创建了 Tag 模型（包含名称和颜色字段）
> - 创建了关联表 `note_tags` 和 `action_item_tags`
> - 为笔记和行动项添加了标签关联功能
> - 创建了标签的完整 CRUD API

c. Graphite Diamond generated code review
> TODO

## Task 4: Improve tests for pagination and sorting
a. Links to relevant commits/issues
> TODO

b. PR Description
> 完善了分页和排序的测试覆盖：
> - 添加了笔记的分页测试（边界情况、skip/limit 参数）
> - 添加了笔记的排序测试（升序/降序）
> - 添加了笔记的搜索功能测试
> - 添加了行动项的分页测试
> - 添加了行动项的排序测试
> - 添加了行动项的过滤测试（按完成状态）
> - 添加了笔记和行动项的删除测试

c. Graphite Diamond generated code review
> TODO

## Brief Reflection 
a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
> TODO 

b. A comparison of **your** comments vs. **Graphite's** AI-generated comments for each PR.
> TODO
c. When the AI reviews were better/worse than yours (cite specific examples)
> TODO
d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.
>TODO 

