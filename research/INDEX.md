# 调研索引

维护或审阅时按问题追溯来源、采用理由和验证边界。日常创作从 [技能主体](../SKILL.md) 和 [参考导航](../references/INDEX.md) 进入，无需逐篇加载调研记录。历史记录中的验证数量只代表记录当时的状态。

需要横向选择方法时，先读[已读打斗方法的选择与验证优先级](2026-10-07-method-selection.md)。该表汇总已有证据与待验证问题，不作为生成效果排名。

用户提供版本的变更去向见[修改版 Skill 融合记录](2026-10-07-user-skill-merge.md)，其中区分新增方法、已覆盖内容和与现行约束冲突的旧模板。

## 常见来源去重入口

下表覆盖近期重复命中的来源，并非完整候选目录或质量排名。短提交号用于定位，记录内保留完整提交链接和读取范围；它们是已读快照，不表示远端最新版本。再次命中时先比较仓库、文件与版本：同版同文件优先复用记录，读未覆盖段落时补充范围；版本变化后再检查相关差异。同一仓库的多篇文件、同一文件的多次阅读和同一样片的重复抽帧，都不自动构成独立验证。

仓库提交变化不等于目标技能更新。可先查看相关路径的差异或文件 blob、参考目录 tree；内容相同就保留原方法结论。对象相同只证明版本内容一致，不证明外部链接仍可用、模型接口未变或视频效果成立。

| 来源与已读版本 | 已覆盖内容与记录入口 | 后续关注点 |
|---|---|---|
| `SkillDB / storyboard-fight-choreography` · 2026-10-07 页面 | [分镜模板的适用边界](2026-10-07-method-selection.md#免费重试分镜模板的适用边界) | 已读正文、规格与反模式；未取得固定版本、独立许可或生成样片，不导入停顿、环境互动配额与击倒结尾 |
| `maciejdzierzek/kling-ai-prompt-generator` · `248b9a275fed` | [Kling 社区 Skill 排错取舍](2026-10-07-combat-pipeline-density.md#kling-专用社区-skill-的排错取舍) | 定向读工作流、语言、提示及排错段落；不采用卡在 99% 等于缺少动作终点的因果断言，未验证其参数与效果排名 |
| `JOKER141/BUNNY_H3_Conditioning_Bridge` · `1c46814a7034` | [工作流内嵌兵器模板](2026-10-07-combat-pipeline-density.md#h3-工作流内嵌兵器模板的选择性核查) | 1038 行文本全文已读，一对四合成对比抽看 11 张静帧；两路进度不同、完整条件未齐，不能归因到模板或组件；未安装，同版模板无需重读 |
| `LearnPrompt/awesome-seedance` · `ea45dc0cc812` | [连续攻防模板及采用边界](2026-10-07-awesome-seedance-retests.md#2026-10-07awesome-seedance-连续攻防模板筛选) | 已核对四例复测字段；巷战复测 23 张、赛博复测 30 张及来源关联视频 27 张静帧已看，风格与片尾差异可见；原速和完整输入未验收，与 GoodCase 属同一策展体系 |
| `CY-CHENYUE/martial-arts-director-cy` · `65c7c1dd35fc` | [兵器词典与适配边界](2026-10-06-motion-reference-adaptation.md#2026-10-07-兵器词典与实际动作适配)、[沙漠案例图及视频抽样](2026-10-07-cy-desert-media.md) | 已看分镜图、30 张全片抽样及接架窗口的 24 张连续帧；双持局部可见，接架处连接仍受重叠遮挡限制，未验收原速或声音 |
| `keithwalsky-ship-it/UGC-ai-prompt-skill` · `58c0542568cd` | [Cinema 打斗章节与上游内容比较](#ugc-ai-prompt-skill-的实测声明与采用边界) | 对应打斗整节与 OSideMedia 固定版本完全相同，不作为独立实测来源；整份文件存在其他差异 |
| `pixelab-ch/higgsfield-skills` · `2f6aa1090ffe` | [打斗入口、多人章节及上游归属](2026-10-06-concurrent-action-and-compression.md#同源候选pixelab-ch-的多人编排模块) | 改编自已读 beshuaxian 项目；未取得运行结果，不作为独立效果验证或默认模型路由 |
| `CyberJ0605/cinematic-video-prompt-engineer-skill` · `53bdce34fd41` | [连续性与竖屏适配全文、近身长镜头及测试定向片段](2026-10-07-cinematic-fight-and-reference-coverage.md) | 核查换机位后的参考覆盖及裁切范围；四个演示视频未看，不采用固定动作配额与默认换机位 |
| `Yunwuxin-666/Wuxin-Film-Skill` · `49146aea4dc8` | [四份动作/特效文件及五份评估/参考职责文件全文](2026-10-07-wuxin-action-and-coverage.md) | 区分硬切与连续运镜、绳带连接与牵引、材质与完成度参考；评估材料为方法和输入，未取得对应运行结果 |
| `wuwangzhang1216/DirectorSKILL` · `c65ae0d144570` | [连续性与易手](2026-10-06-weapon-transfer-and-continuity.md)、[镜头几何与走位取舍](2026-10-06-spatial-direction-and-camera.md) | 各文件为定向阅读，走位全文返回曾截断；不采用通用单人移动限制或未经验证的生成阈值 |
| `AI-KSK/ltx-2-3-prompt-director` · `c9487b13178c` | [QA 与文本检查器的两个实执行反例](2026-10-06-validation-scope-and-evaluation.md) | 已复现阶段镜头误报与不可达接触漏检；未评估生成质量，不将 CLEAN 当作攻防通过 |
| `62656456/ai-film-skills` · `11ad3a8fa5fe` | [打戏模块、拉片案例、三版分镜报告及三张实际图像核验](2026-10-06-validation-scope-and-evaluation.md) | 三张分镜图已对照输入；镜内时序示意与人数分别核查，整批统计仍为作者报告，未做视频或版本优劣验证 |
| `hypit-ai/hypit` · `7f730abf72fa` | [视频导演与参考关系](2026-10-07-reference-request-mapping.md) | 本轮只读两份方法页和根许可证，不将其包语法与模型选择当作通用接口 |
| `jiayushi1-ux/script-to-shot-engine` · `e139226e935e` | [入口、动作与接续规则、素材协议、渲染器、徒手及一对多示例](2026-10-07-subjective-view-and-contact.md) | 采用视点与动作相容及群体人数检查；不采用固定镜头配额或焦距到景别的固定映射，尚无对应媒体验证 |
| `irenerachel/fight-prompt-director` · `fee4387b4c53` | [入口与诊断](2026-10-06-combat-skills.md)、[目标策略复核](2026-10-07-objectives-and-tactics-audit.md) | 现有目标与因果方法已采用；同版固定配额与三方案要求无需反复评估 |
| `snowfrost/skill-movie` · `69f6db670ecf` | [起始范围](2026-10-06-combat-skills.md)、[接触关系](2026-10-06-sustained-contact.md)、[地形](2026-10-06-terrain-and-traversal.md)、[双人抓握](2026-10-07-paired-body-control.md)；各文件有全文与定向阅读之别 | 先定位未读文件或新增方法；不能把大量参考文件视为多套独立实测，子目录许可仍按原记录处理 |
| `nolanx-ai/nolanx.ai` · `595d86364377` | [动作镜头](2026-10-07-occlusion-and-return.md)、[模块化提示](2026-10-07-prompt-compression-scope.md)、[命中模板](2026-10-07-hit-marking-style.md)、[灯光](2026-10-07-magic-lighting.md) | 四份方法分别采用或舍弃；尚无本项目生成对照，不将模板参数当模型能力 |
| `landon2022/minimax-h3-video-prompt` · `32c0fb6f81c9` | [战斗参考全文与诱招判断](2026-10-06-feints-and-perception.md) | 未确认目标文件许可；佯攻可失败，不再导入固定交换数与飞行落地限制 |
| `dgroch/higgsfield-prompt-engineer` · `fdc98872a7cf` | [战斗入口及评测边界](2026-10-06-feints-and-perception.md)、[校验与评估](2026-10-06-validation-scope-and-evaluation.md) | 区分生成成片评审、文本自评和静态量表；发现新结果时核对原始输入与媒体 |
| `zlbigger/story-video-director` · `ecacc4fd125c` | [表演参考的目标、阻碍、策略与诊断片段](2026-10-07-objectives-and-tactics-audit.md) | 仅定向阅读；不套用固定节拍数量、自评分或每场必须换策略 |
| `kangarooking/director-skills` · `a827cccc4460` → `459debadf91f8` | [动作入口、题材与镜头参考及版本复核](2026-10-06-topic-routing.md) | 仓库新增三个提交，但打斗入口与参考目录内容未变；沿用原取舍，避免整包更新被误认作打斗方法增量 |
| `scenario-labs/skills` · `91caa011e137` | [分镜入口及三份参考全文](2026-10-07-continuity-versus-cuts.md) | 已覆盖串联生成、分镜绘制与视频提示；作者样片经验尚未独立复核，固定格式、配乐与摄影限制不作通用规则 |
| `ouyangevan/codex-short-drama-pipeline-skill` · `a669c98515f2` | [入口与九份战斗核心模块全文](2026-10-07-combat-pipeline-density.md) | 已评估九份模块，并读法相示例、定向检查执行提示字段；完整 schema、其余实例及媒体仍未核查 |
| `Emily2040/seedance-2.0` · `4668457e560e` | [动作与压缩](2026-10-06-concurrent-action-and-compression.md)、[接续计划与观察](2026-10-06-continuation-and-observed-state.md)、[特效终止](2026-10-06-emission-and-control.md) | 各记录区分全文与定向阅读；其派生包与引用段落不作为独立验证 |
| `OSideMedia/higgsfield-ai-prompt-skill` · `70754977d188` | [分镜密度及动作与表演拆分片段](2026-10-06-concurrent-action-and-compression.md)、[Seedance 接续与素材片段](2026-10-06-continuation-and-observed-state.md) | 未通读整套技能；保留情绪导致的动作因果，不默认拆镜；平台参数仍需一手核实 |

本项目已取得两条 RunningHub 实际样片：首条接点解除及用户反馈的动作节奏未通过，见[首条记录](2026-10-07-method-selection.md#runninghub-国际站预算内实际出片与局部审阅)；三轮连续攻防候选经全片 193 帧静帧概览及部分大图检查，发现接招转换、额外兵器、攻防对应、末态分离及取景失败，见[第二条记录](2026-10-07-method-selection.md#三轮攻防候选的第二条实际样片)。两条共花费 1.84 美元，原速节奏及声音尚未完成验收。模型和请求都已改变，不能当作同条件提升证据。继续增加文字案例或来源条数不能补足媒体证据；生成执行仍以用户请求、预算和可用工具为准。

## 候选来源核验异常

### UGC-ai-prompt-skill 的实测声明与采用边界

2026-10-07 检索到 [keithwalsky-ship-it/UGC-ai-prompt-skill](https://github.com/keithwalsky-ship-it/UGC-ai-prompt-skill/tree/58c0542568cd2aa6636c0c7b149ab073858c0dc6)，远端 HEAD 为 `58c0542568cd2aa6636c0c7b149ab073858c0dc6`。核查完整递归树（未截断），未发现 MP4、WebM、MOV 或 GIF；这不排除仓库外另有视频。读取根 MIT 许可，版权标为 O-Side Media；README 的徽章及安装命令也指向 OSideMedia 上游，因此不能直接视为独立测试来源，尚未做全部文件的同源差异比较。

定向读取 [Cinema Skill](https://github.com/keithwalsky-ship-it/UGC-ai-prompt-skill/blob/58c0542568cd2aa6636c0c7b149ab073858c0dc6/skills/higgsfield-cinema/SKILL.md) 第 1405–1484 行。该段自称经过实测，但没有附逐次输入、模型设置或配对媒体；建议用笼统打斗、接触前后剪辑和容易隐藏漂移的环境规避精确动作。不能据此把其对拳脚、道具或擒拿的失败断言扩大到所有模型，也不采用这些方法替换当前明确的连续剑斗接触与回应。未通读整个入口、安装或运行外部工作流；本次不新增创作规则，保留来源筛选结果以防重复吸收。

随后实取两份固定版本的同路径文件作内容比较，OSideMedia 远端 HEAD 仍为 `70754977d1884794963ac0a748eaaa85b6e9c82a`。上游文件为 108850 字节、SHA-256 `f3045ba3ed58dd4540cc9701579d7676a9a2291fd7d80f8112b2c6a1a72ed628`；UGC 文件为 114822 字节、SHA-256 `d81eb17534437a9d28e85884a4babae3fb3a3bafded0543a02c4ebffc2369876`。两份文件整体不同，但从 `## Fight Scene & Action Design Rules (Tested)` 到下一处二级标题前的完整章节均为 4655 字符，UTF-8 SHA-256 同为 `7964ed7aabe08359414142911bda2bd066c01538963c1af61a9a3a69a8cf28a1`，逐字符相等。因此该章节只记为一份方法与作者经验声明，不作为两个来源相互佐证。文件比较不代表其余全文已人工阅读，也未证明整个仓库相同。

### MuAPI 聚合页与原仓库定位

2026-10-07 检索到 [muapi-ai-fight-scene 聚合页](https://claudeskills.info/skills/samuraigpt/generative-media-skills/muapi-ai-fight-scene/)，页面展示分镜到视频的技能正文，但所指 `samuraigpt/generative-media-skills` 经 GitHub API 解析为 `Anil-matcha/open-dots`。Git 实取 HEAD 为 `3d8de1cd6657c6d70583f34b89c2dc034512c1ea`；该提交的完整递归树返回 `truncated: false`，不含所指 `library/motion/ai-fight-scene` 或任何 `SKILL.md`。另定向读取 README 开头，内容为代理工作区项目，与聚合页的打斗技能描述不同。可复核 [当前仓库解析](https://api.github.com/repos/samuraigpt/generative-media-skills) 与 [固定提交文件树](https://github.com/Anil-matcha/open-dots/tree/3d8de1cd6657c6d70583f34b89c2dc034512c1ea)。未查全部历史，不断言技能从未存在，也不将聚合页的许可、星数或模型效果归给当前仓库。

因此本次只保留为来源待定位的线索，未安装或采用其接口参数。聚合页关于固定分镜格数保证实际镜头数、特定模型优于其他模型的说法未获一手证据支持；既有分镜顺序与实际剪辑验收规则足以处理，不额外添加运行规则。若后续找到原始技能的固定提交及对应成片，再恢复方法与效果审阅。同轮 Pika Stagefight 的远端 HEAD 仍为已读 `f27b3ba28a7be7c5f3a74d8fdd54b770f5d8157b`，没有重复通读或计作新来源。

## 按问题查阅记录

| 记录 | 查阅目的 |
|---|---|
| [参考素材与本次请求映射](2026-10-07-reference-request-mapping.md) | 重排或替换附件后同步文字引用，区分列表序号与稳定素材标识 |
| [主观视点与接触连续性](2026-10-07-subjective-view-and-contact.md) | 区分眼位、过肩与外部视点，保留第一视角中的自身手和兵器，切换视点不重演接触 |
| [错误动作控制与修复](2026-10-07-control-input-repair.md) | 纠正源动作时明确允许变化，避免同时要求错误控制完全保持 |
| [人体运动与接触验收](2026-10-07-human-motion-evaluation.md) | 区分单人结构、运动稳定与双人接点，避免用平滑度或姿态置信度代替交互核验 |
| [战斗流水线与密度取舍](2026-10-07-combat-pipeline-density.md) | 对照具体动作语法与固定密度质检，避免把镜长、姿态数和自评分配额当作质量证据 |
| [抓腕压缩前后待执行对照](2026-10-07-grab-compression-comparison.md) | 固定真实历史基线、当前输入快照与共同验收条件；尚无生成结果 |
| [连续动作与剪辑形式](2026-10-07-continuity-versus-cuts.md) | 区分实际切镜、连续变景别与后期切段，保留指定硬切及一镜到底要求 |
| [分镜拼图与生成流程](2026-10-07-storyboard-grid.md) | 区分格序、重复身份与分屏，核对拼图职责，不把多格参考当作逐镜执行保证 |
| [调研记录](2026-10-06-combat-skills.md) | 维护时追溯来源、采用与舍弃的理由，不作为每次创作必读材料 |
| [接触与样片证据续研](2026-10-06-contact-evidence.md) | 社区经验的采用范围、公开成片抽帧观察与接续修正的依据 |
| [御剑与多人交锋调研](2026-10-06-flight-and-multi-combat.md) | 移动方式、实体兵器往返、承载切换与多人持续施压的采用依据 |
| [目标与同招变化调研](2026-10-06-objective-and-adaptation.md) | 护送等目标的可见结果、持续压力、同招再次出现时的不同回应 |
| [抽帧方法调研与验证](2026-10-06-evidence-tool.md) | 两套视频审阅技能的采用范围、可变帧率与非零起点测试、公开片段复查 |
| [持续接触与维持条件调研](2026-10-06-sustained-contact.md) | 压剑、沿刃滑脱、第三人打断束缚，以及相关来源的采用边界 |
| [分身、幻影与残影调研](2026-10-06-clones-and-afterimages.md) | 同貌身体的职责、数量与退场，意外复制与明确分身要求的区分 |
| [体型差与媒体对应核查](2026-10-06-scale-and-media-match.md) | 巨兽攻击范围、原地承接条件，以及案例文字与实际预览不符的核查 |
| [声音与攻防事件调研](2026-10-06-sound-and-events.md) | 静音范围、接触音效、法令与追击并行，以及音画分别核验的采用依据 |
| [并发攻防与提示词压缩调研](2026-10-06-concurrent-action-and-compression.md) | 主事件与多方同时行动的区别、压缩保真及互补素材的采用边界 |
| [离手攻击与终止条件调研](2026-10-06-emission-and-control.md) | 停射、断供、失去操控与在途攻击结束的区分，以及相关方法来源 |
| [官方武侠样片与切点核查](2026-10-06-wuxia-sample-and-cuts.md) | 实取官方展示片，分别记录兵刃交会、特效展开和切点两侧的可见证据 |
| [诱招与感知边界调研](2026-10-06-feints-and-perception.md) | 诱招成败、角色与观众的信息差、提前避让与提前受击，以及候选技能的评测边界 |
| [兵器易手与分化连续性调研](2026-10-06-weapon-transfer-and-continuity.md) | 持握与操控的区别、缴械后的状态，以及公开分剑样片的承载核查 |
| [动作参考适配与迁移模式调研](2026-10-06-motion-reference-adaptation.md) | 改编与精确复刻的区别、换兵器后的攻防重建，以及参考视频接口与时长诊断边界 |
| [法阵位置与附着关系调研](2026-10-06-formation-attachment.md) | 区分来源、维持与位置，检查随动、朝向、作用范围和观察条件 |
| [空间方向与机位变化调研](2026-10-06-spatial-direction-and-camera.md) | 区分场景、身体与画面方位，保留指定构图和合理换边，检查投影与接触 |
| [屏障与碰撞结果调研](2026-10-06-barriers-and-impact-results.md) | 分开判断攻击、防御和人物结果，记录公开雷击样片的强光遮挡与结局边界 |
| [校验范围与评估调研](2026-10-06-validation-scope-and-evaluation.md) | 静态评分的漏检与误报、按原始需求比较候选，以及本机缓存与公开引用的检查边界 |
| [受力与恢复动作调研](2026-10-06-recoil-and-recovery.md) | 区分动势、回防与伤势，保留恢复中的应对，以及镜头和游戏战斗技能的采用边界 |
| [专题拆分与按需读取](2026-10-06-topic-routing.md) | 核对参考拆分的来源、内容保留和代表性任务的读取范围 |
| [变速与成片时间调研](2026-10-06-retiming-and-screen-time.md) | 区分慢镜倍率、成片窗口、帧率与停格，以本地测试片核对时长和帧序 |
| [跨段计划与实际结果调研](2026-10-06-continuation-and-observed-state.md) | 区分计划、观察和接续取舍，保留完整文字交付，核对已完成与未完事件 |
| [环境反馈与通行条件调研](2026-10-06-terrain-and-traversal.md) | 区分表面反馈与实际通路变化，核对地物阶段、携物过口，以及公开水幕画面的观察边界 |
| [双人抓握与释放顺序调研](2026-10-07-paired-body-control.md) | 局部控制、共同承重、逐个接点释放，以及人体交互论文与视频提示词之间的证据边界 |
| [遮挡与重新入画调研](2026-10-07-occlusion-and-return.md) | 区分可见性与场内状态，保持出画期间的运动与持物，并保留隐藏过程的观察不确定性 |
| [提示词压缩的作用范围](2026-10-07-prompt-compression-scope.md) | 同段设定去重、独立片段自足，以及抓腕案例中重复反向说明的精简 |
| [命中标记与风格模板](2026-10-07-hit-marking-style.md) | 审阅固定停顿、震屏与粒子配方，补充轻接触反例并保留指定重击风格 |
| [术法照明与连续性](2026-10-07-magic-lighting.md) | 区分受照色与身份色、瞬时爆光与持续光源，并保持机位变化下的场景光源关系 |
| [目标与策略方法复核](2026-10-07-objectives-and-tactics-audit.md) | 复核既有来源，区分目标与方法，保留有效稳守与主动回护，不强制策略反转 |
