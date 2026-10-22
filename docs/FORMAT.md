# Sprite format

**English** · [简体中文](FORMAT.zh-CN.md) · [Documentation](README.md)

The pet uses a static, transparent v2 atlas. The app animates it by selecting cells; the WebP itself is not an animated image.

## Package

```text
phoebe-chupi/
├── pet.json
└── spritesheet.webp
```

The portable manifest contains five fields:

```json
{
  "id": "phoebe-chupi",
  "displayName": "Phoebe Chupi · Coding Companion",
  "description": "Phoebe Chupi, seated with her laptop. For Codex pets and Dot, with blinking, small hops, and a head that follows your cursor. 菲比啾比·坐好了（眨眼版）。",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```

`id` identifies the local package. `spritesheetPath` is relative to the manifest. Account identifiers and application settings are not part of the package. The native import helper reads the release tag from `VERSION`; its URI parameters are described in [Install](INSTALL.md#use-native-import).

## Grid

| Property | Value |
| --- | --- |
| Image | Lossless WebP with alpha |
| Atlas | 1536 × 2288 px |
| Grid | 8 columns × 11 rows |
| Cell | 192 × 208 px |
| Used cells | 73: 57 animation frames + 16 look poses |
| Empty cells | 15, fully transparent |

Rows and columns are zero-indexed. Crop cell `(r, c)` with `(192c, 208r, 192(c+1), 208(r+1))`. Fill each row from the left. [animation-layout.json](../art/animation-layout.json) records the layout and preview durations.

## Animation states

| Row | State | Frames | Behavior |
| ---: | --- | ---: | --- |
| 0 | `idle` | 6 | Seated breathing and blinking. |
| 1 | `running-right` | 8 | Carrying the closed laptop right. |
| 2 | `running-left` | 8 | Carrying the closed laptop left. |
| 3 | `waving` | 4 | A one-handed seated greeting. |
| 4 | `jumping` | 5 | A short seated hop and landing. |
| 5 | `failed` | 8 | Asking for help, then recovering. |
| 6 | `waiting` | 6 | Looking up for a reply. |
| 7 | `running` | 6 | Working at the laptop. |
| 8 | `review` | 6 | Checking the result. |

`running` means task activity; left/right locomotion has separate rows. The [contact sheet](../previews/contact-sheet.png) shows every standard frame.

## Look directions

In Dot, these poses turn the head toward the cursor while the body and laptop remain seated. Angles use screen coordinates, increasing clockwise from up in 22.5° steps.

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

The blue hair clip stays on viewer-right; the tuft and blue cloth stay on viewer-left. Opposite directions are drawn separately to preserve these features. See the [direction sheet](../previews/directions.png).

## Timing

The app controls state selection and playback. `pet.json` and the layout file do not override its scheduler.

The preview uses idle durations `[1680, 660, 660, 840, 840, 1920]` ms, a 6.6-second cycle observed in desktop build `26.1007.71326`. Each look pose is shown for 200 ms in the direction GIF. That loop demonstrates the available poses; Dot chooses them from cursor position.

## Export rules

- Apply one shared viewport and scale policy. Fitting each frame to its own opaque bounds changes the character's apparent size.
- Preserve the approved RGBA colors and alpha. Clean native-alpha artwork needs no neighbor-color averaging.
- Register the body, laptop, and ground contact before assembly. Keep visible artwork inside each cell with a margin.
- Leave unused cells completely transparent. Preserve both look rows.
- Encode losslessly, compare decoded pixels with the PNG, and derive previews and frame crops from the distributed WebP.

The [review guide](REVIEW.md) defines the checks. The [outline repair](OUTLINE-REPAIR.md) explains why export color fidelity is checked separately from PNG/WebP equality.
