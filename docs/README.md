# Documentation

**English** · [简体中文](README.zh-CN.md) · [Project home](../README.md)

Install Phoebe v1.0.2, study how the sprites were made, or use the workflow to build another pet.

## Use the pet

- [Install and update](INSTALL.md): local installation, native import, compatibility, and troubleshooting.
- [Image archive](IMAGE-GALLERY.md): source images, final frames, and animation previews.
- [Credits](../NOTICE.md) · [Artwork usage](../ASSET-USAGE.md): attribution and permitted use.

## Make and maintain a pet

Read the [making guide](MAKING-OF.md) for the full workflow, then use these references as needed:

| Document | Purpose |
| --- | --- |
| [Prompt examples](PROMPTS.md) | Generate a consistent character, edit one frame, and review motion. |
| [Sprite format](FORMAT.md) | Implement the v2 manifest, grid, state rows, and look directions. |
| [Review and validation](REVIEW.md) | Inspect artwork, run checks, and prepare a release. |
| [Sources](SOURCES.md) | Trace the character, visual references, motion studies, and package examples. |
| [v1.0.2 look repair evidence](look-repair-qa/README.md) | Review the revised face and direction poses, direction comparisons, and native-size browser checks. |
| [Outline repair](OUTLINE-REPAIR.md) | Understand the v1.0.1 export correction and reproduce it. |
| [v1.0.1 review evidence](repair-qa/README.md) | Read the historical outline-repair reports and independent direction reviews. |

## Repository map

```text
pets/phoebe-chupi/  Installable manifest and WebP
art/canonical/     Character and pose references
art/approved/      Reviewed runtime pixel baselines
art/frames/        Exact crops of the current atlas
art/archive/       Production images
art/repair/        Repair sources and comparison boards
art/releases/      Historical release snapshots
previews/          Animations, contact sheets, and stills
scripts/           Validation, previews, installation, and packaging
tests/             Artwork and outline regression tests
docs/              Guides and review reports
```

v1.0.2 changes twelve look drawings and keeps the first nine animation rows unchanged from v1.0.1. The reviewed PNG baseline is [art/approved/v1.0.2/spritesheet.png](../art/approved/v1.0.2/spritesheet.png), recorded in [art/approved-runtime.json](../art/approved-runtime.json). The previous release remains in [art/releases/v1.0.1](../art/releases/v1.0.1).

English guides use `.md`; their Chinese editions use `.zh-CN.md`. Gallery pages and the short rights notices present both languages together.
