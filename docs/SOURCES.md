# Sources & Reference Lineage

**English** · [简体中文](SOURCES.zh-CN.md) · [Documentation](README.md)

The Phoebe Chupi Codex pet is built on a clear, traceable lineage that combines **official *Wuthering Waves* character design**, **community chibi turnaround sheets**, **observed motion and expression studies**, and the **native Codex Desktop v2 sprite atlas specification**.

This page documents what each external reference contributed to the project. Listing a source here credits its role in our research and does not grant reuse rights over third-party material; see [Artwork Usage](../ASSET-USAGE.md) for the exact scope of repository files.

---

## Reference-to-Sprite Lineage Map

```text
+-----------------------------------------------------------------------------+
|  [A] Official Character Design (Kuro Games — Wuthering Waves)               |
|      └─> Locks palette, outfit layers, dark-purple hat band,                |
|          viewer-right blue hair clip, and viewer-left ahoge tuft            |
|                                                                             |
|  [B] Community Chibi Turnaround (蓝蓝铜离子 BV1zzAAzPEVA, etc.)             |
|      └─> Locks compact 2-head chibi silhouette, layered purple eyes,        |
|          and broad white hat -> generates Seated & Carry Master Anchors     |
|                                                                             |
|  [C] Motion & Expression Studies (hop timing, late-night desk poses, etc.)  |
|      └─> Informs 9 standard rows (57 frames) + 16 Dot looks + 4 samples     |
|                                                                             |
|  [D] Codex Desktop v2 Specification & Open-Source Pet Precedents            |
|      └─> Packaged as 1536 × 2288 (8×11, 73 used cells) WebP + pet.json      |
+-----------------------------------------------------------------------------+
```

---

## Character and visual references

<p align="center">
  <img src="../art/canonical/user-reference.png" width="680" alt="Community three-view reference sheet with original attribution preserved" />
</p>

| Source | Role in This Project |
| --- | --- |
| Kuro Games: [Phoebe post](https://wutheringwaves.kurogames.com/en/main/news/detail/2106) and [related post](https://wutheringwaves.kurogames.com/en/main/news/detail/2101) | Verifies official character identity, color palette, cleric outfit layering, and the exact placement of signature accessories (hat band, hair clip, cuffs, and leg stripes). |
| 蓝蓝铜离子: [BV1zzAAzPEVA](https://www.bilibili.com/video/BV1zzAAzPEVA/) | Primary community front/profile/back turnaround reference, marked as Doubao AI-generated. Both the full image and the three orthographic crops in `art/canonical/` retain their visible attribution marks. |
| Community collection: [BV1zUJdzdEYF](https://www.bilibili.com/video/BV1zUJdzdEYF/) | Cross-checks the shared community style and attribution trail for the "Phoebe Chupi" chibi persona. |
| Arca: [pack 42655](https://arca.live/e/42655), [pack 47956](https://arca.live/e/47956), [Binci profile](https://arca.live/u/@Binci) | Community-author leads. Site access restrictions prevented direct authorship verification, so these are recorded strictly as research leads. |
| DCCon: [Phoebe pack 165313](https://dccon.dcinside.com/hot/1/title/%ED%8E%98%EB%B9%84#165313), publisher **Binci1** | Sticker expressions and community chibi visual vocabulary. |

> **Attribution Note**: The community reference defines this pet's compact chibi silhouette and is distinct from official Kuro Games character art. Because the connection between the `Binci` and `Binci1` handles is unverified, the repository does not identify them as the same author.

---

## Motion and expression studies

To make Phoebe feel alive beside an active code editor rather than ticking like a metronome, we studied micro-expressions and timing cues across several community posts and re-illustrated them from scratch around our canonical laptop poses (**video frames and bulk sticker downloads are not distributed in this repository**):

<p align="center">
  <img src="../art/samples/samples-overview.png" width="720" alt="Overview of the four core state sample illustrations" />
</p>

| Post | Study & Observed Cue | Resulting Project Asset |
| --- | --- | --- |
| [BV1W2ARznELg](https://www.bilibili.com/video/BV1W2ARznELg/) | Gentle disappointment and recovery for the help state | `failed` (Needs help · 8 frames) loop & `03-help.png` sample |
| Sans_AI: [BV1zn9YBxEVJ](https://www.bilibili.com/video/BV1zn9YBxEVJ/) | Small-hop timing around `17.5–19.75 s` | `jumping` (Small hop · 5 frames) takeoff, apex, and landing curve |
| 喵内特洛夫斯基: [BV1TYMB6CE7U](https://www.bilibili.com/video/BV1TYMB6CE7U/) | Seated desk and chin-rest expressions for later samples | `02-thinking.png` sample & seated expression studies |
| [BV1zycfznE2E](https://www.bilibili.com/video/BV1zycfznE2E/) | Waiting and welcome-home expression studies | `waiting` (6 frames) & `01-waiting.png` / `04-happy.png` samples |
| [BV1HQ8g6VEo7](https://www.bilibili.com/video/BV1HQ8g6VEo7/) | Sleepy workday expressions for later samples | `idle` blink cadence & workday expression studies |
| 虾饺shrimp: [BV1BPaT6vEqk](https://www.bilibili.com/video/BV1BPaT6vEqk/) | Late-night expressions around `21 s` and `26 s` | Exploratory expression studies and candidate frames |

> **Methodological Rule**: A still-frame study records only the observed expression in that still, not an inferred full animation.

---

## 4. Format and Package Examples

| Reference | Use |
| --- | --- |
| [Official import commands](https://learn.chatgpt.com/docs/reference/commands#pets) | Native pet-import URI and v2 parameter specification. |
| [Official Pets guide](https://learn.chatgpt.com/docs/pets) | App controls and import guidance. |
| [phoebe-codex-pet](https://github.com/sherlidian01-web/phoebe-codex-pet) | Bilingual presentation and animation preview layout. |
| [remielle-codex-pet](https://github.com/HanaAyane/remielle-codex-pet) | Installation structure and portable five-field v2 `pet.json` manifest example. |
| [awesome-codex-pet](https://github.com/legeling/awesome-codex-pet) | Gallery navigation and source attribution conventions. |

---

## 5. Archived Material & Version Provenance

To keep every artistic and technical decision auditable, the repository organizes its assets and verification records into four layers:

1. **Complete Source Archive (832 distinct source images / 1,447 working-file occurrences)**
   - The [Image Archive](IMAGE-GALLERY.md) preserves **832 distinct SHA-256 source images**, with **1,447 working-file occurrences** mapped in [`art/index.json`](../art/index.json). It includes generated frames, pose studies, comparisons, unused candidates, and the attributed three-view reference. Current 73 frame crops and repair evidence are stored alongside them.
2. **v1.0.2 Dot Look Redraw & Six-Pose Face Refinement**
   - For `v1.0.2`, **12 look drawings** were redrawn as complete frames with the built-in image generation tools, while four original drawings were reused (`022.5`, `045`, `067.5`, and `090`). The revisions preserve the hat design and use no pasted faces or local face warps.
   - The latest six face refinements cover `000`, `157.5`, `247.5`, `292.5`, `315`, and `337.5`; they address pinched cheeks and apparent face growth during the return from an upward-left look.
3. **Reviewed Runtime Baseline & Historical Protection**
   - The current reviewed baseline is [`art/approved/v1.0.2/spritesheet.png`](../art/approved/v1.0.2/spritesheet.png), recorded in [`art/approved-runtime.json`](../art/approved-runtime.json).
   - The first nine rows (all 57 standard animation frames) retain the exact `v1.0.1` RGBA pixels. That release is preserved in [`art/releases/v1.0.1`](../art/releases/v1.0.1) with its original [outline-repair evidence](repair-qa/README.md), while the new [look repair evidence](look-repair-qa/README.md) documents `v1.0.2`.
4. **External Reference Boundary**
   - Third-party research collections remain linked at their original sources. The repository contains only the production artwork and reproducible technical records needed to inspect the pet.
