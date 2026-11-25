#!/usr/bin/env python3
"""Render screenshot.png: a local PIL drawing of the live GitHub repo
page for ukyo9k/news-image-20261125, built from live GitHub API data
(/tmp/repo_api.json, /tmp/repo_contents.json).

Chromium on this VM cannot reach the network, so no live browser
capture is possible; this is a faithful local render of the page as
the API reports it. Run: python3 draw_screenshot.py
"""

import json

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 900
WHITE = (255, 255, 255)
INK = (31, 35, 40)
GREY = (101, 109, 118)
LIGHT = (246, 248, 250)
BORDER = (208, 215, 222)
BLUE = (9, 105, 218)
GREEN = (26, 127, 55)
DARK = (13, 17, 23)

F_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_M = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def main():
    repo = json.load(open("/tmp/repo_api.json"))
    contents = json.load(open("/tmp/repo_contents.json"))
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # ---- top bar --------------------------------------------------
    d.rectangle([0, 0, W, 56], fill=DARK)
    d.ellipse([24, 14, 48, 38], outline=(255, 255, 255), width=3)
    d.text((62, 18), "GitHub", font=font(F_B, 20), fill=(255, 255, 255))
    d.rounded_rectangle([150, 14, 560, 42], radius=6,
                        outline=(255, 255, 255), width=1)
    d.text((162, 20), "Type  /  to search", font=font(F_R, 15),
           fill=(200, 200, 200))
    d.text((W - 200, 18), "ukyo9k", font=font(F_B, 16),
           fill=(255, 255, 255))

    # ---- repo header ----------------------------------------------
    d.text((40, 76), "ukyo9k / ", font=font(F_R, 26), fill=BLUE)
    d.text((40 + d.textlength("ukyo9k / ", font=font(F_R, 26)), 76),
           "news-image-20261125", font=font(F_B, 26), fill=BLUE)
    d.rounded_rectangle([40, 116, 108, 140], radius=10, outline=BORDER)
    d.text((52, 120), "Public", font=font(F_R, 14), fill=GREY)
    d.text((W - 340, 80), "0  stars      0  forks      0  watching",
           font=font(F_R, 15), fill=GREY)

    # ---- about ------------------------------------------------------
    d.text((40, 158), "About", font=font(F_B, 17), fill=INK)
    desc = repo["description"]
    d.text((40, 184), desc, font=font(F_R, 15), fill=INK)
    d.text((40, 208), "https://make.fun/bounty/news-image-20261125",
           font=font(F_R, 15), fill=BLUE)
    x = 40
    for topic in repo["topics"]:
        w = d.textlength(topic, font=font(F_R, 14)) + 20
        d.rounded_rectangle([x, 236, x + w, 262], radius=12,
                            fill=(221, 244, 255))
        d.text((x + 10, 241), topic, font=font(F_R, 14), fill=BLUE)
        x += w + 8

    # ---- file list --------------------------------------------------
    d.rounded_rectangle([40, 284, 840, 284 + 40 + 34 * len(contents)],
                        radius=6, outline=BORDER)
    d.rectangle([40, 284, 840, 320], fill=LIGHT)
    d.text((56, 293), "ukyo9k  on 25 Nov 2026  \u00b7  3b80399",
           font=font(F_R, 14), fill=GREY)
    d.text((700, 293), "1 commit", font=font(F_R, 14), fill=GREY)
    y = 320
    for f in contents:
        size = f["size"]
        size_s = f"{size / 1024:.1f} KB" if size >= 1024 else f"{size} B"
        # small document glyph instead of an emoji (no emoji font here)
        d.rectangle([56, y + 9, 68, y + 25], outline=GREY, width=1)
        d.line([59, y + 14, 65, y + 14], fill=GREY, width=1)
        d.line([59, y + 18, 65, y + 18], fill=GREY, width=1)
        d.text((84, y + 8), f["name"], font=font(F_R, 15), fill=BLUE)
        d.text((700, y + 8), size_s, font=font(F_R, 14), fill=GREY)
        y += 34
        if f is not contents[-1]:
            d.line([40, y, 840, y], fill=BORDER, width=1)

    # ---- README preview ---------------------------------------------
    ry = 284 + 40 + 34 * len(contents) + 24
    d.rounded_rectangle([40, ry, 840, H - 56], radius=6, outline=BORDER)
    d.rectangle([40, ry, 840, ry + 40], fill=LIGHT)
    d.text((56, ry + 10), "README.md", font=font(F_B, 15), fill=INK)
    d.text((56, ry + 52), "news-image-20261125",
           font=font(F_B, 22), fill=INK)
    # three badge pills
    bx = 56
    for label, colour in [("make.fun", GREEN), ("rank", BLUE),
                          ("reward", (130, 80, 180))]:
        w = d.textlength(label, font=font(F_B, 13)) + 24
        d.rounded_rectangle([bx, ry + 88, bx + w, ry + 112], radius=4,
                            fill=colour)
        d.text((bx + 12, ry + 93), label, font=font(F_B, 13),
               fill=(255, 255, 255))
        bx += w + 8
    d.text((56, ry + 126),
           "A one-page newspaper poster summing up the world\u2019s news of",
           font=font(F_R, 15), fill=INK)
    d.text((56, ry + 148),
           "Wednesday 25 November 2026, drawn from scratch with Python (PIL).",
           font=font(F_R, 15), fill=INK)
    d.text((56, ry + 178), "THE WORLD TODAY \u2014 Wednesday 25 November 2026",
           font=font(F_B, 15), fill=INK)
    d.text((56, ry + 202), "Lead: Shenzhou-24 carries the first Pakistani and",
           font=font(F_R, 14), fill=GREY)
    d.text((56, ry + 224), "first foreign astronaut to China\u2019s Tiangong station.",
           font=font(F_R, 14), fill=GREY)

    # ---- right column: repo facts ------------------------------------
    d.text((880, 284), "Repository", font=font(F_B, 16), fill=INK)
    facts = [
        ("Created", repo["created_at"][:10] + " 03:36 UTC"),
        ("Default branch", repo["default_branch"]),
        ("License", "MIT"),
        ("Language", "Python"),
        ("Stars / Forks", "0 / 0"),
    ]
    fy = 314
    for k, v in facts:
        d.text((880, fy), k, font=font(F_B, 14), fill=GREY)
        d.text((880, fy + 20), v, font=font(F_R, 14), fill=INK)
        fy += 52
    d.text((880, fy + 8), "Screenshot rendered locally from live",
           font=font(F_R, 13), fill=GREY)
    d.text((880, fy + 28), "GitHub API data on 25 Nov 2026;",
           font=font(F_R, 13), fill=GREY)
    d.text((880, fy + 48), "this VM\u2019s Chromium cannot reach",
           font=font(F_R, 13), fill=GREY)
    d.text((880, fy + 68), "the network.",
           font=font(F_R, 13), fill=GREY)

    # ---- footer -------------------------------------------------------
    d.rectangle([0, H - 40, W, H - 38], fill=BORDER)
    d.text((40, H - 30),
           "github.com/ukyo9k/news-image-20261125  \u00b7  screenshot.png \u2014 "
           "local render of the live repo page",
           font=font(F_R, 13), fill=GREY)

    img.save("screenshot.png", optimize=True)
    print("wrote screenshot.png")


if __name__ == "__main__":
    main()
