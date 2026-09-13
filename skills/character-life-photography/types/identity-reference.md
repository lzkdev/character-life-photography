# 正面定妆照与骨相模板

type_id: identity-reference
type_version: 1.0

用于初始化新人物、用户要求补建正面身份图或身体比例参考。默认先生成一张正面头肩候选；用户选定后才能作为主身份图。已有可用、选定的旧主图不因本模板而失效，不自动改写旧 Canon。

固定的是机位、照明和信息组织；脸、年龄、肤色、骨架、发型与服装由本人物资料决定。日常照片与杂志封面仍按各自风格创作，不套用定妆机位。

## 先把结构说清楚

骨架描述包含**面部骨相与五官关系**，以及**肩颈、躯干与四肢比例**。它是可见外形的文字约束，不是 X 光、解剖骨骼图或姿态关键点图。

新建人物在 `canon.structure` 保存以下六项。每项用简短、连贯的语言写有区分度的结构关系；面部每项通常 2–3 个可确认的点即可，避免同一方向反复叠词。已有参考先按可见部分描述；看不见、不确定的内容标 null 或留作问答，不臆测隐藏结构。新设计的重要结构由用户选定或在明确授权范围内代拟，来源写入 provenance。

| 字段 | 要明确的关系 |
|---|---|
| face_shape | 一个主脸型，额颧下颌的收放、面颊轮廓与下巴形状 |
| eyes | 眼形与眼裂长短，眼角走势、眼皮或眼距；瞳色按本人物设定 |
| brows | 眉毛走势，眉峰位置或粗细、浓淡 |
| nose | 鼻梁走向或山根，鼻头形状与鼻翼宽窄 |
| lips | 上下唇的相对厚薄，唇峰或嘴角走势 |
| body_frame | 肩宽与肩线、颈部比例；有依据时补躯干与腿长、整体骨架和惯常体态 |

不要用“五官精致”“完美身材”替代结构，也不把单眼皮、高颧骨、年龄痕迹、自然不对称或用户指定特征改成统一审美。脸型只用一个主结构再补有限过渡点；不叠加圆、短、小下巴、大眼等词去放大某种脸型。数值比例、身高和围度只在用户已定义时使用，不从头肩照测出全身体型。

新人物进入主图生成前，面部五项与头肩可见的骨架方向应足够清楚；不够就按初始化规则每轮问 1–3 项。未显示的全身比例可以保留待定，不为可选数据无限追问。`canon.face`、`canon.body` 与精简 `identity_prompt` 应与结构块一致，结构改变要检查这三处，避免两套冲突描述。

旧档案可继续使用 face/body；缺少 structure 不自动补造细节、不批量迁移。只有用户要求细化时版本化更新；本次生图仍固定实际读取的版本与 hash。

## 固定模板 A：正面头肩主身份候选

template_id: front-head-shoulders
template_version: 1.0

- **构图与机位**：单人、3:4 竖图、头肩近景、少量头顶留白；85mm 等效人像视角作为视觉意图。头部朝正前方，双肩正对镜头并保持自然水平，双眼直视镜头，镜头与眼睛同高。不得改成微侧脸、三分之二侧面、转肩、俯仰或歪头来增加表现力。
- **结构可见**：眉眼、鼻唇、下颌和辨识点清楚；保留已定的发型，必要时整理遮脸发丝。头肩图不证明全身比例，手和腿不必强行挤入画面。
- **表情与衣着**：放松、中性或极轻微闭口笑，不用夸张表情拉动五官。穿用户选定的简单不透明日常上装，妆容遵从人物；服装不占据身份描述主体。无手持道具、场景叙事或镜头互动动作。
- **背景与光线**：干净中性深灰背景，镜头左前约 45° 的大面积柔光，另一侧轻补光；两眼清楚，保留柔和轮廓阴影。避免完全无阴影的平光、单侧脸陷入暗部或彩色环境染肤。
- **质感**：保留本人物年龄、肤色、皮肤细节和自然不对称；照片风格不把脸过度磨平。身份参考不带酒吧、胶片偏色或封面调色，风格效果留到后续作品。

编译下列模板时替换全部槽位。身份段只出现一次；无参考的新设计明确说明首次创建，不声称已经锁脸。延续已有角色则明确所传图片的身份用途并保留原 Canon。工具没有额外拼装层时提交完整模板，不能只提交人物段。

```text
Create one photographic character identity reference, vertical 3:4, a head-and-shoulders portrait with a little headroom and an 85 mm-equivalent perspective.

Character: {new-design statement OR reference-image identity instruction}; {confirmed age or age presentation}; {confirmed identity context if provided}; {skin tone and texture}; {face_shape}; {eyes}; {brows}; {nose}; {lips}; {hair}; {visible shoulder-and-neck structure}; {distinctive marks and fixed accessories, if any}.

The head faces straight ahead, both shoulders face the camera and rest naturally level, and both eyes look directly into the lens. The camera is at eye level. Keep the entire face clearly readable with no head turn, shoulder turn, head tilt or high/low camera angle. Use {approved restrained expression} and {approved simple opaque everyday top and makeup}.

A clean neutral dark-gray background. A broad soft key light from approximately 45 degrees to camera left and gentle fill from the other side keep both eyes clear while preserving soft facial contour shadows. Preserve this character's age, natural skin detail and subtle asymmetry, with neutral color and clearly resolved facial features. One person in one continuous frame, without props, collage panels, lettering or watermark.
```

本包提供 [完整首次设计计划](../examples/generic-identity-reference.plan.json)，没有生成图片、没有选定人物。示例只说明编译后的结构，不是给其他人物套用的外貌。

## 模板 B：按需补充正面全身骨架参考

template_id: front-full-body
template_version: 1.0

只有用户要求或已授权补充全身参考时生成；不把默认 1 张变成自动多张。先使用用户选定的主脸作为 primary_identity，延续同一年龄、骨相、发型与固定辨识点。单人 2:3 竖图，正面自然站立、头脚完整，双肩与骨盆朝前，双手自然放在身体两侧且手指可辨，双脚自然落地；人物不用前倾、扭腰或踮脚。机位约在躯干中部，光轴水平、50–70mm 等效视角，保持头身与腿长透视自然。

人物段加入有依据的完整 body_frame；简单、合身但不紧勒的不透明日常衣裤让轮廓可辨，明确鞋款并避免用厚底或高跟改变身高观感。沿用中性背景与柔光，保留地面接触阴影。沿用模板 A 的身份、质感、单帧限制，替换景别、机位、姿态和衣着，不能同时留下“头肩近景”或“85mm 眼平头肩”的矛盾句。

看图分别核对肩宽、肩线、颈长、躯干与腿长、重心和四肢。此图通过并被用户选定后登记 role=body；不替换主脸。侧面、背面及表情图另行按需求生成，不混进默认主图或拼成唯一身份锚。

## 记录、天气与验收

只有开启 save_records 时才用同一份 JSON 保存计划和结果，`creation` 写 identity-reference 1.0，`spec` 写 template_id 与 template_version；按 [专用 Schema](identity-reference.schema.json) 验证。启用详细记录时保存引用的模板和人物草案；默认关闭记录时只保留候选图片和初始化所需的独立人物资料，不生成重复的阅读文件。

这是明确设计的中性参考环境。context 的地点标 fictionalized，天气 basis=scenario，温度、降水和查询时间等不存在的数据留 null；不声称已查询当前天气。初始化时尚未确定的常住地可保留，首次日常照片前补齐；这不取消日常照片的天气查询规则。

实际 QC 必须检查朝向、双肩、眼平视线、五官结构、辨识点及左右、年龄肤色、发型与肩颈、光线和照片完整性。任何偏转明显、身份改变、辨识点不清或结构异常均标 needs_revision，不能因“看起来好看”就通过。格式、比例检查与肉眼结构检查分开；请求比例不是工具实际尺寸。看过且合格仍只是候选，用户选定后才建立新 Canon；未经选择保留 draft。
