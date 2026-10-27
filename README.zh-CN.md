# 菲比啾比

[English](README.md) · **简体中文**

[![Release 附件累计下载](https://img.shields.io/github/downloads/RiomQAQ/phoebe-chupi-codex-pet/total?label=%E7%B4%AF%E8%AE%A1%E4%B8%8B%E8%BD%BD&color=brightgreen)](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases "所有版本 Release 附件的累计下载次数")

陪你写代码的 **Codex 桌面宠物与 Dot 伙伴**。菲比抱着电脑坐好，工作时会眨眼，在 Dot 里还会跟着鼠标转头。

![抱着电脑坐好的菲比啾比](previews/hero.png)

**9 种动作 · 16 个转头方向 · 透明背景 v2 精灵图**

使用 **GPT-6-Astra** 与内置图像生成功能制作，造型基于《鸣潮》菲比的社区二创「菲比啾比」。

**v1.0.2** 重画了 12 个转头姿态，让转头时的脸颊轮廓和脸部大小更稳定。57 张标准动作帧（含眨眼）与 v1.0.1 保持一致，帽子设计也保留不变。检查结果和仍可见的姿态跳变见[审查结果](docs/REVIEW.zh-CN.md#当前结果)。

## 开始使用

1. 下载 **[phoebe-chupi-v1.0.2.zip](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/download/v1.0.2/phoebe-chupi-v1.0.2.zip)** 并解压。
2. 把 `phoebe-chupi` 文件夹放进 Codex 的 `pets` 目录：

   | 平台 | 目录 |
   | --- | --- |
   | macOS | `~/.codex/pets/` |
   | Windows | `%USERPROFILE%\.codex\pets\` |
   | 自定义配置 | `<CODEX_HOME>/pets/` |

3. 打开**设置 → Pets／Mini 与虚拟宠物**，刷新列表，选择 **Phoebe Chupi · Coding Companion**。

文件夹里只有 `pet.json` 和 `spritesheet.webp`，不需要安装插件。原生导入、旧版更新和显示问题见[安装指南](docs/INSTALL.zh-CN.md)。

## 动作预览

| 坐着陪你 | 工作中 | 等你回复 |
| :---: | :---: | :---: |
| ![待机与眨眼](previews/idle.gif) | ![工作](previews/running.gif) | ![等待](previews/waiting.gif) |

| 抱电脑向右走 | 抱电脑向左走 | 挥手打招呼 |
| :---: | :---: | :---: |
| ![向右走](previews/running-right.gif) | ![向左走](previews/running-left.gif) | ![挥手](previews/waving.gif) |

| 坐着小跳一下 | 需要帮忙 | 检查结果 |
| :---: | :---: | :---: |
| ![坐姿小跳](previews/jumping.gif) | ![求助](previews/failed.gif) | ![检查](previews/review.gif) |

| 在 Dot 里跟随鼠标 | 小跳后回到坐姿 |
| :---: | :---: |
| ![十六个转头方向](previews/look-loop.gif) | ![待机、小跳与落回原位](previews/idle-jump-idle.gif) |

方向预览会依次展示 16 个离散姿态；在 Dot 中，姿态由鼠标位置决定。部分姿态切换仍有可见跳变。动画速度和任务状态切换由应用控制。

九类动作也可以通过[完整动画](previews/all-states.gif)或[逐行布局](docs/FORMAT.zh-CN.md#动作行)查看。

## 适配范围

| 使用场景 | 状态 |
| --- | --- |
| macOS Codex 桌面端 | 自定义 v2 宠物包。 |
| Codex Dot | 16 个跟随鼠标的头部姿态。 |
| Windows 桌面端 | 提供通用安装包，画面尚未实测。 |
| 图片导入或上传 | 使用支持自定义 v2 宠物的应用与导入流程。 |

本包采用 **1536 × 2288** 的 v2 精灵图，应用需要支持自定义 v2 宠物。详见[安装与兼容性](docs/INSTALL.zh-CN.md#兼容性)。

v1.0.2 已在原生尺寸的浏览器预览中复查，原生 Dot 和 Windows 的画面检查仍待完成；v1.0.1 已在 macOS 桌面端和 Dot 中检查。

## 继续阅读

| 指南 | 内容 |
| --- | --- |
| [安装与更新](docs/INSTALL.zh-CN.md) | 导入宠物、更新已有版本、处理显示问题。 |
| [宠物制作流程](docs/MAKING-OF.zh-CN.md) | 从参考图出发，逐帧制作并完成打包。 |
| [提示词示例](docs/PROMPTS.zh-CN.md) | 角色、动作、局部修复和审查的可用模板。 |
| [精灵图格式](docs/FORMAT.zh-CN.md) | 清单字段、动作行、转头方向与播放时长。 |
| [审查与校验](docs/REVIEW.zh-CN.md) | 画面检查方法、文件校验和当前结果。 |
| [图片档案](docs/IMAGE-GALLERY.zh-CN.md) | 832 张源图，包含造型试作、逐帧图片和历史方案。 |

每份指南均有英文版。[文档目录](docs/README.zh-CN.md)还收录了参考来源、署名、当前的[转头修复检查记录](docs/look-repair-qa/README.zh-CN.md)，以及历史版本 v1.0.1 的[头发描线修复记录](docs/OUTLINE-REPAIR.zh-CN.md)。

## 署名与许可

菲比来自库洛游戏《鸣潮》。社区三视图署名为 **蓝蓝铜离子**，详见[制作署名](NOTICE.md#中文)和[参考来源](docs/SOURCES.zh-CN.md)。

原创脚本和文档采用 [MIT 许可](LICENSE.zh-CN.md)；角色图片与参考图适用[单独的使用说明](ASSET-USAGE.md#中文)。本项目为非官方同人作品，与库洛游戏、OpenAI 无隶属或合作关系。
