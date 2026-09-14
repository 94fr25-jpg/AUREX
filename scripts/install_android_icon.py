#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "aurex-icon.png"
RES = ROOT / "android" / "app" / "src" / "main" / "res"

if not SOURCE.exists():
    raise SystemExit(f"Logo no encontrado: {SOURCE}")
if not RES.exists():
    raise SystemExit(f"Android todavía no existe: {RES}")

img = Image.open(SOURCE).convert("RGBA")

# Delete every default Capacitor launcher asset.
for folder in RES.glob("mipmap-*"):
    if not folder.is_dir():
        continue
    for f in folder.glob("ic_launcher*"):
        if f.is_file() or f.is_symlink():
            f.unlink()
        elif f.is_dir():
            shutil.rmtree(f)

# Also remove adaptive icon XMLs, otherwise Android 8+ would prefer them
# over the bitmap icons and could keep showing Capacitor's foreground.
anydpi = RES / "mipmap-anydpi-v26"
if anydpi.exists():
    for f in anydpi.glob("ic_launcher*.xml"):
        f.unlink()

# Standard Android launcher bitmap sizes.
sizes = {
    "mdpi": 48,
    "hdpi": 72,
    "xhdpi": 96,
    "xxhdpi": 144,
    "xxxhdpi": 192,
}

for density, px in sizes.items():
    dest = RES / f"mipmap-{density}"
    dest.mkdir(parents=True, exist_ok=True)
    resized = img.resize((px, px), Image.Resampling.LANCZOS)
    resized.save(dest / "ic_launcher.png", "PNG")
    resized.save(dest / "ic_launcher_round.png", "PNG")

# Final verification.
required = []
for density in sizes:
    required += [
        RES / f"mipmap-{density}" / "ic_launcher.png",
        RES / f"mipmap-{density}" / "ic_launcher_round.png",
    ]

missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit("Faltan iconos Android:\n" + "\n".join(missing))

print("Iconos Aurex instalados correctamente:")
for p in required:
    print(" -", p.relative_to(ROOT))
