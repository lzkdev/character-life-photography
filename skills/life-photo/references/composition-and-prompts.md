# 机位、动作与完整提示词

借鉴既有 `character-candid-photo` 的「人物识别 → 机位 → 动作 → 环境光 → 完整提示词」写法。保留可操作的摄影语言，把观察式抓拍作为日常摄影中的一个选择。抓拍感使用虚构场景或人物知情的摆拍表达，不描述真实非自愿隐私偷拍。

## 机位库

每张选一个主要机位，必要时辅以前景或轻微角度变化。焦段与距离一起决定透视，不能只改数字就当作换了一种摄影。

| 机位 | 怎么写进 prompt | 适用与检查 |
|---|---|---|
| 平视陪伴 | 35–65mm，胸口至眼平机位，在人物侧前方；像同伴在场 | 吃饭、读书、散步等自然日常，不要求每次正视镜头 |
| 手机随手拍 | 24–35mm 等效，轻微偏心、手持角度、较深景深、环境曝光 | 保留人物脸部比例；适量手持感，不故意使每张模糊 |
| 前景后观察 | 门框、植物、椅背、货架或车窗形成柔焦前景，主体清楚 | 遮挡从环境自然产生；不机械占固定比例，不挡掉身份锚点 |
| 远距离长焦 | 85–200mm 的压缩感，从较远位置看一个完整动作 | 公共空间散步、出门、等车；不靠堆叠“偷拍”词制造效果 |
| 缝隙式构图 | 书架、开放的店面门框、栏杆等形成窄视窗 | 需要真实可解释的视线；不把日常扩展为私密窥视场景 |
| 反射取景 | 商店玻璃或镜子中的单一合理反射，写明主视角与直接人物是否入镜 | 检查镜像左右、人物数量与光学关系；档案禁止时不用 |
| 桌边／较低机位 | 35–50mm，在桌面或腰部附近稍向上，给动作留空间 | 做手工、整理桌面、坐着休息；保持自然比例，不强迫极端仰拍 |
| 轻俯拍 | 站立同伴略向下看坐着的人，保留桌面／物品 | 写清摄影者与人物的位置，避免无来源的高空视角 |

前景遮挡、颗粒、运动模糊、压缩和失焦只选必要项。人物识别清晰度优先；并非越不完美越真实。棚拍不属于默认日常场景，生活写真也要有可读的生活环境。

## 动作与人物反应

选择活动的中间状态：翻到下一页、放下杯子、整理包带、把头发拨开、检查清单、抬头听人说话、推开店门、绕过水洼、收起外套、停步看招牌。物体接触、重心和视线应互相支持。

人物可以没看镜头、正在回应镜头、刚发现摄影者或安静直视。按性格和事件选择，不规定每组必须有多少张“发现镜头”；也不让全部照片带惊讶、暧昧或微笑。

用户要求互动感时，按 [镜头互动](camera-interaction.md) 明确画外同伴的触发与人物可见回应。保留“像在和持机朋友说话”的关系感；轻微探身、抬眼听清、展示手中物品是可选实现，不能只增加一句 looking at camera 就算完成。

## 多图不能只换背景

先规划每张的动作阶段、机位／距离、景别、目光与环境信息。例如同一次买画材：走近店面建立地点 → 停下看清单 → 收好清单准备进门。衣服、包与光线一致，画面叙事在推进。

用户指定 10 张时，设计 10 个有区别的有效瞬间，可跨数个明确的小事件。不要硬凑固定比例、固定六种模式或每种机位各一张。用户要求比较风格时，反过来固定人物、衣服、动作和地点，仅改变摄影表达，方便比较。

## 写成一条可以独立执行的 prompt

自然衔接身份参考与识别特征一次、衣服、动作与互动回应、摄影者的位置与景别、场景与实际光源、风格质感。顺序按画面重点调整，避免摄影关键词堆砌。分离身份参考与风格参考的用途。

以下是虚构人物的完整首次设计示例，不是任何真实人物资料，也不是 Ari 的默认特征：

> A 42-year-old man with short curly brown hair, warm medium-brown skin, brown eyes, a broad nose, a short neatly trimmed beard and an average solid build, wearing an oatmeal cotton T-shirt and relaxed dark trousers. He is making breakfast in a small lived-in kitchen, one hand setting a ceramic mug on the counter while the other rests naturally near a folded dish towel. He glances toward someone just outside the frame, mid-conversation, with a relaxed expression. A casual phone photo from chest height about 1.6 meters away, a 28 mm-equivalent field of view, slightly off-center framing and enough depth of field to read the kitchen. Soft side window light and a small warm ceiling light, believable mixed illumination, real skin and fabric texture, modest phone sharpening, no artificial portrait-mode cutout or studio polish. One visible person; an ordinary quiet morning, not a posed advertisement.

已有档案时，把第一句替换成该档案的精简身份块并传入其身份参考；不要借用例子的性别、年龄、肤色或胡须。带参考的 standalone prompt 仍写清画面，不只说“照参考图画”。
