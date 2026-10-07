# 环境反馈与通行条件调研

日期：2026-10-06。范围：环境外观、地物状态与可通行范围的区别。本轮审阅外部技能资料、复看已有公开样片帧，并修订规则和文字案例；未启动生成。

## 本轮问题

现有巨兽与多人脱围案例已包含碎石逼位、狭口限制、收枪穿门和持续追击，无需另立一套地形编排流程。需要细化的是适用边界：泛称“环境变化影响后续行动”可能把水花、石粉和浅灼痕也强行变成封路；反过来，保留裂痕外观又不代表实际障碍已经清除。后续动作必须继承真正改变的条件，同时保留没有改变的可用路线。

## 来源审阅

| 来源 | 本轮读取 | 可借鉴部分与局限 |
|---|---|---|
| [snowfrost：Combat Impact And State Progression](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/action-choreography-reference/references/combat-impact-state-progression.md) | 全文 114 行 | 将影响后续选择的变化与局部材质表现分开记录，延续位置和通路状态。未采用其完整账本、冲击等级或跨技能交接协议；文档本身不是当前模型效果验证 |
| [snowfrost：Fight Dramaturgy And Payoff](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/action-choreography-reference/references/fight-dramaturgy-and-payoff.md) | 全文 103 行 | 地物的后续作用须继承先前建立的位置、方向与状态。作者注明方法来自用户提供文本，没有配对视频、生成设置或受控对照；与上一条属于同一仓库的方法，不能合计成两份独立效果证据 |
| [beshuaxian：Fight Scene & Action Prompt Generator](https://github.com/beshuaxian/higgsfield-seedance2-jineng/blob/83dcb10ee38c9694ac0f455ec55a62f2be3b8a14/skills/05-fight-scenes/SKILL.md) | 全文件 741 行；读取 1–30、78–97、364–417、619–646 行，并检索标题及环境相关命中 | 材质反馈与场景用途可作创作提示。没有把环境列表当作必需效果：雨中必须打滑、每步扬沙、固定两秒钩子、进攻必推镜等不作为本项目规则；其中平台能力描述未被本轮验证 |

两仓库 HEAD 经 GitHub API 核对，分别为上述 `69f6db670ecf305e84f199e418bddbf2c1d988fe` 和 `83dcb10ee38c9694ac0f455ec55a62f2be3b8a14`。两棵完整目录树均未截断：第一仓库只检索到其他子目录的许可文件，第二仓库未检索到许可文件；两者仓库许可字段均为空，所读资料的适用许可仍未确认。仅提炼方法，以本项目自己的条件和中文规则表达，不复制完整模板、动作词典或代码。没有安装来源技能或执行其指令。

## 公开样片复看

素材仍为 [Seedance 官方发布页](https://seed.bytedance.com/en/blog/seedance-2-0-official-launch) 提供的 [武侠展示 MP4](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4uec3mljdopde.mp4)，沿用 [此前下载与抽帧记录](2026-10-06-wuxia-sample-and-cuts.md)。本轮重新计算本地视频 SHA-256，仍为 `50312fdbf3fcf94c3229543df46ffc8119564df274502546f758f2db849d7e5a`；三张单独查看的 PNG 也分别与原清单哈希一致。

重新查看 31 张概览帧的索引图，并单独查看下列三张解码 PNG。三张均已包含在概览内，本轮没有新抽帧，也不把它们另计成 34 个不同源帧。PNG 编码尺寸为 3840 × 2160；没有原速播放或音轨审听。

| 源帧与时间 | 可见内容 | 不能据此推出 |
|---|---|---|
| 240，8.0 秒 | 双方低姿态相向，脚边有溅起的泥水 | 脚边水花本身不能证明滑倒，也不能确认完整的承重与制动过程 |
| 285，9.5 秒 | 两人之间出现较大的环状水幕，脚边仍有泥水 | 水幕的范围不能替代地面塌陷或通路被堵的证据 |
| 390，13.0 秒 | 环状水幕已不再完整可见，双方仍伸兵刃相向 | 散去的水花不等于地形复原；这些采样帧也不能证明全段地形完全未变或从未打滑 |

该复看只帮助限制观察推断，没有以静帧证明地面摩擦、连续位移或全片质量，也不证明新增规则改善了生成。人工观察另存于 `.local-evidence/seedance-wuxia-terrain-review-20261006-cb3_kf64/observation.json`；原抽帧清单的自动审阅标记保持不变。媒体和帧图均未收入 Git。

## 规则与案例改动

- 在 [移动与在途攻击](../references/formats/movement-and-projectiles.md#地形变化与通行条件) 集中说明外观反馈、变化阶段、缺口尺寸与携物通行；入口和导航只补充相应读取条件。
- 缩窄 [编排核查](../references/formats/combat-choreography.md#编排核查) 的地形要求：影响行动的变化继续约束后招，单纯材质反馈不强行转为封路或失衡。
- 在 [跨段接续](../references/formats/video-prompt-grammar.md#跨段接续) 的环境项中传递受损范围、倒落阶段和当前通路；在 [失败诊断](../references/formats/reference-and-iteration.md) 区分“裂痕还在”与“路线仍可通过”。
- 微调 [既有多人脱围案例](../examples/behavior-regression.md)：符矢只留下浅灼痕、门洞开口不变，因此仍能穿门；保留两路施压、12 秒时间轴与枪客收枪过门，不增加新灾变。
- 在 [参考适配案例](../examples/reference-adaptation.md#外观反馈与通路变化) 增加六个文字对照条件：稳定雨中步法、仅容剑尖的窄缝、破裂但仍挡路的门板、只遮视线的烟尘、御空通过破桥、负匣改走可用出口。

上述六项是人工审阅用的条件与失败判据，不是六次模型实测。保留此前有效的碎石逼位、狭口仍受巨爪威胁和下坠支点限制，不另加固定地形破坏配额、完整状态协议或默认滑倒动作。

## 验证

验证结果：

- `quick_validate.py`：技能格式通过。
- `scripts/validate_repository.py`：193 个本地引用、24 个时间轴案例、26 个片段通过结构检查。
- `python -X utf8 -B -m unittest discover -s tests -p test_validate_repository.py`：18 项现有校验器测试通过；本轮未修改脚本。
- `git diff --check` 与 37 个未跟踪文本文件的行尾空白、末尾空行检查通过。Git 仅提示已有的换行符转换行为。
- 八份已有文件与修改前快照比对；多人脱围案例对照本轮已读取原文核对两处改动，原有时间窗与攻防顺序保留。
- 本地视频和三张单独查看的 PNG 共四份文件指纹与原记录一致。`git check-ignore` 确认人工观察记录和帧图仍被忽略；未重新分发媒体。

结构检查与公开样片复看分别报告，不合并为本项目生成质量结论。尚无使用新增规则生成的视频；本轮未提交或推送。
