#!/usr/bin/env python3
"""Build separate runtime and complete-artwork ZIP files from public repository files."""
from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def make_zip(destination, paths, prefix):
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_STORED) as archive:
        for path, relative in paths:
            info = zipfile.ZipInfo(prefix + "/" + relative, date_time=(2026, 10, 22, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def main():
    subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], cwd=ROOT, check=True)
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    runtime = ROOT / "pets/phoebe-chupi"
    pet_zip = out / f"phoebe-chupi-{VERSION}.zip"
    make_zip(pet_zip, [(runtime / name, name) for name in ("pet.json", "spritesheet.webp")], "phoebe-chupi")
    files = []
    for name in ("art", "previews", "docs", "pets", "scripts", "tests", ".github"):
        files.extend((p, p.relative_to(ROOT).as_posix()) for p in sorted((ROOT / name).rglob("*"))
                     if p.is_file() and "__pycache__" not in p.parts)
    for name in ("README.md", "README.zh-CN.md", "NOTICE.md", "ASSET-USAGE.md", "LICENSE", "LICENSE.zh-CN.md", "CHECKSUMS.sha256", "requirements.txt", "VERSION", ".gitignore", ".gitattributes"):
        files.append((ROOT / name, name))
    art_zip = out / f"phoebe-chupi-artwork-{VERSION}.zip"
    make_zip(art_zip, files, "phoebe-chupi-artwork")
    checksum = out / "SHA256SUMS.txt"
    checksum.write_text("".join(hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.name + "\n" for p in (pet_zip, art_zip)), encoding="utf-8")
    for p in (pet_zip, art_zip, checksum):
        print(p.name, p.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
