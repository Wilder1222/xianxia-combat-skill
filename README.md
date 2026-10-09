# 仙侠打斗

编写、改写仙侠战斗的中文视频提示词，支持近战连招、御剑追击、法术对抗、法阵、多人协同、CGI 与真人质感，以及参考适配和成片诊断。创作入口为 [SKILL.md](SKILL.md)，按任务读取 [参考文档](references/INDEX.md)。

## 通过 Codex 插件安装

本项目提供插件 `xianxia-combat`，市场名为 `xianxia-combat-marketplace`。插件包含一项同名 Skill，不要求配置 API 密钥；实际生成视频时使用宿主已有工具和本次生成授权。

### 从 GitHub 安装

插件文件发布到 GitHub 后，在支持插件命令的 Codex CLI 中执行：

```powershell
codex plugin marketplace add Wilder1222/xianxia-combat-skill --ref main
codex plugin add xianxia-combat@xianxia-combat-marketplace
```

桌面端也可在插件目录选择“仙侠打斗插件”来源，再安装“仙侠打斗”。如果当前客户端没有 `codex plugin add`，添加市场后使用桌面插件目录完成安装。不同客户端的插件命令以 `codex plugin --help` 为准。

### 安装当前本地修改

在仓库根目录打包，生成独立的本地市场与插件；包中包含清单、入口、公开文档、辅助脚本及文档引用的校验用例：

```powershell
python -X utf8 -B scripts/plugin_support.py build
codex plugin marketplace add ./dist/codex-plugin
codex plugin add xianxia-combat@xianxia-combat-marketplace
codex plugin list --marketplace xianxia-combat-marketplace --json
```

GitHub 与本地包使用同一市场名，切换来源时先执行 `codex plugin marketplace remove xianxia-combat-marketplace`，再添加希望使用的来源。切换市场来源不会替你卸载已安装插件；添加来源后重新执行安装并核对输出路径。

安装后新建任务，或在客户端刷新插件，再使用：

```text
使用 $xianxia-combat，编写 8 秒正常速度、三轮攻防、一镜到底的中文仙侠提示词。
```

宿主若显示带插件命名空间的技能，选择 `xianxia-combat:xianxia-combat`。插件安装成功只证明文件和技能入口可用，视频效果仍需实际成片核验。

### 更新与卸载

GitHub 安装更新：

```powershell
codex plugin marketplace upgrade xianxia-combat-marketplace
codex plugin add xianxia-combat@xianxia-combat-marketplace
```

本地安装更新先重新运行 `scripts/plugin_support.py build`，再执行安装命令。卸载：

```powershell
codex plugin remove xianxia-combat@xianxia-combat-marketplace
```

## 维护与校验

行为规则只在根目录 `SKILL.md` 和相关参考中维护。`skills/xianxia-combat/SKILL.md` 是自动生成的插件入口，安装包保留完整主工作流及其相对引用，不依赖原仓库绝对路径。

根目录 `plugin.json` 是插件身份与展示信息的来源；`.codex-plugin/plugin.json` 为自动生成的兼容清单。修改主入口或清单后执行：

```powershell
python -X utf8 -B scripts/plugin_support.py sync
python -X utf8 -B scripts/plugin_support.py check
python -X utf8 -B scripts/validate_repository.py
python -X utf8 -B -m unittest discover -s tests -p test_plugin_support.py
```

构建输出在被 Git 忽略的 `dist/codex-plugin/`；`.local-evidence/`、Git 数据、缓存和测试视频不会进入包。构建清单记录文件指纹；未知文件或人工修改过的旧包会阻止覆盖。

插件格式和市场设置依据 [OpenAI 官方插件文档](https://developers.openai.com/plugins/build/plugins)。这套市场用于仓库分发，不代表已进入官方公共插件目录。

2026-10-09 已用本机 Codex CLI 0.147.0 从本地包安装 0.1.0，插件列表显示已安装且已启用；宿主 `skills/list` 实际发现 `xianxia-combat:xianxia-combat`，对应安装缓存中的技能入口，未报告该技能解析错误。包内引用和文件指纹另行核对；这项验证未调用视频生成。
