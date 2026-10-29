# Documentation Index

**English** · [简体中文](README.zh-CN.md) · [Project Home](../README.md)

Welcome to the complete documentation for **Phoebe Chupi v1.0.2**. Here you will find installation and upgrade instructions, the v2 sprite-sheet specification, an illustrated frame-by-frame production guide, reusable prompt templates, and full QA evidence for every release.

![Five core states at native 192 × 208 pixel scale](../previews/stills/five-states.png)

---

## Reading Roadmap: Where Should You Start?

```text
What would you like to do?
 │
 ├─► [Install or update Phoebe Chupi in Codex]
 │     └─► 1. Install & Update (INSTALL.md) ──► 2. Troubleshooting FAQ (INSTALL.md#troubleshooting)
 │
 ├─► [Build your own custom Codex v2 pet]
 │     └─► 1. Making a Pet (MAKING-OF.md)
 │         2. Prompt Examples (PROMPTS.md)
 │         3. Sprite Format Spec (FORMAT.md)
 │         4. Review & Validation (REVIEW.md)
 │
 └─► [Inspect source artwork, repair history, or attribution]
       └─► 1. 832-Image Archive (IMAGE-GALLERY.md)
           2. v1.0.2 Look Repair Evidence (look-repair-qa/README.md)
           3. v1.0.1 Outline Repair (OUTLINE-REPAIR.md & repair-qa/README.md)
           4. Sources & Credits (SOURCES.md / NOTICE.md / ASSET-USAGE.md)
```

---

## 1. Using & Browsing the Pet

| Guide | What It Covers |
| --- | --- |
| **[Install and Update](INSTALL.md)** | Manual installation into your `pets` folder, one-line CLI copy (`scripts/install.py --local`), native URI import, in-place updates that preserve your pet identity, and 7 common troubleshooting scenarios. |
| **[Image Archive](IMAGE-GALLERY.md)** | Browse **832 distinct source images** (mapping **1,447 working-file occurrences**) across 7 production stages, alongside the distributed atlas, all 73 frame crops, and light/dark animations. |
| **[Credits](../NOTICE.md)** · **[Artwork Usage](../ASSET-USAGE.md)** | Character attribution, community turnaround credit, AI generation disclosure, and non-commercial usage and sharing terms. |

---

## 2. Production Workflow, Technical Spec & Quality Assurance

Start with **[Making a Pet](MAKING-OF.md)** for the end-to-end story, then jump into the specialized references as needed:

| Document | Stage | Key Topics |
| --- | --- | --- |
| **[Making a Pet](MAKING-OF.md)** | End-to-end workflow | Illustrated walkthrough from reference breakdown, front/profile/back cutouts, and seated/carry master anchors to 9 action rows, 16 Dot head turns, shared-viewport normalization, and release packaging. |
| **[Prompt Examples](PROMPTS.md)** | Generation & editing | 7 ready-to-use prompt templates (character anchors, single-frame edits, targeted defect repairs, Dot look poses, face-scale smoothing, full-loop review, and unlabeled A/B blind checks) with visual examples. |
| **[Sprite Format](FORMAT.md)** | Assembly & export | Detailed `pet.json` 5-field manifest spec, visual **8 × 11 grid map** (`1536 × 2288` px), `192 × 208` cell math, **16-direction compass diagram**, playback timing, and lossless WebP export rules. |
| **[Review and Validation](REVIEW.md)** | QA & release gate | 8-point single-frame inspection table, full-motion continuity checks, 3-reviewer blind A/B direction testing protocol, v1.0.2 metrics, known limitations, and automated Python checks. |
| **[Sources](SOURCES.md)** | Lore & references | Breakdown of official *Wuthering Waves* Phoebe references, the community three-view turnaround by 蓝蓝铜离子, 6 Bilibili motion/expression studies, and open-source packaging examples. |
| **[v1.0.2 Look Repair Evidence](look-repair-qa/README.md)** | v1.0.2 QA dossier | Illustrated before/after comparison boards for the 12 redrawn head turns, upper-left return zoom boards, 3-reviewer blind A/B logs, and native 1× browser stepping evidence. |
| **[Hair-Outline Repair](OUTLINE-REPAIR.md)** | v1.0.1 QA dossier | How a v1.0.0 edge-cleanup rule caused pale patches in the hair outline, nearest-neighbor RGB pixel comparisons, 3 regression coordinate tests, and reproduction commands. |
| **[v1.0.1 Review Evidence](repair-qa/README.md)** | v1.0.1 historical logs | Preserved geometry, chroma-preservation, 73-frame visual review, and first-round blind direction reports for the restored v1.0.1 atlas. |

---

## 3. Repository Architecture & File Map

```text
phoebe-chupi-codex-pet/
├── pets/phoebe-chupi/           # [Distributable Package] Copy directly into ~/.codex/pets/
│   ├── pet.json                 #   ├─ Portable 5-field v2 manifest
│   └── spritesheet.webp         #   └─ 1536 × 2288 lossless transparent WebP sprite atlas
│
├── art/                         # [Source Artwork & Baselines]
│   ├── canonical/               #   ├─ Community turnaround, cutouts, standing identity, seated/carry masters & cardinals
│   ├── approved/v1.0.2/         #   ├─ Reviewed and locked v1.0.2 PNG pixel baseline
│   ├── approved-runtime.json    #   ├─ Guard file locking release SHA-256 and frozen rows 0–8 against v1.0.1
│   ├── final/spritesheet.png    #   ├─ PNG atlas with decoded RGBA pixels identical to the distributed WebP
│   ├── frames/                  #   ├─ All 73 exact 192 × 208 cell crops from the current atlas (9 states + look)
│   ├── samples/                 #   ├─ 4 character expression samples and native-size comparison board
│   ├── archive/                 #   ├─ 832 deduplicated production images across 7 stages
│   ├── index.json               #   ├─ Manifest mapping 832 unique images to 1,447 working-file occurrences
│   ├── repair/                  #   ├─ v1.0.1 outline and v1.0.2 look repair sources, review boards & HTML viewer
│   └── releases/                #   └─ Historical v1.0.0 and v1.0.1 atlas snapshots kept for regression tests
│
├── previews/                    # [Animated Previews & Contact Sheets]
│   ├── *.gif / dark/*.gif       #   ├─ Light and dark background GIF loops, 16-look loop & idle-hop-idle join
│   ├── contact-sheet*.png       #   ├─ Light and dark full-frame contact sheets for all 9 standard rows
│   ├── directions.png           #   ├─ Labeled 16-direction overview sheet for Dot gaze poses
│   └── stills/                  #   └─ Unscaled 192 × 208 native 1:1 pixel stills
│
├── scripts/                     # [Automation & Verification Scripts]
│   ├── validate.py              #   ├─ Validates manifest, pixel equality, margins, archive hashes, EXIF & privacy
│   ├── audit_artwork.py         #   ├─ Verifies v1.0.2 approved baseline and zero pixel drift on rows 0–8
│   ├── restore_outlines.py      #   ├─ Reproduces and audits the v1.0.1 hair-outline color restoration
│   ├── render_previews.py       #   ├─ Regenerates all GIFs, contact sheets, and stills from the release WebP
│   ├── install.py               #   └─ Copies package locally or launches the official native import URI
│   └── package.py               #   └─ Builds release ZIP archives and SHA256SUMS.txt in dist/
│
├── tests/                       # [Regression Test Suite]
│   ├── test_approved_artwork.py #   ├─ Tests runtime pixel lock, frozen standard rows, and source-map integrity
│   └── test_outline_regression.py # └─ Tests detection of damaged v1.0.0 pixels and v1.0.1 outline recovery
│
└── docs/                        # [Bilingual Documentation & QA Reports]
    ├── *.md / *.zh-CN.md        #   ├─ Paired English (.md) and Chinese (.zh-CN.md) guides
    ├── gallery/                 #   ├─ 22 stage-by-stage archive gallery pages with bilingual captions
    ├── look-repair-qa/          #   ├─ v1.0.2 head-turn metrics, blind review logs, and readback verification
    └── repair-qa/               #   └─ v1.0.1 outline-repair metrics, chroma checks, and blind review logs
```

### Baseline Summary

- **Current release**: `v1.0.2` (updates 12 head-turn drawings in rows 9–10 while keeping all 57 standard animation frames in rows 0–8 pixel-identical to `v1.0.1`).
- **Reviewed pixel baseline**: [art/approved/v1.0.2/spritesheet.png](../art/approved/v1.0.2/spritesheet.png), locked alongside the frozen v1.0.1 row reference in [art/approved-runtime.json](../art/approved-runtime.json).
- **Historical snapshots**: Previous releases remain preserved in [art/releases/v1.0.1](../art/releases/v1.0.1) and [art/releases/v1.0.0](../art/releases/v1.0.0).
- **Language convention**: English guides use `.md` and Chinese editions use `.zh-CN.md`. [Gallery pages](gallery/early-concept-01.md), [Credits](../NOTICE.md), and [Artwork Usage](../ASSET-USAGE.md) present both languages side by side.
