# 2026-10-06 体型差与媒体对应核查

本轮面向人与巨兽的攻防，核查攻击可达范围、占据的路线、环境残留威胁及段落目标。同时实取一份公开案例预览，发现已读文字与抽样画面不符，因此没有把它作为巨体编排的效果证据。新增规则和案例属于待样片验证的创作方法。

## 方法来源与边界

| 来源与固定版本 | 已读内容 | 本项目判断 |
|---|---|---|
| [T8mars/minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8/tree/48a8c30366413add1ee15cab31a321e5ce236565)，`48a8c30366413add1ee15cab31a321e5ce236565` | 完整读取 [asymmetric-scale-evasion-exchange 主体](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/skills/asymmetric-scale-evasion-exchange/SKILL.md)、同目录 `references/summary.md` 和 [template.md](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/skills/asymmetric-scale-evasion-exchange/references/template.md) | 共用地理参照、以大体型动作占路、小体型改变路线，是可用的编排思路。只适用于其选定的闪避路线；巨者必慢、小者不得正面承接、始终共用地面、结尾必不分胜负，都不能成为仙侠通用限制 |
| [landon2022/minimax-h3-video-prompt](https://github.com/landon2022/minimax-h3-video-prompt/tree/32c0fb6f81c941b7ce7a0d113219438721eab066)，`32c0fb6f81c941b7ce7a0d113219438721eab066` | 完整读取 [combat-choreography.md](https://github.com/landon2022/minimax-h3-video-prompt/blob/32c0fb6f81c941b7ce7a0d113219438721eab066/references/combat-choreography.md) | 目标部位、攻击路径、回应、几何状态变化与仙侠术法限制写得具体。采用可达目标和环境后果的检查；不继承固定交换数、巨兽统一避用快速连击、飞行必落地、固定机位禁令或英文输出要求 |
| [AAAAAAAJ 武戏库](https://github.com/AAAAAAAJ/ai-film-general-skill/blob/efedff4cf16f8bef8476945c2e3c95d48779cc26/references/seedance-action-design-library.md)，`efedff4cf16f8bef8476945c2e3c95d48779cc26` | 补读巨物蓄力与吐息章节 | 可按当前生物结构组织局部起动、主体跟随和环境响应；不将固定的眼、头、颈动作顺序、多次呼吸、口部光核和气浪套给所有异形或术法 |

以上文件只作为研究资料，未执行外部技能。T8 原创文字适用其 [CC BY 4.0 内容许可说明](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/LICENSE-CONTENT)，代码许可与第三方媒体权利分别处理；本项目独立改写为仙侠规则与新场景。Landon 的完整仓库树没有找到许可证，AAAAAAAJ 的适用许可此前也未确认，均未复制其原提示词。

## 公开预览与文字不符

核查对象是 T8 固定版本中 `x-iamfakhrealam-2041485269602631944-video-1` 案例。已读取其 [摘要](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/catalog/cases/x-iamfakhrealam-2041485269602631944-video-1/SUMMARY.md)、[清单](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/catalog/cases/x-iamfakhrealam-2041485269602631944-video-1/manifest.json)、[来源记录](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/catalog/cases/x-iamfakhrealam-2041485269602631944-video-1/source.json)，下载该目录的 [preview.gif](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/catalog/cases/x-iamfakhrealam-2041485269602631944-video-1/preview.gif) 和 [poster.webp](https://github.com/T8mars/minimax-h3-prompt-skill-T8/blob/48a8c30366413add1ee15cab31a321e5ce236565/catalog/cases/x-iamfakhrealam-2041485269602631944-video-1/poster.webp)。

来源记录标注作者为 `@iamfakhrealam`，Seedance 2.0 归属为创作者声明；本轮未另行确认原帖视频。案例清单所报原片时长为 15.104 秒，完整 MP4 指向桌面媒体包。本轮只分析 GitHub 提供的 GIF 与海报，不将它们当原片。

| 实取文件 | 探测与指纹 |
|---|---|
| `preview.gif` | 640 × 360，120 帧，15.01 秒，15917215 字节；SHA-256 `b3c63b4545fe792336d1df3a011c236a58ada69edb02d0e47ba5c7a967c2da2f` |
| GIF 的 Git 对象 | 本地按 Git blob 规则计算 SHA-1，与该固定提交的 GitHub contents API 均为 `f28b27be03db51c4eae274e02f9260c753104189`，大小相同；已排除本次误取其他路径文件 |
| `poster.webp` | 12714 字节；SHA-256 `fdf65cc9102ab75bff4503d1d6fbdeb520a4ee8d265c24990094dee2ec028a03`；已实际查看 |

使用本项目 [抽帧工具](../scripts/sample_video.py)，在 GIF 首帧相对时间 `[0, 15.01)` 秒内每 4 帧保存一帧，共 30 帧；实际采样点为 0.0、0.5，依次至 14.5 秒。已查看索引图：多个采样点都显示白衣与深色衣着的两个人形角色，在可见轨道、架空线架与车顶平台的场景中交锋。可见画面没有建立文字模板所要求的显著巨体与小体型比例；配套海报对应同一车顶场景，也不能支持文字提到的巨体与岸边场地。

结论限定为：这份已核对路径的预览不能作为已读巨体方法的视觉验证。原帖原片未核查，抽样也不覆盖 GIF 帧间的全部动作；不推断原片必然错误，不给全片动作质量评分，不因这一例否定该仓库其他条目。文件、哈希、清单齐全仍需做内容对应核查。

下载文件保留在本轮临时目录，抽帧资料位于被忽略的 `.local-evidence/scale-preview-20261006/`，未收入 Git。本记录仅公开来源、指纹与观察边界，不重新分发第三方媒体。

## 本项目修改与人工核查

- [战斗编排](../references/formats/combat-choreography.md)：新增体型差与异形对手；用已建立的结构、可达范围、攻击覆盖区和后续路线编排，体型不替代修为与速度设定。
- [视频文法](../references/formats/video-prompt-grammar.md)：增加尺度覆盖要求，局部接触能追溯到人物、巨体部位及共同地标；不强制每帧展示全部身体。
- [文字案例](../examples/behavior-regression.md)：一例在巨爪落空后继续应对碎石、第二击及仍能伸入岩口的爪尖；另一例保留小体型高修为者原地承接，避免把所有巨兽战改写成闪避。
- [素材与迭代](../references/formats/reference-and-iteration.md) 和 [抽帧说明](../references/formats/video-evidence-tool.md)：补入文字与媒体对应、GIF 与原片观察范围的区分。

人工核查覆盖：前爪是否仍能够到入口；地形变化后是否继续使用原路线；巨兽是否因体型大被无条件降速；明确要求原地挡击是否被改成回避；挡住一次是否被扩大成最终胜利。均为文字推演，没有本项目生成样片支持。

## 验证记录

2026-10-06 完成验证：技能基础检查通过；仓库检查通过 72 个本地引用、19 个时间轴案例、21 个片段；28 项自动测试全部通过，`git diff --check` 通过。另实际执行 GIF 抽帧并查看 30 帧索引图及配套海报，完成文件路径、字节数和 Git blob 对应核查。

结构与工具检查不替代本项目巨兽交锋的视觉验证；本轮公开预览因与所读方法的场景及尺度不符，未计作该方法的成片成功证据。
