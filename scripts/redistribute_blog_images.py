#!/usr/bin/env python3
"""Move blog images from end of article into body after selected paragraphs."""
import os
import re

BLOG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "blog")

# After which paragraph index (0-based) to insert each image block, in order
PLACEMENT = {
    "painting-st-augustine-fl-guide.html": [0, 1, 2],
    "interior-painting-st-augustine-tips.html": [0, 2],
    "exterior-painting-st-augustine-coastal-homes.html": [0, 2],
    "house-painters-st-augustine-how-to-choose.html": [0, 1],
    "painting-jacksonville-fl-services.html": [0, 2],
    "palm-coast-painting-contractors.html": [1],
    "ponte-vedra-house-painting.html": [0],
    "fleming-island-painters.html": [0, 1],
    "local-painting-company-st-augustine.html": [1],
    "residential-painting-st-augustine-fl.html": [0, 1],
    "commercial-painting-st-augustine.html": [1],
    "painting-service-st-augustine-estimates.html": [0, 1],
    "best-exterior-house-painting-florida-coast.html": [0, 1],
    "eco-friendly-painting-st-augustine.html": [1],
    "free-painting-estimate-northeast-florida.html": [0, 1, 2],
}

BLOCK_RE = re.compile(
    r"\s*(?:<figure class=\"blog-figure\">.*?</figure>"
    r"|<div class=\"blog-before-after\">.*?</motion>)",
    re.DOTALL,
)


def redistribute(filename, indices):
    path = os.path.join(BLOG, filename)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    prose_match = re.search(
        r'(<div class="content-prose">)(.*?)(\s*<div class="cta-banner">)',
        content,
        re.DOTALL,
    )
    if not prose_match:
        return False

    prose = prose_match.group(2)
    blocks = BLOCK_RE.findall(prose)
    if not blocks:
        return False

    prose_clean = BLOCK_RE.sub("", prose)
    paragraphs = re.findall(r"<p>.*?</p>", prose_clean, re.DOTALL)
    if len(paragraphs) < max(indices) + 1:
        return False

    for block, idx in zip(blocks, indices):
        if idx < len(paragraphs):
            paragraphs[idx] = paragraphs[idx] + block

    new_prose = "\n        ".join(paragraphs) + "\n        "

    new_content = (
        content[: prose_match.start(2)]
        + new_prose
        + content[prose_match.end(2) :]
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    for filename, indices in PLACEMENT.items():
        ok = redistribute(filename, indices)
        print(f"{'ok' if ok else 'skip'}: {filename}")


if __name__ == "__main__":
    main()
