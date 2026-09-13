# 镜头互动与在场感

镜头可以代表正在一起生活的同伴。互动感来自具体的来回：对方说了什么或正在看什么，人物因此怎样回应，以及画面里能看见的目光和动作。泛写 interactive、intimate、looking at camera 不足以交代这一点。

## 互动方式独立于摄影风格

| mode | 镜头的角色 | 画面线索 |
|---|---|---|
| observational | 记录日常的观察者 | 人物在完成自己的活动，不安排朝镜头的回应；适用独处或远距离纪实 |
| companion | 同行或同桌的同伴 | 共享桌面、并肩步速、同一视线高度；人物可以专注手头活动，不必始终看镜头 |
| responsive | 此刻正在被人物回应的同伴 | 听到一句话抬眼、轻微探身听清、回头等你跟上、把物品转给你看、等你的反应 |

用户说“互动感”“和我对话的感觉”时默认 responsive，无需再问模式名称。指定安静独处、不看镜头或纯观察时按其要求处理。互动程度由性格和事件决定，不自动解释为恋爱、暧昧、撒娇或身体接触；未定义的关系不写成既有事实。

这三个模式均可搭配手机、胶片、生活写真或电影感日常。摄影风格决定画面的质感，互动方式决定人物如何对待镜头。

## 每张明确五件事

1. **同伴位置**：镜头位于同桌对面、侧前方或同行者位置，决定高度、距离和目光落点。摄影者身份通常只需“画外同伴”，不要自动指定恋人或新造具名朋友。
2. **触发**：拍摄者问了一个与当前活动有关的问题、叫了人物一声、停下脚步、正在看人物手里的东西。新的触发属于本次 proposed 情境，不冒充真实经历。
3. **回应**：人物抬眼、转身、稍微靠近听、把书转过来、暂停动作等。探身可以保留，但由交流动机产生，肩颈和重心自然。
4. **目光和表情**：看向镜头后同伴的眼睛、短暂停留、随后回看物品；表情可以认真、好奇、忍笑或等候反馈，不固定每张正面微笑。
5. **可见证据**：写出画面中实际可见的转向、停止的手、递近的物品、留给同伴的空间等。触发声音本身不可见，必须有对应的身体反应支撑。

拍摄者可以完全在画外；单人画面依然有两个人的交流情境。没有要求自拍时用他人持机视角；不要自动加伸向镜头的自拍手臂、第二个人或画外人的手。物品递向共享空间，保持手臂比例和合理距离；不要为了靠近感让脸贴近广角镜头。

## 写入不同摄影风格

互动感是一种画面关系，可选轻微探身、抬眼回应、展示物品或回头等候等动作。焦段、光线、景深、色盘和修饰程度由本次摄影风格及场景决定，不绑定某段完整提示词。保持自然交流与动作中途的瞬间感即可，不要求每次同时使用浅景深、逆光、亮色包或同一种姿势。

可插入场景提示词的互动段如下；使用时把物品和触发换成本次真实设计，不把它当完整身份提示词：

> The camera occupies the eye-level position of a companion seated across the small table. Hearing a quiet question about the sketchbook, the subject pauses turning the page, lifts their gaze to the companion just behind the lens and leans forward slightly to listen. One hand stays on the open page while the other gently rotates the sketchbook toward the companion. Relaxed shoulders, a small attentive expression and a brief expectant pause make this feel like an ongoing exchange. The photographer remains outside the frame; the subject's hands and face stay naturally proportioned.

## 多图的回应节奏

同一组围绕一件事推进，例如“听见你问 → 把速写本转给你看 → 等你看完后继续翻页”。每张明确一个可见回应，用目光、手势和距离变化形成节奏。不要把每张都写成探身笑，也不要在用户明确要互动的一组里全程让人物朝远处出神。自然抓拍可以有镜头意识，不能用“抓拍”自动取消互动要求。

## 记录与检查

逐图 interaction 保存 mode、camera_role、trigger、response、gaze_target 和 visible_cues；摄影距离仍用 photography.camera.distance_m_intent，避免两处互相矛盾。新方案显式记录，旧 JSON 可缺省此块，不能把缺省解释为已完成互动设计。

responsive 需要非空 trigger、response 和至少一条 visible_cue；纯观察允许 trigger、response 留空。event.action、镜头参数、interaction 与完整 prompt 必须表达同一动作。实际看过图才在 QC 中说明互动是否成立；Schema 通过只证明记录完整，不证明人物已回应镜头。

[通用互动计划示例](../examples/generic-interaction.plan.json) 展示早餐桌边对画外同伴的回应，仍为未生图、未选择主身份参考的草案。
