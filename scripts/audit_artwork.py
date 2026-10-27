#!/usr/bin/env python3
"""Verify the reviewed source and frozen standard actions against runtime RGBA."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from PIL import Image, ImageChops

from restore_outlines import audit as audit_outlines, sha

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path("art/approved-runtime.json")
RUNTIME = Path("pets/phoebe-chupi/spritesheet.webp")
ATLAS_SIZE = (1536, 2288)
STANDARD_ROWS = 9
STANDARD_FRAMES = 57
STANDARD_SHA256 = "79ce06935e3491201f7b6b1695480a49cc7bef7f17eaa5ec716e7ed56f478d4d"


def pixel_mismatches(expected, actual):
    """Count any RGBA difference, including alpha and invisible RGB."""
    difference = ImageChops.difference(expected, actual)
    mask = difference.getchannel("R")
    for channel in "GBA":
        mask = ImageChops.lighter(mask, difference.getchannel(channel))
    return expected.width * expected.height - mask.histogram()[0]


def checked_source(record, label, root, errors):
    if not isinstance(record, dict) or not isinstance(record.get("path"), str):
        errors.append(f"{label} must declare a repository-relative path and sha256")
        return None
    relative = Path(record["path"])
    path = root / relative
    if relative.is_absolute() or not path.resolve().is_relative_to(root.resolve()):
        errors.append(f"{label} path must stay inside the repository")
        return None
    if not path.is_file():
        errors.append(f"{label} file is missing: {relative.as_posix()}")
        return None
    declared = record.get("sha256")
    actual = sha(path)
    if not isinstance(declared, str) or re.fullmatch(r"[0-9a-f]{64}", declared) is None:
        errors.append(f"{label} must declare a lowercase SHA-256")
    elif actual != declared:
        errors.append(f"{label} SHA-256 mismatch: {relative.as_posix()}")
    return path, actual


def load_rgba(path, label, errors, png=False):
    try:
        with Image.open(path) as image:
            if png and image.format != "PNG":
                errors.append(f"{label} must be a PNG")
            if image.size != ATLAS_SIZE or "A" not in image.getbands() or getattr(image, "n_frames", 1) != 1:
                errors.append(f"{label} must be a single 1536 x 2288 RGBA image")
                return None
            return image.convert("RGBA")
    except (OSError, ValueError):
        errors.append(f"{label} cannot be decoded")
        return None


def audit(atlas_path=None, *, manifest_path=None, root=ROOT):
    root = Path(root)
    atlas_path = Path(atlas_path) if atlas_path is not None else root / RUNTIME
    manifest_path = Path(manifest_path) if manifest_path is not None else root / MANIFEST
    errors = []
    report = {
        "ok": False, "errors": errors, "mode": "approved_runtime", "version": None,
        "atlas_sha256": None, "atlas_bytes": None,
        "source_sha256": None, "approved_rgba_equal": False,
        "source_pixel_mismatches": None,
        "standard_source_sha256": None,
        "protected_standard_rows": STANDARD_ROWS,
        "protected_standard_frames": STANDARD_FRAMES,
        "standard_pixel_mismatches": None,
    }
    try:
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
    except OSError:
        errors.append("Release VERSION is missing")
        return report
    report["version"] = version
    if not manifest_path.exists():
        if version == "v1.0.1":
            try:
                legacy = audit_outlines(atlas_path)
            except (OSError, ValueError):
                errors.append("Legacy v1.0.1 artwork audit could not read its required files")
                return report
            return {**legacy, "mode": "legacy_v1.0.1_without_manifest"}
        errors.append("art/approved-runtime.json is required for this release")
        return report
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        errors.append("Approved artwork manifest cannot be read as JSON")
        return report
    if not isinstance(manifest, dict):
        errors.append("Approved artwork manifest must be an object")
        return report
    if manifest.get("version") != version:
        errors.append("Approved artwork version does not match VERSION")
    approved = checked_source(manifest.get("source"), "Approved source", root, errors)
    standard_record = manifest.get("standard_source")
    standard = checked_source(standard_record, "Standard source", root, errors)
    if not isinstance(standard_record, dict) or standard_record.get("rows") != STANDARD_ROWS:
        errors.append("Standard source must protect exactly the first 9 rows")
    if standard is not None and standard[1] != STANDARD_SHA256:
        errors.append("Standard source is not the frozen v1.0.1 PNG")
    if not atlas_path.is_file():
        errors.append("Runtime atlas is missing")
        return report
    report["atlas_sha256"] = sha(atlas_path)
    report["atlas_bytes"] = atlas_path.stat().st_size
    atlas = load_rgba(atlas_path, "Runtime atlas", errors)
    if approved is not None:
        path, digest = approved
        report["source"] = manifest["source"]["path"]
        report["source_sha256"] = digest
        source = load_rgba(path, "Approved source", errors, png=True)
        if source is not None and atlas is not None:
            mismatches = pixel_mismatches(source, atlas)
            report["source_pixel_mismatches"] = mismatches
            report["approved_rgba_equal"] = mismatches == 0
            if mismatches:
                errors.append(f"Runtime differs from approved source in {mismatches} RGBA pixels")
    if standard is not None:
        path, digest = standard
        report["standard_source"] = standard_record["path"]
        report["standard_source_sha256"] = digest
        baseline = load_rgba(path, "Standard source", errors, png=True)
        if baseline is not None and atlas is not None:
            box = (0, 0, ATLAS_SIZE[0], STANDARD_ROWS * 208)
            mismatches = pixel_mismatches(baseline.crop(box), atlas.crop(box))
            report["standard_pixel_mismatches"] = mismatches
            if mismatches:
                errors.append(f"Protected standard rows differ from v1.0.1 in {mismatches} RGBA pixels")
    report["ok"] = not errors
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas", type=Path, help="Runtime atlas to audit")
    parser.add_argument("--manifest", type=Path, help="Approved artwork manifest (paths stay relative to repository root)")
    parser.add_argument("--report", type=Path, help="Write the JSON audit report")
    args = parser.parse_args()
    report = audit(args.atlas, manifest_path=args.manifest)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in {"frames", "method"}}, indent=2))
    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
