# 错误动作控制与修复范围

2026-10-07 全文读取 [LynnReal 提示技能](https://github.com/LynnReal-AI/LynnReal-Omni/blob/ad16ac787430bd22456ee55f018764cf53c25935/skill/lynnreal-prompt/SKILL.md)，远端 HEAD 经 Git 只读查询确认为 `ad16ac787430bd22456ee55f018764cf53c25935`。根 LICENSE 标题为 MiniMax H3 Community License Agreement，本次返回内容截断，未完整审阅或确认该技能子目录适用许可；仅提炼判断并独立编写中文条件，没有复制模板、代码或安装运行模型。

来源将提示措辞与实际控制布局分开，并指出修复错误动作控制时不能要求错误部分完全保持。其场景修复经验和成片效果本轮未复核，固定三段/六段格式、流式帧数、参考索引及模型参数均未核验为当前可用能力，不移入本项目默认规则。

本项目在 [动作适配](../references/formats/reference-and-iteration.md#动作借鉴与当前设定的适配)补充这一控制冲突，并在 [有界修正案例](../examples/reference-adaptation.md#接触不可读时的有界修正)加入左右掌盾纠正条件：只调整修复所需的控制部分，保留其余兼容要求。单张修复图不能证明整段动作已修好；只改文字也不能保证覆盖强动作控制。此次没有新样片、推理任务或效果评分。

同一来源还提示检查控制素材实际使用区间与末帧延长。将其抽象为接口相关的诊断条件，扩充已有时长排错：先查送入的控制序列，再解释未出现的后招或停顿。新增三秒控制延长到六秒的文字条件，不把来源的具体帧率与处理实现视为所有平台通则，也不把补写提示当成必然能覆盖静态控制的修复。没有创建控制视频或验证模型响应。

## 控制表示是否承载所需接触

2026-10-07 续查 LTX 路线，全文读取官方 [Union Control 工作流说明](https://docs.ltx.io/open-source-model/feature-guides/structural-control/union-control)。该可变页面当次列出 LTX-2.5 工作流复用 2.3 Union adapter；不将其版本依赖回填成先前社区 skill 已测试的配置。页面明确该示例只使用接到 Resize 的一种标注输出，默认深度，可换边缘或姿态；DWPose 的脸、手和身体检测可分别开关。因此不能把“三类控制均支持”理解为本次三类同时生效，也不能笼统说姿态检测没有手部信息。

本项目据此推导输入审阅方法：先看实际绑定与控制预览，再判断所需兵器几何或交点是否进入表示。手部关键点存在与剑身被约束是不同条件，输入未编码某关系也不等于模型必定生成失败。已有双人输出验收规则保留；仅在[参考适配流程](../references/formats/reference-and-iteration.md#动作借鉴与当前设定的适配)补充输入端核对，在[迁移案例](../examples/reference-adaptation.md#动作参考与迁移模式的边界)增加明确假设的剑身缺失反例。

本轮没有执行预处理器、查看真实控制预览或生成视频；反例不是该工作流的实测失败记录。边缘与深度也不保证接点或持握正确，不将某种控制类型设为所有打斗的默认修复。

### 官方工作流连接复核

随后取得官方文档链接的 [Union Control JSON](https://github.com/Lightricks/ComfyUI-LTXVideo/blob/3bf3ca62595f1764c47d01c35c8e5dfe47e1a88f/example_workflows/2.5/LTX-2.5_ICLoRA_Union_Control_Distilled.json)，Git 远端查询固定提交为 `3bf3ca62595f1764c47d01c35c8e5dfe47e1a88f`。下载文件 SHA-256 为 `cf3553a6bafd8d5398f36cfe06dc580a13dddea9387cc57b4a17c2c14c9a4df0`，原文件与来源指纹留在被忽略的 `.local-evidence/ltx-union-workflow-20261007/`。仅按 JSON 数据解析，未导入 ComfyUI 或执行节点。

定向检查 `Reference Video` 子图及其根图实例：深度节点 5061 经输出节点 5062、连接 9 进入 Resize 节点 5028，再经连接 12 输出控制图像；Canny 节点 4991 与 DWPose 节点 4986 都有图像输入，但输出连接列表为空。根图实例 5548 的 image 输出有连接 13767。本次因此确认这份静态配置在该子图选择深度，没有同时输出三种标注；其余采样与模型实现未逐项审计。

该证据支持前述实际连接检查，并补入一个“节点存在但未接入”的文字反例。它不证明预处理成功、执行依赖可用或兵器接触正确，也不适用于用户自行改线后的其他工作流。后续无需因相同版本再次出现而重复计为新实测来源。
