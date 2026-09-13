# 逐图生图记录

本页只在 save_records=true、用户要求 JSON，或读取既有记录时使用。默认不生成拍摄资料。启用时每张使用一个符合 `image-record.schema.json` 的 `<shot-id>.json`：提交前写计划状态，结果返回后在同一文件更新 generation、record_stage 与 qc，保留原方案和实际提交的完整提示词。用临时文件加原子替换更新本次创建的记录；重试采用新 shot-id，保留旧结果。不要另外生成同内容的 plan.json、meta.json、prompt.txt 与 MD。多个镜头可共享 shoot_id 与 event_id，各自有唯一 shot_id。

逐图记录包含人物、摄影、生图与检查；整组配套贴文只保存 caption.md，不重复塞进每张图的记录。人物档案引用包括 ID、version、文件路径基准和 SHA-256；所用参考图逐个保存 role 与 hash。profile 内路径相对 profile 文件目录，`path_base=record` 相对本记录目录，absolute 必须是实际绝对路径。

实际生成图片也支持 `generation.image.path_base`：新归档用 `record`，local_path 相对本 metadata 文件；旧记录省略时默认 `absolute`。保存位置按 [保存位置与归档](output-storage.md) 配置，复制或换设备时不能继续依赖旧会话的绝对路径。

新方案按 [镜头互动](camera-interaction.md) 记录 interaction，明确镜头角色、触发与回应、目光和可见线索。此块在 Schema 中为可选，兼容旧记录；responsive 的触发、回应和可见线索不得为空。不能只在贴文写“在和你说话”，图片与提示词却没有相应的回应设计。

新记录的 creation 按 [类型契约](creation-types.md) 记录 type_id、type_version、spec。共同结构与人物事实不因类型变化而改名或重复；专用字段放进 spec。旧文件仍可读取，缺省不等于它当时已使用新增模块。

## 旧记录兼容

旧 `.plan.json`、`.meta.json` 与已有 MD 仍可读取，不删除、不强制迁移。新拍摄只写选定的一份 JSON。`render_record.py` 保留用于用户明确要求阅读或转换历史记录的工具用途，日常生成流程不调用它，也不自动再输出一份 MD。

用户手动修改过的旧 MD 必须保留；需要据此更正事实时先按意图合并，不能直接覆盖。该脚本为单向转换，不承诺双向同步。

## 必要区分

- `record_stage=plan` 与 `generation.status=not_requested`：只有方案，没有任务、图片或成图检查结果。
- 实际提交后 stage 改 generated，状态按 submitted／processing／succeeded／failed 更新。保留实际任务 ID 和时间；工具没有任务 ID 时填 null。
- succeeded 必须有实际可用本地路径或结果 URL；宽高来自真实文件或工具返回，不把请求尺寸当成结果尺寸。缺少模型名、seed、用量或账单数据就留空，不猜测。
- 实际查看成图后才写 qc 的 reviewed_at、passed／needs_revision 和发现；未看图保持 not_reviewed。结构校验通过不等于图片身份一致。
- `context.weather.basis` 区分 observed、forecast、user_specified、scenario、unknown、not_applicable。默认当前日常场景先查询人物所在地天气，即使室内画面受影响很小也保留查询结果。观测／当前状况需要来源和查询时间；来源未给独立观测时刻时 valid_at 留空并说明，不能把查询时刻冒充观测时刻。预报必须有对应的适用时间。not_applicable 用于明确不采用真实天气的场景，不用于跳过默认查询。
- `event.basis` 区分 existing_context、user_specified 与 proposed。新的生活方案不是角色已经发生的经历。

已启用 JSON 记录时，生成之前运行 `python3 <skill>/scripts/verify_record.py <record.json>`，可检查本地人物档案和参考图是否仍与记录中的版本、hash 对应。它使用 Python 标准库，不替代完整 JSON Schema 校验或看图。

## Prompt 编译

`prompts.scene` 只写事件、地点、时间、衣服、道具、动作、情绪与摄影表达，用于已经验证会注入身份的执行器。

`prompts.standalone` 使用本次 profile 的 identity_prompt 一次，加同一 scene 和必要的一致性约束；用于直接支持参考图的工具。`prompts.negative` 针对本次不希望出现的问题，不加入与人物特征、风格或场景相反的通用禁词。

风格图和身份图分开传递用途。若工具无法表达参考用途，优先身份锚，用文字表达风格；不能假称工具支持它没有的权重参数或控制方式。

## 示例

[室内手机随拍](../examples/generic-home.plan.json) 展示虚构人物的档案、情境与摄影表达。这是明确的创作示例，没有查询实时天气，也没有生图；人物尚无身份参考，只能演示首次设计方案。
