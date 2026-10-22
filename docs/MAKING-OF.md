# Making a pet

**English** · [简体中文](MAKING-OF.zh-CN.md) · [Documentation](README.md)

This guide follows the production of Phoebe Chupi: establish the character, build a coherent set of actions, create the individual frames, then review the finished package.

The project was made with **GPT-6-Astra** and the built-in image generation tools. Scripts handle normalization, previews, validation, and packaging.

## 1. Establish the reference

Use a front, profile, and back reference to define the silhouette before drawing motion. For this pet, the primary reference is the community three-view image attributed to 蓝蓝铜离子. Official Phoebe material establishes identity and color; community drawings and motion studies inform the chibi interpretation.

![Community three-view reference](../art/canonical/user-reference.png)

Record the source, author attribution, and intended use of each reference. A collection uploader is not necessarily the original creator. The [source list](SOURCES.md) separates character material, community references, and motion studies.

## 2. Create two pose anchors

The seated anchor holds an open laptop. The carry anchor holds the same laptop closed. Standard actions use one of these physical setups.

| Seated anchor | Carry anchor |
| :---: | :---: |
| ![Seated character](../art/canonical/seated-master-approved.png) | ![Carrying the laptop](../art/canonical/carry-master-approved.png) |

Keep these features consistent in every frame:

| Feature | Anchor |
| --- | --- |
| Silhouette | Broad white hat, dark-purple band, long pale-blonde hair, compact body. |
| Face | Small rounded face, layered purple eyes, consistent brow spacing and chin. |
| Accessories | Blue clip on viewer-right; tuft and blue cloth on viewer-left. |
| Clothing | White outfit, dark gloves, gold accents, striped legs, dark shoes. |
| Laptop | One lid, hinge, and keyboard; plausible hand placement. |
| Line work | Dark outer contour, gold/brown internal hair lines, restrained flat color. |

Approve the anchors before producing the full set. Use them as the identity reference throughout; neighboring frames provide motion context.

## 3. Plan the complete action set

Start with the app's [nine state rows](FORMAT.md#animation-states). Give them a shared routine: work at the laptop, pause for a reply, check a result, greet, or ask for help. Movement uses the closed laptop; the small seated hop keeps the open laptop with the character.

Define each loop's start pose, main action, and return pose. Establish the common seated baseline before adding expression changes. The current edition includes half-closed and closed eyes as part of its blink. The always-open-eye study is retained in the archive as an unused alternative.

## 4. Generate and edit one frame at a time

For each frame:

1. Attach the appropriate pose anchor and an adjacent accepted frame.
2. Specify the state, position in the sequence, intended motion, and fixed features.
3. Generate one isolated character on a transparent background.
4. Inspect the full-resolution result and a native-size preview.
5. Repair a specific defect with the same anchor attached.
6. Compare the result with both neighboring frames and another state using the same setup.

The [prompt examples](PROMPTS.md) cover these tasks. Save candidates and accepted frames separately so a rejected drawing does not become the next reference.

| Common defect | Targeted correction |
| --- | --- |
| Extra glove, arm, or sleeve | Recount the hands and restore the arm-to-sleeve connection. |
| Duplicate brow or facial mark | Restore the canonical face landmarks. |
| Two laptop lids or keyboards | Re-establish one hinge, lid, and keyboard. |
| Head, hat, or chin changes size | Correct proportions against the anchor. |
| Accessories change sides | Draw the opposite pose separately; preserve asymmetry. |
| A named direction reads backward | Repair the visible head and eye cues after an unlabeled review. |

A local edit can change another feature. Review the whole frame again after each correction.

## 5. Add Dot head turns

Create up `000`, right `090`, down `180`, and left `270` first. Once those read clearly without labels, add the intermediate directions in 22.5° steps.

Keep the seated body, laptop, feet, and camera registered. Head rotation, eye direction, and the visible hat crown communicate the look; this is not a full-body turnaround.

![Sixteen head directions](../previews/directions.png)

Review the clockwise sequence, its `337.5 → 000` join, and unlabeled horizontal/vertical pairs. The [review guide](REVIEW.md#direction-review) describes the comparison procedure.

## 6. Normalize and assemble

Preserve the high-resolution originals. Apply a shared viewport and scale to the accepted frames, then register them in **192 × 208** cells. Avoid fitting each frame independently to its visible bounds.

Inspect alpha and contour colors on light and dark backgrounds. Preserve clean native alpha without averaging nearby fill colors into dark outlines. The [v1.0.1 repair](OUTLINE-REPAIR.md) documents the failure this prevents.

Assemble the **1536 × 2288** atlas with 73 occupied and 15 transparent cells. Export a lossless WebP and compare it with the approved PNG. Derive the final frame crops and previews from that WebP.

## 7. Review the finished motion

Inspect each loop at native size and at the expected playback speed. Check the loop boundaries, the laptop through every pose, and the hop's return to the seated baseline. Review the look sequence on both backgrounds.

Use the [visual checklist and current results](REVIEW.md) alongside the file checks. Correct dimensions do not establish drawing quality, and PNG/WebP equality does not detect a color mistake already present in both files.

## 8. Validate and package

From the repository, with Python 3.10+:

```sh
python3 -m pip install -r requirements.txt
python3 scripts/render_previews.py
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
python3 scripts/package.py
```

The package script produces a two-file pet ZIP, a complete artwork ZIP, and `SHA256SUMS.txt` in `dist/`. An optional MP4 preview uses `python3 scripts/render_previews.py --mp4` and requires FFmpeg.

Before publishing, update the approved baseline and checksums for any intentional artwork changes, keep the version tag and `VERSION` aligned, and check attribution. After publishing, verify the public file against the local validated artifact.

## Production archive

The [image archive](IMAGE-GALLERY.md) preserves **742 distinct source images**, mapping **1,290 working-file occurrences**. It includes references, accepted frames, comparison boards, rejected candidates, and the unused eye-expression study. Exact current-atlas crops and repair evidence are included separately.
