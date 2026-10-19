# Prompt recipes / 制作与审查提示词

[Making of](MAKING-OF.md) · [中文制作记录](MAKING-OF.zh-CN.md) · [Sources](SOURCES.md)

These examples cover the main production tasks. Attach the shape reference and canonical image, then fill in the state, frame number, and intended change. Work on one frame at a time.

Artwork generation used the built-in image generation feature, with **GPT-6-Astra** assisting planning, prompt writing, iteration, and review.

## 1. Canonical character lock

```text
Create one transparent-background full-body Phoebe Chupi fan character using
the attached community turnaround as the shape authority.

Preserve the compact chibi proportions, pale-blonde long-hair silhouette,
broad white hat with dark-purple band, large layered purple eyes, small face,
white outfit, dark gloves, striped legs, and dark shoes.

Keep the blue clip on the viewer's RIGHT and the tuft/blue cloth on the
viewer's LEFT. Do not mirror the character. Keep clear dark outlines and
restrained soft color so the design remains readable in a small pet cell.

Pose: seated with the feet forward, using one open blue-gray laptop on her lap.
Make the lid, hinge, keyboard, and both hands anatomically and mechanically
clear. One character, one laptop, no extra hands, no text, no panel, no shadow
or opaque background. Preserve full hat, hair, hands, and shoes with margin.
```

Approve this anchor before producing the whole state set. A canonical image with poor proportions spreads the same problem to every later frame.

## 2. Single-frame motion edit

```text
Edit the attached approved canonical character into exactly one animation frame.
State: [waiting]. Frame: [2 of 6]. Intended change: [small expectant head tilt].

Keep the same identity, head/body ratio, hat size, hair silhouette, eye design,
outfit, accessory sides, line weight, and laptop. Use the attached neighboring
approved frame to judge the amount of motion, not to replace the identity lock.

Keep the seated body, feet, laptop placement, and camera stable. Change only
the intended head/face/hand movement. Preserve the purple eye construction;
do not invent a different pupil style. Keep exactly the intended two arms/hands.
Transparent background. One isolated frame, no contact sheet or labels.
```

For movement, attach the carry anchor instead and explicitly request the closed laptop, direction, support leg, and intended step. Left/right must be separately drawn to preserve asymmetry.

## 3. Targeted defect repair

```text
Repair only the identified defect in this candidate:
[The right glove appears twice / the laptop keyboard is duplicated /
the chin is wider than the canonical face / the hat has become too small].

Use the approved canonical reference as the authority for the affected shape.
Preserve the accepted pose and every unaffected identity feature. Keep one
laptop with one hinge and keyboard, the same accessory sides, and a transparent
background. Do not redesign the face, outfit, or prop to hide the defect.
```

Afterward, review the repaired area plus the full silhouette and adjacent frames. A local correction can unintentionally change another feature.

## 4. Small seated hop

```text
Create frame [index] of a restrained seated hop for the attached coding companion.
Sequence intention: neutral seated -> rise -> brief airborne peak -> descend
-> same seated landing. Keep the open laptop with her and preserve its shape.

Keep the character's scale and camera identical to the seated anchor.
Motion should read as a small happy hop, not a standing jump, full-body redesign,
or extreme squash/stretch. Do not independently enlarge the airborne frame.
Transparent background with full silhouette margin.
```

The visible lift is implemented through approved pose/registration, not by fitting each frame to a different bounding box. Verify the landing numerically and visually.

## 5. Screen-space look pose

```text
Create the [090-degree] look pose for the attached seated character.
Angles are screen-space, clockwise from UP: 000 up, 090 viewer-right,
180 down, 270 viewer-left. This pose must visibly read as [screen-right].

Use head orientation and the existing purple eye artwork to communicate that
direction. Keep torso, laptop, feet, camera, scale, and ground contact anchored.
Do not make a full-body turntable pose. Do not mirror accessory sides or invent
new white pupils. Preserve the canonical hat, face proportions, and silhouette.
One transparent-background frame only.
```

Approve cardinal poses first. Add intermediate angles only after the cardinal directions read correctly without labels.

## 6. Per-frame reviewer prompt

```text
Compare this candidate with the canonical reference and neighboring frames.
Identify concrete defects in identity, proportions, accessory sides, anatomy,
face lines, eye style, laptop geometry, alpha edges, and frame registration.

Separate a hard defect from an acceptable expressive variation. Say where the
defect appears and what a targeted repair should change. Evaluate the image at
native pet size as well as enlarged. Do not approve it merely because it looks
cute in isolation. Do not infer motion you cannot see in the supplied frames.
```

## 7. Blind direction reviewer prompt

```text
The two images have no direction labels. Describe each character's apparent
gaze using SCREEN coordinates: left/right or up/down, plus confidence.
Report what the image visibly communicates, not what its file name might mean.
If a direction is ambiguous, say so. Do not access the answer key.
```

Randomize pair ordering and keep the answer key separate. Ask multiple reviewers before revealing it. Record disagreement rather than converting uncertainty into an automatic pass.

## 8. Final holistic review prompt

```text
Review all nine state loops, the sixteen-look loop, and idle-hop-idle together.
Does one coherent character perform one understandable coding-companion routine?
Check transitions, first/last-frame joins, eye-expression range, body scale,
hat/hair stability, laptop continuity, and accessory sides.

Use actual expected runtime durations. Distinguish a bad drawing from a
deliberate blink caught in a screenshot. Report remaining weaknesses and the
practical consequence of each. A mechanical validation pass is not visual approval.
```

## 中文使用建议

先附上社区造型参考和确认过的基准图，再填写状态、帧位置和这次要改的动作。

提示词需要把不变的部分写具体：头身比例、帽子大小、长发轮廓、紫色眼睛、发夹和蓝布的方向、手套，以及同一台电脑。不要每次重新描述一个近似角色，也不要让失败稿变成下一张的造型标准。

修改时只指定清楚的问题，例如多一只手、重复眉毛、两层键盘、下巴太宽或帽子变小。改完仍要看完整轮廓和前后帧，局部修改也可能带来别处的变化。

视线按屏幕方向定义，先画上、右、下、左，再补斜方向。身体和电脑稳定，头与眼神表达方向；不要镜像配饰，不要凭空改瞳孔风格。

审查者应指出可定位的问题，而不是只说好看。方向盲测先藏标签和答案，允许回答不确定，最后再比对。整体验收要看所有循环与实际时长，既不能把眨眼截帧一律当作坏图，也不能用校验通过代替画面审查。
