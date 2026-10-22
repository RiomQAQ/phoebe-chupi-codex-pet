#!/usr/bin/env python3
"""Re-export approved pixels without the edge averaging that damaged the ink."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "art/repair/v1.0.1/source-before-cleanup.png"
SOURCE_SHA256 = "f251ad33412857d1c02d42a506a4fdfff8b8b430ff564e28cc2c2526309aadd2"
PREVIOUS = ROOT / "art/releases/v1.0.0/spritesheet.png"
PNG = ROOT / "art/final/spritesheet.png"
WEBP = ROOT / "pets/phoebe-chupi/spritesheet.webp"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    with Image.open(path) as opened:
        return opened.convert("RGBA")


def audit(atlas_path=WEBP):
    source, previous, atlas = load(SOURCE), load(PREVIOUS), load(atlas_path)
    layout = json.loads((ROOT / "art/animation-layout.json").read_text())
    errors, frames = [], []
    if sha(SOURCE) != SOURCE_SHA256:
        errors.append("The approved pre-cleanup source changed")
    if any(im.size != (1536, 2288) for im in (source, previous, atlas)):
        errors.append("Source, previous release, and atlas must have v2 dimensions")
    alpha_equal = atlas.getchannel("A").tobytes() == previous.getchannel("A").tobytes()
    if not alpha_equal:
        errors.append("Alpha/pose registration differs from the previous release")
    if source.getchannel("A").tobytes() != previous.getchannel("A").tobytes():
        errors.append("Pre-cleanup source is not aligned to the previous release")
    for row, count in enumerate([s["count"] for s in layout["states"]] + [8, 8]):
        for col in range(count):
            label = (f'{layout["states"][row]["key"]}/{col:02}' if row < 9 else
                     "look/" + layout["look_angles"][(row - 9) * 8 + col])
            box = (col * 192, row * 208, (col + 1) * 192, (row + 1) * 208)
            src = source.crop(box)
            old = previous.crop(box)
            new = atlas.crop(box)
            restored, mismatches, protected, ink_mismatches = 0, 0, 0, 0
            for expected, before, actual in zip(src.getdata(), old.getdata(), new.getdata()):
                if expected[3] == 0:
                    continue
                if expected[:3] != before[:3]:
                    restored += 1
                if expected != actual:
                    mismatches += 1
                if expected[3] >= 180 and max(expected[:3]) <= 80:
                    protected += 1
                    if actual != expected:
                        ink_mismatches += 1
            if mismatches:
                errors.append(f"{label}: {mismatches} visible pixels differ from approved source")
            if ink_mismatches:
                errors.append(f"{label}: {ink_mismatches} protected ink pixels changed")
            frames.append({
                "frame": label, "row": row, "column": col,
                "restored_rgb_pixels": restored,
                "source_pixel_mismatches": mismatches,
                "protected_dark_ink_pixels": protected,
                "dark_ink_mismatches": ink_mismatches,
                "alpha_matches_previous": new.getchannel("A").tobytes() == old.getchannel("A").tobytes(),
            })
    return {
        "version": "v1.0.1", "ok": not errors, "errors": errors,
        "source_sha256": sha(SOURCE), "atlas_sha256": sha(atlas_path),
        "atlas_bytes": atlas_path.stat().st_size,
        "alpha_and_pose_registration_unchanged": alpha_equal,
        "reviewed_cells": len(frames),
        "restored_visible_rgb_pixels": sum(f["restored_rgb_pixels"] for f in frames),
        "source_pixel_mismatches": sum(f["source_pixel_mismatches"] for f in frames),
        "protected_dark_ink_pixels": sum(f["protected_dark_ink_pixels"] for f in frames),
        "dark_ink_mismatches": sum(f["dark_ink_mismatches"] for f in frames),
        "method": "Recover the approved pre-cleanup RGBA pixels; retain the exact previous alpha and cell placement; lossless encode without neighbor-color averaging.",
        "frames": frames,
    }


def build():
    if sha(SOURCE) != SOURCE_SHA256:
        raise ValueError("Pre-cleanup source checksum mismatch")
    source, previous = load(SOURCE), load(PREVIOUS)
    if source.size != (1536, 2288) or source.getchannel("A").tobytes() != previous.getchannel("A").tobytes():
        raise ValueError("Cannot restore from a source with changed geometry/alpha")
    # These are already approved normalized pixels, including clean transparency.
    # No drawing, recoloring, resizing, or matte averaging is needed.
    PNG.parent.mkdir(parents=True, exist_ok=True)
    source.save(PNG)
    source.save(WEBP, format="WEBP", lossless=True, quality=100, method=6, exact=True)
    if load(PNG).tobytes() != load(WEBP).tobytes():
        raise ValueError("Lossless encode did not preserve RGBA")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="Rebuild the current PNG/WebP from approved pre-cleanup pixels")
    parser.add_argument("--atlas", type=Path, default=WEBP, help="Atlas to audit (defaults to the shipped WebP)")
    parser.add_argument("--report", type=Path, help="Save the full per-frame report")
    args = parser.parse_args()
    if args.build:
        build()
    report = audit(args.atlas)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "frames"}, indent=2))
    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
