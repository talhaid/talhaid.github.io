"""talhaid.tech ikon seti: Inter SemiBold 't', site renkleriyle.

Proje kokunden calistir:  python src/icons/make-icons.py
Gerekli:  pip install fonttools brotli pillow
Tek kaynak -> favicon.svg + favicon.ico + icon-192/512 + apple-touch-icon."""
import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.misc.transform import Transform
from PIL import Image, ImageDraw, ImageFont

FONT   = "assets/fonts/inter-latin.woff2"
OUT    = "assets/img"
WGHT   = 600            # SemiBold: 16px'te Regular'dan belirgin okunur
BG     = "#0d0d0d"      # body bg-[#0d0d0d]
FG     = "#d4d4d4"      # text-neutral-300
RADIUS = 0.22           # kutu kenarina oran
LETTER = 0.56           # harf yuksekligi / kutu

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_build")
os.makedirs(SP, exist_ok=True)

def instance(wght=None):
    f = TTFont(FONT)
    instancer.instantiateVariableFont(f, {"wght": wght or WGHT}, inplace=True)
    return f

f = instance()
gs = f.getGlyphSet()
bp = BoundsPen(gs); gs["t"].draw(bp)
xmin, ymin, xmax, ymax = bp.bounds
gw, gh = xmax - xmin, ymax - ymin

def place(box):
    """Glyph'i box x box kutusunda ortalayan olcek + oteleme."""
    h = box * LETTER
    s = h / gh
    w = gw * s
    tx = (box - w) / 2 - s * xmin
    ty = (box - h) / 2 + s * ymax      # SVG y-asagi icin flip dahil
    return s, tx, ty

# ---------- SVG ----------
BOX = 512
s, tx, ty = place(BOX)
pen = SVGPathPen(gs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
gs["t"].draw(TransformPen(pen, Transform(s, 0, 0, -s, tx, ty)))
d = pen.getCommands()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BOX} {BOX}" role="img" aria-label="talhaid">
  <rect width="{BOX}" height="{BOX}" rx="{round(BOX*RADIUS)}" fill="{BG}"/>
  <path fill="{FG}" d="{d}"/>
</svg>
'''
open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8").write(svg)
print("favicon.svg", len(svg), "bytes")

# ---------- raster ----------
_ttf_cache = {}
def ttf_for(wght):
    """Verilen agirlikta ornekleme -> gecici TTF (Pillow variable font istemez)."""
    if wght not in _ttf_cache:
        fi = instance(wght)
        path = os.path.join(SP, f"inter-{wght}.ttf")
        fi.save(path)
        _ttf_cache[wght] = path
    return _ttf_cache[wght]

SS = 4  # supersampling

def render(box, rounded=True, wght=WGHT, letter=LETTER):
    B = box * SS
    img = Image.new("RGBA", (B, B), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    if rounded:
        dr.rounded_rectangle([0, 0, B-1, B-1], radius=B*RADIUS, fill=BG)
    else:
        dr.rectangle([0, 0, B-1, B-1], fill=BG)   # apple-touch: iOS kendi maskeler

    target_h = B * letter
    size = int(round(target_h * f["head"].unitsPerEm / gh))
    font = ImageFont.truetype(ttf_for(wght), size)
    # harfi ayri maskede cizip olcerek tam ortala
    m = Image.new("L", (B*2, B*2), 0)
    ImageDraw.Draw(m).text((B//2, B//2), "t", font=font, fill=255)
    bb = m.getbbox()
    glyph = m.crop(bb)
    gx = (B - glyph.width) // 2
    gy = (B - glyph.height) // 2
    layer = Image.new("L", (B, B), 0)
    layer.paste(glyph, (gx, gy))
    img.paste(Image.new("RGBA", (B, B), FG), (0, 0), layer)
    return img.resize((box, box), Image.LANCZOS)

render(512).save(os.path.join(OUT, "icon-512.png"))
render(192).save(os.path.join(OUT, "icon-192.png"))
# apple-touch: kosesiz + opak, iOS kendi maskesini uygular
render(180, rounded=False).convert("RGB").save(os.path.join(OUT, "apple-touch-icon.png"))

# ICO: kucuk boyutlarda optik duzeltme - daha kalin ve biraz buyuk harf
ico_frames = [
    render(16, wght=700, letter=0.62),
    render(32, wght=700, letter=0.60),
    render(48, wght=650, letter=0.58),
    render(64),
]
# sizes tum kareleri saymali; append_images o boyutlarin olcekli halini degistirir
ico_frames[-1].save(os.path.join(OUT, "favicon.ico"), format="ICO",
                    sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
                    append_images=ico_frames[:-1])
for n in ("favicon.svg", "favicon.ico", "icon-192.png", "icon-512.png", "apple-touch-icon.png"):
    print(f"  {n:24} {os.path.getsize(os.path.join(OUT, n)):>7} B")
