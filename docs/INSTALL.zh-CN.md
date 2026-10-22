# 安装与更新

[English](INSTALL.md) · **简体中文** · [文档目录](README.zh-CN.md)

应用需要支持自定义 v2 宠物。当前宠物安装包为 **v1.0.1**。

## 本地安装

1. 下载 [phoebe-chupi-v1.0.1.zip](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/download/v1.0.1/phoebe-chupi-v1.0.1.zip)。
2. 把解压后的 `phoebe-chupi` 文件夹放进 macOS 的 `~/.codex/pets/`，或 Windows 的 `%USERPROFILE%\.codex\pets\`。设置过 `CODEX_HOME` 的，使用该目录下的 `pets` 子目录。
3. 打开**设置 → Pets／Mini 与虚拟宠物**，刷新列表，选择 **Phoebe Chupi · Coding Companion**。

安装后的结构应为：

```text
<Codex home>/pets/phoebe-chupi/
├── pet.json
└── spritesheet.webp
```

如果已经下载完整仓库，也可以运行：

```sh
python3 scripts/install.py --local
```

Windows 可将 `python3` 换成 `py`。指定目录时添加 `--pets-dir PATH`。脚本只复制这两个文件，遇到内容不同的已有安装会保留原文件。

## 原生导入

在完整仓库目录运行：

```sh
python3 scripts/install.py
```

在应用中完成导入，再选择宠物。只想复制导入链接，可以运行 `python3 scripts/install.py --print-url`。

脚本使用[官方宠物导入 URI](https://learn.chatgpt.com/docs/reference/commands#pets)，传入 HTTPS 图片地址、名称、说明和 `spriteVersionNumber=2`。图片地址固定到 `VERSION` 指定的发布版本。

## 更新已有安装

本地宠物先把文件夹备份到 `pets` 目录外，再**只替换 `spritesheet.webp`**。保留原来的 `pet.json`，名称和身份就不会改变。替换后回到设置刷新列表。

云端导入的宠物应通过应用支持的更新流程替换原条目的图片。新建条目会得到另一份独立身份。

## 兼容性

| 使用场景 | 支持情况 |
| --- | --- |
| macOS 桌面端 | 已验证安装与画面表现。 |
| Codex Dot | 16 个头部姿态用于跟随鼠标方向。 |
| Windows 桌面端 | 提供 v2 文件和导入脚本，画面尚未实测。 |
| 网页上传器 | [官方指南](https://learn.chatgpt.com/docs/pets)要求 1536 × 1872。本包为 1536 × 2288，需使用支持 v2 的导入方式。 |

本地桌面文件和云端上传是两份独立安装。菜单名称和功能开放情况可能随应用版本变化。本包未提供 IDE 扩展中的宠物集成。

## 常见问题

| 现象 | 处理方法 |
| --- | --- |
| 列表里找不到宠物 | 刷新列表。确认两个文件直接位于 `pets/phoebe-chupi/`，没有多套一层文件夹。 |
| 预览空白 | 用发布页的 `SHA256SUMS.txt` 核对下载文件，并确认清单中写有 `spriteVersionNumber: 2`。 |
| 浮窗仍显示之前的角色 | 选中菲比后隐藏再显示浮窗。若画面仍未刷新，保存工作后择时重启应用。 |
| 宠物停在一张静帧 | 检查系统的“减少动态效果”设置及当前任务状态。眨眼动作包含半闭眼和闭眼姿态。 |
| 转头时取错帧 | 保留完整的 1536 × 2288 图片和 v2 字段，最后两行是转头姿态。 |
| 本地脚本拒绝覆盖 | 备份已有安装，再按上面的更新步骤替换图片。 |
| 放大后看起来发糊 | 先按原生 192 × 208 尺寸检查。截图缩放和 GIF 调色板都会影响观感。 |

仍有显示问题时，可以[提交 Issue](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues)，附上应用版本、操作系统、安装方式和出问题的帧。
