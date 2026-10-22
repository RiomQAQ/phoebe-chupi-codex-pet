#!/usr/bin/env python3
"""Open the documented v2 pet import flow, or install the two local files."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlencode
import webbrowser

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "pets" / "phoebe-chupi"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
RAW_URL = f"https://raw.githubusercontent.com/RiomQAQ/phoebe-chupi-codex-pet/{VERSION}/pets/phoebe-chupi/spritesheet.webp"


def install_url():
    manifest = json.loads((SOURCE / "pet.json").read_text(encoding="utf-8"))
    return "codex://pets/install?" + urlencode({
        "name": manifest["displayName"], "imageUrl": RAW_URL,
        "description": manifest["description"], "spriteVersionNumber": 2,
    })


def local_install(pets_dir):
    manifest = json.loads((SOURCE / "pet.json").read_text(encoding="utf-8"))
    pet_id = manifest["id"]
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pet_id):
        raise ValueError("Unsafe pet id")
    destination = pets_dir / pet_id
    if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
        raise ValueError("Destination is not a regular directory")
    names = ("pet.json", "spritesheet.webp")
    if destination.exists():
        if all((destination / n).is_file() and not (destination / n).is_symlink()
               and (destination / n).read_bytes() == (SOURCE / n).read_bytes() for n in names):
            print("Already installed; refresh the pet picker and select Phoebe Chupi.")
            return
        raise FileExistsError("A different pet already uses this directory. Rename or back it up before installing.")
    pets_dir.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".phoebe-chupi-", dir=pets_dir))
    try:
        for name in names:
            shutil.copyfile(SOURCE / name, temporary / name)
            if hashlib.sha256((temporary / name).read_bytes()).digest() != hashlib.sha256((SOURCE / name).read_bytes()).digest():
                raise IOError("Copy verification failed")
        # Do not replace an existing pet, and never edit application settings.
        if destination.exists():
            raise FileExistsError("Destination appeared during installation")
        temporary.rename(destination)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    print("Installed:", destination)
    print("Open Settings > Pets (or Mini & Pets), refresh, and select Phoebe Chupi.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--print-url", action="store_true", help="Print the native install URI without opening the app")
    mode.add_argument("--local", action="store_true", help="Install only the portable manifest and atlas locally")
    parser.add_argument("--pets-dir", type=Path, help="Custom local pets directory (requires --local)")
    args = parser.parse_args()
    if args.pets_dir and not args.local:
        parser.error("--pets-dir requires --local")
    if args.local:
        default = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "pets"
        local_install((args.pets_dir or default).expanduser())
    elif args.print_url:
        print(install_url())
    else:
        url = install_url()
        if sys.platform == "darwin":
            subprocess.run(["open", url], check=True)
        elif sys.platform == "win32":
            os.startfile(url)
        elif not webbrowser.open(url):
            raise SystemExit("No registered handler. Use --print-url or --local.")


if __name__ == "__main__":
    main()
