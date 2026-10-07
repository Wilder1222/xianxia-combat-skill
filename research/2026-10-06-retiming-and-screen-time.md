# 变速与成片时间调研

日期：2026-10-06。关注慢镜、停格和帧率在打斗提示词中的时间含义。本轮运行本地程序生成的诊断测试片，核对文件时长、显示时间戳和解码帧序；没有调用 AIGC 生成服务，没有作战斗画面或音频质量评审。

## 来源与采用边界

| 来源 | 本轮审阅 | 采用与舍弃 |
|---|---|---|
| [teskor-hub/minimax-h3-skill](https://github.com/teskor-hub/minimax-h3-skill/blob/a33b8dff6157e9162da4eeb9874831a02f25bd6b/SKILL.md) 及 [提示词参考](https://github.com/teskor-hub/minimax-h3-skill/blob/a33b8dff6157e9162da4eeb9874831a02f25bd6b/references/prompting.md) | 时长预算、动作估时、速度与帧数边界相关段落；[MIT 许可证](https://github.com/teskor-hub/minimax-h3-skill/blob/a33b8dff6157e9162da4eeb9874831a02f25bd6b/LICENSE) 已读 | 采用按事件考虑时间余量的思路；不把其固定收势时间、动作估时表或特定节点帧数网格变成本项目通用规则，也未验证它的模型精确执行承诺 |
| [tsogjavklann/video-prompt-builder](https://github.com/tsogjavklann/claude-skills/blob/7d6dbaef25e0eb18eefc72bc3c9027fd7b2da33a/video-prompt-builder/SKILL.md) | 完整 122 行入口 | 明确变速方向、必要时说明近似倍率有助于表达意图；不采用固定镜数、特效密度指标、四段输出协议或必需标志特效 |

第二个来源的完整文件树未截断，本轮未在仓库根目录或对应技能目录找到独立许可证文件，授权范围不作已确认声明。仅整理一般方法，不复制模板或执行外部脚本。第一项只审阅了本次相关段落，不能据此宣称整包已完成评测。

[Adobe 关于片段速度的说明](https://helpx.adobe.com/ca/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-using-the-speedduration-option.html)区分播放倍率、音高与时间插值；[解释帧率的说明](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/change-the-frame-rate-of-a-clip.html)说明改变素材解释帧率会按比例改变时长。[FFmpeg 官方文档](https://ffmpeg.org/ffmpeg-filters.html)则明确：`fps` 可通过重复或舍弃帧达到目标帧率，`setpts` 用于改变显示时间戳。由此不能将“重采样输出帧率”和“重定时播放”混为一谈。

这些官方说明支持时间处理的区别，不证明任何文生视频模型会精确执行提示词中的倍率。

## 本地测试片与实际结果

使用 FFmpeg / ffprobe `8.1.1-full_build-www.gyan.dev`，从 `testsrc2` 创建 160×96、24 帧/秒、2 秒无声测试片，采用 FFV1 无损编码及 AVI 容器。测试图案不包含人物和打斗动作，不能用其结果评价运动审美。

| 文件 | 处理 | 帧数 | 帧率 | 实际时长 | 最后一帧 PTS |
|---|---|---:|---:|---:|---:|
| `source-24fps.avi` | 原始诊断输入 | 48 | 24 | 2.000000 秒 | 1.958333 秒 |
| `resample-48fps.avi` | `fps=48` | 96 | 48 | 2.000000 秒 | 1.979167 秒 |
| `half-speed-12fps.avi` | 时间戳扩大两倍，按 12 帧/秒输出 | 48 | 12 | 4.000000 秒 | 3.916667 秒 |
| `append-hold-250ms.avi` | 末尾重复末帧 0.25 秒 | 54 | 24 | 2.250000 秒 | 2.208333 秒 |

逐帧解码指纹比较确认：48 帧/秒版本把源帧各重复两次；半速版本保留原来 48 帧的全部内容与顺序；停格版本在原 48 帧后增加六个末帧副本。连同源帧数量及“帧数÷帧率与文件时长一致”的检查，五项诊断全部通过。最后一帧 PTS 是该帧的显示起点，不是整段结束时间。

复现时在空的测试目录运行以下命令；这些只是本地诊断，不是视频生成接口参数：

```powershell
ffmpeg -n -f lavfi -i testsrc2=size=160x96:rate=24:duration=2 -an -c:v ffv1 -pix_fmt yuv420p source-24fps.avi
ffmpeg -n -i source-24fps.avi -an -vf fps=48 -c:v ffv1 -pix_fmt yuv420p resample-48fps.avi
ffmpeg -n -i source-24fps.avi -an -vf "setpts=2*(PTS-STARTPTS)" -r 12 -fps_mode cfr -c:v ffv1 -pix_fmt yuv420p half-speed-12fps.avi
ffmpeg -n -i source-24fps.avi -an -vf tpad=stop_mode=clone:stop_duration=0.25 -c:v ffv1 -pix_fmt yuv420p append-hold-250ms.avi
```

首次半速输出同时使用 `-r 12` 和 `-fps_mode passthrough`，被当前 FFmpeg 拒绝；保留已经完成的源片与重采样片，仅将失败分支改成 `cfr` 后继续，最终核对确认没有改变源帧顺序。失败原因及修正一并记录，没有将失败尝试计入成功结果。

资料保存在本机 `.local-evidence/retiming-fixture-20261006-46tuqoul/`，含四个文件、各自探测 JSON、逐帧 MD5 和 `manifest.json`。清单明确标记非 AI 生成、无音轨、未作视觉质量审阅。文件 SHA-256：

- 原始输入：`4897dac435ef63de2775ecab2dbf27a0483c332c06834e343526b34e6fb53418`
- 重采样版：`ad797064473a6782138a912191a0760720c7008e4506a7fb73573c43bce80c08`
- 半速版：`7c1010a55fd4cc7e797e9739af895df349402b37606efd03a911b6de1b910238`
- 追加停格版：`41c7c5edd0fb1b73783584c8f795b3c15d56e909d3a424021119d28645d9ff82`

本次输入是固定帧率且无声，以上帧数除法不能直接替代可变帧率或含音轨文件的实际时间戳核查。测试也未涉及光流补帧、原速战斗观看、音高处理或声音同步。

## 本项目落地

- [时间与镜头规则](../references/formats/video-prompt-grammar.md)：成片窗口、素材时长、倍率与追加停格分别计算；避免二次除倍率；区分整幅画面停格与人物冻结时的相机环绕。
- [技能入口](../SKILL.md)：交付检查明确慢镜和冻结占用成片时间。
- [平台执行](../references/formats/platforms-markets.md) 与 [失败修正](../references/formats/reference-and-iteration.md)：实际检查变速、重采样、播放器倍率及音轨处理，不把参数或文件回执当成动作验证。
- [素材适配案例](../examples/reference-adaptation.md)：给已有 8 秒冻结案例补齐成片时间预算，新增倍率、追加停格、保时长重采样和二次变速的边界推演。

诊断片说明时间处理如何改变文件，没有证明本技能生成的打斗更快、更有冲击力或更连贯。原有时间轴案例未增加；本轮不改动检查器或抽帧程序。

最终复查：技能格式、179 个本地引用、24 个时间轴案例及 26 个片段通过，引用与时间轴的 18 项单元测试通过，`git diff --check` 未发现格式错误。上述结构检查与本地诊断片的五项检查分别报告，不合并为生成视频质量成绩。
