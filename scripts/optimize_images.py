"""
Resize + compress real photos for the web before dropping them into /images.

Usage:
    python3 scripts/optimize_images.py path/to/raw_photos_folder

It reads every .jpg/.jpeg/.png in the given folder, resizes the long edge
down to 2000px (plenty sharp for web, much smaller file size), and saves
web-optimized copies into /images/optimized/ — keeping the original
filenames so you can then rename/move them into place.

Requires: pip install Pillow --break-system-packages
"""
import os
import sys
from PIL import Image, ImageOps

MAX_LONG_EDGE = 2000
JPEG_QUALITY = 82

def optimize(src_folder):
    out_folder = os.path.join(os.path.dirname(__file__), "..", "images", "optimized")
    os.makedirs(out_folder, exist_ok=True)

    valid_ext = (".jpg", ".jpeg", ".png")
    files = [f for f in os.listdir(src_folder) if f.lower().endswith(valid_ext)]

    if not files:
        print(f"No images found in {src_folder}")
        return

    for fname in files:
        path = os.path.join(src_folder, fname)
        img = Image.open(path)
        img = ImageOps.exif_transpose(img)  # fix phone-camera rotation
        img = img.convert("RGB")

        w, h = img.size
        long_edge = max(w, h)
        if long_edge > MAX_LONG_EDGE:
            scale = MAX_LONG_EDGE / long_edge
            img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

        base = os.path.splitext(fname)[0]
        out_path = os.path.join(out_folder, f"{base}.jpg")
        img.save(out_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        print(f"Saved {out_path}  ({os.path.getsize(out_path)//1024} KB)")

    print(f"\nDone. {len(files)} images optimized into images/optimized/")
    print("Rename/move them into /images using the filenames the site expects (see README).")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/optimize_images.py path/to/raw_photos_folder")
        sys.exit(1)
    optimize(sys.argv[1])
