# Making a Pet: From Reference Turnaround to v2 Sprite Atlas

**English** · [简体中文](MAKING-OF.zh-CN.md) · [Documentation Index](README.md)

This guide walks through the complete production of **Phoebe Chupi**—starting from a single community three-view turnaround, establishing locked pose anchors, animating 9 everyday coding states, solving perspective jumps across 16 Dot head turns, and assembling the final **1536 × 2288** lossless v2 sprite sheet.

The artwork was created frame by frame with **GPT-6-Astra** and the built-in image generation tools and normalized through a shared camera viewport during atlas assembly, while the checked-in Python scripts handle preview rendering, pixel-level regression checks, and release packaging. You can follow this exact workflow to build your own custom Codex pet.

---

## End-to-End Production Pipeline

```text
Stage 1: Reference Breakdown   Stage 2: Master Pose Anchors     Stage 3: 73 Action & Look Frames
┌──────────────────────────┐   ┌────────────────────────────┐   ┌────────────────────────────────┐
│ Community Turnaround     │──►│ Standing Identity Sheet    │──►│ Rows 0–8: 57 Standard Frames   │
│ Front / Side / Back Cuts │   │ Seated Master (Open Mac)   │   │ Rows 9–10: Cardinals → 16 Looks│
└──────────────────────────┘   │ Carry Master (Closed Mac)  │   └────────────────┬───────────────┘
                               └────────────────────────────┘                    │
                                                                                 ▼
Stage 6: Validation & Release  Stage 5: Blind & 1× Visual QA    Stage 4: Shared-Viewport Assembly
┌──────────────────────────┐   ┌────────────────────────────┐   ┌────────────────────────────────┐
│ validate.py Pixel Guards │◄──│ Native 1× Light/Dark Check │◄──│ Normalize into 192 × 208 Cells │
│ Unittests + ZIP Packaging│   │ 3-Reviewer Blind A/B Tests │   │ Preserve Native Alpha → 8×11   │
└──────────────────────────┘   └────────────────────────────┘   └────────────────────────────────┘
```

---

## 1. Establish the Reference & Perspective Cutouts

Before drawing a single animation frame, lock down the character's 3D silhouette from **front, profile, and back** views:

- **Official character lore**: Kuro Games' official *Wuthering Waves* Phoebe references establish her pale-blonde hair, wide white hat with a dark-purple ribbon, layered purple eyes, white outfit, dark gloves, and striped socks.
- **Chibi proportion reference**: The primary two-head-tall chibi proportions follow the community three-view turnaround attributed to **蓝蓝铜离子** (see [Sources](SOURCES.md) for full provenance).

![Community three-view reference](../art/canonical/user-reference.png)

So the image generation tools can focus on one clean angle at a time without cross-view confusion, the turnaround is split into three isolated cutouts:

| Front Silhouette Cutout | Left Profile Cutout | Back Hair & Ribbon Cutout |
| :---: | :---: | :---: |
| ![Front reference cutout](../art/canonical/reference-front-cutout.png) | ![Profile reference cutout](../art/canonical/reference-left-profile-cutout.png) | ![Back reference cutout](../art/canonical/reference-back-cutout.png) |
| Locks the rounded cheeks, brow spacing, hat brim width, and gold chest trim. | Locks the forward brim projection, short chin, and high-waisted skirt flare. | Locks the dark-purple back bow and the layered flow of her long blonde hair. |

---

## 2. Build the Standing Identity & Two Master Pose Anchors

Generating dozens of animation frames directly from a turnaround often causes laptop geometry or seated posture to drift between states. To prevent that, we first establish a **standing identity sheet** and then derive **two master pose anchors** that every animation row locks onto:

| 1. Standing Identity Sheet | 2. Seated Master Anchor (Open Laptop) | 3. Carry Master Anchor (Closed Laptop) |
| :---: | :---: | :---: |
| ![Standing identity](../art/canonical/standing-identity.png) | ![Seated master anchor](../art/canonical/seated-master-approved.png) | ![Carry master anchor](../art/canonical/carry-master-approved.png) |
| Translates the turnaround into clean dark outer contours and warm gold-brown inner hair lines. | Anchors `idle`, `waving`, `jumping`, `failed`, `waiting`, `running`, `review`, and all 16 `look` poses. | Anchors the `running-right` and `running-left` locomotion loops with the laptop closed in her arms. |

Every frame across the project must preserve these six visual invariants against the master anchors:

| Feature | Locked Visual Rule |
| --- | --- |
| **Silhouette** | Broad white hat brim, dark-purple ribbon band, long pale-blonde hair, and compact chibi body. |
| **Facial proportions** | Small rounded cheeks, layered purple eyes, steady brow spacing, and a short chin. |
| **Asymmetric accessories** | **Blue cross hair clip always stays on viewer-right**; **ahoge tuft and blue cloth always stay on viewer-left** (never horizontally mirrored). |
| **Outfit** | White dress, dark gloves, gold accents, striped legs, and dark rounded shoes. |
| **Laptop prop** | Blue-gray body; when open, strictly **one lid, one hinge, and one keyboard deck** with natural hand placement. |
| **Line work & shading** | Continuous dark outer contours, warm gold-brown internal hair strands, and restrained flat cel shading. |

---

## 3. Plan the Nine Action Rows & Expression Studies

Starting from Codex's [nine standard state rows](FORMAT.md#animation-states), we choreographed a cohesive daily routine around her laptop: breathing and blinking beside you (`idle`), waving hello (`waving`), typing focused code (`running`), pausing for your reply (`waiting`), leaning in to inspect output (`review`), looking up for help when a command fails (`failed`), hopping with joy (`jumping`), and trotting left or right with her closed laptop (`running-left` / `running-right`).

Before producing full frame sequences, expression studies tested how clearly each mood reads:

![Character mood and expression studies overview](../art/samples/samples-overview.png)

- **Shared seated baseline**: Every seated state shares the exact same torso, foot, and laptop coordinates so switching between `idle`, `jumping`, `waiting`, and `running` never causes a position pop.
- **Blink design**: The shipped `idle` loop uses a natural **half-closed → closed → open** blink sequence. An alternative 192-frame "always-open-eye" study was also produced and is preserved in the [Image Archive · Unused Open-Eye Study](gallery/awake-experiment-01.md).

---

## 4. Generate and Refine One Frame at a Time

When generating animation sequences, **always generate or edit one isolated frame at a time** rather than asking an image model for a multi-cell grid (which almost always introduces grid drift and proportion changes):

1. **Attach dual references**: Supply both the **master pose anchor** (to lock identity and scale) and an **adjacent accepted frame** (used strictly to judge motion step size).
2. **Specify one targeted change**: Name the state, frame index, and exact hand/head/expression change while explicitly locking the camera, body, feet, and laptop (see [Prompt Examples](PROMPTS.md)).
3. **Inspect at both full resolution and native 1× size**: Check fine line connections zoomed in, then verify readability at the actual **192 × 208** cell size.
4. **Quarantine rejected candidates**: Store rejected attempts separately so a distorted frame never becomes the reference for the next step.

Across 832 source images, six recurring AI sprite defects required targeted fixes:

| Common Defect | Why It Happens | Targeted Fix |
| --- | --- | --- |
| **Extra glove, arm, or sleeve** | During typing or waving edits, the model may leave the previous hand behind while drawing a new one. | Point out the duplicate hand explicitly and restore a single arm-to-sleeve connection against the master anchor. |
| **Duplicate brow or stray facial line** | Half-closed blink or head-tilt transitions can leave ghost upper-lid lines. | Attach the seated master face and restore clean single brows and layered purple eyes. |
| **Double laptop lid or keyboard** | Upward hops or pitched camera angles can trigger a second lid plane. | Enforce "one blue-gray laptop with a single lid, single hinge, and single keyboard deck." |
| **Head, hat, or chin changes size** | When turning from profile back toward front, the model tends to expand the face. | Use the fixed laptop width as a ruler and regenerate the full intermediate frame between two good endpoints. |
| **Hair clip and tuft swap sides** | Horizontal flipping or model confusion between left and right walks. | Draw `running-left` separately and explicitly lock "blue clip on viewer-right, tuft on viewer-left." |
| **Named look angle gazes backward** | Numerical angles alone are weak cues; sclera highlights can flip apparent gaze. | Catch ambiguous frames via unlabeled A/B blind checks and reinforce head turn, brim crown, and pupil placement. |

---

## 5. Build Dot's 16 Head Turns & v1.0.2 Face-Scale Refinements

Codex Dot uses 16 discrete head-turn poses advancing clockwise in `22.5°` steps from `000°` (up) to `337.5°` (up-left). Drawing all 16 sequentially in one pass accumulates drift by the time `337.5°` wraps back to `000°`. Instead, we use a **cardinals-first, intermediates-second** workflow:

### Step 1: Lock the Four Cardinal Directions (`000° / 090° / 180° / 270°`)

![Approved cardinal directions reference](../art/canonical/approved-cardinal-reference.png)

Establish straight-up, right, down, and left first. Verify that each reads unmistakably without labels while the seated body, feet, and laptop remain stationary.

### Step 2: Fill the Twelve 22.5° Intermediate Poses

![Sixteen head-turn directions overview](../previews/directions.png)

Using the stationary laptop as a visual ruler, step through the 12 intermediates so cheek width, eye spacing, far-eye foreshortening, and chin height transition smoothly.

### Step 3: v1.0.2 Redraws for Cheek Width & Upper-Left Return Continuity

In earlier builds, turning back toward the front from the left/upper-left quadrant (`270° → 292.5° → 315° → 337.5° → 000°`) or lifting from downward poses made the cheeks look pinched in side angles and made the whole face appear to swell on return.

In **v1.0.2**, **12 complete look frames were redrawn** with the built-in image generation tools (`022.5`, `045`, `067.5`, and `090` already read cleanly and were kept from `v1.0.1`), with dedicated face-scale refinements on `000`, `157.5`, `247.5`, `292.5`, `315`, and `337.5`—generated as complete connected frames **without face pasting or local mesh warping**:

![v1.0.1 vs v1.0.2 16-direction before/after comparison board](../art/repair/v1.0.2/review-boards/before-after-directions.png)

---

## 6. Normalize via Shared Viewport, Protect Native Alpha & Assemble

High-resolution source frames must never be cropped and stretched individually to their own opaque bounding boxes—doing so causes the character's body and laptop to pulse in size whenever she waves or tilts her hat.

- **Shared camera viewport**: Normalization applies a single shared viewport and scale per pose family, registering every frame onto the same baseline inside its **192 × 208** cell with at least `1 px` of transparent margin on all four sides.
- **Native alpha & dark contour preservation**: Inspect edges on both light and dark backgrounds. When generated alpha edges are already clean, **keep the native RGBA pixels untouched**—never run neighbor-color spill-averaging scripts that bleed blonde hair or white hat fills into dark contour lines (see [Hair-Outline Repair](OUTLINE-REPAIR.md) for how `v1.0.1` restored 88,948 contour pixels damaged by `v1.0.0` cleanup).
- **Frozen rows 0–8 guard**: After assembling the **1536 × 2288** atlas (73 used cells + 15 transparent cells) and exporting lossless WebP, `scripts/audit_artwork.py` verifies that all 57 standard animation frames in rows 0–8 remain **100% pixel-identical** to `v1.0.1`.

---

## 7. Multi-Stage Visual Review & Blind Direction QA

Passing file-dimension checks does not guarantee good drawings, and PNG/WebP equality cannot catch an artifact present in both files. Every release goes through three visual review gates (detailed in [Review and Validation](REVIEW.md)):

1. **Native 192 × 208 light/dark loop inspection**: Check loop wraparounds, the `idle → jumping → idle` takeoff and 0 px landing return, and forward/reverse single-frame stepping across `270° → 337.5° → 000°`.
2. **Three-reviewer unlabeled A/B blind direction tests**: Strip all filenames and angle labels, randomize 14 horizontal and vertical comparison pairs, and have 3 isolated AI reviewers classify gaze directions independently. All 14 pairs in `v1.0.2` passed by strict majority (see [Look Repair Evidence](look-repair-qa/README.md#blind-direction-checks)).
3. **Transparent documentation of discrete-pose limits**: Because Dot switches between 16 static drawings, `045` and `067.5` remain visually close, and `225 → 247.5` and `270 → 292.5` remain larger angular steps than their neighbors.

---

## 8. Automated Validation & Release Packaging

From the repository root with Python 3.10+, run the complete build, validation, and packaging suite:

```sh
# 1. Install Pillow
python3 -m pip install -r requirements.txt

# 2. Regenerate all GIFs, contact sheets, and native stills from the release WebP
python3 scripts/render_previews.py

# 3. Validate manifest, pixel equality, margins, all 832 archive hashes, EXIF, and privacy markers
python3 scripts/validate.py --report docs/validation.json

# 4. Run approved-artwork and v1.0.1 outline-restoration regression tests
python3 -m unittest discover -s tests

# 5. Build the distributable pet ZIP, full artwork archive ZIP, and SHA256SUMS.txt in dist/
python3 scripts/package.py
```

- To render optional MP4 video previews (requires FFmpeg), run `python3 scripts/render_previews.py --mp4`.
- Any intentional artwork update requires saving a newly reviewed baseline in `art/approved/<version>/spritesheet.png`, updating [art/approved-runtime.json](../art/approved-runtime.json) and `CHECKSUMS.sha256`, keeping historical snapshots and regression tests intact, and verifying the published GitHub Release download against local checksums.

---

## 9. Explore the 832-Image Production Archive

Every stage of Phoebe Chupi's creation—6 early concepts, 37 standing studies, 489 seated production frames, 192 unused open-eye experiments, and 99 head-turn and face refinements—is preserved across **832 unique source images** (**1,447 working-file occurrences**) in the [Image Archive](IMAGE-GALLERY.md).
