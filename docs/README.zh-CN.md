# 文档目录

[English](README.md) · **简体中文** · [项目首页](../README.zh-CN.md)

这里介绍宠物的安装方法、精灵图的制作过程，以及如何复用这套流程制作另一只宠物。

## 使用宠物

- [安装与更新](INSTALL.zh-CN.md)：本地安装、原生导入、兼容性与常见问题。
- [图片档案](IMAGE-GALLERY.zh-CN.md)：源图、最终帧和动画预览。
- [制作署名](../NOTICE.md#中文) · [图片使用说明](../ASSET-USAGE.md#中文)：来源与使用范围。

## 制作与维护

[制作流程](MAKING-OF.zh-CN.md)介绍完整步骤，其他文档可以按需查阅：

| 文档 | 用途 |
| --- | --- |
| [提示词示例](PROMPTS.zh-CN.md) | 固定角色造型、编辑单帧、审查动作。 |
| [精灵图格式](FORMAT.zh-CN.md) | 查阅 v2 清单、格子布局、动作行和转头方向。 |
| [审查与校验](REVIEW.zh-CN.md) | 检查画面、运行校验、准备发布。 |
| [参考来源](SOURCES.zh-CN.md) | 查找角色资料、造型图、动作研究和打包示例。 |
| [描线修复记录](OUTLINE-REPAIR.zh-CN.md) | 了解 v1.0.1 的导出修正并复现修复。 |
| [检查记录索引](repair-qa/README.zh-CN.md) | 查阅逐帧报告和独立方向审查。 |

## 仓库结构

```text
pets/phoebe-chupi/  安装用清单与 WebP
art/canonical/     角色和姿势基准图
art/frames/        当前精灵图的原像素裁剪帧
art/archive/       制作图片
art/repair/        修复源图与对照图
art/releases/      历史版本快照
previews/          动画、总览图与静帧
scripts/           校验、预览、安装与打包脚本
tests/             描线回归测试
docs/              指南与检查报告
```

英文指南使用 `.md`，对应的中文使用 `.zh-CN.md`。图片目录和简短的权利说明在同一页提供中英文。
