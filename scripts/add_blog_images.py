#!/usr/bin/env python3
"""Insert project images into blog post HTML files."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, "blog")

ALT = "Sunset Home Painting project in St. Augustine, Florida"
ALT_BEFORE = "Before house painting project in St. Johns County"
ALT_AFTER = "After house painting project in St. Johns County"
ALT_EXTERIOR = "Exterior house painting in Northeast Florida"


def fig(src, alt=ALT):
    return f"""        <figure class="blog-figure">
          <img src="../images/{src}" alt="{alt}" width="1200" height="800" loading="lazy">
        </figure>"""


def before_after(before, after, alt_b=ALT_BEFORE, alt_a=ALT_AFTER):
    return f"""        <motion class="blog-before-after" role="group" aria-label="Before and after painting comparison">
          <figure>
            <img src="../images/{before}" alt="{alt_b}" width="600" height="800" loading="lazy">
            <figcaption>Before</figcaption>
          </figure>
          <figure>
            <img src="../images/{after}" alt="{alt_a}" width="600" height="800" loading="lazy">
            <figcaption>After</figcaption>
          </figure>
        </motion>""".replace("<motion", "<div").replace("</motion>", "</div>")


# Each post: HTML block inserted before the CTA banner (uses every project image 1–19).
POST_IMAGES = {
    "painting-st-augustine-fl-guide.html": "\n".join([
        fig("2.jpeg", "Professional painting in St. Augustine, FL"),
        fig("1.jpeg"),
        before_after("16.jpg", "17.jpg"),
    ]),
    "interior-painting-st-augustine-tips.html": "\n".join([
        before_after("9.jpeg", "10.jpeg"),
        fig("3.jpeg", "Interior painting finish in a St. Augustine home"),
    ]),
    "exterior-painting-st-augustine-coastal-homes.html": "\n".join([
        before_after("13.jpeg", "14.jpeg", ALT_EXTERIOR, ALT_AFTER),
        before_after("18.jpeg", "19.jpeg", ALT_EXTERIOR, ALT_AFTER),
    ]),
    "house-painters-st-augustine-how-to-choose.html": "\n".join([
        fig("4.jpeg"),
        fig("5.jpg", "House painting work in Northeast Florida"),
    ]),
    "painting-jacksonville-fl-services.html": "\n".join([
        fig("6.jpeg", "Painting project in the Jacksonville area"),
        fig("7.jpeg", "Residential painting in Northeast Florida"),
    ]),
    "palm-coast-painting-contractors.html": "\n".join([
        fig("8.jpeg", "Exterior painting in Palm Coast and coastal Florida"),
    ]),
    "ponte-vedra-house-painting.html": "\n".join([
        fig("15.jpeg", "House painting in Ponte Vedra and coastal communities"),
    ]),
    "fleming-island-painters.html": "\n".join([
        fig("5.jpg", "House painting in Fleming Island and Orange Park"),
        fig("8.jpeg"),
    ]),
    "local-painting-company-st-augustine.html": "\n".join([
        fig("2.jpeg", "Local painters serving Saint Augustine, FL"),
    ]),
    "residential-painting-st-augustine-fl.html": "\n".join([
        before_after("11.jpeg", "12.jpeg"),
        fig("10.jpeg", "Fresh interior paint in a St. Augustine home"),
    ]),
    "commercial-painting-st-augustine.html": "\n".join([
        fig("4.jpeg", "Professional painting for St. Augustine properties"),
    ]),
    "painting-service-st-augustine-estimates.html": "\n".join([
        fig("6.jpeg"),
        fig("1.jpeg", "Sunset Home Painting crew at work in St. Johns County"),
    ]),
    "best-exterior-house-painting-florida-coast.html": "\n".join([
        fig("18.jpeg", ALT_EXTERIOR),
        fig("19.jpeg", "Completed exterior repaint on the Florida coast"),
    ]),
    "eco-friendly-painting-st-augustine.html": "\n".join([
        fig("9.jpeg", "Interior room ready for low-VOC painting in St. Augustine"),
    ]),
    "free-painting-estimate-northeast-florida.html": "\n".join([
        fig("2.jpeg"),
        before_after("13.jpeg", "14.jpeg"),
        fig("7.jpeg"),
    ]),
}


def main():
    marker = '      <div class="cta-banner">'
    for filename, block in POST_IMAGES.items():
        path = os.path.join(BLOG, filename)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        if "blog-figure" in content or "blog-before-after" in content:
            print(f"skip (already has images): {filename}")
            continue
        if marker not in content:
            print(f"warn: no CTA marker in {filename}")
            continue
        content = content.replace(marker, block + "\n" + marker, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"updated: {filename}")


if __name__ == "__main__":
    main()
