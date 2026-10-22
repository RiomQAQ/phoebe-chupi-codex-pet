# 菲比啾比 · 坐好了

[English](README.md) · **简体中文**

把电脑抱过来，坐好，陪你写代码。

这是给 **Codex 宠物和 Dot（Codex 里的那个点）**做的菲比啾比。**放进 Dot 后，她会跟着鼠标转头**；平时会眨眼、打字、抬头等你回复，偶尔抱着电脑挪一挪，再小跳一下。

![菲比啾比](previews/hero.png)

使用 **GPT-6-Astra 制作**，图片通过内置图像生成功能生成、修改。[完整署名](NOTICE.md)。

**v1.0.1：**修复了上一版清理透明边缘时被误改浅的头发描线。眨眼、动作和 Dot 转头都保留。[修复对照与检查记录](docs/OUTLINE-REPAIR.md#中文)。

| 坐着陪你 | 忙着写代码 | 等你回一句 |
| :---: | :---: | :---: |
| ![待机](previews/idle.gif) | ![工作](previews/running.gif) | ![等待](previews/waiting.gif) |

## 在 Dot 里，会跟着鼠标转头

这版补齐了 16 个视线姿态。鼠标移到不同方向时，她会转头看过去，身体和腿上的电脑尽量保持稳定。

| 16 个转头方向 | 小跳一下，再坐好 |
| :---: | :---: |
| ![转头](previews/look-loop.gif) | ![小跳衔接](previews/idle-jump-idle.gif) |

上面的 GIF 为了展示所有方向，会依次循环。在 Dot 里，方向由鼠标位置决定。当前安装包保留有眨眼变化的版本；后来试过一直睁眼，反而少了些灵气，就退回来了。

## 安装

只想用宠物，去 [Releases](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/latest) 下载 **`phoebe-chupi-v1.0.1.zip`**。另一个大得多的图片档案包，用来看原图和制作过程，不是安装必需的。

安装目录里只有两个文件：

```text
phoebe-chupi/
├── pet.json
└── spritesheet.webp
```

### 打开应用的原生导入

下载或克隆本仓库后，运行：

```sh
python3 scripts/install.py
```

Windows 可以用 `py scripts/install.py`。脚本会打开应用的宠物导入流程，传入本次发布的图片地址和 `spriteVersionNumber=2`。在应用里完成导入，再选择 **Phoebe Chupi · Coding Companion**。

要复制安装链接，运行 `python3 scripts/install.py --print-url`。链接采用[官方原生导入格式](https://learn.chatgpt.com/docs/reference/commands)。

### 直接复制到本地

这种方法不需要 Python：

1. 下载并解压小安装包。
2. 把 `phoebe-chupi` 文件夹放进 macOS 的 `~/.codex/pets/`，或 Windows 的 `%USERPROFILE%\.codex\pets\`。自定义过 `CODEX_HOME` 的，放进该目录下的 `pets` 文件夹。
3. 打开**设置 → Pets／Mini 与虚拟宠物**，点刷新，再选 **Phoebe Chupi · Coding Companion**。菜单名字可能随版本变化。

确认没有多套一层文件夹：

```text
<Codex home>/pets/phoebe-chupi/pet.json
<Codex home>/pets/phoebe-chupi/spritesheet.webp
```

也可以从完整仓库运行：

```sh
python3 scripts/install.py --local
```

它只复制清单和 WebP，不改应用设置，遇到不同的已有文件也不会直接覆盖。指定目录用 `--local --pets-dir PATH`。

### 更新已有的本地宠物

先把原来的宠物文件夹备份到 `pets` 目录外，再用新版的 `spritesheet.webp` 替换旧图片，保留自己的 `pet.json`。这样名字和身份不会变，也不会多一个重复条目。回到设置刷新即可。云端导入的宠物应在应用里更新原条目。

### 可以用在哪里

- **Codex 桌面宠物：**已在 macOS 上安装、切换并查看实际效果。
- **Codex Dot：**已适配，能在里面使用，头部会跟随鼠标方向转动。
- **Windows 桌面端：**提供通用 v2 文件和原生导入方法，尚未在 Windows 上逐帧验收。
- **网页上传：**当前网页上传说明要求 1536 × 1872；本项目为 1536 × 2288 的 v2，不能当 v1 直接上传。见[官方宠物文档](https://learn.chatgpt.com/docs/pets)。

应用需要支持自定义 v2 宠物。这是宠物文件，不需要另装插件。

## 她平时会做什么

大多数时候，她都坐着用同一台电脑：打字、想事情、抬头等你，或检查刚做完的结果。需要移动时，就把电脑合上抱走。

| 状态 | 帧数 | 动作 |
| --- | ---: | --- |
| `idle` | 6 | 坐着呼吸、眨眼。 |
| `running-right` | 8 | 抱着合上的电脑向右走。 |
| `running-left` | 8 | 抱电脑向左走，单独画，配饰不会镜像换边。 |
| `waving` | 4 | 轻轻挥一只手打招呼。 |
| `jumping` | 5 | 带着电脑小跳一下，再落回原位。 |
| `failed` | 8 | 有点委屈，需要帮忙，随后恢复。 |
| `waiting` | 6 | 歪头，等你回复。 |
| `running` | 6 | 专心打字、思考，这个状态表示工作中。 |
| `review` | 6 | 看过结果，露出一点满意的表情。 |
| 视线扩展 | 16 | 在 Dot 里跟着鼠标转头。 |

| 抱电脑向右 | 抱电脑向左 | 打个招呼 |
| :---: | :---: | :---: |
| ![向右](previews/running-right.gif) | ![向左](previews/running-left.gif) | ![挥手](previews/waving.gif) |
| 检查结果 | 小跳一下 | 帮帮我？ |
| ![检查](previews/review.gif) | ![小跳](previews/jumping.gif) | ![求助](previews/failed.gif) |

何时播放哪个状态，由应用决定。GIF 用来预览，颜色数量比实际文件少，播放时长也不会写进宠物设置。发布 WebP 与最终 PNG 的 RGBA 像素完全一致。

## 她是怎么做出来的

不是画好第一张就算完成。[制作记录](docs/MAKING-OF.zh-CN.md)写了整个过程，也保留了没画好的部分：

1. **先找对社区造型。** 以选定的正、侧、背面参考为准，不混用官方成年比例或其他二创风格。
2. **先固定两张基准。** 坐着用电脑、站着抱电脑；脸、帽子、头发、发夹和电脑都跟着同一套标准走。
3. **逐帧生成、逐帧修改。** 多一只手、重复眉毛、头突然缩小、电脑结构画错，都要回到基准图修。
4. **连起来看。** 看前后帧、整行循环、小尺寸效果，也看动作结束后能不能自然回到坐姿。
5. **补齐并检查转头。** 先做四个正方向，再补斜方向，藏起标签检查到底像在看哪里。
6. **检查真正安装的文件。** 最终 WebP、裁剪帧、图片索引和双文件安装包一起核对。

脚本负责预览、裁剪、校验和打包，动作和表情再单独看一遍。

### 想看详细过程

| 文档 | 内容 |
| --- | --- |
| [中文制作记录](docs/MAKING-OF.zh-CN.md) · [English](docs/MAKING-OF.md) | 参考怎么选、造型怎么固定、逐帧怎么改、怎么拼图审查，以及为什么退回睁眼试验。 |
| [审查记录](docs/REVIEW.md) | 查了什么、方向怎么盲测、哪些通过了、哪些仍需留意。 |
| [v1.0.1 描线修复](docs/OUTLINE-REPAIR.md#中文) | 导出问题的原因、修复前后对照、全帧检查和恢复脚本。 |
| [提示词示例](docs/PROMPTS.md) | 角色、动作、修复、视线和审查的提示词写法。 |
| [格式说明](docs/FORMAT.md) | 清单、格子、动作行、角度、时长和排版规则。 |
| [参考来源](docs/SOURCES.md) | 社区造型、B 站动作、作者署名和 README 参考项目。 |
| [全部图片](docs/IMAGE-GALLERY.md) | **742 张不同源图片**，含原图、单帧、样张、失败稿和已回退的试验。 |

## 这一版保留了什么

- **9 种动作、16 个转头方向：**73 个有效格，另外 15 格全透明。
- **原生 v2：**整图 1536 × 2288，共 8 列 11 行，每格 192 × 208。
- **无损 WebP：**1,910,162 字节，解码后与修复后的 PNG 像素一致。
- **保留眨眼。** 半闭眼和闭眼属于这个版本的表情变化。一直睁眼的试验放在档案里，不会装进去。
- **完整图片过程：**742 张不同原图，索引对应 1,290 个工作文件实例；另附公开预览和最终精灵图的裁剪帧。

还有几处可以继续打磨：`045` 和 `067.5` 看起来接近，`225 → 247.5` 变化更明显；原生小图放大后也会变柔和。这些都保留在记录里，没有写成完美无缺。

## 校验与重新打包

维护者可以使用 Python 3.10+：

```sh
python3 -m pip install -r requirements.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/render_previews.py
python3 scripts/package.py
```

CI 运行文件校验和描线回归测试，会拦下有问题的 v1.0.0 图片。改过图片后，仍要重新看动作。小 ZIP 只装宠物，独立图片包保留完整制作过程。[文件校验值](CHECKSUMS.sha256)也一并提供。

## 遇到问题

- **列表缩略图空白：**点刷新，等图片重新载入，确认下载完整、版本字段为 2。
- **浮窗还是上一个角色：**选好菲比后隐藏再显示。如果应用一直保留旧渲染状态，保存工作，方便时重启。
- **动作行或转头方向不对：**保留完整 v2 尺寸和版本字段，不裁末尾两行，也不把每格单独撑满。
- **像停在眨眼：**检查系统减少动态效果的设置和应用当前状态。这版保留眨眼，改 GIF 时长不会改变实际播放。
- **安装脚本不肯覆盖：**先查看并备份已有目录，它是在保留你本地不同的文件。

## 署名与使用

菲比来自库洛游戏《鸣潮》，「啾比」是社区二创方向。选定的 AI 三视图署名为蓝蓝铜离子。作者线索、未确认之处与全部链接见[参考来源](docs/SOURCES.md)和[完整署名](NOTICE.md)。

README 编排参考了 [phoebe-codex-pet](https://github.com/sherlidian01-web/phoebe-codex-pet)、[remielle-codex-pet](https://github.com/HanaAyane/remielle-codex-pet) 和 [awesome-codex-pet](https://github.com/legeling/awesome-codex-pet)。

原创脚本与文档采用 [MIT](LICENSE)，角色图片和参考资料有单独的[使用说明](ASSET-USAGE.md)。这是非官方同人项目，与库洛游戏、OpenAI 无官方合作关系。
