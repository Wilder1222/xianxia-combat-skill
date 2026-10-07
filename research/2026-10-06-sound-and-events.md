# 2026-10-06 声音与攻防事件调研

本轮检查兵器接触、持续压剑、护盾与短法令的声音描述，补足无配乐、无对白、人物无声和全静音的边界。重点是让声音服务已经成立的动作，并在修正时区分画面错误与音效错误；没有生成或听辨新的样片。

## 来源与采用范围

| 来源与固定版本 | 已读范围 | 本项目采用与舍弃 |
|---|---|---|
| [snowfrost/skill-movie](https://github.com/snowfrost/skill-movie/tree/69f6db670ecf305e84f199e418bddbf2c1d988fe)，`69f6db670ecf305e84f199e418bddbf2c1d988fe` | 完整读取 [cinematic-music-sound-design/SKILL.md](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/cinematic-music-sound-design/SKILL.md) 与 [sound-design-and-mix.md](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/cinematic-music-sound-design/references/sound-design-and-mix.md) | 声源、材质、动作阶段、主次层次和有意留白具有参考价值。独立改写为接触、滑动、分离与术法解除的判断。不继承强制声音层、固定短片段落、完整配乐交付表，或为绝对静音保留底噪的建议；人物无声时也不能补喘息来确认命中 |
| [beshuaxian/higgsfield-seedance2-jineng](https://github.com/beshuaxian/higgsfield-seedance2-jineng/tree/83dcb10ee38c9694ac0f455ec55a62f2be3b8a14)，`83dcb10ee38c9694ac0f455ec55a62f2be3b8a14` | 补读 [打斗章节](https://github.com/beshuaxian/higgsfield-seedance2-jineng/blob/83dcb10ee38c9694ac0f455ec55a62f2be3b8a14/skills/05-fight-scenes/SKILL.md) 的完整声音制作小节及相关错误示例 | 接触材质、挥动声与环境响应可分开考虑。其“后期添加”表述不能作为当前平台不支持原生声音的证据；重击前静默、高潮管弦和统一低频重击只适用于选定风格，不作为每段默认 |
| [Google 官方视频提示词指南](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) | 阅读音频章节，记录本轮检索日期为 2026-10-06 | 官方指南区分音效、环境声与对白，并建议独立句子描述声音。采用分类与清晰表述的思路；该页的特定模型说明不证明本地工具支持，也不证明 Seedance 或其他平台能力 |

外部文件仅作为研究资料，没有执行、安装其技能或制作控制音轨。Snowfrost 的固定版本仓库树完整，发现的许可证位于其他技能或音效资源目录，未找到适用于本次声音技能的许可证；Beshuaxian 的适用许可仍未确认。本项目记录来源并独立编写规则和案例，不复制其示例提示词。Google 文档的能力说明仅用于提醒按具体模型核查，没有据此发起生成。

## 补足的决策

- 声音范围来自用户要求，无配乐、无对白、人物无声、全静音各自保留，不能统一简化成同一开关。
- 落空与击中有不同声音来源；连续贴刃摩擦不等于连续新命中，开场已相抵时不补造起始撞击，分离后允许已发生声音的余振衰减。
- 法令与步法、结印并行；对手的攻击继续推进。仅在故事要求时安排词句，不能把念咒当成默认停战时间。
- 画外预警、声桥、残响与主观静默可以有明确叙事用途，不能一律判成同步错误，也不能用它们替代指定可见的接触。
- 按已有正确动作修正音效，不将“听见击打声但画面没有接触”一律归因于画面漏拍。若需要独立声音修正，先核查有无相应能力；整段重生成会影响画面，必须准确说明。
- 分别记录观看和听辨范围。音轨存在、波形或语音转录只提供有限信息，不能证明音画关系、听感和口型通过。

这些是针对本项目缺口的编排与审阅规则，不是所读仓库已经验证过的模型成功率结论。

## 修改与文字核查

- [技能入口](../SKILL.md) 增加声音范围与按需路由，详细规则留在 [视频文法](../references/formats/video-prompt-grammar.md)。
- [平台执行](../references/formats/platforms-markets.md) 分开创作意图、原生音频和后期能力；[素材与迭代](../references/formats/reference-and-iteration.md) 补足只修声音及实际听辨的边界。
- [时间轴案例](../examples/behavior-regression.md) 的既有压剑场景加入无配乐、无对白和连续摩擦声；新增短法令与追击并行案例，区分木杖触盾、滑动、撤盾的声音。
- [素材适配案例](../examples/reference-adaptation.md) 增加四种声音范围的独立变体与声音修正推演，保留原动作和时长。

人工核查覆盖：无配乐是否误删指定法令；人物无声是否残留喘息；静音是否偷加底噪；开场相抵是否伪造撞击；压剑是否被配成多击；撤盾是否凭空爆炸；念咒是否让追击停止；只修声音是否无故重写动作。上述核查针对本轮文本，不代表实际样片中的音效、口型或同步表现。

## 验证记录

2026-10-06 完成验证：技能基础检查通过；仓库检查通过 79 个本地引用、20 个时间轴案例、22 个片段；28 项自动测试全部通过，`git diff --check` 通过。

已有自动测试只验证引用、时间轴与抽帧工具行为；没有音频生成、播放听辨或本项目声音效果对照试验，不能以这些检查替代音画质量验证。
