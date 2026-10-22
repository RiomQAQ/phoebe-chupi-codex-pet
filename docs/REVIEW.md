# Review and validation

**English** · [简体中文](REVIEW.zh-CN.md) · [Documentation](README.md)

Review the drawings, motion, and distributed files as separate checks. Use the canonical poses for identity and the final WebP for release verification.

## Review each frame

Inspect every occupied cell on a light background and a dark background. Start at the native **192 × 208** size; enlarge a region to diagnose a defect.

| Area | Acceptance criteria |
| --- | --- |
| Identity | Face, hat, hair, clothing, and head/body proportions match the anchors. |
| Accessories | Clip remains on viewer-right; tuft and blue cloth remain on viewer-left. |
| Anatomy | Two intended hands and arms, with clear glove/sleeve connections. |
| Face | Consistent purple eyes, brows, chin, and mouth; no duplicate marks. |
| Laptop | One lid, hinge, and keyboard; hands hold the intended surfaces. |
| Contour | Dark outer lines remain continuous; gold/brown inner hair lines retain their source color. |
| Transparency | No opaque backdrop, clipped extremity, fringe, or interior hole. |
| Registration | Body, laptop, and ground contact stay stable where the pose requires them to. |

Compare a changed frame with its anchor, both neighbors, and another state using the same physical setup. Recheck after normalization and encoding.

## Review the motion

- Play all nine loops at the expected speed and inspect each last-to-first join.
- Watch `idle → jumping → idle` for takeoff, the attached laptop, and the recovered baseline.
- Compare working, waiting, review, and help expressions as one continuous character.
- Check both carry directions for consistent proportions and accessory placement.
- Run all sixteen looks through the wraparound while watching body/laptop drift separately from head cues.

Use the [all-state animation](../previews/all-states.gif), [hop transition](../previews/idle-jump-idle.gif), [direction loop](../previews/look-loop.gif), and [dark previews](../previews/dark). GIF palettes have fewer colors; the [PNG](../art/final/spritesheet.png) and [exact crops](../art/frames) preserve the distributed pixels.

## Direction review

First inspect the labeled direction sheet and ordered loop. Then use unlabeled A/B pairs to check the apparent direction:

1. Compare seven horizontal and seven vertical pairs, with cardinal directions as required passes.
2. Hide the labels and answer key; vary A/B order.
3. Ask three independent reviewers for the visible screen direction and supporting cues. Allow an ambiguous answer.
4. Save the answers before revealing the key, then aggregate by strict per-cell majority.
5. Inspect any disagreement against the ordered sequence before accepting or repairing the pose.

The v1.0.1 review used three AI reviewers. All fourteen majority comparisons passed. Individual answers, the key, and the full-frame review are in [review evidence](repair-qa/README.md).

## Current results

These results apply to the **v1.0.1** runtime identified in [validation.json](validation.json) and [production-review.json](production-review.json).

| Check | Result |
| --- | --- |
| Layout | 1536 × 2288; 73 occupied cells and 15 transparent cells. |
| Export fidelity | PNG and lossless WebP have identical decoded RGBA pixels. |
| Frame crops | All 73 crops match their atlas cells. |
| Source-color fidelity | All 73 cells match the approved pre-cleanup source. |
| Outline restoration | 88,948 visible RGB pixels restored; 263,885 dark-ink pixels checked with zero mismatches. |
| Hop | 21 px peak lift; 0 px landing offset. |
| Head registration | Maximum horizontal center drift 3.5 px; maximum width ratio 1.0625. |
| Visual inspection | All 73 frames reviewed on light/dark backgrounds, plus a separate independent pass and native-size playback. |
| Source archive | 742 distinct source images; 1,290 working-file occurrences indexed. |

Movement measurements use alpha > 16. The raw bounds in `validation.json` include any nonzero alpha; keep these two measurement policies distinct.

## Known limitations

- `045` and `067.5` remain visually close.
- `225 → 247.5` is a larger step than its immediate neighbors. These refinements are tracked in [issue #2](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues/2).
- Blink poses include partly closed and closed eyes. Reduced motion or app timing can hold one pose visibly.
- macOS desktop and Dot behavior have been checked; Windows visual verification is pending.

The [outline repair record](OUTLINE-REPAIR.md) explains the v1.0.0 cleanup error. Its lesson is part of the export check: comparing two formats does not detect a mistake already present in both.

## Run the file checks

With Python 3.10+ and the repository dependencies installed:

```sh
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
```

The validator checks the five-field manifest, static v2 image, cell population and margins, PNG/WebP equality, final crops, source-color fidelity, archive hashes, decoding, metadata, common private-data markers, file sizes, and distribution checksums. Regression tests reject the actual damaged v1.0.0 atlas and check three reported hair pixels.

The color guard uses the approved v1.0.1 source. An intentional artwork revision needs a newly reviewed baseline and checksum, with the historical source and regression case preserved. CI runs the file validator and regression tests; visual review remains a separate step.

## Release checklist

- [ ] Review changed frames, adjacent frames, complete loops, and state transitions.
- [ ] Repeat independent direction comparisons after changing a look pose.
- [ ] Generate previews from the exact WebP to be distributed.
- [ ] Update source records, checksums, and both language editions.
- [ ] Check attribution, metadata, and public-file privacy.
- [ ] Run file validation and regression tests; inspect the package contents.
- [ ] Align `VERSION`, the installer URL, and the version tag.
- [ ] Verify CI on the release commit and compare public downloads with the validated files.
