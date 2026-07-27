"""
Generates placeholder images so the site layout can be previewed before
Sharley's real photos are dropped in. Run once now; delete /images/*.jpg
and replace with real photos later (see README.md for exact filenames).
"""
from PIL import Image, ImageDraw, ImageFont
import os
import random

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUT_DIR, exist_ok=True)

INK = (14, 14, 12)
CHARCOAL = (26, 26, 23)
AMBER = (221, 154, 60)
PAPER = (247, 244, 238)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def gradient(size, c1, c2, direction="diag"):
    w, h = size
    img = Image.new("RGB", size, c1)
    px = img.load()
    for y in range(h):
        for x in range(w):
            if direction == "diag":
                t = (x / w + y / h) / 2
            elif direction == "vert":
                t = y / h
            else:
                t = x / w
            px[x, y] = lerp(c1, c2, t)
    return img

def label(img, big_text, small_text):
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    try:
        f_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(h * 0.055))
        f_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(h * 0.022))
    except Exception:
        f_big = ImageFont.load_default()
        f_small = ImageFont.load_default()
    # subtle vignette
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([0, h - int(h * 0.22), w, h], fill=(0, 0, 0, 120))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"), (0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((int(w * 0.05), h - int(h * 0.16)), big_text, font=f_big, fill=PAPER)
    draw.text((int(w * 0.05), h - int(h * 0.08)), small_text, font=f_small, fill=AMBER)
    return img

shots = [
    ("01-lifestyle", "LIFESTYLE", (900, 1125)),
    ("02-lifestyle", "LIFESTYLE", (1200, 900)),
    ("03-lifestyle", "LIFESTYLE", (900, 1125)),
    ("04-family", "FAMILY", (1200, 900)),
    ("05-family", "FAMILY", (900, 1125)),
    ("06-family", "FAMILY", (900, 900)),
    ("07-portrait", "PORTRAIT", (900, 1125)),
    ("08-portrait", "PORTRAIT", (1200, 900)),
    ("09-portrait", "PORTRAIT", (900, 1125)),
]

random.seed(7)
for name, cat, size in shots:
    c2 = AMBER if random.random() > 0.6 else CHARCOAL
    img = gradient(size, INK, c2, direction=random.choice(["diag", "vert", "horiz"]))
    label(img, "PLACEHOLDER", f"{cat} — REPLACE ME")
    img.save(os.path.join(OUT_DIR, f"{name}.jpg"), quality=85)

# Hero (wide) and About portrait placeholder
hero = gradient((1920, 1080), INK, CHARCOAL, "vert")
label(hero, "PLACEHOLDER", "HERO IMAGE — REPLACE ME")
hero.save(os.path.join(OUT_DIR, "hero.jpg"), quality=85)

about = gradient((900, 1125), CHARCOAL, INK, "diag")
label(about, "PLACEHOLDER", "SHARLEY — REPLACE ME")
about.save(os.path.join(OUT_DIR, "about.jpg"), quality=85)

print("Generated", len(shots) + 2, "placeholder images in", OUT_DIR)
