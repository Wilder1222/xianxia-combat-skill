# 战斗流水线与动作密度取舍

## 来源与当前阅读范围

2026-10-07 核查 [Short Drama Pipeline](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/tree/a669c98515f28f3ac3c52671775687a8cd09f70f)，提交 `a669c98515f28f3ac3c52671775687a8cd09f70f` 由 `git ls-remote` 确认。完整读取 README、技能入口、根目录 MIT 许可，以及 `core/combat/` 下九份模块：`fight_director_layer`、`combat_grammar`、`impact_system`、`power_escalation_system`、`vfx_power_system`、`combat_camera_coverage`、`combat_prompt_assembler`、`style_routes`、`combat_qc`（均为 `.md`）。

另完整读取下述法相压制 JSON 示例，定向查看单镜 schema 的执行提示字段；完整 schema 条件、其余实例和其他生产参考未核查。没有安装技能、运行外部脚本、复跑 schema 校验或调用生成接口。同仓库各模块不计为独立效果验证。

## 方法取舍

[战斗语法](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/blob/a669c98515f28f3ac3c52671775687a8cd09f70f/skills/short-drama-pipeline/core/combat/combat_grammar.md)拆分动作、战术意义、接触、反馈与接续，导演层联系目标与对手压力，编译层要求最终保留可见动作。这些已由本项目覆盖，不复制字段表或强制所有短提示先输出 JSON。持续压剑、试探落空和完整追逐不必每拍都有冲击与余波。

[质检模块](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/blob/a669c98515f28f3ac3c52671775687a8cd09f70f/skills/short-drama-pipeline/core/combat/combat_qc.md)强调空间可读，但固定镜长、姿态数、事件密度、前段爆发与末段停留比例未取得本次生成对照依据，不引入其配额和自评分门槛。缩短、拆镜、换参考或升级路线前须核对用户要求与实际接口；不能自动删去指定事件，也不把“高控制路线”的名称当作能力证明。

| 模块 | 可用方法与本项目取舍 |
|---|---|
| [力量升级](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/blob/a669c98515f28f3ac3c52671775687a8cd09f70f/skills/short-drama-pipeline/core/combat/power_escalation_system.md) | 用空间比例说明大尺度力量有用；不采用每镜最多升一级或先展示再接触的固定顺序，保留突然显现、一击碾压与用户指定连续镜头 |
| [特效力量](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/blob/a669c98515f28f3ac3c52671775687a8cd09f70f/skills/short-drama-pipeline/core/combat/vfx_power_system.md) | 来源、运动、交互与终态均与现有法阵规则相容；不把所有压制写成重力变大，或把所有法相限定为轮廓到完整显现 |
| [镜头覆盖](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/blob/a669c98515f28f3ac3c52671775687a8cd09f70f/skills/short-drama-pipeline/core/combat/combat_camera_coverage.md) | 用景别承担信息任务有用；不要求每场拆成多条提示，不以一张接触帧证明来路与分离成立 |
| [冲击反馈](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/blob/a669c98515f28f3ac3c52671775687a8cd09f70f/skills/short-drama-pipeline/core/combat/impact_system.md) | 将接触、回应、声音及终态分开检查；近失不产生该次命中反馈，轻接触不强制停格、碎裂和低频巨响。不能从其声音建议推断平台无原生音频能力 |

风格路线仅作可选表现手段：3D 不必始终环绕或使用体积光，2D 不必每击停格或加墨迹，真人风格可按设定使用术法。现有 [时长与事件分配](../references/formats/video-prompt-grammar.md#时长与事件分配)、[简化约束](../references/formats/reference-and-iteration.md#简化时保留关键事件)、[力量与法阵](../references/formats/powers-and-formations.md)及 [镜头文法](../references/formats/video-prompt-grammar.md)已覆盖这些取舍，无需重复扩写。

## 实例中的提交遗漏

[法相压制示例](https://github.com/ouyangevan/codex-short-drama-pipeline-skill/blob/a669c98515f28f3ac3c52671775687a8cd09f70f/skills/short-drama-pipeline/examples/combat/3d_guoman_avatar_suppression.json)的术法来源字段包含掌印，终态字段要求地阵保留；执行提示描述剑枪接触、地阵扩展与半跪，却未明确保留掌印参与和地阵延续至下一镜。附件内容未取得，不能断言生成必然遗漏。直接按 UTF-8 解码的中文展示字段仍含乱码，不以该字段推断动作要求。

单镜 schema 对 `provider_execution_prompt` 的直接定义为字符串、最少 80 字符；本次未审阅全部条件或运行校验器。内部字段完整、示例自评分或仓库声称的 schema 通过，均不能证明最终提交完整或视频质量成立。

据此将最终提交对照并入主体已有交付检查，确保只读主体的普通单段任务也覆盖；素材参考说明压缩与绑定的细节，同步双挡案例增加交付遗漏反例：指定接触、施术条件与接续终态须由实际提交文本或有效绑定素材承载，不能只留在内部计划。无需输出内部表单，也不机械重复参数与素材已承载的信息。

## 本地回查与证据边界

分批检查 25 个时间轴案例的要求在可复制正文中的保留情况，修正以下遗漏，原动作、时间窗、力量与结局保持一致：

- 观察与破阵：提前建立封路光幕，第二段独立说明仍有效的各侧光幕。
- 盾阵偏转与脱身：第一段补入不说法令。
- 旧友留手、共鸣同伤：补明旧友与旧日同门关系。
- 残影、正面承爪、持续压剑、短法令：补明原请求中的双方无伤；持续压剑另补明一镜到底。

其余所查维持条件、解除动作、承载切换、兵器数量与分身退场已有正文承载，未为凑改动重写。抓腕对照两份冻结文本的 SHA-256 与记录一致，候选乙仍与当前主案例完全相同，没有改变实验输入。

以上是源文件与文字约束审阅，不是独立盲测、全项动作质量认证或生成改善证据；未取得来源示例的任务记录及视频。后续针对未读 schema、其余实例或可追溯媒体开展核查，同版已读模块优先复用本记录。
