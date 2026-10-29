# 文档总目录

[English](README.md) · **简体中文** · [返回项目首页](../README.zh-CN.md)

这里汇总了 **菲比啾比（Phoebe Chupi）v1.0.2** 的全部使用指南、精灵图技术规范、逐帧制作笔记、提示词模板，以及两次版本修复的完整审查档案。无论你是想把菲比装进 Codex 桌面端，还是想照着这套流程自己动手做一只 v2 桌面宠物，都可以从下面的路线图快速找到入口。

![原生尺寸五状态静帧预览](../previews/stills/five-states.png)

---

## 阅读路线图：按你的目标选择入口

```text
你是哪种读者？
 │
 ├─► 【我想安装或升级菲比啾比】
 │     └─► 1. 安装与更新 (INSTALL.zh-CN.md) ──► 2. 常见问题排查 (INSTALL.zh-CN.md#常见问题)
 │
 ├─► 【我想自己做一只 Codex v2 桌宠】
 │     └─► 1. 宠物制作全流程 (MAKING-OF.zh-CN.md)
 │         2. 提示词实战手册 (PROMPTS.zh-CN.md)
 │         3. 精灵图格式规范 (FORMAT.zh-CN.md)
 │         4. 审查与自动校验 (REVIEW.zh-CN.md)
 │
 └─► 【我想查阅原画档案、修复细节或版权来源】
       └─► 1. 832 张源图档案 (IMAGE-GALLERY.zh-CN.md)
           2. v1.0.2 转头修复记录 (look-repair-qa/README.zh-CN.md)
           3. v1.0.1 描线修复记录 (OUTLINE-REPAIR.zh-CN.md & repair-qa/README.zh-CN.md)
           4. 参考来源与署名 (SOURCES.zh-CN.md / NOTICE.md / ASSET-USAGE.md)
```

---

## 一、使用与欣赏宠物

| 文档入口 | 内容简介 |
| --- | --- |
| **[安装与更新](INSTALL.zh-CN.md)** | 手动放入 `pets` 目录、运行 `scripts/install.py` 本地复制或拉起官方 URI 原生导入、保留身份无损升级，以及 7 类常见显示问题排查。 |
| **[图片档案总览](IMAGE-GALLERY.zh-CN.md)** | 按 7 个制作阶段分类浏览 **832 张独立源图**（对应 **1,447 个工作文件记录**），并提供当前发布整图、73 张单帧裁剪图与深浅背景动画入口。 |
| **[制作署名](../NOTICE.md#中文)** · **[图片使用说明](../ASSET-USAGE.md#中文)** | 原作角色归属、社区三视图署名、AI 辅助说明，以及个人非商业使用、修改与分享的具体边界。 |

---

## 二、制作流程、技术规范与质量审查

建议先读 **[宠物制作全流程](MAKING-OF.zh-CN.md)** 建立整体概念，再按需查阅配套手册：

| 文档入口 | 适用阶段 | 核心内容 |
| --- | --- | --- |
| **[宠物制作全流程](MAKING-OF.zh-CN.md)** | 全流程主线 | 从社区三视图考据、正/侧/背去背拆解、建立“坐姿工作”与“抱电脑行走”双母本，到 9 行标准动作、16 向 Dot 转头、统一取景拼图与打包发布的完整图文记录。 |
| **[提示词实战手册](PROMPTS.zh-CN.md)** | 生成与修图 | 7 套可直接复用的提示词模板（角色基准、单帧动作、局部缺陷修复、Dot 转头、脸型跳变修整、全片审查、无标签 A/B 盲审），附带每条约束的设计意图与配图示例。 |
| **[精灵图格式规范](FORMAT.zh-CN.md)** | 拼图与导出 | 详解 `pet.json` 五字段清单、`1536 × 2288`（8 列 × 11 行）可视化网格图例、`192 × 208` 单格坐标公式、16 向顺时针角度罗盘、预览时长及无损 WebP 导出规则。 |
| **[审查与自动校验](REVIEW.zh-CN.md)** | 验收与发布 | 单帧 8 项肉眼检查清单、连贯动作与跨状态衔接审查、三方无标签方向盲审流程、v1.0.2 完整实测数据、已知限制及 Python 自动化校验用法。 |
| **[参考来源考据](SOURCES.zh-CN.md)** | 设定与考据 | 区分库洛游戏《鸣潮》官方菲比设定、蓝蓝铜离子发布的社区三视图、6 份 Bilibili 动作/神态参考视频，以及开源 Codex 宠物打包参考。 |
| **[v1.0.2 转头修复检查记录](look-repair-qa/README.zh-CN.md)** | v1.0.2 专项档案 | 图文展示 v1.0.2 重绘 12 张转头姿态的前后对比图板、左上回正过渡放大图、三名独立 AI 审查员的盲审原始记录及原生尺寸浏览器抽查报告。 |
| **[头发描线修复记录](OUTLINE-REPAIR.zh-CN.md)** | v1.0.1 专项档案 | 复盘 v1.0.0 导出清理为何把深色轮廓染成浅色斑段，展示最近邻放大像素对比图、三处典型坐标 RGB 回归测试及复现命令。 |
| **[v1.0.1 检查记录索引](repair-qa/README.zh-CN.md)** | v1.0.1 历史证据 | 保存 v1.0.1 描线恢复后的图集几何报告、73 帧独立审查与第一轮三方方向盲审 JSON 记录。 |

---

## 三、仓库目录与文件关系图例

```text
phoebe-chupi-codex-pet/
├── pets/phoebe-chupi/           # 【最终运行包】直接放入 ~/.codex/pets/ 即可使用的两个文件
│   ├── pet.json                 #   ├─ 5 字段标准 v2 清单
│   └── spritesheet.webp         #   └─ 1536 × 2288 无损透明 WebP 精灵整图
│
├── art/                         # 【美术源图与基准资产】
│   ├── canonical/               #   ├─ 角色三视图、去背视角图、站姿设定、坐姿/抱电脑母本、十字四向基准
│   ├── approved/v1.0.2/         #   ├─ 经人工与脚本双重审查锁定的 v1.0.2 PNG 像素基准
│   ├── approved-runtime.json    #   ├─ 锁定发布版哈希及前 9 行（57 帧）与 v1.0.1 像素一致性的守卫配置
│   ├── final/spritesheet.png    #   ├─ 与发布版 WebP 解码 RGBA 完全相同的 PNG 整图
│   ├── frames/                  #   ├─ 从当前整图精确裁剪出的 73 张 192 × 208 单格 PNG（9 态 + look）
│   ├── samples/                 #   ├─ 4 张角色表情样张与原生尺寸对比图
│   ├── archive/                 #   ├─ 7 个制作阶段的 832 张去重历史源图
│   ├── index.json               #   ├─ 832 张源图的哈希、尺寸与 1,447 个工作文件名映射索引
│   ├── repair/                  #   ├─ v1.0.1 描线修复与 v1.0.2 转头修复的源图、对照板及 HTML 预览器
│   └── releases/                #   └─ v1.0.0 与 v1.0.1 历史发布整图快照（用于回归测试对照）
│
├── previews/                    # 【预览动画与总览图】
│   ├── *.gif / dark/*.gif       #   ├─ 浅色与深色背景下的各状态循环 GIF、16 向转头 GIF、小跳衔接 GIF
│   ├── contact-sheet*.png       #   ├─ 浅色与深色背景的 9 行标准动作全帧总览图
│   ├── directions.png           #   ├─ Dot 16 向转头角度总览图
│   └── stills/                  #   └─ 192 × 208 原生 1:1 像素代表静帧
│
├── scripts/                     # 【自动化工具链】
│   ├── validate.py              #   ├─ 校验清单、像素一致性、边距、源图哈希、EXIF 清理与隐私标记
│   ├── audit_artwork.py         #   ├─ 核对 v1.0.2 批准基准与前 9 行标准动作像素零改动
│   ├── restore_outlines.py      #   ├─ 复现 v1.0.1 头发深色描线无损恢复与像素审计
│   ├── render_previews.py       #   ├─ 从发布的 WebP 重新生成全部 GIF、总览图与静帧
│   ├── install.py               #   └─ 本地目录复制安装或生成官方导入 URI
│   └── package.py               #   └─ 在 dist/ 下构建发布 ZIP 与 SHA256SUMS.txt
│
├── tests/                       # 【回归测试套件】
│   ├── test_approved_artwork.py #   ├─ 验证当前运行包、前 9 行冻结像素与源图映射
│   └── test_outline_regression.py # └─ 验证 v1.0.0 错误像素识别与 v1.0.1 描线恢复准确性
│
└── docs/                        # 【中英文双语文档与 QA 证据】
    ├── *.zh-CN.md / *.md        #   ├─ 中文（.zh-CN.md）与英文（.md）一一对应的全套指南
    ├── gallery/                 #   ├─ 22 个分阶段源图浏览页（中英双语图注）
    ├── look-repair-qa/          #   ├─ v1.0.2 转头修复的测量、盲审与安装回读 JSON 证据
    └── repair-qa/               #   └─ v1.0.1 描线修复的几何、色彩与盲审 JSON 证据
```

### 版本基准速查

- **当前版本**：`v1.0.2`（修改了第 9、10 行的 12 张转头姿态；前 9 行共 57 张标准动作帧与 `v1.0.1` 的 RGBA 像素逐点一致）。
- **像素基准文件**：[art/approved/v1.0.2/spritesheet.png](../art/approved/v1.0.2/spritesheet.png)，其哈希与前 9 行冻结校验规则记录在 [art/approved-runtime.json](../art/approved-runtime.json)。
- **历史快照**：上一版完整快照保存在 [art/releases/v1.0.1](../art/releases/v1.0.1)，初始版本保存在 [art/releases/v1.0.0](../art/releases/v1.0.0)。
- **语言约定**：所有专题指南均采用英文 `.md` 与中文 `.zh-CN.md` 成对维护；[图片档案分页](gallery/early-concept-01.md)、[制作署名](../NOTICE.md) 与 [图片使用说明](../ASSET-USAGE.md) 则在同一页面内提供中英双语对照。
