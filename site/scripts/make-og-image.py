"""Render the 1200x630 social share card to site/public/og/aoi-share.png.

Colours are the site's dark-theme tokens (aoi-shell.css). Font is Helvetica Neue, the
site's own sans fallback, so the card matches the page typography without bundling a font.
Run: python3 site/scripts/make-og-image.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG, SURFACE = "#0F1216", "#171B21"
INK, MUTED = "#EAEDF1", "#98A2AF"
GOLD, ACCENT = "#D6A94E", "#C4A986"
FONT = "/System/Library/Fonts/HelveticaNeue.ttc"
REGULAR, BOLD = 0, 1

def font(size, idx=REGULAR):
    return ImageFont.truetype(FONT, size, index=idx)

def spaced(d, xy, text, f, fill, tracking):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + tracking
    return x

def wrap(d, text, f, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

d.rectangle([0, 0, W, 8], fill=GOLD)
d.rectangle([0, H - 96, W, H], fill=SURFACE)
d.line([0, H - 96, W, H - 96], fill="#2A303A", width=2)

PAD = 80
spaced(d, (PAD, 70), "AI OWNERSHIP INDEX", font(28, BOLD), GOLD, 5)

head = font(78, BOLD)
y = 150
for line in ["Who really owns", "the AI you use?"]:
    d.text((PAD, y), line, font=head, fill=INK)
    y += 94

sub = font(32)
y += 22
for line in wrap(d, "Independent, sourced ratings of open-source AI models and the providers that serve them.", sub, W - 2 * PAD - 40):
    d.text((PAD, y), line, font=sub, fill=MUTED)
    y += 46

d.text((PAD, H - 96 + 30), "ownershipindex.ai", font=font(30, BOLD), fill=ACCENT)
tag = "Provenance  |  Licence  |  Safety  |  Ownership"
d.text((W - PAD - d.textlength(tag, font=font(24)), H - 96 + 34), tag, font=font(24), fill=MUTED)

out = Path(__file__).resolve().parent.parent / "public" / "og" / "aoi-share.png"
out.parent.mkdir(parents=True, exist_ok=True)
img.save(out, optimize=True)
print(out, img.size)
