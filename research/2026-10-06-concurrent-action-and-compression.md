# 2026-10-06 并发攻防与提示词压缩调研

本轮核查主事件聚焦是否被误用为“一次只准一人行动”，以及压缩是否丢失用户指定的同时接触、人物和镜头。当前技能原有“复杂事件拆成相邻窗口”的概括容易将围攻串行化，因此替换为先判断攻防关系、依赖和覆盖，再处理具体冲突。没有以新规则替代实际生成验证。

## 来源与固定版本

| 来源 | 已读范围 | 采用与舍弃 |
|---|---|---|
| [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0/tree/4668457e560eee06e95d7fcfdf441c8c0bba802e)，`4668457e560eee06e95d7fcfdf441c8c0bba802e` | 完整读取 [motion](https://github.com/Emily2040/seedance-2.0/blob/4668457e560eee06e95d7fcfdf441c8c0bba802e/skills/seedance-motion/SKILL.md)、[prompt-short](https://github.com/Emily2040/seedance-2.0/blob/4668457e560eee06e95d7fcfdf441c8c0bba802e/skills/seedance-prompt-short/SKILL.md)、[allocation-model](https://github.com/Emily2040/seedance-2.0/blob/4668457e560eee06e95d7fcfdf441c8c0bba802e/references/allocation-model.md) 和 `intent-vs-precision.md`；另读入口的质量检查与优先关系 | 采用以动作后果压缩空话、保留当前状态和接续、按镜头任务安排细节的思路。其“生成预算”属于作者经验模型，不能当作已知内部算力分配机制。拒绝把多角色接触统一减为一次、被动结果一律移出画面、完整中间表单或固定字数作为本项目通用要求；用户明确指定的镜头也不能仅因被归入较低类别而自动覆盖 |
| [allenGKC/Seedance-2.5](https://github.com/allenGKC/Seedance-2.5/tree/ebc68d3c19a62fba0f9ba9d2805af1f711a82aa7)，`ebc68d3c19a62fba0f9ba9d2805af1f711a82aa7` | 完整读取 [技能主体](https://github.com/allenGKC/Seedance-2.5/blob/ebc68d3c19a62fba0f9ba9d2805af1f711a82aa7/skill/seedance-25/SKILL.md) | 采用按因果组织多个事件、避免互相争夺控制的参考、局部问题局部修改的思路。将“同维度唯一来源”细化为属性和阶段不冲突，允许多图互补同一身份。本轮未核验其模型能力表，不采用所列版本、时长、原生延长或编辑能力作为本地执行事实 |
| [OSideMedia 分镜技能](https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/70754977d1884794963ac0a748eaaa85b6e9c82a/skills/higgsfield-shotlist-director/SKILL.md)，`70754977d1884794963ac0a748eaaa85b6e9c82a` | 补读提示密度章节的合并、拆段条件与数量门槛 | 同一空间和时间单元是否可合并，值得按当前事件判断；不采用超过两项强动作、三名重要人物或一个复杂特效就拆段的通用门槛。该文的 `OFFICIAL` 标签不代替供应商一手证据，不将其字数和时长上限固化到本技能 |

Emily2040 和 Allen 的完整仓库树及根目录 MIT 许可证均已读取；OSideMedia 的 MIT 许可在此前调研中已确认。只独立改写方法、例子和边界，没有执行或安装外部技能，也没有复制其提示模板。新来源之间的相似建议不计作相互独立的生成成功证明。

## 当前规则的修正

- [技能主体](../SKILL.md) 与 [视频文法](../references/formats/video-prompt-grammar.md) 不再将主事件等同于单角色动作；相关进攻、回应、支援和后果可以并发，先后依赖仍须明确。
- [战斗编排](../references/formats/combat-choreography.md) 补入明确指定同步接触的检查：各个接点是否有可用的兵器、肢体或术法承接，覆盖范围是否成立。
- 压缩按信息作用取舍。阵线与光纹若证明供能或接触，属于必需因果；不能因为属于特效词便删除。人数、字数、招式数不单独作为拆段依据。
- [素材与迭代](../references/formats/reference-and-iteration.md) 允许多个素材互补同一维度，按具体属性处理冲突，优先使用用户已经指定的局部关系。

## 文字核查

[素材适配案例](../examples/reference-adaptation.md) 新增一份完整的同步双挡压缩提示词与一组互补参考推演，未附真实素材。结合已有时间轴逐项核查：

| 条件 | 本轮文本结果与边界 |
|---|---|
| 三人、两个同时接点、一镜到底 | 保留两个分别由掌盾承接的攻击，不改成先后单挑；同步执行尚未生成验证 |
| 一记掌劲分层破盾 | 已有案例的多层反馈仍来自同一击，不因三个结果就强制拆成三个独立片段 |
| 近身枪客与远处符修施压 | 已有案例保留射线变化、同时回应和仍在活动的支援者，不把次要人物冻结 |
| 指定镜头或接触次数 | 压缩只处理非必要装饰，不能自动把固定单镜换成切镜、把多次接触改为一次 |
| 正面身份图与背面结构图互补 | 保留两份素材的用途，已有发式优先关系直接使用；未见附件不声称视觉核验 |

这些是人工文字对照，不是模型行为实验。它们能够检查当前文档是否自相矛盾，不能证明提示词变短或并发写法一定提高成功率。

## 验证记录

2026-10-06 完成验证：技能基础检查通过；仓库检查通过 85 个本地引用、20 个时间轴案例、22 个片段；28 项自动测试全部通过，`git diff --check` 通过。素材适配文件现有 11 组文字案例，本轮新增两组，未计入自动时间轴数量。

没有新的生成样片、音画审阅或平台能力验证。自动测试不判断多处接触是否实际同步，也不证明压缩后生成质量提高。
