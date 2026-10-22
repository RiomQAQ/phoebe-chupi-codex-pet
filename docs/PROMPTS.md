# Prompt examples

**English** · [简体中文](PROMPTS.zh-CN.md) · [Documentation](README.md)

Attach the relevant reference images before using these templates. Replace bracketed fields with a specific state, frame, or defect. Generate and edit one frame at a time.

## Character anchor

Use the community reference to establish the seated and carry poses before making animation frames.

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

Compare the face, head/body ratio, hat width, accessory sides, and laptop before accepting the anchor.

## Edit one animation frame

Attach the pose anchor and a neighboring accepted frame.

```text
Edit the attached character into one frame.
State: [waiting]. Position: [2 of 6]. Change: [small expectant head tilt].

Preserve identity, head/body ratio, hat size, hair silhouette, purple eye
construction, line weight, outfit, accessory sides, and laptop geometry.
Keep the camera, seated body, feet, and laptop anchored. Use the neighboring
frame only to judge motion amplitude. Change the intended head/face/hand
movement and keep a transparent background. Output one isolated frame.
```

For a carry frame, specify the screen direction, support leg, and step phase. Draw left/right separately. For the seated hop, specify takeoff, peak, descent, or landing, retaining the open laptop and the shared scale.

## Repair a defect

State the location and visible problem. Include the anchor for the affected feature.

```text
Repair [the duplicate glove at the right edge of the laptop].
Restore [one hand connected to the white sleeve] using the canonical pose.
Preserve the accepted expression, silhouette, proportions, accessories,
and every unaffected feature. Keep one laptop and a transparent background.
```

Recheck the whole silhouette and adjacent frames after the edit.

## Create a Dot look pose

Use screen coordinates. The [format reference](FORMAT.md#look-directions) defines all sixteen angles.

```text
Create the [090] look pose: the character must visibly look [screen-right].
Angles increase clockwise from screen-up: 000 up, 090 right, 180 down, 270 left.

Use head orientation, eye direction, face shape, and visible hat crown to
communicate the look. Preserve the established purple eyes and accessory sides.
Keep the torso, laptop, feet, camera, scale, and ground contact registered.
One transparent-background frame; the seated body does not rotate with the head.
```

Establish the cardinal directions first, then fill the intermediate poses. Compare each new pose with both neighbors.

## Review frames and motion

Provide the canonical poses, neighboring frames, native-size stills, and the actual loops.

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

Use the result to locate repairs, then rerun the affected comparisons. File validation is a separate check.

## Review directions without labels

Keep filenames, direction labels, and the answer key out of the review material. Collect independent answers before revealing the intended directions.

```text
For each unlabeled A/B pair, report the apparent gaze of both images in screen
coordinates: left/right or up/down. Give confidence and the visible cue.
If the direction is ambiguous, say so. Use only the supplied images and do
not consult the answer key.
```

Save disagreements and compare them with the ordered direction loop. The [review guide](REVIEW.md#direction-review) describes the aggregation and acceptance procedure.
