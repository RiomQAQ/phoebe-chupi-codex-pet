# Making Phoebe Chupi, frame by frame

[English README](../README.md) · [中文版](MAKING-OF.zh-CN.md) · [All images](IMAGE-GALLERY.md)

This document explains what was referenced, what was generated, how consistency was checked, which attempts were rejected, and what finally shipped.

**Production credit:** **GPT-6-Astra** assisted research, art direction, prompt construction, iteration, frame review, and documentation. The **built-in image generation feature** produced and edited raster images. The project owner chose the visual reference and accepted the expressive blinking version.

## 1. Decide what character is actually being made

The target was the community's **Phoebe Chupi**, not an official adult-proportioned Phoebe illustration and not a generic blonde mascot. Early work was insufficiently close to the desired shape. The project owner supplied a community front/profile/back image and explicitly asked to use it as the baseline.

That image became the shape authority. It is an AI-derived community reference attributed to 蓝蓝铜离子, with Doubao AI markings; it must not be presented as an official design sheet. Official Kuro Games material remained useful for identifying Phoebe and her primary design cues. Community stickers and Bilibili posts helped explain the Chupi expression vocabulary. [SOURCES.md](SOURCES.md) separates these roles and records attribution uncertainty.

The reference process was:

1. Identify the character and community variant before choosing a pose.
2. Collect frontal, profile, and rear information; note whether each source is official, fan-made, AI-derived, or uncertain.
3. Choose one controlling silhouette rather than averaging several inconsistent drawings.
4. Keep the original reference and useful working crops together.
5. Attribute every external source; avoid treating a reposting account as the original artist without evidence.

![Selected community turnaround](../art/canonical/user-reference.png)

## 2. Define the character lock

The pet needed to remain recognizably the same individual across every state. The following anchors were carried into generation prompts and review:

| Anchor | Requirement |
| --- | --- |
| Silhouette | Broad white brim, rounded crown with a dark/purple band, long pale-blonde hair, compact chibi body. |
| Face | Rounded small face, large purple layered eyes, restrained mouth and blush, consistent brow spacing. |
| Asymmetry | Blue clip on viewer-right; small tuft and blue cloth on viewer-left. |
| Outfit | White coat, dark gloves, gold/star accent, striped legs, dark shoes. |
| Prop | One blue-gray laptop with consistent lid, hinge, keyboard, and hand placement. |
| Rendering | Dark readable outline, soft flat color, limited detail suitable for a small native cell. |
| Proportions | Match the selected reference's head/body relationship; do not let a pose grow the chin or shrink the hat. |

Two canonical poses were then established: **seated with an open laptop** and **standing/carrying the closed laptop**. Those explain the two physical situations in the animation set. The transition changes how the same prop is held instead of inventing a different computer for movement.

| Seated anchor | Carry anchor |
| :---: | :---: |
| ![Seated](../art/canonical/seated-master-approved.png) | ![Carry](../art/canonical/carry-master-approved.png) |

New frames used these anchors and, where helpful, a neighboring approved frame. A rejected result was not allowed to silently become the next identity reference.

## 3. Choose actions that make sense while coding

The design question was what a coding companion should communicate over a long work session. Large unrelated dances would have weakened the connection between task state and character behavior. A seated setup made typing, waiting, checking, and a small greeting feel like one routine.

The nine required states were planned before filling the sheet:

- **Idle:** quiet seated breathing and a blink.
- **Working:** attention on the laptop, small typing changes.
- **Waiting:** look up, tilt slightly, invite a reply.
- **Review:** check the result, acknowledge it gently.
- **Failed/help:** brief disappointment, then recovery; avoid implying permanent distress or sleep.
- **Wave:** a restrained seated greeting with one hand.
- **Jump:** a small seated hop that returns to the same baseline.
- **Left/right movement:** carry the closed laptop with independently drawn directions.

The app decides when to play each state.

## 4. Generate and edit individual frames

The artwork was developed through image-generation/edit calls for individual frames. It was not assembled by procedurally redrawing a character or by stretching one finished pose into every motion. High-resolution originals and intermediate edits were retained.

For each frame:

1. Attach the relevant canonical pose and a nearby accepted frame where useful.
2. Name the state, frame position, intended movement, and fixed anchors.
3. Ask for one isolated character on transparent background, with no contact-sheet labels or unrelated objects.
4. Inspect the result at full resolution and at a small display size.
5. Request a targeted edit when anatomy, proportions, accessories, or props drift.
6. Preserve both the candidate and accepted result, and record why the candidate failed.

Parallel production helped collect references and produce candidates during the original creation session. Identity approval, cross-state comparisons, final normalization, and release selection still required shared anchors and a serial acceptance decision. More simultaneous generation does not itself make frames consistent.

The standard set contains **57 frames**. Once its visual language was stable, the look extension added another **16 poses**. Prompt patterns and review questions are in [PROMPTS.md](PROMPTS.md).

## 5. Repair concrete defects

Several failures only became clear when adjacent drawings were compared. Retaining them makes the process more useful than showing final images alone.

| Observed defect | Why it mattered | Repair strategy |
| --- | --- | --- |
| Extra hand, glove, or sleeve | Small-scale silhouettes looked anatomically wrong. | Edit the affected region; recount hands and check where each arm starts. |
| Duplicate eyebrow / stray facial line | Changed expression and made eyes look malformed. | Keep the canonical face geometry and remove the duplicate mark. |
| Laptop lid/keyboard duplication | Made a single prop look like two computers. | Re-establish one hinge and keyboard; compare against the carry/seated prop anchor. |
| Head or hat shrinkage | Made another state look like a different character. | Reject the frame or edit proportions using the canonical pose as the authority. |
| Enlarged chin / altered face width | Broke the chosen community silhouette. | Compare facial landmarks, not only overall bounding-box size. |
| Swapped accessory side | Destroyed asymmetry and implied an accidental mirrored frame. | Regenerate/edit that direction rather than horizontally flipping the other one. |
| Direction that read backward | A correctly named file still looked wrong on screen. | Review without labels, then repair the visible head/eye cue. |
| Baseline drift | A neutral look appeared to bounce or slide. | Register with measured offsets after the actual pose was approved. |

An edit was accepted only after comparing the repaired frame with the canonical image, the previous/next frame, and another state using the same physical setup.

## 6. Normalize without making the character change size

The image tool's high-resolution canvases were normalized into native **192 × 208** cells. A shared viewport and scale policy kept the character consistent. Fitting each opaque bounding box independently would enlarge a tilted pose or shrink a raised hand, so that approach was avoided.

The preparation order was: preserve the original → inspect alpha → apply the shared normalization → make justified registration corrections → inspect edges on light/dark backgrounds → assemble the sheet → encode the final WebP. Edge de-spill was applied consistently before the final acceptance pass, not repeatedly to unrelated individual frames.

The release includes both original source frames and **73 exact crops from the final distributed WebP**. They serve different purposes: source images explain generation and repairs; final crops show the actual pixels the renderer receives.

## 7. Build the sixteen look directions

The look extension makes her turn her head to follow the mouse in Codex Dot, while the seated body and laptop stay anchored. This is not a full-body turnaround and not an instruction to invent new white pupils inside the existing purple eye artwork.

The four cardinal directions were established first: up `000`, right `090`, down `180`, left `270`. Intermediate poses then filled the clockwise sequence in 22.5° steps. Left and right use **screen space**, not the character's own anatomical left/right.

Direction review included:

- a labeled 16-pose contact sheet to check order and registration;
- an unlabeled comparison to test what direction the image actually reads as;
- neighboring-pose loops, including the `337.5 → 000` wraparound;
- comparisons at the native small size and on dark backgrounds;
- laptop and torso stability, accessory sides, and visible face proportions.

![Sixteen final directions](../previews/directions.png)

Three AI reviewers performed the final blinded comparison procedure. Fourteen horizontal/vertical pairs passed by majority in the final review. See [REVIEW.md](REVIEW.md) for the method and results.

## 8. Review animation, not only pictures

A frame can be attractive in isolation and still interrupt the loop. Review therefore covered each state, each first/last-frame join, the hop's takeoff/landing, and transitions back to the seated baseline.

The original template preview understated how long idle eye poses could remain visible. Inspection of the locally used desktop build found idle durations multiplied by six, totaling **6.6 seconds**. A half-blink that seemed fleeting in a fast preview could therefore appear more conspicuous in the floating pet.

The solution was evaluated against the character's expression, not just a freeze-frame screenshot. A later experiment opened the eyes more consistently and tightened the shared viewport. The project owner felt it had lost liveliness and explicitly chose the earlier blinking version. That decision controls this release.

The final package therefore intentionally preserves the half-closed and closed-eye frames as part of a blink. The fully awake experiment remains in the archive as **rolled back**, and no install helper selects it.

![Idle to hop and back](../previews/idle-jump-idle.gif)

## 9. Validate the actual deliverable

The accepted master is a transparent **1536 × 2288 PNG**. Its lossless WebP distribution has the same decoded RGBA pixels. The portable manifest explicitly declares v2 and points to the local WebP.

Mechanical validation checks:

1. Manifest keys, relative atlas path, v2 version, static-image dimensions, and alpha.
2. All 73 required cells contain artwork; all 15 unused cells remain transparent.
3. Visible content has a margin inside its cell.
4. Every final crop matches the corresponding distributed-atlas pixels exactly.
5. Every archived source image exists and matches its published checksum.
6. Images decode successfully and do not retain unreviewed EXIF/XMP/comments.
7. Public text does not contain known private-path, account-ID, token, or expiring-link markers.
8. The runtime ZIP contains only the two portable files.
9. Public downloads match the local validated files after upload.

The [validation report](validation.json) covers the files. The [production review](production-review.json) records the visual checks and decisions.

## 10. Results, limits, and archive

| Result | Evidence / qualification |
| --- | --- |
| All required states present | 57 standard frames plus 16 look poses. |
| Correct v2 geometry | 8 × 11 grid, native 192 × 208 cells. |
| Lossless distribution | PNG and WebP decode to identical RGBA pixels. |
| Hop returns to the baseline | The production measurement recorded 21 px peak lift, 0 px landing delta, using its thresholded visible-boundary method. |
| Gaze remains registered | Recorded horizontal center drift ≤ 3.5 px and width ratio ≤ 1.0625 under that same production measurement. |
| Blinded direction review | Fourteen comparisons passed the final three-reviewer majority procedure. |
| User-selected expression | Expressive blinking version restored after the awake experiment. |
| Full working-image archive | 742 distinct source images; 1,290 working-file occurrences mapped without storing identical copies repeatedly. |

Known limitations remain visible: the `045` and `067.5` poses are close, `225 → 247.5` changes more abruptly than its neighbors, blink poses can be noticed when held, and small native artwork softens when magnified. Dot use and mouse-following head turns were confirmed by the project owner. Windows has not had a visual acceptance run.

Browse the [archive](IMAGE-GALLERY.md) for early concepts, standing studies, seated production, rejected drafts, later expression samples, and the rolled-back awake experiment. Generated originals outside the main working folders that were referenced by production records were also recovered and included. Private application screenshots, account-bound upload records, and bulk third-party research downloads are excluded.

## 11. Reuse the process for another pet

**v1.0.1 follow-up:** the original review missed an edge-cleanup error that faded some dark contours. The [repair record](OUTLINE-REPAIR.md) shows how the approved pre-cleanup pixels were recovered, checked across all 73 frames, and re-exported without changing the motion. The public validator now checks that source-color fidelity too.

Choose one identity anchor, define the whole state set, and approve the canonical pose before multiplying frames. Keep asymmetry explicit. Generate candidates independently if useful, but reconcile every candidate against the same anchors. Measure geometry after artistic approval, and visually review again after normalization and encoding.

For a public release, separate the two-file runtime from the image archive, write honest compatibility and known-limit sections, attribute references, keep third-party rights separate from code licensing, sanitize metadata, and verify the remote download. Preserve rejected experiments so the next iteration can understand why a seemingly cleaner result was not selected.
