#!/usr/bin/env python3
"""Draw the news poster for Wednesday 25 November 2026.

One-page newspaper poster, 1024x1024, drawn from scratch with PIL
primitives and DejaVu fonts. No stock photos, no copied artwork.
Every story below was verified against a real news source on the day.
Run: python3 draw_poster.py  ->  writes entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 68, 126)
GREY = (90, 86, 78)

F_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill=INK):
    draw.text((W // 2, y), text, font=fnt, fill=fill, anchor="ma")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36  # margin

    # ---- masthead -------------------------------------------------
    d.rectangle([mx, 26, W - mx, 30], fill=INK)
    draw_centered(d, 42, "THE WORLD TODAY", font(F_SERIF_B, 82))
    d.rectangle([mx, 148, W - mx, 152], fill=INK)
    draw_centered(d, 164, "WEDNESDAY  25  NOVEMBER  2026",
                  font(F_SANS_B, 40), fill=RED)
    d.rectangle([mx, 222, W - mx, 226], fill=INK)
    draw_centered(d, 236, "Seven stories from a single day \u2014 as reported around the world",
                  font(F_SERIF, 20), fill=GREY)

    # ---- lead story ----------------------------------------------
    ly0, ly1 = 276, 506
    d.rectangle([mx, ly0, W - mx, ly1], outline=INK, width=3)
    d.rectangle([mx, ly0, W - mx, ly0 + 30], fill=INK)
    d.text((mx + 14, ly0 + 4), "LEAD STORY  \u00b7  SPACE",
           font=font(F_SANS_B, 19), fill=(255, 255, 255))

    lead_head = "First foreigner flies to China\u2019s space station"
    lead_body = ("China\u2019s Shenzhou-24 blasted off at 00:18 UTC carrying "
                 "Pakistani pilot Muhammad Zeeshan Ali \u2014 the first "
                 "Pakistani in orbit, and the first foreign astronaut to "
                 "visit the Tiangong station.")
    tx, tw = mx + 16, 560
    y = ly0 + 38
    for line in wrap(d, lead_head, font(F_SERIF_B, 32), tw):
        d.text((tx, y), line, font=font(F_SERIF_B, 32), fill=INK)
        y += 38
    y += 4
    for line in wrap(d, lead_body, font(F_SERIF, 19), tw):
        d.text((tx, y), line, font=font(F_SERIF, 19), fill=INK)
        y += 26

    # illustration: Earth, stars and a rocket, right of the lead text
    cx, cy, r = 838, 392, 74
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(58, 110, 165),
              outline=INK, width=3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255),
              width=1)
    # continents (stylised blobs)
    d.ellipse([cx - 52, cy - 38, cx - 8, cy - 2], fill=(74, 140, 74))
    d.ellipse([cx - 6, cy + 6, cx + 44, cy + 46], fill=(74, 140, 74))
    d.ellipse([cx + 18, cy - 48, cx + 52, cy - 14], fill=(74, 140, 74))
    for sx, sy in [(716, 320), (962, 320), (700, 452), (958, 452),
                   (742, 300), (930, 300)]:
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=INK)
    # rocket: body, window, fins, flame
    rx, ry = 700, 330
    d.polygon([(rx, ry - 26), (rx + 12, ry - 4), (rx + 12, ry + 26),
               (rx - 12, ry + 26), (rx - 12, ry - 4)], fill=(220, 220, 220),
              outline=INK)
    d.polygon([(rx - 12, ry - 4), (rx, ry - 26), (rx + 12, ry - 4)],
              fill=RED, outline=INK)
    d.ellipse([rx - 6, ry - 2, rx + 6, ry + 10], fill=BLUE, outline=INK)
    d.polygon([(rx - 12, ry + 26), (rx - 22, ry + 40), (rx - 12, ry + 34)],
              fill=RED, outline=INK)
    d.polygon([(rx + 12, ry + 26), (rx + 22, ry + 40), (rx + 12, ry + 34)],
              fill=RED, outline=INK)
    d.polygon([(rx - 7, ry + 26), (rx + 7, ry + 26), (rx, ry + 48)],
              fill=(255, 170, 0), outline=INK)

    # ---- six more stories, 2 columns x 3 rows --------------------
    stories = [
        ("CYBERATTACK \u00b7 USA", RED,
         "CIA and US intel office hit by hack",
         "The CIA and the US intelligence chief\u2019s office were hit by "
         "an apparent cyberattack on an unclassified system. No "
         "classified data was hit; early signs point to China."),
        ("PACIFIC", BLUE,
         "Australia\u2013Solomons security pact",
         "Australia and Solomon Islands signed a security pact making "
         "Canberra the islands\u2019 defence partner of choice, replacing "
         "an earlier deal with China."),
        ("COURTS \u00b7 USA", RED,
         "Huawei guilty in US secrets trial",
         "A New York jury found Huawei guilty on 10 of 12 counts, "
         "including bank fraud and conspiracy to steal trade secrets, "
         "after a three-month trial."),
        ("MIDDLE EAST", BLUE,
         "Houthi drone hits Riyadh tower",
         "A drone struck the PIF tower in Riyadh\u2019s financial district, "
         "injuring 11 people \u2014 the second hit on the capital\u2019s "
         "tallest tower in under a week."),
        ("HEALTH \u00b7 AFRICA", RED,
         "Ebola teams evacuated after 3 days",
         "WHO staff and Congolese health workers were evacuated from a "
         "hospital in Akwe, DR Congo, after sheltering three days amid "
         "fierce fighting."),
        ("USA", BLUE,
         "Iowa braces for huge lead-azide blast",
         "The US Army will detonate 9,500 lbs of ageing lead azide at "
         "9 a.m. today in Middletown, Iowa \u2014 the largest such blast "
         "in nearly 50 years."),
    ]

    gx0, gy0 = mx, 522
    col_w = (W - 2 * mx - 24) // 2
    row_h = 146
    for i, (tag, colour, head, body) in enumerate(stories):
        col, row = i % 2, i // 2
        x = gx0 + col * (col_w + 24)
        y = gy0 + row * row_h
        if col == 1:
            d.line([gx0 + col_w + 12, y + 4, gx0 + col_w + 12,
                    y + row_h - 14], fill=(200, 192, 176), width=2)
        if row > 0:
            d.line([x, y - 10, x + col_w, y - 10], fill=(200, 192, 176),
                   width=2)
        d.text((x, y), tag, font=font(F_SANS_B, 16), fill=colour)
        y += 24
        for line in wrap(d, head, font(F_SERIF_B, 22), col_w):
            d.text((x, y), line, font=font(F_SERIF_B, 22), fill=INK)
            y += 26
        y += 2
        for line in wrap(d, body, font(F_SERIF, 17), col_w):
            d.text((x, y), line, font=font(F_SERIF, 17), fill=INK)
            y += 21

    # ---- footer ---------------------------------------------------
    fy = 970
    d.rectangle([mx, fy, W - mx, fy + 2], fill=INK)
    draw_centered(d, fy + 10,
                  "Sources: Reuters \u00b7 Xinhua \u00b7 CNN \u00b7 AP \u00b7 WHO \u00b7 "
                  "Des Moines Register \u00b7 Saudi Civil Defence",
                  font(F_SANS, 14), fill=GREY)
    draw_centered(d, fy + 30,
                  "Stories as reported on Wednesday 25 November 2026",
                  font(F_SANS, 14), fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
