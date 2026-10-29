# 安装与更新指南

[English](INSTALL.md) · **简体中文** · [返回文档目录](README.zh-CN.md)

菲比啾比采用 Codex 标准 **v2 自定义宠物格式**，当前发布版本为 **v1.0.2**。安装包内只包含两个文件（`pet.json` 与 `spritesheet.webp`），无需安装任何额外插件或运行后台进程。

![原生 192 × 208 尺寸五状态静帧预览](../previews/stills/five-states.png)

---

## 两种安装方式对比：该选哪一种？

Codex 支持**本地目录加载**与**官方 URI 原生导入**两种方式，它们在应用内相互独立：

```text
选择安装方式
 │
 ├─► 方式 A：本地目录安装（推荐，离线可用、升级最简单）
 │     └─► 将 phoebe-chupi/ 放入 ~/.codex/pets/
 │         特点：直接读取本地无损 WebP；后续升级只需覆盖 spritesheet.webp
 │
 └─► 方式 B：原生 URI 导入（通过官方导入链接写入应用）
       └─► 运行 python3 scripts/install.py 拉起导入链接
           特点：通过 HTTPS 拉取对应 Release 的图片并注册到应用宠物列表中
```

---

## 本地安装

### 方法 1：下载 Release 压缩包手动放入（最快）

1. 下载最新安装包 **[phoebe-chupi-v1.0.2.zip](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/download/v1.0.2/phoebe-chupi-v1.0.2.zip)** 并解压。
2. 将解压得到的 `phoebe-chupi` 文件夹放入对应系统的 Codex `pets` 目录：

   | 操作系统 / 环境 | 目标 `pets` 目录路径 |
   | --- | --- |
   | **macOS** | `~/.codex/pets/` |
   | **Windows** | `%USERPROFILE%\.codex\pets\` |
   | **自定义 `CODEX_HOME`** | `<CODEX_HOME>/pets/` |

3. 打开 Codex 桌面端 **设置 → Pets（或 Mini 与虚拟宠物）**，点击**刷新列表**，选择 **Phoebe Chupi · Coding Companion**。

> **目录层级检查图例（避免多套一层文件夹）**
>
> ```text
> ✅ 正确结构（两个文件直接位于 phoebe-chupi/ 下）：
> <Codex home>/pets/
> └── phoebe-chupi/
>     ├── pet.json
>     └── spritesheet.webp
>
> ❌ 常见错误（解压软件自动多建了一层版本号目录，会导致列表刷不出）：
> <Codex home>/pets/
> └── phoebe-chupi-v1.0.2/
>     └── phoebe-chupi/
>         ├── pet.json
>         └── spritesheet.webp
> ```

### 方法 2：使用仓库脚本一键复制

如果你已经在本地克隆了完整仓库，可以直接运行安装脚本：

```sh
python3 scripts/install.py --local
```

- **Windows 环境**：可将 `python3` 替换为 `py`（即 `py scripts/install.py --local`）。
- **指定自定义目录**：附加 `--pets-dir PATH` 参数。
- **安全保护机制**：脚本只会复制 `pet.json` 和 `spritesheet.webp` 两个文件；如果目标位置已经存在内容不同的同名文件，脚本会拒绝盲目覆盖并提示你先备份，防止冲掉你自己的修改。

---

## 原生导入

如果你希望通过 Codex 的 [官方宠物导入 URI](https://learn.chatgpt.com/docs/reference/commands#pets) 导入，可以在完整仓库目录下运行：

```sh
python3 scripts/install.py
```

脚本会自动构造固定到当前 `VERSION`（`v1.0.2`）发布页 HTTPS 图片地址的导入链接并调用系统打开，随后在 Codex 应用弹窗中确认导入并选中宠物即可。

- **仅打印导入链接（不自动唤起应用）**：
  ```sh
  python3 scripts/install.py --print-url
  ```
- **URI 参数说明**：导入链接包含经过校验的 Release HTTPS 图片地址、显示名称（`Phoebe Chupi · Coding Companion`）、简介以及 `spriteVersionNumber=2`。

---

## 更新已有安装

从旧版本（如 `v1.0.0` 或 `v1.0.1`）升级到 `v1.0.2` 时，请按安装类型操作，以保留你现有的宠物条目与选中状态：

```text
平滑升级流程（保留原有宠物 ID 与设置）
  1. 先把旧的 ~/.codex/pets/phoebe-chupi/ 备份到 pets 目录之外（不要留在 pets/ 里，否则会显示两只同名宠物）
  2. 用新版的 spritesheet.webp 覆盖原目录中的 spritesheet.webp
  3. 保留原有的 pet.json 不动 ──► 回到 Codex 设置点击“刷新列表”
```

- **本地安装的宠物**：先把原文件夹备份到 `pets/` 目录以外的位置，然后**只替换 `spritesheet.webp`**，保留原来的 `pet.json`。这样宠物的本地身份标识不会改变，刷新列表或重开浮窗即可生效。
- **云端 / URI 导入的宠物**：请通过应用支持的更新流程替换原有条目上的图片；如果直接重新执行新建导入，应用会生成另一条独立身份的宠物记录。
- **v1.0.2 变更范围说明**：`v1.0.2` 仅更新了第 9、10 行的 12 张转头姿态；前 9 行共 57 张标准动作帧（含待机眨眼）的 RGBA 像素与 `v1.0.1` **逐字节完全一致**。

---

## 兼容性

| 使用场景 | 当前支持与验证状态 |
| --- | --- |
| **macOS Codex 桌面端** | **完整支持**。`v1.0.2` 已完成本机安装与应用端保存图片回读校验，解码后的 RGBA 像素与发布版完全一致（见 [安装回读记录](look-repair-qa/installation-verification.json)）。 |
| **Codex Dot 悬浮球** | **提供完整 16 向头部姿态**。鼠标移动时按 `22.5°` 步进选择对应朝向（`v1.0.1` 已在原生 Dot 实测，`v1.0.2` 完成 1× 浏览器逐帧核对，原生 Dot 实机画面待补）。 |
| **Windows Codex 桌面端** | **提供通用 v2 包与脚本**。文件结构与 macOS 完全通用，Windows 实机画面截图待后续补充。 |
| **原生 URI 导入或图片上传** | 需使用支持自定义 v2 宠物的客户端构建版本；应用内宠物交互方式详见 [Codex 官方宠物指南](https://learn.chatgpt.com/docs/pets)。 |

- **关于离散转头步进的说明**：Dot 的视线跟随由 16 张独立绘制的静态角度帧驱动，而非 3D 实时骨骼插值。在 `225° → 247.5°`（左下侧转）和 `270° → 292.5°`（正左向左上抬头）等跨度较大的相邻角度间切换时，仍能看到清晰的姿态步进，详情见 [审查范围与已知限制](REVIEW.zh-CN.md#已知限制)。
- **关于原生尺寸与放大观感**：单格原生尺寸为 **192 × 208 px**，在桌面实际窗口中线条锐利紧凑：

![原生尺寸与放大观察对比](../art/samples/native-size-comparison.png)

---

## 常见问题

| 遇到的现象 | 原因分析与处理步骤 |
| --- | --- |
| **宠物列表里找不到菲比** | 1. 点击设置页的“刷新列表”；<br>2. 检查路径是否为 `pets/phoebe-chupi/pet.json`，确认解压时没有多套一层文件夹。 |
| **选中后预览框一片空白** | 1. 对照发布页的 `SHA256SUMS.txt`（或仓库根目录的 `CHECKSUMS.sha256`）检查 `spritesheet.webp` 是否下载完整；<br>2. 确认客户端版本已支持 `spriteVersionNumber: 2`。 |
| **切换宠物后浮窗还是旧角色** | 选中菲比后，先关闭再重新打开宠物浮窗；若渲染缓存仍未刷新，保存当前会话后重启一次 Codex 桌面端即可。 |
| **宠物一直停在某一张静帧不动** | 1. 检查系统辅助功能中是否开启了“减弱动态效果（Reduce Motion）”；<br>2. 注意菲比的眨眼周期为 6.6 秒，其中包含半闭眼与闭眼帧，降帧或暂停时可能刚好停在眨眼瞬间。 |
| **Dot 里转头时切到了错误的动作帧** | 请确认使用的是未经裁切的完整 **1536 × 2288**（8 列 × 11 行）整图且 `spriteVersionNumber` 为 `2`——最后两行（第 9、10 行）专门存放 16 个转头姿态。 |
| **运行 `install.py --local` 提示拒绝覆盖** | 这是脚本的防误删保护。请先把已有的 `pets/phoebe-chupi` 备份移出 `pets` 目录，再重新运行或按上文“更新已有安装”步骤仅替换 `spritesheet.webp`。 |
| **把图片放大几倍看觉得线条偏软或 GIF 有噪点** | 请优先按 **192 × 208 原生 1× 尺寸** 观察 WebP 或 PNG 原图；高倍截图插值与 GIF 的 256 色调色板抖动都会损失平滑度，实际运行使用的是 32 位无损 WebP。 |

如果以上步骤仍未解决你的显示问题，欢迎 [提交 Issue](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues)，并附上你的 Codex 客户端版本号、操作系统、安装方式以及问题截图。
