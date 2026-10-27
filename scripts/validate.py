#!/usr/bin/env python3
"""Validate the actual distributable, all archived images, and public-file hygiene."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from PIL import Image, ImageSequence
from audit_artwork import audit as audit_artwork
from restore_outlines import audit as audit_outlines, HISTORICAL_WEBP

ROOT = Path(__file__).resolve().parents[1]
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
PRIVATE_MARKERS = [
    r"/(?:Users|home)/[A-Za-z0-9._-]+/",
    r"\b(?:pet|page|env_e|user)_[a-f0-9]{20,}\b",
    r"(?:sk-proj-|ghp_|gho_|github_pat_)[A-Za-z0-9_-]{16,}",
    r"(?:[?&](?:sig|signature|X-Amz-Signature|se|sp|sv)=)",
    r"(?:library" r"-file:|oaiusercontent" r"\.com|\." r"codex/generated_images)",
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Write a sanitized JSON report")
    args = parser.parse_args()
    errors = []
    layout = json.loads((ROOT / "art/animation-layout.json").read_text())
    manifest_path = ROOT / "pets/phoebe-chupi/pet.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected_keys = {"id", "displayName", "description", "spriteVersionNumber", "spritesheetPath"}
    if set(manifest) != expected_keys or manifest.get("spriteVersionNumber") != 2:
        errors.append("Manifest must contain the five portable v2 fields")
    if manifest.get("spritesheetPath") != "spritesheet.webp" or manifest.get("id") != "phoebe-chupi":
        errors.append("Unexpected runtime path or pet id")
    runtime = manifest_path.parent / "spritesheet.webp"
    with Image.open(runtime) as im:
        if im.size != (1536, 2288) or "A" not in im.getbands() or getattr(im, "n_frames", 1) != 1:
            errors.append("Runtime atlas must be a single 1536 x 2288 RGBA image")
        atlas = im.convert("RGBA")
    with Image.open(ROOT / "art/final/spritesheet.png") as im:
        if im.convert("RGBA").tobytes() != atlas.tobytes():
            errors.append("WebP pixels differ from the accepted PNG")
    counts = [s["count"] for s in layout["states"]] + [8, 8]
    used, empty, bounds = 0, 0, []
    for row, count in enumerate(counts):
        for col in range(8):
            cell = atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
            box = cell.getchannel("A").getbbox()
            if col >= count:
                empty += 1
                if box is not None:
                    errors.append(f"Unused cell contains pixels: {row},{col}")
                continue
            used += 1
            if box is None:
                errors.append(f"Required cell is empty: {row},{col}")
                continue
            if box[0] < 1 or box[1] < 1 or box[2] > 191 or box[3] > 207:
                errors.append(f"Visible artwork touches a cell edge: {row},{col}")
            if row < 9:
                name = layout["states"][row]["key"]
                frame = ROOT / "art/frames" / name / f"{col:02}.png"
            else:
                angle = layout["look_angles"][(row - 9) * 8 + col]
                frame = ROOT / "art/frames/look" / f"{angle}.png"
            if not frame.is_file():
                errors.append(f"Missing final crop: {frame.relative_to(ROOT)}")
            else:
                with Image.open(frame) as im:
                    if im.size != (192, 208) or im.convert("RGBA").tobytes() != cell.tobytes():
                        errors.append(f"Final crop differs from atlas: {frame.relative_to(ROOT)}")
            bounds.append({"row": row, "column": col, "alpha_bbox": list(box)})
    if (used, empty) != (73, 15):
        errors.append("Expected 73 used and 15 transparent cells")
    artwork_audit = audit_artwork(runtime)
    errors.extend(artwork_audit["errors"])
    outline_audit = audit_outlines(HISTORICAL_WEBP)
    errors.extend(f"Historical v1.0.1: {error}" for error in outline_audit["errors"])
    archive = json.loads((ROOT / "art/index.json").read_text())
    seen = set()
    for record in archive["images"]:
        p = ROOT / record["path"]
        if not p.is_file() or not p.resolve().is_relative_to(ROOT.resolve()):
            errors.append(f"Missing/unsafe archive path: {record['id']}")
            continue
        if sha(p) != record["published_sha256"]:
            errors.append(f"Archive checksum mismatch: {record['id']}")
        if record["source_sha256"] in seen:
            errors.append(f"Repeated source hash: {record['id']}")
        seen.add(record["source_sha256"])
    if len(seen) != archive["unique_source_images"]:
        errors.append("Archive count mismatch")
    scanned_images, scanned_text = 0, 0
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or any(part in {".git", ".venv", "__pycache__", "dist"} for part in p.relative_to(ROOT).parts):
            continue
        if p.is_symlink():
            errors.append(f"Public file is a symlink: {p.relative_to(ROOT)}")
        if p.stat().st_size >= 100 * 1024 * 1024:
            errors.append(f"File exceeds GitHub limit: {p.relative_to(ROOT)}")
        if p.suffix.lower() in IMAGE_SUFFIXES:
            scanned_images += 1
            try:
                with Image.open(p) as im:
                    for frame in ImageSequence.Iterator(im):
                        for key in ("exif", "xmp", "XML:com.adobe.xmp", "comment"):
                            if key in frame.info:
                                errors.append(f"Unreviewed image metadata: {p.relative_to(ROOT)} ({key})")
                        frame.load()
                with Image.open(p) as im:
                    im.verify()
            except Exception as exc:
                errors.append(f"Image decode failed: {p.relative_to(ROOT)}: {type(exc).__name__}")
        elif p.suffix.lower() in {".md", ".json", ".py", ".txt", ".html", ".yml"}:
            scanned_text += 1
            content = p.read_text(encoding="utf-8")
            for marker in PRIVATE_MARKERS:
                if re.search(marker, content):
                    errors.append(f"Private-data marker in {p.relative_to(ROOT)}")
                    break
    checksum_file = ROOT / "CHECKSUMS.sha256"
    if checksum_file.exists():
        for line in checksum_file.read_text().splitlines():
            expected, name = line.split("  ", 1)
            if sha(ROOT / name) != expected:
                errors.append(f"Distribution checksum mismatch: {name}")
    report = {
        "ok": not errors, "errors": errors,
        "runtime_sha256": sha(runtime), "runtime_bytes": runtime.stat().st_size,
        "decoded_png_webp_pixels_equal": not any("WebP pixels" in e for e in errors),
        "atlas_size": list(atlas.size), "cell_size": [192, 208],
        "used_cells": used, "transparent_unused_cells": empty,
        "approved_artwork": {k: v for k, v in artwork_audit.items() if k not in {"frames", "errors", "method"}},
        "outline_restoration": {"scope": "historical_v1.0.1_snapshot", **{k: v for k, v in outline_audit.items() if k not in {"frames", "errors", "method"}}},
        "unique_archived_source_images": len(seen),
        "image_files_checked": scanned_images, "text_files_scanned": scanned_text,
        "bounds": bounds,
        "visual_review": "See docs/REVIEW.md for the drawing and animation checks.",
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "bounds"}, indent=2))
    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
