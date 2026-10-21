"""Replace Capacitor's default splash images with Tidy Day's logo on the app background."""
import glob, sys
from PIL import Image

logo = Image.open(sys.argv[2]).convert("RGBA")
for path in glob.glob(f"{sys.argv[1]}/**/splash.png", recursive=True):
    w, h = Image.open(path).size
    img = Image.new("RGBA", (w, h), (245, 247, 250, 255))
    s = int(min(w, h) * 0.32)
    img.alpha_composite(logo.resize((s, s), Image.LANCZOS), ((w - s) // 2, (h - s) // 2))
    img.convert("RGB").save(path)
    print("splash", path, w, h)
