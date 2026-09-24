from pathlib import Path
import re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import qrcode

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUT = ASSETS / "qr-homepage-card.png"
POSTER = ROOT / "poster.html"

W, H = 1334, 710
RED = (232, 20, 33, 255)
BLACK = (15, 18, 22, 255)
GRAY = (104, 110, 118, 255)

def find_font():
    candidates = [
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    for base in [Path("/usr/share/fonts"), Path("/usr/local/share/fonts")]:
        if base.exists():
            hits = list(base.rglob("*NotoSansCJK*Bold*")) + list(base.rglob("*DejaVuSans-Bold.ttf"))
            if hits:
                return str(hits[0])
    raise FileNotFoundError("No suitable font found")

FONT = find_font()

def f(size):
    return ImageFont.truetype(FONT, size=size)

canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# Soft shadow behind the white card.
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((14, 14, W-14, H-18), radius=44, fill=(70, 90, 110, 45))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
canvas.alpha_composite(shadow)

draw = ImageDraw.Draw(canvas)
draw.rounded_rectangle((8, 8, W-8, H-14), radius=42, fill=(255, 255, 255, 255),
                       outline=(236, 240, 243, 255), width=2)

# Subtle lower-left gray waves.
wave = Image.new("RGBA", (W, H), (0,0,0,0))
wd = ImageDraw.Draw(wave)
wd.ellipse((-250, 525, 800, 1020), fill=(236, 239, 242, 180))
wd.ellipse((-120, 575, 680, 940), fill=(246, 248, 249, 230))
canvas.alpha_composite(wave)

draw = ImageDraw.Draw(canvas)

# Red curved accent at the bottom-left.
pts = []
for i in range(110):
    t = i / 109
    x = 16 + t * 635
    y = 678 - (1-t) * 0 - 95 * (1 - (2*t-1)**2)
    pts.append((x, y))
draw.line(pts, fill=RED, width=5)

# Espressif mark from repository asset.
mark_path = ASSETS / "espressif-mark.png"
mark = Image.open(mark_path).convert("RGBA")
mark.thumbnail((125, 125), Image.Resampling.LANCZOS)
canvas.alpha_composite(mark, (58, 70))

# Wordmark.
draw = ImageDraw.Draw(canvas)
draw.text((196, 83), "ESPRESSIF", font=f(70), fill=BLACK)

# Red short divider.
draw.rounded_rectangle((66, 307, 195, 314), radius=4, fill=RED)

# Japanese callout.
draw.text((66, 340), "日本語公式サイト", font=f(60), fill=BLACK)
draw.text((66, 426), "はこちら", font=f(60), fill=BLACK)
draw.text((390, 423), "›", font=f(72), fill=RED)

# English helper line.
draw.text((68, 548), "SCAN TO VISIT ESPRESSIF HOMEPAGE", font=f(21), fill=GRAY)

# Real QR code.
url = "https://www.espressif.com/ja-jp/"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=4)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
qr_size = 430
qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.NEAREST)
qr_x, qr_y = 835, 145
canvas.alpha_composite(qr_img, (qr_x, qr_y))

# Four red scan brackets.
bx0, by0, bx1, by1 = 790, 78, 1310, 635
L = 68
BW = 8
# TL
draw.line([(bx0, by0+L), (bx0, by0+16), (bx0+16, by0), (bx0+L, by0)], fill=RED, width=BW)
# TR
draw.line([(bx1-L, by0), (bx1-16, by0), (bx1, by0+16), (bx1, by0+L)], fill=RED, width=BW)
# BL
draw.line([(bx0, by1-L), (bx0, by1-16), (bx0+16, by1), (bx0+L, by1)], fill=RED, width=BW)
# BR
draw.line([(bx1-L, by1), (bx1-16, by1), (bx1, by1-16), (bx1, by1-L)], fill=RED, width=BW)

OUT.parent.mkdir(parents=True, exist_ok=True)
canvas.convert("RGB").save(OUT, format="PNG", optimize=True, compress_level=9)

# Cache-bust the generated asset in poster.html.
text = POSTER.read_text(encoding="utf-8")
text = re.sub(r'assets/qr-homepage-card(?:-v2)?\.png(?:\?v=\d+)?',
              'assets/qr-homepage-card.png?v=8', text)
POSTER.write_text(text, encoding="utf-8")

print(f"generated {OUT} ({W}x{H})")
