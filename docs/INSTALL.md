# Install and update

**English** · [简体中文](INSTALL.zh-CN.md) · [Documentation](README.md)

Use a desktop app with custom v2 pets enabled. The current pet package is **v1.0.2**.

## Install locally

1. Download [phoebe-chupi-v1.0.2.zip](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/releases/download/v1.0.2/phoebe-chupi-v1.0.2.zip).
2. Extract the `phoebe-chupi` folder into `~/.codex/pets/` on macOS or `%USERPROFILE%\.codex\pets\` on Windows. If you set `CODEX_HOME`, use its `pets` subdirectory.
3. In **Settings → Pets** or **Mini & Pets**, refresh the list and select **Phoebe Chupi · Coding Companion**.

Check the resulting structure:

```text
<Codex home>/pets/phoebe-chupi/
├── pet.json
└── spritesheet.webp
```

With a complete repository checkout, you can also run:

```sh
python3 scripts/install.py --local
```

On Windows, use `py` in place of `python3`. To choose a directory, add `--pets-dir PATH`. The helper copies the two files and preserves any different existing installation.

## Use native import

From a complete repository checkout, run:

```sh
python3 scripts/install.py
```

Complete the import in the app and choose the pet. To copy the link instead of opening it, run `python3 scripts/install.py --print-url`.

The helper uses the [official pet-install URI](https://learn.chatgpt.com/docs/reference/commands#pets): an HTTPS image URL, the pet name and description, and `spriteVersionNumber=2`. The image URL is pinned to the release named in `VERSION`.

## Update an existing installation

For a local pet, back up its folder outside `pets`, then replace **only `spritesheet.webp`** with the new file. Keep the existing `pet.json` to preserve its name and identity. Refresh the pet list after the replacement.

For a cloud-imported pet, update the image on the existing entry through the app's supported update flow. Creating another entry gives it a separate identity.

v1.0.2 changes the look poses. All 57 standard frames, including blinking, retain the exact v1.0.1 RGBA pixels.

## Compatibility

| Surface | Support |
| --- | --- |
| macOS desktop | v1.0.1 installation and visual behavior verified. v1.0.2 checked in a native-size browser preview. |
| Codex Dot | Sixteen head poses support cursor-following gaze. v1.0.2 has not been checked in native Dot. |
| Windows desktop | v2 package and import helper provided; visual verification pending. |
| Image import or upload | Use an app with custom v2 pet support and follow its import flow. See the [official guide](https://learn.chatgpt.com/docs/pets) for app controls. |

Local desktop files and cloud uploads are separate installations. Menu names and feature availability can vary by app build. This package does not include an IDE-extension pet integration.

The look animation uses sixteen discrete drawings. Some pose steps remain visible, particularly `225 → 247.5` and `270 → 292.5`. See the [review scope and limitations](REVIEW.md#known-limitations).

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Pet does not appear in the list | Refresh the list. Confirm that the two files are directly inside `pets/phoebe-chupi/`, without an extra nested folder. |
| Preview is blank | Check the download against `SHA256SUMS.txt` in the release and confirm `spriteVersionNumber: 2` in the manifest. |
| Floating pet still shows the previous character | Select Phoebe, then hide and show the floating pet. If the renderer remains stale, save your work and restart the app when convenient. |
| Pet holds a still pose | Check the operating system's reduced-motion setting and the app's current activity state. Blink poses include partly closed and closed eyes. |
| Head turns use the wrong frames | Keep the full 1536 × 2288 sheet and the v2 version field. The final two rows contain the look poses. |
| Local helper refuses to overwrite a folder | Back up that installation and follow the update steps above. |
| Enlarged artwork looks soft | Inspect at the native 192 × 208 cell size. Screenshot scaling and preview GIF palettes can change the appearance. |

For an unresolved display issue, [open an issue](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues) with the app version, operating system, installation method, and an image showing the affected frame.
