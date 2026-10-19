#!/usr/bin/env python3
"""Render public previews and exact cell crops from the shipped atlas (Pillow only)."""
from __future__ import annotations

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
LAYOUT = json.loads((ROOT / "art/animation-layout.json").read_text())
OUT = ROOT / "previews"
CELL = tuple(LAYOUT["cell_size"])


def font(size):
    return ImageFont.load_default(size=size)


def canvas(cell, label, dark=False):
    result = Image.new("RGB", (192, 240), "#17191f" if dark else "#f5f6fa")
    draw = ImageDraw.Draw(result)
    if not dark:
        for y in range(0, 208, 16):
            for x in range(0, 192, 16):
                if (x // 16 + y // 16) % 2:
                    draw.rectangle((x, y, x + 15, y + 15), fill="#e4e7ee")
    result.paste(cell, (0, 0), cell)
    draw.text((8, 219), label, font=font(12), fill="#e8eaf0" if dark else "#252936")
    return result


def gif(frames, durations, path):
    strip = Image.new("RGB", (frames[0].width, frames[0].height * len(frames)))
    for i, frame in enumerate(frames):
        strip.paste(frame, (0, i * frame.height))
    palette = strip.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    converted = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    converted[0].save(path, save_all=True, append_images=converted[1:], duration=durations,
                      loop=0, disposal=2, optimize=False)


def main():
    OUT.mkdir(exist_ok=True)
    frames_dir = ROOT / "art/frames"
    with Image.open(ROOT / "pets/phoebe-chupi/spritesheet.webp") as im:
        atlas = im.convert("RGBA")
    contact = Image.new("RGB", (192 * 8, 240 * 9), "#f5f6fa")
    all_frames, all_times, cells = [], [], {}
    for row, spec in enumerate(LAYOUT["states"]):
        state = spec["key"]
        cells[state] = []
        directory = frames_dir / state
        directory.mkdir(parents=True, exist_ok=True)
        for col in range(spec["count"]):
            cell = atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
            cell.save(directory / f"{col:02}.png")
            cells[state].append(cell)
            labeled = canvas(cell, f'{spec["label"]} {col + 1}/{spec["count"]}')
            contact.paste(labeled, (col * 192, row * 240))
            all_frames.append(labeled)
        preview = [canvas(c, spec["label"]) for c in cells[state]]
        gif(preview, spec["preview_ms"], OUT / f"{state}.gif")
        all_times.extend(spec["preview_ms"])
    contact.save(OUT / "contact-sheet.png")
    gif(all_frames, all_times, OUT / "all-states.gif")
    transition, durations = [], []
    for state in ("idle", "jumping", "idle"):
        spec = next(s for s in LAYOUT["states"] if s["key"] == state)
        transition.extend(canvas(c, spec["label"]) for c in cells[state])
        durations.extend(spec["preview_ms"])
    gif(transition, durations, OUT / "idle-jump-idle.gif")
    directions, dark = [], []
    direction_sheet = Image.new("RGB", (192 * 8, 240 * 2), "#f5f6fa")
    (frames_dir / "look").mkdir(parents=True, exist_ok=True)
    for i, angle in enumerate(LAYOUT["look_angles"]):
        row, col = 9 + i // 8, i % 8
        cell = atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
        cell.save(frames_dir / "look" / f"{angle}.png")
        directions.append(canvas(cell, f"Look {angle} degrees"))
        direction_sheet.paste(directions[-1], (col * 192, i // 8 * 240))
        dark.append(canvas(cell, f"Look {angle} degrees", dark=True))
    direction_sheet.save(OUT / "directions.png")
    gif(directions, [LAYOUT["look_preview_ms"]] * 16, OUT / "look-loop.gif")
    gif(dark, [LAYOUT["look_preview_ms"]] * 16, OUT / "look-dark.gif")
    hero = Image.new("RGB", (1000, 440), "#f5f1e9")
    with Image.open(ROOT / "art/canonical/seated-master-approved.png") as im:
        character = im.convert("RGBA")
    character = character.crop(character.getchannel("A").getbbox())
    character.thumbnail((340, 360), Image.Resampling.LANCZOS)
    hero.paste(character, (50 + (340 - character.width) // 2, 40), character)
    draw = ImageDraw.Draw(hero)
    draw.text((425, 60), "PHOEBE CHUPI", font=font(43), fill="#302840")
    draw.text((427, 123), "For Codex pets + Dot", font=font(25), fill="#615a6e")
    draw.text((427, 174), "Turns her head to follow your cursor", font=font(19), fill="#615a6e")
    draw.text((427, 215), "Native v2  /  9 states  /  16 head directions", font=font(18), fill="#615a6e")
    draw.rounded_rectangle((427, 282, 901, 339), radius=16, fill="#e4dcf0")
    draw.text((446, 301), "Created with GPT-6-Astra + image generation", font=font(17), fill="#453853")
    draw.text((427, 377), "Unofficial fan creation  /  Not affiliated with Kuro Games", font=font(14), fill="#767080")
    hero.save(OUT / "hero.png")
    print("Rendered 73 exact frame crops, 9 state GIFs, transition/look previews, and contact sheets.")


if __name__ == "__main__":
    main()
