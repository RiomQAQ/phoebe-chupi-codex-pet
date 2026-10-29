# 参考来源与考据脉络

[English](SOURCES.md) · **简体中文** · [文档目录](README.zh-CN.md)

菲比啾比（Phoebe Chupi）Codex 桌宠并不是凭空捏造的形象，而是把**《鸣潮》官方角色设定**、**社区二创 Q 版三视图**、**B 站 / 论坛动态表情研究**以及 **Codex 桌面端 v2 精灵整图规范**融合在一起的产物。

本页完整记录了每一类参考资料在项目中承担的具体职责。收录来源仅用于交代考据脉络与署名致谢，不等于授予第三方素材的转载或使用权；关于仓库内文件的使用边界，请一并参阅[图片使用说明](../ASSET-USAGE.md#中文)。

---

## 考据与转化链路总览

```text
+-----------------------------------------------------------------------------+
|  [A] 官方角色设定（库洛游戏《鸣潮》）                                         |
|      └─> 锁定配色、服饰结构、宽白帽深紫帽带、右侧蓝发夹与左侧呆毛             |
|                                                                             |
|  [B] 社区 Q 版三视图（蓝蓝铜离子 BV1zzAAzPEVA 等）                            |
|      └─> 锁定二头身圆润比例、分层紫色眼睛、宽檐帽轮廓 -> 生成坐姿/抱电脑母本 |
|                                                                             |
|  [C] 社区视频与表情研究（小跳节奏、深夜伏案、失落求助等）                     |
|      └─> 转化为 9 类标准动作（57 帧）+ Dot 16 向转头 + 4 张日常表情样张       |
|                                                                             |
|  [D] Codex v2 宠物规范与社区开源桌宠仓库                                      |
|      └─> 封装为 1536 × 2288 (8×11, 73 有效格) WebP + pet.json + 自动校验套件 |
+-----------------------------------------------------------------------------+
```

---

## 角色与造型参考

<p align="center">
  <img src="../art/canonical/user-reference.png" width="680" alt="社区三视图参考图（保留原图署名水印）" />
</p>

| 来源 | 在项目中承担的作用 |
| --- | --- |
| 库洛游戏：[菲比资料](https://wutheringwaves.kurogames.com/en/main/news/detail/2106)与[相关资料](https://wutheringwaves.kurogames.com/en/main/news/detail/2101) | 核对官方角色身份、主副配色、圣职服饰层次以及标志性配饰（帽子、发夹、袖口、腿部条纹）的准确位置。 |
| 蓝蓝铜离子：[BV1zzAAzPEVA](https://www.bilibili.com/video/BV1zzAAzPEVA/) | 主要社区正面、侧面、背面参考，原投稿标注为豆包 AI 生成。收录图及三张正/侧/背裁剪图均完整保留了原署名水印。 |
| 社区合集：[BV1zUJdzdEYF](https://www.bilibili.com/video/BV1zUJdzdEYF/) | 研究“菲比啾比”的社区二创风格特征与署名线索。 |
| Arca：[表情包 42655](https://arca.live/e/42655)、[表情包 47956](https://arca.live/e/47956)、[Binci 主页](https://arca.live/u/@Binci) | 社区作者溯源线索；受限于站点访问限制，原帖作者身份未能直接核实，仅作线索记录。 |
| DCCon：[菲比表情包 165313](https://dccon.dcinside.com/hot/1/title/%ED%8E%98%EB%B9%84#165313)，发布者 **Binci1** | 表情与社区 Q 版造型语言研究。 |

> **考据说明**：本项目的 Q 版圆润轮廓以社区三视图为准，该图不属于官方角色设定。`Binci` 与 `Binci1` 两个账号的身份关联尚未核实，仓库不将二者标为同一作者。

---

## 动作与表情研究

为了让桌宠在陪伴写代码时不显得像机械钟摆，我们参考了多支社区投稿中的微表情与动作节奏，并将其重新绘制为本项目统一的坐姿/抱电脑帧（**仓库不分发视频原帧或批量下载的表情包**）：

<p align="center">
  <img src="../art/samples/samples-overview.png" width="720" alt="四张关键日常表情样张总览" />
</p>

| 投稿 | 研究内容与观察节点 | 对应项目产出 |
| --- | --- | --- |
| [BV1W2ARznELg](https://www.bilibili.com/video/BV1W2ARznELg/) | 求助状态中的轻微失落与恢复节奏 | `failed`（求助 · 8 帧）状态循环与 `03-help.png` 样张 |
| Sans_AI：[BV1zn9YBxEVJ](https://www.bilibili.com/video/BV1zn9YBxEVJ/) | 约 `17.5–19.75 秒` 的轻快小跳节奏 | `jumping`（坐姿小跳 · 5 帧）起跳、腾空与落地曲线 |
| 喵内特洛夫斯基：[BV1TYMB6CE7U](https://www.bilibili.com/video/BV1TYMB6CE7U/) | 后续样张中的伏案与托腮思考表情 | `02-thinking.png` 样张与坐姿表情研究 |
| [BV1zycfznE2E](https://www.bilibili.com/video/BV1zycfznE2E/) | 等待和迎接的表情研究 | `waiting`（等待 · 6 帧）与 `01-waiting.png` / `04-happy.png` 样张 |
| [BV1HQ8g6VEo7](https://www.bilibili.com/video/BV1HQ8g6VEo7/) | 后续样张中的困倦工作表情 | `idle`（待机眨眼）与工作神态研究 |
| 虾饺shrimp：[BV1BPaT6vEqk](https://www.bilibili.com/video/BV1BPaT6vEqk/) | 约 `21 秒`、`26 秒` 的深夜表情 | 衍生表情研究与候选帧探索 |

> **方法论原则**：单帧研究只记录实际看到的五官与姿态表情，不在审查或文档中把它推断成原视频未展示的完整动画。

---

## 4. 格式与打包示例

| 资料 | 用途 |
| --- | --- |
| [官方导入命令](https://learn.chatgpt.com/docs/reference/commands#pets) | 宠物原生导入 URI 与 v2 参数规范。 |
| [官方宠物指南](https://learn.chatgpt.com/docs/pets) | 应用控制方式和导入说明。 |
| [phoebe-codex-pet](https://github.com/sherlidian01-web/phoebe-codex-pet) | 双语展示与动画预览组织方式。 |
| [remielle-codex-pet](https://github.com/HanaAyane/remielle-codex-pet) | 安装目录结构与通用 5 字段 v2 `pet.json` 清单示例。 |
| [awesome-codex-pet](https://github.com/legeling/awesome-codex-pet) | 图片目录导航和来源署名规范。 |

---

## 5. 收录范围与版本台账

为了保证整个制作与修复过程可核查、可复现，仓库将全部制作图片与技术记录归档如下：

1. **全量源图档案（832 张不同源图 / 1,447 个工作文件实例）**
   - [图片档案](IMAGE-GALLERY.zh-CN.md)保留 **832 张不同 SHA-256 源图**，[`art/index.json`](../art/index.json) 对应 **1,447 个工作文件实例**，包含生成帧、姿势研究、对照图、未采用候选和保留署名的三视图。当前 73 张裁剪帧与修复证据另外收录。
2. **v1.0.2 转头重绘与 6 帧脸型细化**
   - `v1.0.2` 使用内置图像生成功能重画了 **12 张完整转头帧**，另有 4 张沿用原画：`022.5`、`045`、`067.5` 和 `090`。修改保留了原有帽子设计，没有粘贴脸部或对脸部做局部变形。
   - 最新一轮细化覆盖 `000`、`157.5`、`247.5`、`292.5`、`315`、`337.5` 六个角度，专门处理脸颊过窄，以及从左上注视姿态转回时脸部显得变大的问题。
3. **当前审查基准与历史快照保护**
   - 当前经过审查的基准为 [`art/approved/v1.0.2/spritesheet.png`](../art/approved/v1.0.2/spritesheet.png)，记录在 [`art/approved-runtime.json`](../art/approved-runtime.json)。
   - 前九行（共 57 张标准动作帧）原样保留 `v1.0.1` 的 RGBA 像素。`v1.0.1` 快照保存在 [`art/releases/v1.0.1`](../art/releases/v1.0.1)，原有[描线修复检查记录](repair-qa/README.zh-CN.md)继续保留；新的[转头修复检查记录](look-repair-qa/README.zh-CN.md)对应 `v1.0.2`。
4. **第三方链接边界**
   - 第三方研究合集仅保留外部来源链接；仓库内只收录制作图片和可复现的技术记录，便于检查宠物成品。
