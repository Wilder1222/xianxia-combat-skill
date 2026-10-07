# 2026-10-06 分身、幻影与残影调研

本轮检查当前技能的身份绑定规则能否兼容用户主动要求的分身。原规则已处理实体剑、剑气和三视图误生多人，但缺少同一外观对应多具身体时的数量、独立动作、持物与退场关系。本轮补足这些关系，仍由用户设定决定术法能力。

## 已核查的来源

外部文件只作为研究材料，未安装或执行其技能。下列固定版本和路径用于复查，不代表已经验证这些方法在本项目的生成效果。

| 来源 | 已读范围与价值 | 本项目取舍 |
|---|---|---|
| [AAAAAAAJ/ai-film-general-skill](https://github.com/AAAAAAAJ/ai-film-general-skill/tree/efedff4cf16f8bef8476945c2e3c95d48779cc26)，`efedff4cf16f8bef8476945c2e3c95d48779cc26` | 在前轮基础上补读 [武戏库的分身章节](https://github.com/AAAAAAAJ/ai-film-general-skill/blob/efedff4cf16f8bef8476945c2e3c95d48779cc26/references/seedance-action-design-library.md#分身)。把数量、生成来源、空间去向、伤害共享和回收一起考虑，能发现仅写“幻化分身”遗漏的状态 | 采用相关状态检查，不强制所有分身都从本体表面剥离，也不要求永远彼此留出空隙；允许正常接触和遮挡，按既有术法选择生成与退场方式。适用许可证仍未确认，没有复制原案例 |
| [cclank/lanshu-awesome-ai-video-kit](https://github.com/cclank/lanshu-awesome-ai-video-kit/tree/b4ceecc4ca27ded6b6f542b04ac756bf5bd7816d)，`b4ceecc4ca27ded6b6f542b04ac756bf5bd7816d` | 读取 [seedance-debugger](https://github.com/cclank/lanshu-awesome-ai-video-kit/blob/b4ceecc4ca27ded6b6f542b04ac756bf5bd7816d/skills/seedance-debugger/SKILL.md) 的身份漂移、双胞胎、参考人物过多、症状采集和双胞胎修复例；核查根目录 [MIT 许可证](https://github.com/cclank/lanshu-awesome-ai-video-kit/blob/b4ceecc4ca27ded6b6f542b04ac756bf5bd7816d/LICENSE)。按症状追查提示词与素材有助于缩小问题 | 采用预期人数与素材职责核查。全局禁止同脸人物会冲突于指定分身；不把三视图一律禁用，不采用缺少本轮对照支持的人数硬阈值或成功率数字 |
| [T8mars/minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8/tree/48a8c30366413add1ee15cab31a321e5ce236565)，`48a8c30366413add1ee15cab31a321e5ce236565` | 读取 [身份与风格轮转 skill 主体](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/skills/identity-locked-fashion-world-rhythm-carousel/SKILL.md)，以及关联花田案例的摘要、清单、来源、结构描述和 Seedance 文本。其来源、模型归属、派生模板和预览状态分开记录，便于追溯 | 将它作为“形象相似不等于同一交互能力”的对照；该 skill 面向风格轮转，不能直接用作战斗模板。未采用固定双模型输出、规定数量的身份锚点或固定收尾 |

T8mars 许可范围按其 [内容许可](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/LICENSE-CONTENT) 区分：原创摘要、结构描述和提示词等标注为 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，代码另用 MIT，第三方原始作品不随内容许可重新授权。本轮只提取判断方法并独立改写仙侠规则，未收入原视频、原提示词或风格轮转情节。

## 标题、模板和成片证据须分开

T8 的花田案例标题含“分身”，但已读 [Seedance 提示词](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/catalog/cases/x-chikazoemakoto-2098634525920354799-browser-2098634525920354799-video-1/prompts/seedance-2.0.md) 描述的是随手臂路线短暂出现的半透明动作回声。其 [来源记录](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/catalog/cases/x-chikazoemakoto-2098634525920354799-browser-2098634525920354799-video-1/source.json) 将 MiniMax H3 归属标为创作者声明，完整 MP4 标为桌面媒体包资源。

本轮没有观看该案例的 GIF、原帖视频或完整 MP4，也没有运行派生提示词。因而不能将标题、文本校验标记或仓库自评分数当作“可交互分身独立攻防已实现”的证据；更不能把作者的 H3 归属声明当成派生 Seedance 文本已经生成成功。这一对照只支持先检查实际行为定义，再决定分身能力和验证范围。

## 落实到当前技能

- [战斗编排](../references/formats/combat-choreography.md)：区分视觉残影、诱导幻象和可交互分身；按本次设定处理凝实或攻击能力，保留生成、独立行动、受击与退场。
- [素材与迭代](../references/formats/reference-and-iteration.md)：三视图提供外观，剧情提供身体数量；意外复制与指定同貌人物分别诊断，不能用全局禁同脸误删分身。
- [视频文法](../references/formats/video-prompt-grammar.md)：跨段携带仍在场的本体与分身、已退场者，避免重新补生或换兵器。
- [文字回归案例](../examples/behavior-regression.md)：新增“身法残影不新增攻击者”和“同貌分身分工与退场”，分别核查残影不承力和多具可交互身体的职责、数量与原剑归属。
- [素材适配案例](../examples/reference-adaptation.md)：新增明确要求同脸分身的场景，防止把参考视图数或防复制规则当成人数指令。

## 人工反例核查

| 反例 | 应有处理 |
|---|---|
| 来枪碰上纯视觉残影后反弹 | 保留穿过关系和后续去处；不能偷偷增加承力能力 |
| 保留本体另放两个分身，却只剩两具青衣身体 | 区分新增两个与总共三个，检查生成与退场阶段 |
| 两个分身只是和本体同步挥剑、没有各自目标 | 按请求分担牵制和推门，原剑不随外貌复制 |
| 分身被打散时本体同步倒地，但设定不共享伤害 | 只改变被命中的那具身体和其接触关系 |
| 推门分身消散时木门一起消失 | 先解除手与门的接触，真实门扇保留实际终态 |
| 用户要求同脸同衣，被修复为不同服装或删去分身 | 用生成来源和行动职责追踪，保留指定外观与数量 |
| 分身被柱子遮挡，下一段被当作退场后重新生成 | 区分遮挡、退场和观察未覆盖；携带真实的在场状态 |

以上为人工文字推演，不是独立模型盲测或视频评审。实际分身数量稳定性、肢体边界和多方交互仍需本项目样片验证。

## 验证记录

2026-10-06 完成验证：技能基础检查通过；仓库检查通过 65 个本地引用、17 个时间轴案例、19 个片段；28 项自动测试全部通过，`git diff --check` 通过。新增两例时间轴案例与一例素材适配场景完成上述人工反例核查；结果只用于相应检查范围，不为实际生成效果评分。
