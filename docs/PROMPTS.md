# Prompt Playbook & Multimodal Workflow

**English** · [简体中文](PROMPTS.zh-CN.md) · [Documentation](README.md)

When building a 73-frame Codex v2 desktop pet sprite atlas (`1536 × 2288`, 8 columns × 11 rows), most failures happen not because the image model cannot draw, but because **prompts ask for too much at once, omit visual anchors, or feed a slightly distorted intermediate frame into the next generation like a game of telephone**.

This playbook documents the seven core prompt templates used across the Phoebe Chupi pipeline—from establishing canonical pose anchors and expanding motion loops to repairing local defects, drawing the 16-angle Dot look ring, and running unlabeled blind QA. Alongside each copy-ready prompt, you will find **why specific reference images are attached** and **what failure mode each constraint prevents**.

---

## 0. Golden Rules of Sprite Prompting

```text
+-------------------------------------------------------------------------+
|  1. Generate or edit ONE frame at a time (never ask for a whole strip)  |
|  2. Always anchor on the approved master pose; use neighbors only       |
|     to judge motion step size                                           |
|  3. Explicitly separate what moves from what stays locked               |
|     (camera / laptop / torso / feet)                                    |
|  4. When face proportions drift, discard the bad frame and interpolate  |
|     fresh between two approved neighbors                                |
+-------------------------------------------------------------------------+
```

Before running any template below, attach the indicated reference images to the conversation context and replace bracketed fields (`[...]`) with your target state, frame index, or specific defect.

---

## 1. Character Anchor

Before drawing a single animation frame, establish two canonical master poses from the community three-view turnaround: **seated with an open laptop** and **carrying the same laptop closed**. These two masters govern the head-to-body ratio, hat width, left/right accessory placement, and laptop geometry across all 73 occupied cells.

<table>
  <tr>
    <td align="center" width="33%">
      <img src="../art/canonical/reference-front-cutout.png" width="150" alt="Front reference cutout" /><br />
      <sub><b>Input Reference A</b>: Front turnaround crop</sub>
    </td>
    <td align="center" width="33%">
      <img src="../art/canonical/seated-master-approved.png" width="150" alt="Approved seated master" /><br />
      <sub><b>Output Anchor 1</b>: Seated state master (open laptop)</sub>
    </td>
    <td align="center" width="33%">
      <img src="../art/canonical/carry-master-approved.png" width="150" alt="Approved carry master" /><br />
      <sub><b>Output Anchor 2</b>: Carry/move state master (closed laptop)</sub>
    </td>
  </tr>
</table>

### Prompt Template

```text
Create one transparent-background Phoebe Chupi character from the attached
front/profile/back reference. Keep the compact chibi proportions, pale-blonde
long hair, broad white hat with a dark-purple band, layered purple eyes,
white outfit, dark gloves, striped legs, and dark shoes.

Keep the blue hair clip on viewer-right and the tuft/blue cloth on viewer-left.
Use a dark outer contour and gold/brown internal hair lines.

Pose: [seated with one open blue-gray laptop / carrying the same laptop closed].
Keep one lid, hinge, and keyboard, with clear hand placement. Show the entire
hat, hair, hands, and feet with margin. One character, transparent background,
no text or labels.
```

### Why These Constraints Matter

- **"viewer-right" and "viewer-left"**: Specifying screen-relative sides rather than character-left/right prevents the model from accidentally mirroring asymmetric accessories.
- **"Keep one lid, hinge, and keyboard"**: Image models frequently hallucinate double laptop lids or place keys on the back of the screen. Naming the exact mechanical parts eliminates most prop defects up front.
- **"dark outer contour and gold/brown internal hair lines"**: At the native **192 × 208** cell size, pale-blonde hair disappears into light desktop backgrounds without a dark outer silhouette, while black internal hair lines make the head look muddy.

---

## 2. Edit One Animation Frame

Once the pose anchor passes review, the 57 standard animation frames across the first nine rows are built as controlled single-frame steps around that anchor. Attach the **canonical pose anchor** plus **one neighboring accepted frame**.

<table>
  <tr>
    <td align="center" width="50%">
      <img src="../art/canonical/seated-master-approved.png" width="150" alt="Seated master anchor" /><br />
      <sub><b>Anchor Input</b>: Locks camera, laptop, and body scale</sub>
    </td>
    <td align="center" width="50%">
      <img src="../art/frames/waiting/01.png" width="150" alt="Waiting frame 2" /><br />
      <sub><b>Single-Frame Output (waiting 2 of 6)</b>: Subtle head tilt; base remains locked</sub>
    </td>
  </tr>
</table>

### Prompt Template

```text
Edit the attached character into one frame.
State: [waiting]. Position: [2 of 6]. Change: [small expectant head tilt].

Preserve identity, head/body ratio, hat size, hair silhouette, purple eye
construction, line weight, outfit, accessory sides, and laptop geometry.
Keep the camera, seated body, feet, and laptop anchored. Use the neighboring
frame only to judge motion amplitude. Change the intended head/face/hand
movement and keep a transparent background. Output one isolated frame.
```

### State-Specific Notes

- **Carry rows (`running-right` / `running-left`)**: Specify the screen direction, support leg, and step phase. Draw left and right sequences separately—never horizontally mirror the artwork.
- **Seated hop (`jumping`)**: Specify takeoff, peak, descent, or landing while retaining the open laptop and shared scale so `idle → jumping → idle` joins with zero landing offset.

---

## 3. Repair a Defect

When a frame has great expression and timing but suffers from a local flaw—such as a duplicate glove beside the laptop, a broken sleeve cuff, or an extra screen seam—do not regenerate the whole pose from scratch. Attach the canonical feature reference and apply a targeted surgical edit.

### Prompt Template

```text
Repair [the duplicate glove at the right edge of the laptop].
Restore [one hand connected to the white sleeve] using the canonical pose.
Preserve the accepted expression, silhouette, proportions, accessories,
and every unaffected feature. Keep one laptop and a transparent background.
```

> **Tip**: Always recheck the whole silhouette and drop the repaired frame back into its neighboring sequence at native **192 × 208** size to verify that the fix did not introduce line-weight jumps or edge halos.

---

## 4. Create a Dot Look Pose

Rows 9 and 10 store the 16 head-turn poses used by Codex Dot in screen coordinates (see the [format reference](FORMAT.md#look-directions) for all 16 angles). Without strict body-lock constraints, image models tend to rotate the entire character and laptop together.

<p align="center">
  <img src="../art/repair/v1.0.2/review-boards/before-after-cardinals.png" width="760" alt="Cardinal directions before and after v1.0.2 repair" />
</p>

### Prompt Template

```text
Create the [090] look pose: the character must visibly look [screen-right].
Angles increase clockwise from screen-up: 000 up, 090 right, 180 down, 270 left.

Use head orientation, eye direction, face shape, and visible hat crown to
communicate the look. Preserve the established purple eyes and accessory sides.
Keep the torso, laptop, feet, camera, scale, and ground contact registered.
One transparent-background frame; the seated body does not rotate with the head.
```

### Recommended Order of Operations

1. **Establish the four cardinal directions first**: Lock `000` (up), `090` (right), `180` (down), and `270` (left) so hat-crown foreshortening and horizontal gaze cues are unmistakable.
2. **Fill the intermediate poses**: Compare every new `22.5°` pose side-by-side with both immediate neighbors to verify monotonic gaze progression.

---

## 5. Repair a Face-Size Jump

During the v1.0.2 Dot look repair, we encountered a subtle failure mode along the upper-left return arc (`292.5° → 315° → 337.5° → 000°`): even though the laptop stayed still, Phoebe's face appeared to grow larger on some frames or pinch at the cheeks on others.

Feeding a distorted frame into the next attempt carries its distorted proportions forward. Instead, **use a good neighboring pose as the edit target and generate one complete transparent frame between two accepted poses** (keeping the failed frame only for side-by-side comparison):

### Prompt Template

```text
Generate one complete transparent frame between the two supplied accepted poses.
Use the first pose as the exact body, laptop, camera, and character-size anchor.
Rotate the head, face, fringe, and attached accessories together by a small step.
Keep the original eye artwork, cheek proportions, eye spacing, and short chin.
Let perspective change gradually toward the second pose.

Keep the torso, hands, laptop, seated legs, and feet in place. Preserve the
existing hat design. No head-only resizing, pasted face pieces, new eye
patterns, camera zoom, or fitting the character independently to the canvas.
Output the entire connected character as one frame.
```

### Why "No Pasted Face Pieces"?

- Phoebe's broad white hat brim, blonde fringe, hair clip, and cheeks overlap in tight perspective. Scaling or warping the face region alone breaks the fringe-to-hat junction and immediately reads as a cut-and-paste collage at **192 × 208** native size.
- Generating a complete connected character anchored to two approved neighbors preserves the hat design and eliminates apparent face growth while the laptop stays still.

---

## 6. Review Frames and Motion

Once frames are sliced into the grid, provide the **canonical poses + neighboring frames + native-size stills + actual loops** with this comprehensive inspection prompt:

### Prompt Template

```text
Review the supplied frames and loops against the canonical poses.
Check identity, head/body ratio, accessory sides, hands, face lines, laptop
geometry, contour color, transparency, and registration.

Watch all nine loops, the sixteen-look sequence, and idle-hop-idle. Inspect
last-to-first joins, expression changes, scale, prop continuity, and landing.

For each finding, report pass/warning/fail, the affected frame or transition,
the visible evidence, and a targeted correction. Distinguish deliberate blink
poses from drawing errors. Do not infer motion absent from the supplied media.
```

Use the findings to locate targeted repairs, then rerun the affected comparisons. File validation (`scripts/validate.py`) is run as a separate automated check.

---

## 7. Review Directions Without Labels (Blind QA)

If you hand a multimodal model an image named `270.png` and ask where the character is looking, it can infer the answer from the label rather than the drawing.

To measure true visual readability, keep filenames, direction labels, and the answer key out of the review material, and present opposing angles as unlabeled `A / B` pairs (see the [review guide](REVIEW.md#direction-review) for the aggregation and acceptance procedure):

<p align="center">
  <img src="../art/repair/v1.0.2/review-boards/blind-axis-pairs.png" width="720" alt="Unlabeled A/B opposite-axis blind test board" />
</p>

### Prompt Template

```text
For each unlabeled A/B pair, report the apparent gaze of both images in screen
coordinates: left/right or up/down. Give confidence and the visible cue.
If the direction is ambiguous, say so. Use only the supplied images and do
not consult the answer key.
```

Save all independent answers before revealing the answer key, and compare any disagreements against the ordered 16-angle direction loop.
