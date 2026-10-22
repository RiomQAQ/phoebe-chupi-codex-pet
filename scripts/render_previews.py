#!/usr/bin/env python3
"""Render public previews and exact cell crops from the shipped atlas (Pillow only)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mp4", action="store_true", help="Also render all-states.mp4; requires ffmpeg")
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    frames_dir = ROOT / "art/frames"
    with Image.open(ROOT / "pets/phoebe-chupi/spritesheet.webp") as im:
        atlas = im.convert("RGBA")
    contact = Image.new("RGB", (192 * 8, 240 * 9), "#f5f6fa")
    dark_contact = Image.new("RGB", contact.size, "#17191f")
    dark_dir = OUT / "dark"
    dark_dir.mkdir(exist_ok=True)
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
            dark_contact.paste(canvas(cell, f'{spec["label"]} {col + 1}/{spec["count"]}', dark=True), (col * 192, row * 240))
            all_frames.append(labeled)
        preview = [canvas(c, spec["label"]) for c in cells[state]]
        gif(preview, spec["preview_ms"], OUT / f"{state}.gif")
        gif([canvas(c, spec["label"], dark=True) for c in cells[state]], spec["preview_ms"], dark_dir / f"{state}.gif")
        all_times.extend(spec["preview_ms"])
    contact.save(OUT / "contact-sheet.png")
    dark_contact.save(OUT / "contact-sheet-dark.png")
    gif(all_frames, all_times, OUT / "all-states.gif")
    if args.mp4:
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            parser.error("ffmpeg is required for --mp4")
        command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo",
                   "-pix_fmt", "rgb24", "-s:v", "192x240", "-r", "100", "-i", "pipe:0",
                   "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                   "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUT / "all-states.mp4")]
        with subprocess.Popen(command, stdin=subprocess.PIPE) as process:
            for frame, duration in zip(all_frames, all_times):
                for _ in range(duration // 10):
                    process.stdin.write(frame.tobytes())
            process.stdin.close()
            if process.wait():
                raise RuntimeError("ffmpeg failed")
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
    stills = OUT / "stills"
    stills.mkdir(exist_ok=True)
    five_states = Image.new("RGB", (192 * 5, 240))
    for position, (state, index) in enumerate([("idle", 0), ("running-right", 3), ("running", 2), ("jumping", 2), ("review", 3)]):
        still = canvas(cells[state][index], f"{state} / {index + 1}")
        still.save(stills / f"{state}-{index:02}.png")
        five_states.paste(still, (position * 192, 0))
    five_states.save(stills / "five-states.png")
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
