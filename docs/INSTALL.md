# Install and Update Guide

**English** · [简体中文](INSTALL.zh-CN.md) · [Documentation Index](README.md)

Phoebe Chupi uses the portable **Codex v2 custom pet format**, and the current release is **v1.0.2**. The entire package consists of just two files (`pet.json` and `spritesheet.webp`) and requires no plugins or background daemons.

![Five core states at native 192 × 208 pixel scale](../previews/stills/five-states.png)

---

## Choosing an Installation Method

Codex supports two independent ways to add a custom pet—**Local Folder Installation** and **Native URI Import**:

```text
Choose Your Setup Flow
 │
 ├─► Option A: Local Folder Install (Recommended — offline-ready & easiest to update)
 │     └─► Place phoebe-chupi/ inside ~/.codex/pets/
 │         How it works: Reads the local lossless WebP directly; update anytime by replacing spritesheet.webp
 │
 └─► Option B: Native URI Import (Official app import link)
       └─► Run python3 scripts/install.py to trigger the import URI
           How it works: Fetches the pinned Release image over HTTPS and registers an app-managed entry
```

---

## Install locally

### Method 1: Manual ZIP Extraction (Fastest)

1. Download **[phoebe-chupi-v1.0.2.zip](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/download/v1.0.2/phoebe-chupi-v1.0.2.zip)** and extract it.
2. Move the `phoebe-chupi` folder into your Codex `pets` directory:

   | Platform / Setup | Target `pets` Directory |
   | --- | --- |
   | **macOS** | `~/.codex/pets/` |
   | **Windows** | `%USERPROFILE%\.codex\pets\` |
   | **Custom `CODEX_HOME`** | `<CODEX_HOME>/pets/` |

3. Open Codex desktop **Settings → Pets** (or **Mini & Pets**), click **Refresh**, and select **Phoebe Chupi · Coding Companion**.

> **Folder Structure Check (Avoid Extra Nesting)**
>
> ```text
> ✅ Correct layout (both files live directly inside phoebe-chupi/):
> <Codex home>/pets/
> └── phoebe-chupi/
>     ├── pet.json
>     └── spritesheet.webp
>
> ❌ Common archive-extractor mistake (an extra outer folder hides the pet from discovery):
> <Codex home>/pets/
> └── phoebe-chupi-v1.0.2/
>     └── phoebe-chupi/
>         ├── pet.json
>         └── spritesheet.webp
> ```

### Method 2: One-Line CLI Copy

From a complete repository checkout, run the installation helper:

```sh
python3 scripts/install.py --local
```

- **Windows**: Replace `python3` with `py` (`py scripts/install.py --local`).
- **Custom destination**: Pass `--pets-dir PATH`.
- **Overwrite protection**: The script copies only `pet.json` and `spritesheet.webp` and refuses to overwrite an existing installation if its files differ, keeping any local customizations safe.

---

## Use native import

To import Phoebe through the [official Codex pet-install URI](https://learn.chatgpt.com/docs/reference/commands#pets), run from a repository checkout:

```sh
python3 scripts/install.py
```

The script builds and opens the official import URI pinned to the release tag in `VERSION` (`v1.0.2`). Confirm the import prompt inside Codex and select the pet.

- **Print the URI without opening it**:
  ```sh
  python3 scripts/install.py --print-url
  ```
- **URI parameters**: The generated link passes the pinned HTTPS release image URL, the display name (`Phoebe Chupi · Coding Companion`), the description, and `spriteVersionNumber=2`.

---

## Update an existing installation

When upgrading from an earlier release (`v1.0.0` or `v1.0.1`) to `v1.0.2`, follow the flow below so your pet's identity and selection state stay intact:

```text
In-Place Local Upgrade (Preserves Pet Identity)
  1. Back up your existing ~/.codex/pets/phoebe-chupi/ folder OUTSIDE the pets/ directory
     (Leaving a backup folder inside pets/ will register a duplicate pet entry!)
  2. Replace ONLY spritesheet.webp inside ~/.codex/pets/phoebe-chupi/
  3. Keep the existing pet.json untouched ──► Refresh the pet list in Codex Settings
```

- **Local folder installations**: Back up the folder outside `pets/`, then replace **only `spritesheet.webp`**. Keeping your original `pet.json` preserves the pet's local identity.
- **Cloud / URI-imported pets**: Update the image on the existing entry through the app's supported update flow rather than creating a brand-new entry (which would assign a separate identity).
- **What changed in v1.0.2**: `v1.0.2` updates 12 head-turn poses in rows 9–10. All 57 standard animation frames across rows 0–8 (including blinking) retain the exact `v1.0.1` RGBA pixels byte for byte.

---

## Compatibility

| Surface | Support & Verification Status |
| --- | --- |
| **macOS desktop** | **Supported**. `v1.0.2` local installation and app image readback verified byte-for-byte against the distributed WebP (see [Installation Verification Record](look-repair-qa/installation-verification.json)). |
| **Codex Dot** | **16 cursor-following head poses**. Selects gaze poses in `22.5°` clockwise increments (`v1.0.1` verified in native Dot; `v1.0.2` checked via native 1× browser stepping, with native Dot check pending). |
| **Windows desktop** | **Portable v2 package & helper provided**. Uses the exact same two-file layout; native Windows visual capture is pending. |
| **Image import or upload** | Supported on app builds with custom v2 pet support; see the [Official Pets Guide](https://learn.chatgpt.com/docs/pets) for app controls. |

- **Discrete head-turn steps**: Because Dot selects from sixteen discrete drawings rather than continuous 3D interpolation, wider transitions—especially `225° → 247.5°` and `270° → 292.5°`—remain visible as discrete pose steps. See [Review Scope & Known Limitations](REVIEW.md#known-limitations).
- **Native 1× scale vs zoomed inspection**: Each cell is designed for **192 × 208 px** native playback:

![Native 1× scale vs enlarged diagnostic view](../art/samples/native-size-comparison.png)

---

## Troubleshooting

| Symptom | What to Check & How to Fix It |
| --- | --- |
| **Pet does not appear in the list** | 1. Click **Refresh** in the Pets settings panel;<br>2. Confirm that `pet.json` and `spritesheet.webp` sit directly inside `pets/phoebe-chupi/` without an extra wrapper folder. |
| **Preview box is blank** | 1. Verify your download against `SHA256SUMS.txt` (or `CHECKSUMS.sha256` in the repo root);<br>2. Confirm your app version supports `spriteVersionNumber: 2`. |
| **Floating pet still shows the previous character** | Select Phoebe, then hide and re-show the floating pet window. If the renderer cache stays stale, save your work and restart the Codex app when convenient. |
| **Pet stays frozen on a single frame** | 1. Check whether your OS has **Reduce Motion** enabled;<br>2. Note that Phoebe's 6.6-second idle cycle includes half-closed and closed blink frames, which may be held when animations are paused. |
| **Head turns show the wrong frames in Dot** | Keep the full **1536 × 2288** (8 × 11) sheet intact and `spriteVersionNumber: 2` in `pet.json`—Dot reads rows 9 and 10 for the 16 gaze directions. |
| **`install.py --local` refuses to overwrite** | Back up your existing `pets/phoebe-chupi/` folder outside `pets/`, then replace `spritesheet.webp` as shown in the upgrade section above. |
| **Enlarged screenshots or GIFs look soft** | Inspect at the native **192 × 208** cell size using the lossless WebP or PNG crops. Browser zoom interpolation and 256-color GIF quantization both soften fine line work. |

Still running into display issues? Please [open an issue](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues) with your Codex app build number, OS version, installation method, and a screenshot of the affected frame.
