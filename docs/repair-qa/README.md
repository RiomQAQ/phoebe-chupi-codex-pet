# v1.0.1 review evidence / 检查记录

[Repair notes](../OUTLINE-REPAIR.md) · [Frame boards](../../art/repair/v1.0.1/review-boards)

These reports cover the exact runtime WebP identified by its SHA-256. Paths are repository-relative.

- `atlas.json`: grid, alpha, empty cells, chroma fringe and encoded file identity.
- `frames.json`: standard-frame geometry and final crops.
- `continuity.json`: adjacent head directions, silhouette continuity and the recorded local warning.
- `chroma-preservation.json`: clean native alpha preserved without color averaging.
- `direction-semantics.json`: all sixteen labeled directions and specific visual evidence.
- `blind-reviewer-a.json`, `blind-reviewer-b.json`, `blind-reviewer-c.json`: independent answers, saved before revealing the answer key.
- `blind-majority.json`, `blind-answer-key.json`, `blind-validation.json`: aggregation and comparison with the intended directions.
- `independent-all-frames.json`: a separate visual review of all 73 frames on light/dark backgrounds.
- `pet-quality.json`: final file identity, jump/landing measurement and head registration.

These are AI-assisted reviews. The primary pass also checked the ordered frame boards, loops and timed browser playback. The earlier missed defect and the remaining subtle head poses are described in the repair notes.

这里保留了独立审查者的原始判断、盲看答案与汇总、全帧检查、方向依据和文件检查结果。审查由 AI 辅助完成；没有把尺寸通过当作画面无误的证明。
