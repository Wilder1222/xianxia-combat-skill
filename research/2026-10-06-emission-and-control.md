# 2026-10-06 离手攻击与终止条件调研

本轮检查发射结束之后，攻击、兵器和环境的状态是否继续成立。已有规则分别提到停射、召回和束缚解除，但缺少将它们放在同一处比较的判断，容易把施术者改招写成所有攻击同时消失。本轮按当前世界设定区分发射、供能、操控与攻击自身的终止。

## 来源与固定版本

| 来源 | 已读范围 | 本项目判断 |
|---|---|---|
| [Snowfrost 特效导演](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/cinematic-vfx-director/SKILL.md)，`69f6db670ecf305e84f199e418bddbf2c1d988fe` | 补读效果任务、主信息与过程章节；[机制图谱](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/cinematic-vfx-director/references/mechanism-atlas.md) 的轨迹与能量章节；[构建文法](https://github.com/snowfrost/skill-movie/blob/69f6db670ecf305e84f199e418bddbf2c1d988fe/vfx-effect-construction-engine/references/effect-construction-grammar.md) 的因果过程、状态延续、生命周期选择，以及粒子、投射、轨迹、冲击波、阵法与召唤语法 | 采用来源、传播、作用、响应与收束的观察顺序；只保留当前画面需要的阶段。不导入完整效果卡、词库原子或固定时长配额，也不把轨迹残光与仍能攻击的本体当作同一对象 |
| [Emily2040 的 seedance-vfx](https://github.com/Emily2040/seedance-2.0/blob/4668457e560eee06e95d7fcfdf441c8c0bba802e/skills/seedance-vfx/SKILL.md)，`4668457e560eee06e95d7fcfdf441c8c0bba802e` | 完整读取技能主体 | 来源、路径、交互和结束状态值得采用。拒绝把每段只留一个主特效、所有魔法必须服从现实重力、复杂效果统一形成后消散作为通用限制；用户要求持续存在的阵法可以跨段保留 |
| [ByteDance agentkit-samples 提示词技能](https://github.com/bytedance/agentkit-samples/blob/2e4feace57d6d181b544a2489ff264fdfba2cdbc/skills/byted-sol-seedance-prompt/SKILL.md)，`2e4feace57d6d181b544a2489ff264fdfba2cdbc` | 阅读入口、时间戳说明与仙侠示例、仙侠策略、交互与注意事项；读取完整仓库树和根许可证头部 | 中文具体动作、素材编号清楚等方法与当前方向一致。所读仙侠示例未提供攻击中断后的状态对照，不把其效果堆叠或来源身份当成此问题的验证。不继承强制风格、固定分镜模块、默认多版本或时间码精确控制承诺；其示例时间窗也不直接符合本项目连续区间约定 |

Snowfrost 相关子目录的适用许可未确认；Emily2040 根目录 MIT 许可已在前轮核查；ByteDance 仓库根目录标示 Apache 2.0。以上仅作为研究资料，未执行、安装或复制外部技能与示例。本轮没有核验这些技能所列的平台参数或生成能力。

“停发不必等于消除在途攻击”是本项目在上述过程方法基础上补出的机制判断。它不是外部仓库已经完成的生成对照试验，也不用于断言所有仙侠作品共享同一物理规则。

## 修改与对照

- [战斗编排](../references/formats/combat-choreography.md) 增加发出后的维持与终止，区分自持投射、持续供能、遥控实体和自主锁定；修正发射阵结束状态，避免把停射与清空已有攻击混写。
- [技能主体](../SKILL.md) 在动作检查中加入发出后是否仍需控制；[视频文法](../references/formats/video-prompt-grammar.md) 的跨段状态保留在途攻击的路线与维持条件。
- [素材与迭代](../references/formats/reference-and-iteration.md) 增加改招后在途攻击突然消失的诊断，依据已建立机制修复。
- [时间轴案例](../examples/behavior-regression.md) 新增停射后仍须避开已发符矢的一例，与此前拆印即解除束缚的案例形成文字对照。
- [素材适配案例](../examples/reference-adaptation.md) 增加五种明确设定的推演，包含用户指定撤手后立即消散的反例，避免将本轮规则反向固化成“一律不能取消”。

人工核查覆盖：阵口消失后是否凭空删掉自持符矢；施术者转身是否让直射弹道自动转弯；控制中断是否抹掉实体飞剑；挡住施术者视线是否被误当所有追踪都失效；法术散去时已造成的真实浅坑是否保留。只对输入明确的条件作判断，不为制造反制机会临时添加弱点。

## 验证记录

2026-10-06 完成验证：技能基础检查通过；仓库检查通过 92 个本地引用、21 个时间轴案例、23 个片段；28 项自动测试全部通过，`git diff --check` 通过。素材适配文件现有 12 组文字案例，本轮新增的一组包含五种机制条件，未计入自动时间轴数量。

本轮没有新增生成样片或音画观察；文字对照和自动结构检查不证明视频模型能正确表现这些状态变化。
