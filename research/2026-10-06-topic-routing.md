# 专题拆分与按需读取

日期：2026-10-06。目的：在持续吸收打斗方法后，减少单一任务需要读取的无关规则，保留组合战斗的完整约束。本轮调整组织方式，没有增加招式配方或生成视频。

## 调研来源与取舍

### Seedance 技能的分层方法

核对 `LeoYeAI/seedance-skills@797e16efaa3c5ac01c0e391d0b8466a87cc5aadc` 的完整 [入口](https://github.com/LeoYeAI/seedance-skills/blob/797e16efaa3c5ac01c0e391d0b8466a87cc5aadc/SKILL.md)、[按需读取计划](https://github.com/LeoYeAI/seedance-skills/blob/797e16efaa3c5ac01c0e391d0b8466a87cc5aadc/references/progressive-disclosure.md)、[动作子技能](https://github.com/LeoYeAI/seedance-skills/blob/797e16efaa3c5ac01c0e391d0b8466a87cc5aadc/skills/seedance-motion/SKILL.md) 和 [MIT 许可证](https://github.com/LeoYeAI/seedance-skills/blob/797e16efaa3c5ac01c0e391d0b8466a87cc5aadc/LICENSE)。

该包标明来自 Emily2040/seedance-2.0，由 LeoYeAI 打包；这属于已调研来源的分层实现补充，不能当作独立团队验证过同一方法。值得采用的是明确读取条件、把大份参考留到具体任务需要时、区分规则主源和示例职责。未复制其子技能数量、安装路径、平台参数、固定动作配额或完整执行流程。

### Action Fight Prompt 的题材增量规则

核对 `kangarooking/director-skills@a827cccc4460c9ca01e8cc8abcf624fb2c5ed1bb` 的完整 [动作入口](https://github.com/kangarooking/director-skills/blob/a827cccc4460c9ca01e8cc8abcf624fb2c5ed1bb/action-fight-prompt/SKILL.md)、[题材参考](https://github.com/kangarooking/director-skills/blob/a827cccc4460c9ca01e8cc8abcf624fb2c5ed1bb/action-fight-prompt/references/scene-patterns.md)、[镜头与反馈参考](https://github.com/kangarooking/director-skills/blob/a827cccc4460c9ca01e8cc8abcf624fb2c5ed1bb/action-fight-prompt/references/camera-and-impact.md) 和 [MIT 许可证](https://github.com/kangarooking/director-skills/blob/a827cccc4460c9ca01e8cc8abcf624fb2c5ed1bb/LICENSE)。

题材参考只补当前题材的差异，有利于保留共同因果关系而不整套复制规则。本项目采用这种组织思路，未采用其统一 15 秒上限、固定 2–3 秒阶段、每段环境反馈配额、禁止固定机位、默认无音乐、巨兽首击必须失败、所有敌人必须不同脸或先确认阶段表的流程。相关通道限制与质量承诺本轮没有通过接口或生成验证，不引入本项目。

2026-10-07 更新核对：仓库 HEAD 为 `459debadf91f85b9603f7adb8c071fbdbf7b29e4`，相对上次快照新增三个提交。[版本比较](https://github.com/kangarooking/director-skills/compare/a827cccc4460c9ca01e8cc8abcf624fb2c5ed1bb...459debadf91f85b9603f7adb8c071fbdbf7b29e4)仅涉及 README、情绪表演和旅行视频技能；动作入口 blob 在两版均为 `d854c084d375a44e9a86f85335a513907c2fb551`，参考目录 tree 均为 `54896221efaa62d2283e691da8502e76859afdf5`。因此该打斗子技能内容未更新，沿用既有取舍，不重复计为新方法或独立证据。此次读取入口全文，并通过 GitHub API 核对比较结果及目录对象，没有阅读新增的无关技能或重新生成样片。

本轮外部文件只作为研究材料读取，未安装技能、执行脚本或调用其生成工作流。分层方法也与当前使用的 skill-creator 关于按需读取和避免重复正文的指导一致。

## 文件职责与内容保留

原 [战斗编排](../references/formats/combat-choreography.md) 包含 274 行、10,404 个字符，入口把近战、飞行、法阵和分身都指向它。调整后：

| 文件 | 当前职责 | 行数 |
|---|---|---|
| [战斗编排](../references/formats/combat-choreography.md) | 目标、近战、代价与恢复、压抵、缴械、节奏强度和情感选择 | 125 |
| [移动与在途攻击](../references/formats/movement-and-projectiles.md) | 移动方式、实体兵器往返、停射、控制与维持中断 | 45 |
| [力量与法阵](../references/formats/powers-and-formations.md) | 屏障、力量层次、相克、体型差、阵法附着与破阵 | 86 |
| [分身与多人协同](../references/formats/clones-and-multi-combat.md) | 分身数量和能力、多人持续施压、同步接触与射线 | 33 |

[技能入口](../SKILL.md) 直接链接这些专题，不要求先读取一个大目录再跳转。各专题只按实际需要交叉引用；御剑、分身与破阵组合时可以读多份，不能为了少读文件把同时发生的攻防拆成轮流演出。

拆分前保存了源文件快照，按七个完整内容块核对迁移后的正文；统一标题层级和块首尾空行后，所有块逐字保留且各出现一次。移动专题的小节标题升为二级，原有 23 个二、三级标题均在新的专题集合中保留一次。增加的是读取条件和导航，替换的是原总览句，没有改写动作规则来凑更短的文档。

原战斗编排路径仍可用，并提供三个专题链接。历史调研记录保持原来的观察与验证语境；[参考导航](../references/INDEX.md) 聚焦创作和验证用途，20 条原调研记录完整移入 [调研索引](INDEX.md)，再添加本条记录。素材适配中的分身引用改为直接指向新专题。

## 代表性读取范围比较

以下按“入口完整文本＋命中的完整编排参考”计算 Unicode 字符数，统一按 LF 换行；没有将其他本来不需要的参考加入旧方案。只处理某个专题的条件在表中明确，组合任务需要什么就读什么。这是文件长度比较，不是实际模型 token、响应延迟、选读准确率或视频质量测试。

| 请求范围 | 调整前字符 | 调整后字符 | 变化 |
|---|---:|---:|---:|
| 普通单段，入口已经足够 | 3,653 | 3,950 | 增加 8.1% |
| 近战、受力恢复与缴械细节 | 14,057 | 8,587 | 减少 38.9% |
| 只处理移动、飞剑往返与在途攻击 | 14,057 | 5,912 | 减少 57.9% |
| 只处理屏障、体型差或法阵机制 | 14,057 | 7,063 | 减少 49.8% |
| 只处理分身数量职责及多人关系 | 14,057 | 5,318 | 减少 62.2% |
| 御剑、分身与法阵的组合关系 | 14,057 | 10,393 | 减少 26.1% |
| 四类编排细节全部需要 | 14,057 | 15,030 | 增加 6.9% |

代价是入口从 90 行增至 93 行，以及专题的说明和交叉链接；因此不能宣称所有任务都更省。拆分的收益主要出现在只需要部分专题时，完整复杂任务仍以约束齐全为先。

快照、固定版本来源和比较明细位于本机 `D:/Temp/xianxia-routing-research-_xbitvf0/`，包含 `before/`、`before-sha256.json`、`combat-sections-before.json`、`files.json` 与 `routing-comparison.json`。公开记录已经给出文件职责、方法和结果，不依赖临时目录才能理解结论。

## 验证边界

内容保留和目录指向已按上述快照核查；原有 24 个时间轴案例、26 个片段本轮未改。技能格式检查通过；172 个本地引用及全部案例的时间轴结构通过；引用与时间轴的 18 项单元测试通过。没有指向原战斗编排文件内标题的 Markdown 链接需要迁移。上述检查不代表模型实际选读准确率或成片质量改善，抽帧程序本轮未改、媒体验证未重跑。

## 2026-10-07 整体复核

复核近期未提交修改的主入口、参考导航、案例增量及工具检查范围。修复一处发现路径遗漏：分镜拼图已在素材参考中说明，现在主入口的素材类型与读取路由、参考导航均明确包含分镜拼图；普通单段仍无需加载研究记录或全部案例。

本次完整运行 33 项测试通过：15 项媒体采样测试、18 项引用与时间轴校验测试。技能格式检查通过；仓库结构检查覆盖 233 个本地引用、25 个时间轴案例、27 个片段。新增素材条件没有被冒算为时间轴案例。数字仅记录本次快照，后续以实际检查输出为准。

本轮对近期修改的审阅确认：追逐案例保留原时长与持续追击结尾；抓腕案例仅删重复解释，仍有两处接点及先后释放；分镜与照明等条件明确保留用户指定分屏、剪影和风格化效果。工具测试验证抽帧、元数据和失败处理，不能证明这些提示词在生成模型中的表现。新增规则对应的真实输出对照、原速运动与声音审阅仍未完成，未给项目整体质量打分。

## 2026-10-07 章节入口复核

补做现有仓库校验器未覆盖的章节锚点检查：遍历公开 Markdown 中本地带 `#` 的链接，对目标文件标题生成小写、去标点、空格转连字符并处理重名后缀的候选锚点，核对 51 个链接，未发现无对应标题的候选。跳过 `.git`、`.local-evidence` 与缓存目录；没有将该临时检查加入正式校验器或增加测试数量。此为当前标题与链接的静态核对，未在 GitHub 页面逐一点击，也不证明外部链接可访问或模型会选择正确章节。
