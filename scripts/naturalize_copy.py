#!/usr/bin/env python3
"""Rewrite keyword-stuffed visible copy into natural sentences across the site."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FOOTER_OLD = [
    "Interior and exterior painting in Saint Augustine, FL 32084. Serving Jacksonville, Palm Coast, Ponte Vedra, and Fleming Island.",
    "Interior and exterior painting in Saint Augustine, FL 32084. Jacksonville, Palm Coast, Ponte Vedra, Fleming Island.",
]
FOOTER_NEW = (
    "We provide interior and exterior painting from Saint Augustine, FL 32084, "
    "and serve homeowners throughout Northeast Florida."
)

CTA_H3_OLD = "Ready for professional painting in Northeast Florida?"
CTA_H3_NEW = "Ready to get started?"

CTA_P_OLD = (
    "Sunset Home Painting offers free estimates for interior and exterior projects "
    "in Saint Augustine, Jacksonville, and nearby communities."
)
CTA_P_NEW = (
    "Sunset Home Painting offers free estimates for interior and exterior work "
    "in Saint Augustine, Jacksonville, and nearby communities."
)

BLOG_POSTS = {
    "painting-st-augustine-fl-guide.html": [
        "If you are planning a paint project in St. Augustine, it helps to work with a crew that understands historic homes, coastal humidity, and how weather differs from the beaches to downtown. Sunset Home Painting is a family-owned company based in Saint Augustine, FL 32084, and we focus on interior and exterior finishes built to last in Northeast Florida.",
        "Whether you need a full exterior repaint, fresh interior walls, or cabinet refinishing, local experience matters. Salt air, intense sun, and summer storms all affect how paint adheres and how long a finish will hold up. We use quality coatings and thorough prep so your investment pays off for years.",
        'Our <a href="../interior-painting-st-augustine.html">interior painting services</a> include walls, ceilings, trim, and more, with low-VOC options when you prefer them. For curb appeal and protection, see how we approach <a href="../exterior-painting-st-augustine.html">exterior painting</a>—from power washing through the final walkthrough.',
        'We serve Saint Augustine, St. Augustine Beach, and surrounding communities. When you are ready to talk, <a href="../schedule-appointment.html">schedule a free estimate</a> or call <a href="tel:3864053015">(386) 405-3015</a>.',
    ],
    "interior-painting-st-augustine-tips.html": [
        "Most interior paint jobs are won or lost in the prep stage. Furniture protection, hole repair, sanding, and primer choice all determine how smooth the walls look and how well the paint holds up in Florida humidity.",
        "Sunset Home Painting follows a clear process: consultation, color guidance, surface prep, careful application, and cleanup. We use eco-friendly, low-odor paints when possible so families can return to their rooms quickly.",
        "Homeowners often ask us to refresh living rooms, bedrooms, kitchens, and accent walls in historic downtown homes and in newer neighborhoods. We match sheen to each space—matte for bedrooms and scrubbable satin for kitchens and hallways.",
        'You can review our full <a href="../interior-painting-st-augustine.html">interior painting services</a> or browse the <a href="../gallery.html">gallery</a> for recent work.',
    ],
    "exterior-painting-st-augustine-coastal-homes.html": [
        "Exterior painting in St. Augustine takes more than a ladder and a brush. Coastal UV, moisture, and salt can cause peeling quickly if surfaces are not cleaned, repaired, and primed the right way.",
        "We inspect siding, stucco, trim, and fascia; caulk gaps; and apply coatings rated for Florida exteriors. From Vilano Beach to Davis Shores, we have helped homeowners protect and beautify their properties.",
        "Choosing colors? Lighter palettes reflect heat, and crisp trim contrast can improve curb appeal in the local market. We document the scope up front so timelines and expectations stay clear.",
        'Learn more on our <a href="../exterior-painting-st-augustine.html">exterior painting page</a> or <a href="../contact.html">request a free quote</a>.',
    ],
    "house-painters-st-augustine-how-to-choose.html": [
        "When you hire house painters in St. Augustine, look beyond the lowest bid. Check reviews, confirm insurance, and ask for a written scope of work.",
        "Ask about prep, paint brands, crew size, and warranty coverage. A professional company should explain surface repairs, primer use, and how weather may affect scheduling.",
        "Sunset Home Painting is family-owned with more than 10 years serving Saint Augustine, FL 32084, Jacksonville, Palm Coast, Ponte Vedra, and Fleming Island. We provide detailed estimates and keep you updated throughout the project.",
        'Read more <a href="../about.html">about us</a> and our <a href="../faq.html">FAQs</a>, or <a href="../schedule-appointment.html">book a consultation</a>.',
    ],
    "painting-jacksonville-fl-services.html": [
        "Sunset Home Painting provides interior and exterior work across Jacksonville—from Riverside and San Marco to Mandarin, Jacksonville Beach, and the Westside. We bring the same prep standards and premium coatings we use on Saint Augustine projects.",
        "Jacksonville homes include brick, stucco, and wood siding, and each surface needs tailored prep. Our crews handle residential repaints, accent updates, and exterior refreshes with as little disruption as possible.",
        'Whether your project is in Jacksonville or Saint Augustine, you work with one accountable team, clear pricing, and a local phone number: <a href="tel:3864053015">(386) 405-3015</a>.',
        'See our <a href="../painting-jacksonville.html">Jacksonville service page</a> for more detail.',
    ],
    "palm-coast-painting-contractors.html": [
        "If you need painting in Palm Coast, Sunset Home Painting serves local communities with interior and exterior repaints, trim work, and detailed surface prep.",
        "Coastal Flagler County homes face many of the same challenges as St. Augustine—humidity, sun, and storm exposure. We specify durable exterior systems and moisture-aware interior products.",
        'We are based in Saint Augustine, FL 32084, and our crews travel to Palm Coast regularly. <a href="../service-areas.html">View all service areas</a>.',
    ],
    "ponte-vedra-house-painting.html": [
        "Painting in Ponte Vedra often means high-end finishes, careful protection of landscaping, and coordination with HOAs. Our team delivers crisp lines, quality paints, and respectful job sites.",
        "From Marsh Landing to Sawgrass, we handle full repaints, interior updates, and exterior refreshes designed for coastal conditions.",
        'Explore <a href="../services.html">all of our services</a> or schedule an estimate for your Ponte Vedra home.',
    ],
    "fleming-island-painters.html": [
        "Sunset Home Painting is a trusted choice for homeowners on Fleming Island who want reliable scheduling and quality finishes without the runaround of a large firm.",
        "We paint interiors, exteriors, and trim throughout Fleming Island and Orange Park, with free estimates and clear communication from start to finish.",
        'Reach us at <a href="mailto:sunsethomepainting@gmail.com">sunsethomepainting@gmail.com</a> or call <a href="tel:3864053015">(386) 405-3015</a>.',
    ],
    "local-painting-company-st-augustine.html": [
        "A local painting company understands neighborhood architecture, local expectations, and the best weather windows for exterior work. Sunset Home Painting is based in Saint Augustine, FL 32084—not a distant call center.",
        "We support our community with fair pricing, eco-conscious paint options when requested, and crews who treat your home with care. Reviews often mention professionalism, punctuality, and attention to detail.",
        'If you would like to work with a local team you can reach by phone, <a href="../contact.html">get in touch today</a>.',
    ],
    "residential-painting-st-augustine-fl.html": [
        "Residential painting is our core focus—whole-home repaints, single-room updates, and exterior facelifts for families across Northeast Florida.",
        "We work around your schedule, protect floors and furniture, and leave job sites clean at the end of each day. Our services include walls, ceilings, doors, trim, siding, and stucco.",
        'Many homeowners combine interior and exterior work for a cohesive look from curb to foyer. <a href="../services.html">See our residential services</a>.',
    ],
    "commercial-painting-st-augustine.html": [
        "We paint offices, retail spaces, and light commercial properties in St. Augustine, with after-hours scheduling available when needed to reduce downtime.",
        "Brand colors, durable finishes, and neat crews matter for business impressions. We document the scope in writing and work to stay on schedule.",
        "Ask us about pairing commercial exterior touch-ups with interior refresh packages.",
    ],
    "painting-service-st-augustine-estimates.html": [
        "Our estimates include consultation, surface prep, premium paint, application, cleanup, and a final walkthrough. When the scope is agreed up front, there are no surprise add-ons.",
        "We also help with touch-ups, accent walls, and seasonal maintenance for homeowners who want a long-term partner.",
        '<a href="../schedule-appointment.html">Book online</a> for a free estimate in Saint Augustine, Jacksonville, Palm Coast, Ponte Vedra, or Fleming Island.',
    ],
    "best-exterior-house-painting-florida-coast.html": [
        "Quality exterior painting on Florida's coast starts with washing, scraping failing paint, sealing wood, and choosing acrylic systems rated for your siding or masonry.",
        "In St. Augustine and nearby beach communities, regular maintenance cycles help you avoid costly repairs after bare substrate has been exposed.",
        'Sunset Home Painting specializes in <a href="../exterior-painting-st-augustine.html">exterior work in St. Augustine</a> and coastal Northeast Florida.',
    ],
    "eco-friendly-painting-st-augustine.html": [
        "Many families ask about low-VOC latex paints, low odor, and how quickly they can return to freshly painted rooms.",
        "Sunset Home Painting uses modern coatings that perform well in humidity without harsh fumes. They are a good fit for nurseries, bedrooms, and seniors' homes.",
        'Ask about environmentally conscious product lines during your <a href="../interior-painting-st-augustine.html">interior painting</a> estimate.',
    ],
    "free-painting-estimate-northeast-florida.html": [
        "We provide free estimates for projects in Saint Augustine, Jacksonville, Palm Coast, Ponte Vedra, and Fleming Island. We review scope on site or virtually, explain prep, and provide clear pricing.",
        "Whether you need interior work, exterior work, or a whole-home project, one call connects you with our team at Sunset Home Painting.",
        '<a href="../schedule-appointment.html">Schedule online</a> or call <a href="tel:3864053015">(386) 405-3015</a>.',
    ],
}

BLOG_CARD_BLURBS = {
    "painting-st-augustine-fl-guide.html": "A practical overview of planning a paint project in St. Augustine—what to expect, what to ask, and how local weather affects your home.",
    "interior-painting-st-augustine-tips.html": "How proper prep, paint choice, and sheen selection lead to a smoother interior finish in humid Florida homes.",
    "exterior-painting-st-augustine-coastal-homes.html": "Why coastal and historic homes in St. Augustine need extra prep, durable coatings, and thoughtful color choices.",
    "house-painters-st-augustine-how-to-choose.html": "What to look for in a painting contractor—insurance, written scope, reviews, and clear communication before you sign.",
    "painting-jacksonville-fl-services.html": "Interior and exterior painting across Jacksonville with the same prep standards we use in St. Augustine.",
    "palm-coast-painting-contractors.html": "Interior and exterior repaints for Palm Coast homeowners, with crews traveling from our Saint Augustine base.",
    "ponte-vedra-house-painting.html": "Careful interior and exterior work for Ponte Vedra homes, including HOA coordination and premium finishes.",
    "fleming-island-painters.html": "Reliable residential painting on Fleming Island with free estimates and clear communication.",
    "local-painting-company-st-augustine.html": "Why hiring a local, family-owned painting company in St. Augustine can mean better service and accountability.",
    "residential-painting-st-augustine-fl.html": "Whole-home repaints, room updates, and exterior refreshes for families across Northeast Florida.",
    "commercial-painting-st-augustine.html": "Light commercial painting for offices and retail spaces, with scheduling options to limit business disruption.",
    "painting-service-st-augustine-estimates.html": "What is included in our estimates—from consultation and prep through cleanup and final walkthrough.",
    "best-exterior-house-painting-florida-coast.html": "Best practices for exterior paint on Florida's coast, including prep, products, and maintenance timing.",
    "eco-friendly-painting-st-augustine.html": "Low-VOC and low-odor paint options for families who want a healthier interior refresh.",
    "free-painting-estimate-northeast-florida.html": "How to request a free estimate anywhere we serve in Northeast Florida.",
}


def apply_globals(text):
    for old in FOOTER_OLD:
        text = text.replace(old, FOOTER_NEW)
    text = text.replace(CTA_H3_OLD, CTA_H3_NEW)
    text = text.replace(CTA_P_OLD, CTA_P_NEW)
    return text


def update_blog_article(path, paras):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    paras_html = "\n".join(f"        <p>{p}</p>" for p in paras)
    html = re.sub(
        r'(<div class="content-prose">)\s*.*?\s*(<div class="cta-banner">)',
        lambda m: m.group(1) + "\n" + paras_html + "\n      " + m.group(2),
        html,
        count=1,
        flags=re.DOTALL,
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    for dirpath, _, files in os.walk(ROOT):
        if ".git" in dirpath or "scripts" in dirpath and dirpath != os.path.join(ROOT, "scripts"):
            pass
        for name in files:
            if not name.endswith(".html"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8") as f:
                html = f.read()
            html = apply_globals(html)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)

    blog_dir = os.path.join(ROOT, "blog")
    for slug, paras in BLOG_POSTS.items():
        update_blog_article(os.path.join(blog_dir, slug), paras)

    blog_index = os.path.join(blog_dir, "index.html")
    with open(blog_index, encoding="utf-8") as f:
        html = f.read()
    for slug, blurb in BLOG_CARD_BLURBS.items():
        pattern = rf'(<a href="{re.escape(slug)}">[^<]+</a></h3>\s*<p>)(.*?)(</p>)'
        html = re.sub(pattern, rf"\1{blurb}\3", html, count=1, flags=re.DOTALL)
    with open(blog_index, "w", encoding="utf-8") as f:
        f.write(html)

    print("Applied global copy updates and blog article rewrites.")


if __name__ == "__main__":
    main()
