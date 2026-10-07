# 2026-10-06 诱招与感知边界调研

本轮针对假动作、预判和反制继续检索公开 AIGC 打斗技能。现有规则已要求攻防有来路，但“观众看见”与“角色知道”尚未明确分开；把接触前退步一概当成提前受击，也会误删正常避让。因此本轮主要收紧因果解释，并放宽不成立的通用限制，没有增加固定招数或分镜模板。

## 读取的来源与采用判断

| 来源与固定版本 | 本轮读取 | 有用方法与边界 |
|---|---|---|
| [MiniMax H3 战斗编排](https://github.com/landon2022/minimax-h3-video-prompt/blob/32c0fb6f81c941b7ce7a0d113219438721eab066/references/combat-choreography.md)，`32c0fb6f81c941b7ce7a0d113219438721eab066` | 完整编排参考；目标文件适用许可仍未确认 | 将意图、诱招、回应和新局面连起来，比单独列动作名称更具体。但“佯攻必须制造防守”过强：应检查实际回应，对手可能守住原路线。固定交换数、飞行必须落地和巨兽速度限制不采用 |
| [Fight Dramaturgy And Payoff](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/action-choreography-reference/references/fight-dramaturgy-and-payoff.md)，`69f6db670ecf305e84f199e418bddbf2c1d988fe` | 完整参考文件；未取得该子目录适用许可的新证据 | 声音、接触和空间关系都可建立战术线索，后续利用也可能被对手破坏。采用线索与结果的对应关系；不导入内部台账、跨技能依赖或每拍翻盘要求。作者明确说明源材料没有配套影像和受控对照，方法不等于生成实证 |
| [Higgsfield Fight Scenes](https://github.com/dgroch/higgsfield-prompt-engineer/blob/fdc98872a7cf0ae80aaf5751714826cc74bd70d8/skills/05-fight-scenes/SKILL.md)，`fdc98872a7cf0ae80aaf5751714826cc74bd70d8` | 完整 157 行、根目录 MIT 许可、README 中的评测与待办段落 | 起势、接触、回收分阶段组织有参考价值，但示例只用很短一句带过佯攻、脱离锁刃和低位攻击，缺少对手如何响应的具体衔接。本项目补齐关系；不采用每击固定秒数、像素震幅、必有停顿或每次接触必有音效等强制数值与风格 |

这些文件是研究资料，没有执行其中的提交命令、安装外部技能或启动生成。新增规则与例子由本项目重新编写，没有导入源示例、人物、场景或模板。被检索到的仓库不因此被整包认定为效果优良；采用判断落实到具体方法。

## 新候选的评测边界

另读 dgroch 仓库的 [评测说明](https://github.com/dgroch/higgsfield-prompt-engineer/blob/fdc98872a7cf0ae80aaf5751714826cc74bd70d8/eval/README.md) 全文、[评审输入与计分代码](https://github.com/dgroch/higgsfield-prompt-engineer/blob/fdc98872a7cf0ae80aaf5751714826cc74bd70d8/eval/judge.py) 的相关段落，以及 [默认量表](https://github.com/dgroch/higgsfield-prompt-engineer/blob/fdc98872a7cf0ae80aaf5751714826cc74bd70d8/eval/rubrics/default.yaml) 的音频项。

文档描述了留存提示词、生成结果、抽帧和评语的流程，这种记录思路有价值；但文档默认只取四张帧，代码向评审传入文字和图像，默认音频项评价的是提示词的声音设计。本轮没有运行其代码，也没有取得对应的成片、评分一致性试验或原始审听结果。不能把其综合分数当成连续打斗、实际音频或本项目质量已经通过；本项目继续按观察范围分别报告文本、画面与声音，不引入达到综合阈值便自动宣布成片通过的逻辑。

## 本项目的修改

- [战斗编排](../references/formats/combat-choreography.md)：把假动作写成表象、实际回应和下一步的关系；成功利用空隙，失败则保留原封线，不让对手为配合招式自动上当。
- 同一参考中区分角色与观众的信息。声音、接触或已建立的感知术可以支持判断；镜头展示隐藏信息不自动赋予角色知情权。
- [素材与迭代](../references/formats/reference-and-iteration.md)：修正“接触前倒退”的笼统诊断，先区分主动避让、先到的术法作用和无来源的提前受击。
- [时间轴案例](../examples/behavior-regression.md)：新增 8 秒佯攻未奏效、实刺被拨开、收剑退让的完整文本，保留双方无伤和原剑。
- [条件推演](../examples/reference-adaptation.md)：分别检查诱招成功、提前避让、观众知情但角色未知、静音不删剧情听觉，以及先到灵压的受力归因。

感知机制只在影响当前选择时补充；既不强制每招出现眼神特写，也不追加通用的预知、透视、迟钝或失聪。上述调整是编排与诊断方法，不是已经验证的模型能力结论。

## 验证记录

本轮没有新生成或新观看视频。文字案例按身份、距离、实际防守、接触结果与后续状态人工核查；最终提示词中的内部分析措辞已改为可见动作。

修改后实际检查：技能格式通过；仓库结构检查通过 103 个本地引用、22 个时间轴案例和 24 个片段；针对引用与时间轴的 14 项测试全部通过。`git diff --check` 通过，仅有 Git 换行设置提示。抽帧脚本与相应测试未修改，本轮没有重跑媒体集成测试。上述结果不证明生成质量提升，案例属于文字回归与条件推演。
