# Image Archive Overview (832 Source Images / 1,447 Working-File Occurrences)

**English** · [简体中文](IMAGE-GALLERY.zh-CN.md) · [Documentation](README.md)

To document every step of Phoebe Chupi's creation from early concept sketches to the final `v1.0.2` sprite atlas, this archive preserves **832 distinct SHA-256 source images** representing **1,447 working-file occurrences** across the production pipeline.

Byte-identical files share a single stored image, while [`art/index.json`](../art/index.json) maps every image ID (`image-0001` through `image-0832`), SHA-256 checksum, production stage, and original working path. You can also [download all images and current guides](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/archive/refs/heads/main.zip) to browse the entire repository offline.

---

## 1. Archive Architecture Map

```text
+-----------------------------------------------------------------------------+
|  [Layer 1: Production Source Archive · 832 Unique Images / 22 Gallery Pages] |
|   ├─ 1. Early concepts (6 images)          ──► Initial style & close-ups    |
|   ├─ 2. Standing studies (37 images)       ──► Turnaround & standing masters|
|   ├─ 3. Seated production (489 images)     ──► 9 state loops & prop repairs |
|   ├─ 4. Unused open-eye study (192 images) ──► Early non-blinking pass      |
|   ├─ 5. Character samples (14 images)      ──► High-res state illustrations |
|   ├─ 6. Generation originals (4 images)    ──► Raw 1254×1254 master outputs |
|   └─ 7. Look & face studies (99 images)    ──► v1.0.2 16-angle look redraws |
|                                                                             |
|  [Layer 2: Current Distributed Artwork & Derived Previews]                  |
|   └─ pets/phoebe-chupi/spritesheet.webp + art/frames/ (73 cells) + previews/|
|                                                                             |
|  [Layer 3: Release Snapshots & QA Repair Evidence]                          |
|   └─ art/approved/v1.0.2/ + art/releases/v1.0.0..v1.0.1 + art/repair/       |
+-----------------------------------------------------------------------------+
```

---

## 2. Production Stage Galleries (22 Pages)

Each gallery page provides a **contact-sheet banner**, **150px lazy-loaded thumbnails**, **clickable full-resolution originals**, and **bilingual English/Chinese captions** derived from the original production paths (note: because canonical anchors were reused across multiple stages, some source images appear in more than one stage gallery):

<table>
  <tr>
    <td align="center" width="33%">
      <a href="gallery/early-concept-01.md"><img src="../previews/archive/early-concept-01.jpg" width="240" alt="Early concepts contact sheet" /></a><br />
      <sub><b>1. Early Concepts (6)</b><br /><a href="gallery/early-concept-01.md">Open Gallery</a></sub>
    </td>
    <td align="center" width="33%">
      <a href="gallery/standing-study-01.md"><img src="../previews/archive/standing-study-01.jpg" width="240" alt="Standing studies contact sheet" /></a><br />
      <sub><b>2. Standing Studies (37)</b><br /><a href="gallery/standing-study-01.md">Open Gallery</a></sub>
    </td>
    <td align="center" width="33%">
      <a href="gallery/seated-production-01.md"><img src="../previews/archive/seated-production-01.jpg" width="240" alt="Seated production contact sheet" /></a><br />
      <sub><b>3. Seated Production (489 · 11 Pages)</b><br /><a href="gallery/seated-production-01.md">Open Part 1</a></sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="gallery/awake-experiment-01.md"><img src="../previews/archive/awake-experiment-01.jpg" width="240" alt="Unused open-eye study contact sheet" /></a><br />
      <sub><b>4. Unused Open-Eye Study (192 · 4 Pages)</b><br /><a href="gallery/awake-experiment-01.md">Open Part 1</a></sub>
    </td>
    <td align="center" width="33%">
      <a href="gallery/character-samples-01.md"><img src="../previews/archive/character-samples-01.jpg" width="240" alt="Character samples contact sheet" /></a><br />
      <sub><b>5. Character Samples (14)</b><br /><a href="gallery/character-samples-01.md">Open Gallery</a></sub>
    </td>
    <td align="center" width="33%">
      <a href="gallery/generation-originals-01.md"><img src="../previews/archive/generation-originals-01.jpg" width="240" alt="Additional generation originals contact sheet" /></a><br />
      <sub><b>6. Additional Generation Originals (4)</b><br /><a href="gallery/generation-originals-01.md">Open Gallery</a></sub>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="3">
      <a href="gallery/look-face-repair-01.md"><img src="../art/repair/v1.0.2/review-boards/before-after-cardinals.png" width="480" alt="Look and face studies preview" /></a><br />
      <sub><b>7. Look & Face Studies (99 · 3 Pages)</b><br /><a href="gallery/look-face-repair-01.md">Part 1</a> · <a href="gallery/look-face-repair-02.md">Part 2</a> · <a href="gallery/look-face-repair-03.md">Part 3</a></sub>
    </td>
  </tr>
</table>

| Stage | Images | Scope & Highlights | Gallery Pages |
| --- | ---: | --- | --- |
| **1. Early concepts** | 6 | Initial character master explorations, close-ups, and raw generation tests. | [Open](gallery/early-concept-01.md) |
| **2. Standing studies** | 37 | Community turnaround reference, orthographic front/profile/back crops, standing identity masters, and proportion studies. | [Open](gallery/standing-study-01.md) |
| **3. Seated production** | 489 | Seated and carry masters, plus raw generations, local hand/laptop repairs, and normalized cell frames across all 9 standard rows and early 16-angle looks. | [Part 1](gallery/seated-production-01.md) · [Part 2](gallery/seated-production-02.md) · [Part 3](gallery/seated-production-03.md) · [Part 4](gallery/seated-production-04.md) · [Part 5](gallery/seated-production-05.md) · [Part 6](gallery/seated-production-06.md) · [Part 7](gallery/seated-production-07.md) · [Part 8](gallery/seated-production-08.md) · [Part 9](gallery/seated-production-09.md) · [Part 10](gallery/seated-production-10.md) · [Part 11](gallery/seated-production-11.md) |
| **4. Unused open-eye study** | 192 | Complete set of non-blinking ("always awake") state candidates and sliced cells explored before adopting the final blinking idle cycle. | [Part 1](gallery/awake-experiment-01.md) · [Part 2](gallery/awake-experiment-02.md) · [Part 3](gallery/awake-experiment-03.md) · [Part 4](gallery/awake-experiment-04.md) |
| **5. Character samples** | 14 | High-resolution standalone illustrations and candidate passes for waiting, thinking, help, and happy expressions. | [Open](gallery/character-samples-01.md) |
| **6. Additional generation originals** | 4 | Uncropped `1254 × 1254` raw generator outputs for key master poses and samples. | [Open](gallery/generation-originals-01.md) |
| **7. Look and face studies** | 99 | `v1.0.2` Dot 16-angle head-turn redraws, rejected candidates (such as scale jumps or narrow-cheek drafts), and the final six-pose face refinements. | [Part 1](gallery/look-face-repair-01.md) · [Part 2](gallery/look-face-repair-02.md) · [Part 3](gallery/look-face-repair-03.md) |

> **Scope & Attribution Note**: Archive images document the full iterative production process; they do not all belong to the installed animation. The attributed community turnaround (`image-0011`) and its three orthographic crops (`image-0012` through `image-0014`) are third-party references subject to the [artwork terms](../ASSET-USAGE.md#third-party-references).

---

## 3. Current Artwork and Previews

To inspect or use the final `v1.0.2` production assets directly:

| Material | Entry Point | Notes |
| --- | --- | --- |
| **Canonical seated and carry poses** | [Character anchors (`art/canonical/`)](../art/canonical) | Orthographic reference crops, standing identity, seated master, carry master, and cardinal look anchor. |
| **Distributed atlas (`1536 × 2288`)** | [Lossless WebP](../pets/phoebe-chupi/spritesheet.webp) · [Accepted PNG](../art/final/spritesheet.png) | Identical decoded RGBA pixels across 73 occupied cells and 15 transparent cells. |
| **All 73 current cells** | [Exact frame crops (`art/frames/`)](../art/frames) | Lossless `192 × 208` individual cell crops (57 standard frames + 16 `look/` frames). |
| **Animation and head directions** | [Light state sheet](../previews/contact-sheet.png) · [Dark state sheet](../previews/contact-sheet-dark.png) · [Direction sheet](../previews/directions.png) | Full contact sheets for the 9 standard state rows and 16 clockwise look angles. |
| **Light and dark playback** | [All states GIF](../previews/all-states.gif) · [Hop transition GIF](../previews/idle-jump-idle.gif) · [Dark loops (`previews/dark/`)](../previews/dark) | Animated GIF previews rendered on light and dark backgrounds. |
| **Native-size stills** | [Five states (`five-states.png`)](../previews/stills/five-states.png) | Unscaled `192 × 208` (`1×`) native-resolution still comparison. |

---

## 4. Repair and Release History

- **v1.0.2 look redraw & face refinement records**: Archived in [`art/approved/v1.0.2/`](../art/approved/v1.0.2), [`art/repair/v1.0.2/`](../art/repair/v1.0.2), and [look repair evidence](look-repair-qa/README.md). Its 90 new source drawings are indexed in Stage 7 above (expanding the earlier 742-image archive to **832 unique source images**).
- **v1.0.1 outline-repair records**: Adds [pre-cleanup source pixels](../art/repair/v1.0.1/source-before-cleanup.png), [nearest-neighbor before/after details](../art/repair/v1.0.1/before-after.png), and [11 light/dark row review boards](../art/repair/v1.0.1/review-boards) alongside the 742-image v1.0.1 source archive.
- **Historical release snapshots**: [`art/releases/v1.0.0`](../art/releases/v1.0.0) and [`art/releases/v1.0.1`](../art/releases/v1.0.1) preserve the earlier atlases and crops; see the [outline repair guide](OUTLINE-REPAIR.md) and [review guide](REVIEW.md) for their exact relationship to the current release.
