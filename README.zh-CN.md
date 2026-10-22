# 菲比啾比

[English](README.md) · **简体中文**

陪你写代码的 **Codex 桌面宠物与 Dot 伙伴**。菲比抱着电脑坐好，工作时会眨眼，在 Dot 里还会跟着鼠标转头。

![抱着电脑坐好的菲比啾比](previews/hero.png)

**9 种动作 · 16 个转头方向 · 透明背景 v2 精灵图**

使用 **GPT-6-Astra** 与内置图像生成功能制作，造型基于《鸣潮》菲比的社区二创「菲比啾比」。

## 开始使用

1. 下载 **[phoebe-chupi-v1.0.1.zip](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/download/v1.0.1/phoebe-chupi-v1.0.1.zip)** 并解压。
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

| 在 Dot 里跟随鼠标 | 坐着小跳一下 |
| :---: | :---: |
| ![十六个转头方向](previews/look-loop.gif) | ![待机、小跳与落回原位](previews/idle-jump-idle.gif) |

方向预览会依次展示 16 个姿态；在 Dot 中，姿态由鼠标位置决定。动画速度和任务状态切换由应用控制。

其他动作包括抱电脑左右移动、挥手、求助和检查结果。可以查看[全部动作](previews/all-states.gif)或[逐行布局](docs/FORMAT.zh-CN.md#动作行)。

## 适配范围

| 使用场景 | 状态 |
| --- | --- |
| macOS Codex 桌面端 | 已安装并检查画面。 |
| Codex Dot | 支持头部跟随鼠标方向转动。 |
| Windows 桌面端 | 提供通用安装包，画面尚未实测。 |
| 网页上传 | 官方说明中的上传器接受 v1；本包需使用支持 v2 的导入方式。 |

本包采用 **1536 × 2288** 的 v2 精灵图，应用需要支持自定义 v2 宠物。详见[安装与兼容性](docs/INSTALL.zh-CN.md#兼容性)。

## 继续阅读

| 指南 | 内容 |
| --- | --- |
| [安装与更新](docs/INSTALL.zh-CN.md) | 导入宠物、更新已有版本、处理显示问题。 |
| [宠物制作流程](docs/MAKING-OF.zh-CN.md) | 从参考图出发，逐帧制作并完成打包。 |
| [提示词示例](docs/PROMPTS.zh-CN.md) | 角色、动作、局部修复和审查的可用模板。 |
| [精灵图格式](docs/FORMAT.zh-CN.md) | 清单字段、动作行、转头方向与播放时长。 |
| [审查与校验](docs/REVIEW.zh-CN.md) | 画面检查方法、文件校验和当前结果。 |
| [图片档案](docs/IMAGE-GALLERY.zh-CN.md) | 742 张源图，包含造型试作、逐帧图片和历史方案。 |

每份指南均有英文版。[文档目录](docs/README.zh-CN.md)还收录了参考来源、署名和 v1.0.1 的[头发描线修复记录](docs/OUTLINE-REPAIR.zh-CN.md)。

## 署名与许可

菲比来自库洛游戏《鸣潮》。社区三视图署名为 **蓝蓝铜离子**，详见[制作署名](NOTICE.md#中文)和[参考来源](docs/SOURCES.zh-CN.md)。

原创脚本和文档采用 [MIT 许可](LICENSE.zh-CN.md)；角色图片与参考图适用[单独的使用说明](ASSET-USAGE.md#中文)。本项目为非官方同人作品，与库洛游戏、OpenAI 无隶属或合作关系。
