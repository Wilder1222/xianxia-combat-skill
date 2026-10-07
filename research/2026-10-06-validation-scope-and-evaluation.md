# 校验范围与评估调研

日期：2026-10-06。目标：提高技能维护时的判断可靠性，避免结构分数与本机缓存掩盖实际问题。本轮运行了本地文本审计和仓库检查，没有生成或观看新视频。

## 来源与采用范围

### Hell Grind AIGC Skill 的静态审计

仓库版本固定为 `renmu2017/Hell-Grind-AIGC-Skill@742cb1fedfd862d7fad84a2bbe4c90cd71559fc1`；其 [MIT 许可证](https://github.com/renmu2017/Hell-Grind-AIGC-Skill/blob/742cb1fedfd862d7fad84a2bbe4c90cd71559fc1/LICENSE) 已核对。本轮阅读了完整 [审计脚本](https://github.com/renmu2017/Hell-Grind-AIGC-Skill/blob/742cb1fedfd862d7fad84a2bbe4c90cd71559fc1/skill/hell-grind-aigc-skill/scripts/audit_prompt.py)、[提示词评分说明](https://github.com/renmu2017/Hell-Grind-AIGC-Skill/blob/742cb1fedfd862d7fad84a2bbe4c90cd71559fc1/skill/hell-grind-aigc-skill/references/prompt-quality-rubric.md) 和 [项目检查说明](https://github.com/renmu2017/Hell-Grind-AIGC-Skill/blob/742cb1fedfd862d7fad84a2bbe4c90cd71559fc1/skill/hell-grind-aigc-skill/references/project-qa-gates.md)。

其有用之处是检查范围清晰、告警有位置和处理建议，并区分结构检查与成片审阅。脚本将非空输入从 100 分开始，按错误扣 15 分、警告扣 5 分；输出明确称为结构分数，不能将下述结果说成作者宣称的“视频质量评分”被推翻。

对完整脚本作只读审查后，在临时目录运行三个自行编写的输入，命令形式为 `python -X utf8 -B audit_prompt.py 输入.txt --medium video --json`。脚本仅读取文本并输出诊断，未安装外部技能或调用生成服务。取得脚本的 SHA-256 为 `b17645892afb3b7f18108e6a6daf7a24590e6a4118a414ec9b86d38e0245965f`。

| 自编输入 | 实际结果 | 可复现的边界 |
|---|---|---|
| 相隔十步且不移动，用一尺短剑直接抵住对方的盾 | 100 分，无告警，退出码 0 | 所需字段齐全不能证明触及范围成立 |
| 甲保持不动，乙奔跑接近 | 85 分，`P-CONFLICT-MOTION`，退出码 1 | 不同人物的动作被词语共现误判为冲突 |
| 前 4 秒固定机位，后 4 秒推进 | 85 分，`P-CAMERA-CONFLICT`，退出码 1 | 已分阶段的镜头动作被合并判断 |

三个输入的完整文本如下，可配合固定版本重现；它们是检查器的测试输入，不是推荐创作提示词。

```text
总时长8秒。场景为石桥。两名剑修相距十步，各持一尺短剑，双方脚下位置全程不变；不能延长兵刃，也没有飞剑、剑气等远程攻击。0-4秒：甲在原位伸直持剑手，用短剑剑尖直接碰到乙身前盾面。4-8秒：乙的盾挡住短剑，双方留在原位。摄影机固定。结尾画面为两人仍相距十步，实体短剑剑尖抵在乙的盾面。声音只有金属抵压声。
```

```text
总时长8秒。场景为石门前，甲全程保持不动守门，乙沿石墙奔跑接近。摄影机固定；结尾画面为双方同框。声音只有乙的脚步。
```

```text
总时长8秒。场景为石桥，两名角色持剑对峙。0-4秒：固定机位，双方分处桥两端。4-8秒：摄影机推进，靠近甲的持剑手。结尾画面为剑柄与甲的手。声音只有风声。
```

这些例子支持“静态告警须按主体和阶段复核”，不支持断言该技能的所有建议无效，也不证明任何生成模型会如何执行。这三个完整 JSON 结果和输入留存在本机临时目录 `D:/Temp/xianxia-validation-research-mld4_mkg/audit-fixtures-3d3kul4u/`；公开记录不依赖该目录才能读懂结论。

### SkillPE 的候选技能评估

[SkillPE 预印本 v1](https://arxiv.org/html/2609.34335v1) 发布于 2026-09-28，页面许可为 CC BY 4.0。本轮核对附录 D.4、D.6 与 A：候选变化保留用户语义，以原始请求和实际生成视频评估保真及表现，要求先列可观察证据。其研究限于两种生成模型与 10 秒短片，不能据此证明本技能或所有模型有效。

本项目据此补充比较方法：候选共享原始需求，完整保留各自提交文本；关键要求是否实现与审美收益分别记录。后一句的“关键事件缺失不能由平均分抵消”是本项目对战斗约束的应用，不声称是论文所有候选选择策略。未复制其固定技能数量、变异配额、10 秒格式、评分尺度或自动调用链；也未把论文报告的提升记作本项目成绩。

## 本项目引用检查的实测问题与修复

原 [检查器](../scripts/validate_repository.py) 遍历全部 Markdown，仅跳过 `.git`；只要链接目标存在且位于仓库内就接受。此前将抽帧材料写入 `.local-evidence/`，因此出现两个独立问题：

1. 正常公开文档只含一个有效链接时，检查结果是零错误、一个引用；加入 `.local-evidence/report.md`，其中链接到不存在的 `missing.png`，就变为一个错误、两个引用。本机分析笔记改变了公开文档的检查结果。
2. 让公开 `SKILL.md` 指向实际存在的 `.local-evidence/report.md`，原检查返回零错误、一个引用。该目录被 Git 忽略，文件存在不能证明公开仓库中的链接可用。

在 [测试文件](../tests/test_validate_repository.py) 新增四项回归：本机笔记不改变结果、现存本机笔记不能成为公开引用、嵌套文档不能引用本机图片、类似 `.local-evidence-guide` 的普通目录仍受检查。修复前共运行 18 项测试，三个测试方法暴露问题，按子测试计五个失败；修复后 18 项全部通过。

修复对 `.git`、`.local-evidence`、`__pycache__` 作完整目录名判断：跳过其中的 Markdown，并拒绝普通文档指向其中的已解析链接。其他新建文档仍被检查，不要求先提交或依赖 Git 已跟踪列表。本轮未实现通用 `.gitignore`、完整 Markdown 语法或页内锚点解析。

本机资料可在公开记录中以代码格式标注来源与位置，供复查定位；不能把它包装成读者可打开的仓库文件链接。公开媒体本身的授权、来源和观察范围仍按既有要求记录。

## 落地与验证

- [素材与迭代](../references/formats/reference-and-iteration.md)：增加原始需求比较依据和静态告警复核方法。
- [抽帧说明](../references/formats/video-evidence-tool.md)：明确本机材料与公开引用的关系。
- [文本回归案例](../examples/behavior-regression.md)：说明引用检查的实际范围。
- 检查器与测试已完成上述失败复现和修复验证；时间轴案例内容及抽帧程序本轮未改。

最终复查：技能格式检查通过；137 个本地引用、24 个时间轴案例、26 个片段通过；引用与时间轴的 18 项单元测试通过。`git diff --check` 未发现格式错误，28 个未跟踪文本文件的尾随空白检查通过。抽帧测试本轮未重跑，不能将上述 18 项记作媒体验证。

本轮结果是检查器可靠性及评估方法改进，不是新的视频质量证据。


## 2026-10-07：文字合规与实际分镜图偏差

新来源 [Open Film Skills](https://github.com/62656456/ai-film-skills/tree/11ad3a8fa5fe18b00087cdfa08300bc7689dcb9b)，Git 固定提交 `11ad3a8fa5fe18b00087cdfa08300bc7689dcb9b`。全文读 `skills/ai-storyboard-director/references/fight-design.md`、七题材 `report.md` 及 `THIRD_PARTY_NOTICES.md`；定向读 `storyboards.json` 的近身打戏共同故事与 B 版、`image-prompts.md` 的对应 B 版提交段落和 `image-manifest.json` 对应条目。入口及其余模块未通读，未执行外部技能。仓库展示 Apache-2.0 标记，本轮未做完整许可审计，未复制来源正文、角色模板或媒体进本项目。

来源打戏模块区分攻防条件与摄影选择，并保留施力方反作用及多人场内行动；多数已被本项目覆盖，不重复扩写。报告保留失败观察、文字检查与图像检查的差别，值得继续核验，但报告中的整批统计仍属作者陈述。

本次实看[近身打戏 B 版原图](https://github.com/62656456/ai-film-skills/blob/11ad3a8fa5fe18b00087cdfa08300bc7689dcb9b/docs/research/skill-overhaul/seven-genres/images/04-fight-b.png)：941×1672 像素，SHA-256 `fa47c5be9eb04384b4cc4a01c44ea261a861c00f2e7097e36b3561144761985e`，与来源清单一致。查看整板并重点对照第 4—6 格；第 6 格人物朝向画右，画左扶绳的手臂可追溯到其自身右肩，另一臂垂在身体另一侧。原稿与实际生图提示的第 4、5 镜明确要求左手连续支撑，故此处存在左右职责偏差，不能仅凭格下说明文字判断图像正确。其余格与其他版本未作完整独立审查，不把作者整批结论当作本次全部复核结果。

这支持既有的“按实际输入与输出定位问题”规则，不能将图像偏差直接诊断为正文漏写，也不能证明多加一次左手要求就会修好。未看视频或听音轨，静帧无法验证转身、绊腿、桥面回摆或 30 秒运动节奏。来源另称三版本图像共用外观参考、不是严格盲测，本轮不据问题数排名。

人工观察保存在被忽略的 `.local-evidence/open-film-storyboard-20261007/observation.json`。局部工作树提取失败后改用固定提交的 `git show` 取得对象并核验指纹，未改动来源仓库内容。下一步若研究该来源，应先查未读内容或另一个具体媒体问题，不再把本图当作新增独立样本。


同版超能力图复核：实看[超能力 A 版原图](https://github.com/62656456/ai-film-skills/blob/11ad3a8fa5fe18b00087cdfa08300bc7689dcb9b/docs/research/skill-overhaul/seven-genres/images/07-superpower-a.png)，941×1672 像素，SHA-256 `065e2738737b1ceaaa730a09b91f154d3a1b8d00df68b8451bec421e4549dcbc` 与清单一致。定向阅读共同故事、A 版第 3、4 镜及实际生图提示相应段落，明确要求隔空托举，局部描述同时使用向上撑起、托举等动作词。全图查看后重点对照第 1、3、4 格：第 1 格螺栓与掌心之间有可辨空隙；第 3 格右侧和第 4 格左侧，手指与板底轮廓相接，缺少可辨的隔空距离。

本次结论限定为隔空关系没有清楚呈现。不能仅凭投影相接证明三维实体接触，也不能因整段已写“隔空”便把画面记为通过；更不能证明是哪一句措辞导致该结果。局部改写时可明确手掌与作用物的间隔、作用来源及取景，在相同任务约束下比较输出；不得顺手取消身体承重代价或改成实体托举。该建议尚未生成重测，不记为修复成功。与前一张打戏图共两张独立静态分镜板，仍不是两段生成视频，也不是三版整体排名。观察文件为被忽略的 `.local-evidence/open-film-storyboard-20261007/superpower-a-observation.json`。

本地适配复核：上述隔空观察用于检查近身编排的能力例外，在既有规则中明确非接触方式与身体代价分别按设定处理；另用独立石盾受掌劲案例同时保留间隔、传力和守住入口，并给出不传回重量时不强加下沉的反向条件。没有复制来源救援情节，也未将这一文字修正计为生成效果改善。


同版拉片案例续读：全文读取 `skills/ai-storyboard-director/references/fight-reference-case.md`。该文件引用[佳聪《这样的打斗不热血吗？》](https://www.douyin.com/video/7677917664052134121)，作者记录时长 49.04 秒、一般约每秒 2 帧和重点约每秒 6 帧抽样，明确未完成连续音画观看。本轮原作品链接无法通过浏览工具访问，未取得或观看原片；时长、采样密度与各时间点观察均只属于来源陈述，不能并入本项目已看媒体数量。

案例的取舍较具体：按接触与全身位移需要变换观看尺度，身体高低变化由当前应答造成，拼接段落不强行解释为同一因果链，斜构图不证明连续滚转。这些与本项目已有镜头覆盖、支撑、切点及采样边界规则重合，故不追加运行规则，也不复制其动作顺序、特效或固定单变量要求。当前可复用结论是这份文件的证据表述方式；对原片效果与作者时间点判断的独立复核仍未完成。


## 2026-10-07：LTX 文本检查器的误报与漏检

来源 [AI-KSK/ltx-2-3-prompt-director](https://github.com/AI-KSK/ltx-2-3-prompt-director/tree/c9487b13178cf3c0c109ce55c49828df8909a7c0)，实取提交 `c9487b13178cf3c0c109ce55c49828df8909a7c0`。全文阅读 `scripts/ltx_prompt_lint.py` 和 `references/troubleshooting-and-qa.md`，另读 README 页面与仓库文件清单；未通读技能入口和其他参考。文件清单未见许可证、媒体样片或测试结果；QA 中的 A/B 章节是测试方法，不是已执行结果。未安装技能、调用生成服务或采纳其平台参数。

检查器仅使用 Python 标准库，读取指定文本并输出启发式诊断，源码明确不预测生成质量。读完代码后在临时目录执行两个自编英文输入，固定 `--mode t2v --duration 10 --json`：

| 自编输入条件 | 实际结果 | 说明 |
|---|---|---|
| 起初固定机位，随后开始环绕，最后人物停下；时序明确 | 退出码 1，`CAMERA_CONFLICT` | 全段关键词匹配未区分阶段，正常的摄影顺序被报冲突 |
| 两人始终相隔十米，各持一米普通剑，不接近、不离手，却要求实体剑在中间碰撞 | 退出码 0，`CLEAN` | 未检查距离与可达范围；文字通过不能证明接触成立 |

两例结果保存在被忽略的 `.local-evidence/ltx-lint-review-20261007/observations.json`，只证明该版本对这两个输入的行为。未测全套规则，不推算整体准确率，也不将合理告警一概忽略。QA 正文允许有意时序转换，与脚本的整段匹配能力有差别；其“只改一个变量”和简化动作的建议仍须服从本项目既有的有界联动与用户约束。

本项目已有关键词按主体和阶段复核、结构校验不覆盖攻防语义的规定，因此本轮仅补充可复现证据，不引入该检查器作为质量门槛，不为消除误报删掉指定镜头或添加无意义关键词。


### 两个反例的精确复现输入

以下为本项目自编的实际输入，英文用于匹配该检查器的英文词表。将代码块各保存为标注的 UTF-8 文本文件，在上述固定提交的外部仓库目录运行；不需要生成模型。指纹按不含末尾换行的 UTF-8 输入计算。

`camera_phases.txt`，SHA-256 `147c6fabae7bc04f778c6b4d13fcb7a789e536cb000fc550092436d28a961773`：

```text
At first, a static camera watches two adult swordsmen standing on a stone bridge. Then the camera begins to orbit them as they slowly circle each other. Finally they stop without attacking.
```

`unreachable_blade.txt`，SHA-256 `0f7b485369df694090dba9233eed0a2d8b7cd1ba3af98c4f98307e99b8b32a2b`：

```text
Two adult swordsmen stand ten meters apart. Neither moves closer, neither sword leaves its hand, and each ordinary sword is one meter long. Then their physical blades collide in the center between them. Finally they lower their swords. A locked camera records the whole event with quiet wind.
```

```powershell
python -X utf8 -B scripts/ltx_prompt_lint.py camera_phases.txt --mode t2v --duration 10 --json
python -X utf8 -B scripts/ltx_prompt_lint.py unreachable_blade.txt --mode t2v --duration 10 --json
```

分别检查每条命令的退出码，不能用第二条成功覆盖第一条失败。上述表格记录该固定版本的预期诊断；复现用于检查文本工具的边界，不用于接受或拒绝实际打斗成片。


同版分段控制续读：定向阅读 `references/prompt-relay.md` 的接口依赖、语法、全局与局部职责、时间分配、转场、首帧及失败处理章节。来源明确其为社区工作流控制，不能把竖线、段名或相对权重当作所有接口都支持的语法。可借鉴的是先确认时间单位和条件职责；静态开场与结尾停留的比例建议不作通用要求。本地平台检查补充分段单位与实际切镜的区分，首帧相抵案例补充不因全局身份描述新增冻结开场的反例。未运行相关节点或验证其具体参数；条件边界、权重转换和实际镜头仍需目标接口与返回媒体确认。
