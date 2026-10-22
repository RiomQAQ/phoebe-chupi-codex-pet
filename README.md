# Phoebe Chupi · Coding Companion

**English** · [简体中文](README.zh-CN.md)

Phoebe brought her laptop, sat down, and is ready to keep you company while you code.

This is an unofficial **Phoebe Chupi / 菲比啾比** pet for **Codex and Dot—the dot in Codex**. In Dot, **she turns her head to follow your mouse**. She also blinks, types, waits for your reply, carries her laptop around, and does a little seated hop when the moment calls for it.

![Phoebe Chupi](previews/hero.png)

Made with **GPT-6-Astra**, using the built-in image generation tools for the artwork. [Credits](NOTICE.md).

**v1.0.1:** restored the dark hair outlines that the previous edge-cleanup pass had faded. The blinking, poses, and Dot head turns stay the same. [Before/after and review](docs/OUTLINE-REPAIR.md).

| Keeping you company | Busy with her laptop | Waiting for your reply |
| :---: | :---: | :---: |
| ![Idle](previews/idle.gif) | ![Working](previews/running.gif) | ![Waiting](previews/waiting.gif) |

## She follows your mouse in Dot

The sixteen look poses let her turn her head toward your cursor while her seated body and laptop stay put. This is the **v2** release, with the two extra rows of look directions included.

| Following the cursor: sixteen head poses | A small hop, then back to work |
| :---: | :---: |
| ![Head turns](previews/look-loop.gif) | ![Idle, hop, idle](previews/idle-jump-idle.gif) |

The look GIF cycles through the poses to show them all; in Dot, the mouse position chooses the direction. We kept the blinking edition because the later always-awake experiment felt less alive.

## Install

Grab **`phoebe-chupi-v1.0.1.zip`** from [Releases](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/latest) if you only want the pet. The much larger artwork ZIP is for browsing the whole making-of archive.

The installable pet is just two files:

```text
phoebe-chupi/
├── pet.json
└── spritesheet.webp
```

### Open the native import flow

From a downloaded or cloned copy of this repository:

```sh
python3 scripts/install.py
```

On Windows, use `py scripts/install.py`. The helper opens the app's pet-import flow with the release image URL and `spriteVersionNumber=2`. Finish the import in the app, then choose **Phoebe Chupi · Coding Companion**.

To copy the install link, run `python3 scripts/install.py --print-url`. It uses the [official native import format](https://learn.chatgpt.com/docs/reference/commands).

### Copy the files locally

No Python is needed for this method:

1. Download and extract the small install ZIP.
2. Put its `phoebe-chupi` folder in `~/.codex/pets/` on macOS, or `%USERPROFILE%\.codex\pets\` on Windows. With a custom `CODEX_HOME`, use its `pets` subfolder.
3. Open **Settings → Pets** or **Mini & Pets**, hit **Refresh**, and select **Phoebe Chupi · Coding Companion**. The menu name depends on your app version.

Check that the folder is not nested twice:

```text
<Codex home>/pets/phoebe-chupi/pet.json
<Codex home>/pets/phoebe-chupi/spritesheet.webp
```

Or let the local helper copy those two files:

```sh
python3 scripts/install.py --local
```

It leaves different existing files alone and never edits your app settings. Use `--local --pets-dir PATH` to choose another directory.

### Update an existing local copy

Back up your existing pet folder somewhere outside `pets`, then replace only its `spritesheet.webp` with the new one. Keep its `pet.json` so its name and identity stay the same. Refresh the pet picker afterward. If you imported a cloud pet, use the app's update flow for that existing pet.

### Where it works

- **Codex desktop pets:** the released blinking version was installed and checked on macOS.
- **Codex Dot:** supported, including mouse-following head turns through all sixteen look directions.
- **Windows desktop:** the portable v2 package and native import method are provided; a Windows visual review has not been done for this release.
- **Web upload:** the current web uploader documents a 1536 × 1872 sheet. This pet is 1536 × 2288 v2, so do not upload it as a v1 sheet. See the [official Pets guide](https://learn.chatgpt.com/docs/pets).

Use an app build with custom v2 pets enabled. This is a pet package, so there is no plugin to install.

## What she does

Most of her day is spent sitting with the same open laptop: typing, looking up at you, checking the result, or waiting patiently. When she moves, she closes it and carries it along.

| State | Frames | What you see |
| --- | ---: | --- |
| `idle` | 6 | Breathing and blinking while seated. |
| `running-right` | 8 | Carrying the closed laptop to the right. |
| `running-left` | 8 | Carrying it to the left, drawn separately to keep the accessories on the correct sides. |
| `waving` | 4 | A small one-handed greeting. |
| `jumping` | 5 | A short seated hop, laptop included. |
| `failed` | 8 | A little disappointed, asking for help, then recovering. |
| `waiting` | 6 | An expectant tilt while waiting for your reply. |
| `running` | 6 | Typing and thinking—this state means working. |
| `review` | 6 | Checking the result, then looking pleased. |
| Look extension | 16 | Turning her head toward the mouse in Dot. |

| Carry right | Carry left | Say hello |
| :---: | :---: | :---: |
| ![Right](previews/running-right.gif) | ![Left](previews/running-left.gif) | ![Wave](previews/waving.gif) |
| Check the result | Little hop | Need a hand? |
| ![Review](previews/review.gif) | ![Hop](previews/jumping.gif) | ![Help](previews/failed.gif) |

The app chooses when to play each state. GIFs are previews: their palettes have fewer colors, and their timing does not change the installed pet. The shipped WebP preserves the final PNG's RGBA pixels exactly.

## How we made her

There is more to the process than drawing a cute first frame. The [making-of](docs/MAKING-OF.md) walks through the whole job, including the attempts that did not work.

1. **Choose the right community shape.** We used the selected front/side/back reference, keeping it separate from official character art and unrelated fan styles.
2. **Keep one character across every pose.** Hat, face, hair, clip, outfit, and laptop were locked in seated and carry reference poses.
3. **Generate and edit each frame.** Extra hands, duplicate brows, changing head sizes, and broken laptop geometry were repaired against those same references.
4. **Watch the motion.** We reviewed adjacent frames, whole loops, small display sizes, and the return to the seated pose.
5. **Make and test the head turns.** Cardinal directions came first, then intermediate angles; unlabeled comparisons checked which way she actually seemed to look.
6. **Check what gets installed.** The final WebP, exact frame crops, archive hashes, and two-file install package are validated together.

The scripts handle previews, crops, file checks, and packaging. The loops still get a visual review.

### Read the full process

| Document | Inside |
| --- | --- |
| [Making of](docs/MAKING-OF.md) · [中文制作记录](docs/MAKING-OF.zh-CN.md) | References, character rules, per-frame work, repairs, assembly, review, and why we rolled back the awake experiment. |
| [Review notes](docs/REVIEW.md) | What was checked, how the direction comparisons worked, what passed, and what still needs care. |
| [v1.0.1 outline repair](docs/OUTLINE-REPAIR.md) | The export mistake, before/after crops, all-frame checks, and the reproducible repair. |
| [Prompt recipes](docs/PROMPTS.md) | Practical starting points for character, motion, repair, gaze, and review prompts. |
| [Format](docs/FORMAT.md) | Manifest, grid, row counts, angles, timing, and assembly rules. |
| [Sources](docs/SOURCES.md) | Character and community references, Bilibili motion studies, attribution, and README inspirations. |
| [All images](docs/IMAGE-GALLERY.md) | **742 different source images**, including originals, frames, samples, rejected drafts, and the rolled-back experiment. |

## What made it into this release

- **9 animation states + 16 head directions:** 73 occupied cells, with the other 15 fully transparent.
- **Native v2 geometry:** 1536 × 2288 atlas, 8 × 11 grid, 192 × 208 per cell.
- **Lossless WebP:** 1,910,162 bytes; the decoded pixels match the restored PNG.
- **Blinking stays.** Half-closed and closed eyes are part of the selected blink cycle. The awake trial is kept in the archive, outside the install folder.
- **Full image history:** 742 distinct originals, with an index mapping 1,290 working-file copies. Additional public previews and final-atlas crops are included too.

A few rough edges remain: the `045` and `067.5` looks are close, and `225 → 247.5` is a bigger step. Small native artwork also looks softer when enlarged. We have left those notes visible rather than calling the result flawless.

## Check or rebuild

For maintainers, with Python 3.10+:

```sh
python3 -m pip install -r requirements.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/render_previews.py
python3 scripts/package.py
```

CI runs the validator and outline regression tests, including a check that rejects the damaged v1.0.0 image. After changing artwork, review the loops again as well. The small ZIP contains only the manifest and WebP; the separate artwork ZIP includes the full image history. See [checksums](CHECKSUMS.sha256).

## If something looks wrong

- **Blank thumbnail:** refresh the pet picker and let it reload. Check that the image downloaded completely and the manifest says v2.
- **The floating pet still shows the previous character:** select Phoebe, then hide and show the floating pet. If the app keeps stale renderer state, restart it when convenient after saving your work.
- **Wrong rows or head directions:** keep the full v2 size and version field. Do not trim the last two rows or fit each cell independently.
- **A blink seems frozen:** check reduced-motion settings and the current app state. The blink is intentional; editing a preview GIF will not change runtime playback.
- **The local helper will not overwrite a folder:** inspect and back up that folder first. It is preserving your different local files.

## Credits and use

Phoebe is from Kuro Games' *Wuthering Waves*. Chupi is the community interpretation; the selected AI-derived turnaround is attributed to 蓝蓝铜离子. Author leads, their limits, and all reference links are listed in [Sources](docs/SOURCES.md) and [Credits](NOTICE.md).

README organization was inspired by [phoebe-codex-pet](https://github.com/sherlidian01-web/phoebe-codex-pet), [remielle-codex-pet](https://github.com/HanaAyane/remielle-codex-pet), and [awesome-codex-pet](https://github.com/legeling/awesome-codex-pet).

Original scripts and documentation use [MIT](LICENSE). Artwork and references have [separate usage terms](ASSET-USAGE.md). This is an unofficial fan project, unaffiliated with Kuro Games or OpenAI.
