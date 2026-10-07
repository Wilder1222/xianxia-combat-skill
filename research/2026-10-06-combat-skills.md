# 2026-10-06 打斗技能调研与采用记录

2026-10-07 复核说明：再次读取同版本 Fight Prompt Director 的 `references/diagnostics.md` 全文，其“每轮只修改一类变量”和“唯一修改”有助于控制尝试范围，但不适用于必须联动的起态、距离与覆盖修复。本项目保留优先单组调整，明确允许在原要求范围内修正直接依赖项；联合改善不归因于某一个变量。对应实例补入 [有界修正案例](../examples/reference-adaptation.md#接触不可读时的有界修正)。此次为同源复核，不新增独立来源或样片证据；下文保留原调研日期与当时验证结果。

本轮从公开检索发现候选，再读取维护者仓库中的实际文件与视频模型官方说明。判断依据是方法是否具体、适用条件是否清楚、能否补足本项目缺口；星数、名称和作者自评不作为效果证明。没有运行这些外部技能，也没有观看其全部生成样片。

## 来源快照

| 来源 | 核查范围与版本 | 采用判断 |
|---|---|---|
| [Fight Prompt Director](https://github.com/irenerachel/fight-prompt-director/blob/fee4387b4c53a4b282efa67e143ac9b54d964150/SKILL.md) | 提交 `fee4387b4c53a4b282efa67e143ac9b54d964150`；入口、失败诊断；已查看根目录 MIT 许可 | 角色打法、素材职责和分组排错值得参考；不采用固定三方案、毫秒级起手及模型时间码的泛化要求 |
| [Action Choreography Reference](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/action-choreography-reference/SKILL.md) | 提交 `69f6db670ecf305e84f199e418bddbf2c1d988fe`；入口相关段落、回应逻辑与受击状态参考；未确认该子目录适用许可 | 防守变化影响下一拍的思路有价值；不引入其跨技能依赖和繁复内部表单 |
| [Action Master Kinetic Director](https://github.com/cloudaipro/openclaw-agent-skills/blob/4bee15da6e495fa5f2abb3f808c71793a85209a0/skills/action-master-kinetic-director/SKILL.md) | 提交 `4bee15da6e495fa5f2abb3f808c71793a85209a0`；入口与领域说明；未发现仓库许可证文件 | 本次所读内容偏框架概括，未提供足够具体的攻防增量；不采用固定双语及多工具提示词包 |
| [Runway 图生视频指南](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide) | 2026-10-06 访问；页面自述主要针对 Gen-4.5 | 借鉴运动优先、首帧动势检查和渐进增加细节；不将时长文字当成精确控制 |
| [Google 视频提示词指南](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide) | 2026-10-06 访问；原 Vertex AI 地址已跳转至此地址 | 用其可选提示组成、音频和排除提示说明提醒平台差异；不把页面列举的模型当成当前执行能力 |

许可状态只记录本轮找到的证据，其他子目录的许可证不推定适用于目标技能。正文与案例由本项目重新编写，没有导入第三方技能全文、固定场景或可执行脚本。在线文档可能继续变化，实际执行时仍核对具体模型及工具接口。

## 采用位置与本项目判断

| 当前缺口 | 这次改动 | 保留的边界 |
|---|---|---|
| 角色颜色不同但打法相近 | [编排参考](../references/formats/combat-choreography.md) 增加距离偏好、出手回收、防守余地与目标取舍 | 同门可以相似，用户设定优先；不强制角色全部属于不同流派 |
| 受击与破防只作为一拍效果 | 将防守空隙、支撑和术法资源纳入下一次选择 | 不预设统一恢复秒数或所有世界共用的耗能规则 |
| 主体仍容易把时间码当通用输出 | [主体](../SKILL.md) 与 [文法](../references/formats/video-prompt-grammar.md) 分开内部事件预算和最终表达 | 精确时间轴需求保留，模型实际遵循程度待样片检验 |
| 图生视频沿用文生视频写法 | [素材与迭代](../references/formats/reference-and-iteration.md) 明确首帧、身份图、动作及相机参考的用途 | 不虚构看过素材，不把多视图当多个角色 |
| 失败后容易整体重写 | 先记录可见问题，再选变量组修正，并记录未控制的随机性 | 一次样片改善不能证明全场景有效 |
| 文本检查易被误读为成片验证 | 案例区分时间结构、人工语义审阅和实际视频证据 | 本轮没有生成或评审视频 |

## 本轮验证与尚待验证

- 对旧有六个时间轴案例保留验证，并添加“退路封闭后的受限回应”和“符箓消耗后的夺路”两例，核查本次增加的方法。
- [素材适配案例](../examples/reference-adaptation.md) 用明确标注的文字条件推演检查自然顺序提示词、参考职责、冲突处理和修正边界。没有真实附件，因此不声称完成图像识别测试。
- [结构检查器](../scripts/validate_repository.py) 只检查本地引用与时间结构；[自动测试](../tests/test_validate_repository.py) 覆盖其接受和拒绝行为，不评分编排质量。
- 待积累实证：以相同素材和可控参数比较时间窗与自然叙述，核验复杂接触是否执行、角色打法是否可辨、状态代价是否延续。保留原始视频与缺陷时间，不用新增规则本身证明提升。

2026-10-06 实际检查结果：技能创建器的基础检查通过；`python -X utf8 scripts/validate_repository.py` 通过 30 个本地引用、8 个时间轴案例、10 个片段；`python -X utf8 -B -m unittest discover -s tests -v` 通过 14 项测试（含 11 种无效时间轴变体）；`git diff --check` 通过。四个素材适配案例仅经本轮人工文字审阅。以上均不代表已观看或生成视频。

## 后续调研重点

下一轮优先寻找带可回看样片和失败记录的多角色接触、首尾帧过渡与御剑转向案例；对本轮方法先核验有效范围，再决定扩展。避免继续堆砌抽象词库或把未经核实的模型参数固定进核心规则。
