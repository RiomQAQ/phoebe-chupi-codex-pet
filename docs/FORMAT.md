# Native v2 package format / 新版宠物结构

[English README](../README.md) · [中文说明](../README.zh-CN.md)

## Portable runtime

The directory `pets/phoebe-chupi/` is the entire installable pet. Its `pet.json` is:

```json
{
  "id": "phoebe-chupi",
  "displayName": "Phoebe Chupi · Coding Companion",
  "description": "Phoebe Chupi, seated with her laptop. For Codex pets and Dot, with blinking, small hops, and a head that follows your cursor. 菲比啾比·坐好了（眨眼版）。",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```

`id` is a portable local identifier, not a cloud account's pet ID. `spritesheetPath` resolves within the pet directory. No plugin manifest, account binding, app database, signed media URL, or settings migration is required.

The native import URI accepts an HTTPS image URL and an explicit `spriteVersionNumber=2`; see the [official command reference](https://learn.chatgpt.com/docs/reference/commands). The installer reads `VERSION` and pins its public image URL to that release, currently `v1.0.1`. Update `VERSION` and publish the corresponding tag together.

## Grid

| Property | Value |
| --- | --- |
| Format | Static WebP with alpha, lossless encoding |
| Atlas | 1536 × 2288 px |
| Grid | 8 columns × 11 rows |
| Cell | 192 × 208 px |
| Standard rows | 0–8, 57 frames total |
| Direction rows | 9–10, 16 look poses |
| Used / unused | 73 / 15 |

Rows are zero-indexed. Standard counts are `[6, 8, 8, 4, 5, 8, 6, 6, 6]`. Fill cells left to right; unused cells must have alpha zero throughout. The sheet itself is not an animated WebP; the renderer selects cells.

For row `r` and column `c`, crop `(192*c, 208*r, 192*(c+1), 208*(r+1))`. [art/animation-layout.json](../art/animation-layout.json) records the complete layout and preview durations. [previews/contact-sheet.png](../previews/contact-sheet.png) shows all standard frames; [previews/directions.png](../previews/directions.png) shows all look poses.

## Look directions

In Codex Dot, these poses make the head follow the mouse. Angles are screen-space, clockwise from up. They describe the head/gaze direction while the seated body stays in place.

| Angle | Direction | Row / column |
| ---: | --- | --- |
| 000 | Up | 9 / 0 |
| 022.5 | Up-right | 9 / 1 |
| 045 | Up-right | 9 / 2 |
| 067.5 | Up-right | 9 / 3 |
| 090 | Right | 9 / 4 |
| 112.5 | Down-right | 9 / 5 |
| 135 | Down-right | 9 / 6 |
| 157.5 | Down-right | 9 / 7 |
| 180 | Down | 10 / 0 |
| 202.5 | Down-left | 10 / 1 |
| 225 | Down-left | 10 / 2 |
| 247.5 | Down-left | 10 / 3 |
| 270 | Left | 10 / 4 |
| 292.5 | Up-left | 10 / 5 |
| 315 | Up-left | 10 / 6 |
| 337.5 | Up-left | 10 / 7 |

The blue hair clip stays on the viewer's right; the tuft and blue cloth stay on the viewer's left. Do not mirror a pose to make the opposite direction. The body, laptop, and ground contact should remain visually registered while the head/eyes indicate direction.

## Timing

The runtime owns state selection and frame timing. Neither the manifest nor the preview layout file overrides it.

The locally reviewed desktop build `26.1007.71326` used idle durations `[1680, 660, 660, 840, 840, 1920]` ms, a 6.6 s cycle. These were six times the initial template preview's idle durations. This difference explains why an intermediate eye pose can be more noticeable in the app than in a fast preview. Other state durations and the illustrative 200 ms look-loop timing are listed in the layout JSON.

If the app changes its playback speed, update the preview timing and review the loops again.

## Assembly rules

1. Keep the original high-resolution image-tool outputs separate from normalized cells.
2. Use one shared character viewport and scale policy. Do not fit each frame's opaque bounding box independently; that turns small pose changes into body-size changes.
3. Preserve alpha and the original ink colors. Review on both light and dark backgrounds. Do not average neighboring fill colors into legitimate dark edge pixels. Native-alpha art that already passes the fringe check needs no chroma cleanup; see the [v1.0.1 repair](OUTLINE-REPAIR.md).
4. Register ground contact and the laptop anchor using measured, justified offsets; never silently flip a left/right frame.
5. Composite cells on a transparent 1536 × 2288 canvas. Leave the unused cells empty.
6. Encode once to lossless WebP and compare decoded RGBA against the accepted PNG.
7. Render previews **from the distributed WebP**, validate that file, and compare its public-download checksum after publishing.

## 中文要点

安装目录只需要 `pet.json` 和 `spritesheet.webp`。版本字段必须是 `spriteVersionNumber: 2`。这不是插件，也不需要复制账号设置或云端宠物编号。

整图为 1536 × 2288，每格 192 × 208，共 8 列 11 行。前 9 行是动作，最后 2 行是 16 个视线方向。不能删去末尾两行后仍称 v2，也不能把这张图当 v1 上传。

角度从屏幕正上方开始，顺时针增加。左、右都指观看者看到的屏幕方向。头和眼神可以动，身体和电脑保持稳定；发夹、呆毛和蓝布不能镜像换边。

所有帧共用缩放基准。逐格按不透明边界自动撑满，会让角色忽大忽小。先审查动作与比例，再排版、编码、比对 PNG/WebP 像素，最后检查实际下载的文件。播放速度由应用控制，预览 GIF 的时长不会写进宠物配置。
