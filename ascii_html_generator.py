import pyfiglet
import random
import colorsys

def escape_html(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&#39;"))

def hsv_to_rgb_css(h: float, s: float, v: float) -> str:
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f"rgb({int(r*255)},{int(g*255)},{int(b*255)})"

def ascii_to_colored_html(ascii_art: str, hue_start: float = 0.0, hue_step: float = 0.005) -> str:
    hue = hue_start
    out_lines = []
    for line in ascii_art.splitlines():
        out = []
        for ch in line:
            hue = (hue + hue_step) % 1.0
            color = hsv_to_rgb_css(hue, 1.0, 1.0)
            out.append(f'<span style="color:{color}">{escape_html(ch)}</span>')
        out_lines.append("".join(out))
    return "<pre style=\"font-family:Consolas,monospace; line-height:1; white-space:pre;\">" + "\n".join(out_lines) + "</pre>"

def main():
    print("=== ASCII → HTML Generator ===")
    text = input("Text: ").strip()
    font = input("Font (Enter=standard): ").strip() or "standard"

    try:
        art = pyfiglet.figlet_format(text, font=font, width=200)
    except Exception:
        print("Font nicht gefunden -> nehme standard.")
        art = pyfiglet.figlet_format(text, font="standard", width=200)

    # random start hue für jedes Artwork
    hue_start = random.random()
    html = ascii_to_colored_html(art, hue_start=hue_start, hue_step=0.006)

    print("\n--- HTML SNIPPET (kopieren) ---\n")
    print(html)

    save = input("\nAls Datei speichern? (j/n): ").lower().strip()
    if save == "j":
        with open("ascii_snippet.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ Gespeichert: ascii_snippet.html")

if __name__ == "__main__":
    main()
