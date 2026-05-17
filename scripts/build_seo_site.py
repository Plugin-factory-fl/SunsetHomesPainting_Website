#!/usr/bin/env python3
"""Build blog posts and sitemap for sunsethomepainting.com"""
import os

SITE = "https://sunsethomepainting.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANALYTICS_HEAD = """  <script src="/js/site-config.js"></script>
  <script src="/js/analytics.js"></script>"""


def prefix(depth):
    return "../" * depth


def head_block(title, desc, path, depth=0, article=False, article_schema_extra=""):
    pre = prefix(depth)
    url = f"{SITE}/{path.lstrip('/')}"
    schema = article_schema_extra if article else SCHEMA_BUSINESS
    return f"""  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <title>{title}</title>
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="{'article' if article else 'website'}">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}/images/2.jpeg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{pre}images/Sunset Home 2.PNG" type="image/png">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  <link rel="stylesheet" href="{pre}css/style.css?v=3">
{schema}
{ANALYTICS_HEAD}"""


SCHEMA_BUSINESS = """  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HousePainter",
  "name": "Sunset Home Painting",
  "image": "https://sunsethomepainting.com/images/2.jpeg",
  "url": "https://sunsethomepainting.com",
  "telephone": "+1-386-405-3015",
  "email": "sunsethomepainting@gmail.com",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Saint Augustine",
    "addressRegion": "FL",
    "postalCode": "32084",
    "addressCountry": "US"
  },
  "areaServed": ["Saint Augustine", "St. Augustine", "Jacksonville", "Palm Coast", "Ponte Vedra", "Fleming Island"],
  "sameAs": ["https://www.facebook.com/share/19x4X4LCrX/?mibextid=wwXIfr"]
}
</script>"""


def nav_block(active, depth=0):
    pre = prefix(depth)
    items = [
        ("index.html", "Home", "home"),
        ("about.html", "About", "about"),
        ("services.html", "Services", "services"),
        ("interior-painting-st-augustine.html", "Interior", "interior"),
        ("exterior-painting-st-augustine.html", "Exterior", "exterior"),
        ("gallery.html", "Gallery", "gallery"),
        ("blog/index.html", "Blog", "blog"),
        ("schedule-appointment.html", "Schedule", "schedule"),
        ("contact.html", "Contact", "contact"),
    ]
    links = []
    for href, label, key in items:
        ac = " active" if key == active else ""
        cur = ' aria-current="page"' if key == active else ""
        links.append(
            f'          <li class="nav-item"><a class="nav-link{ac}" href="{pre}{href}"{cur}>{label}</a></li>'
        )
    return f"""  <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
    <motion class="container">
      <a class="navbar-brand" href="{pre}index.html" aria-label="Sunset Home Painting Home">
        <img src="{pre}images/Sunset Home 2.PNG" alt="Sunset Home Painting painters St Augustine FL" class="logo-img">
        <span>Sunset Home Painting</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
{chr(10).join(links)}
        </ul>
      </div>
    </motion>
  </nav>""".replace("<motion", "<motion").replace("<motion class", "<div class").replace("</motion>", "</motion>").replace("<motion class=\"container\">", "<div class=\"container\">").replace("</motion>", "</motion>")

# Fix nav - do replace properly
def nav_html(active, depth=0):
    pre = prefix(depth)
    items = [
        ("index.html", "Home", "home"),
        ("about.html", "About", "about"),
        ("services.html", "Services", "services"),
        ("interior-painting-st-augustine.html", "Interior", "interior"),
        ("exterior-painting-st-augustine.html", "Exterior", "exterior"),
        ("gallery.html", "Gallery", "gallery"),
        ("blog/index.html", "Blog", "blog"),
        ("schedule-appointment.html", "Schedule", "schedule"),
        ("contact.html", "Contact", "contact"),
    ]
    links = []
    for href, label, key in items:
        ac = " active" if key == active else ""
        cur = ' aria-current="page"' if key == active else ""
        links.append(
            f'          <li class="nav-item"><a class="nav-link{ac}" href="{pre}{href}"{cur}>{label}</a></li>'
        )
    return (
        f'  <nav class="navbar navbar-expand-lg navbar-dark fixed-top">\n'
        f'    <motion class="container">\n'
        f'      <a class="navbar-brand" href="{pre}index.html" aria-label="Sunset Home Painting Home">\n'
        f'        <img src="{pre}images/Sunset Home 2.PNG" alt="Sunset Home Painting" class="logo-img">\n'
        f'        <span>Sunset Home Painting</span>\n'
        f'      </a>\n'
        f'      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">\n'
        f'        <span class="navbar-toggler-icon"></span>\n'
        f'      </button>\n'
        f'      <div class="collapse navbar-collapse" id="navbarNav">\n'
        f'        <ul class="navbar-nav ms-auto">\n'
        + "\n".join(links)
        + "\n        </ul>\n      </div>\n    </motion>\n  </nav>"
    ).replace("<motion class=\"container\">", '<motion class="container">').replace("<motion", "<div").replace("</motion>", "</div>")


def footer_html(depth=0):
    pre = prefix(depth)
    return f"""  <footer class="footer" role="contentinfo">
    <motion class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h4>Sunset Home Painting</h4>
          <p>Interior and exterior painting in Saint Augustine, FL 32084. Serving Jacksonville, Palm Coast, Ponte Vedra, and Fleming Island.</p>
        </div>
        <motion class="footer-section">
          <h4>Services</h4>
          <a href="{pre}interior-painting-st-augustine.html">Interior Painting St. Augustine</a>
          <a href="{pre}exterior-painting-st-augustine.html">Exterior Painting St. Augustine</a>
          <a href="{pre}painting-jacksonville.html">Painting Jacksonville</a>
          <a href="{pre}service-areas.html">Service Areas</a>
          <a href="{pre}faq.html">FAQ</a>
          <a href="{pre}blog/index.html">Blog</a>
        </motion>
        <div class="footer-section">
          <h4>Contact</h4>
          <p><i class="fas fa-phone"></i> <a href="tel:3864053015">(386) 405-3015</a></p>
          <p><i class="fas fa-envelope"></i> <a href="mailto:sunsethomepainting@gmail.com">sunsethomepainting@gmail.com</a></p>
          <p><i class="fas fa-map-marker-alt"></i> Saint Augustine, FL 32084</p>
        </motion>
        <div class="footer-section">
          <h4>Follow Us</h4>
          <div class="social-links">
            <a href="https://www.facebook.com/share/19x4X4LCrX/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
          </div>
        </motion>
      </motion>
      <div class="footer-bottom"><p>&copy; 2026 Sunset Home Painting. All rights reserved.</p></div>
    </motion>
  </footer>
  <a href="{pre}schedule-appointment.html" class="sticky-cta-button" aria-label="Schedule Appointment"><i class="fas fa-calendar-check"></i><span>Schedule Appointment</span></a>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  <script src="{pre}js/main.js"></script>""".replace("<motion", "<div").replace("</motion>", "</div>")


def article_schema(headline, desc, url):
    h, d = headline.replace('"', '\\"'), desc.replace('"', '\\"')
    return f"""  <script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{h}","description":"{d}","author":{{"@type":"Organization","name":"Sunset Home Painting"}},"publisher":{{"@type":"Organization","name":"Sunset Home Painting"}},"mainEntityOfPage":"{url}"}}
</script>"""


def nav_mount(depth=0):
    return (
        '  <div id="site-nav-mount"></div>\n\n'
        '  <script src="/js/site-nav.js?v=5" defer></script>'
    )


def page_html(title, desc, path, body, active, depth=0, article=False, h1=None):
    art_schema = ""
    if article:
        art_schema = article_schema(h1 or title, desc, f"{SITE}/{path.lstrip('/')}")
    body_class = "inner-page blog-article" if article else "inner-page"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head_block(title, desc, path, depth, article=article, article_schema_extra=art_schema)}
</head>
<body class="{body_class}">
{nav_mount(depth)}
{body}
{footer_html(depth)}
</body>
</html>"""


def cta_block(depth=0):
    pre = prefix(depth)
    return f"""      <div class="cta-banner">
        <h3>Ready for professional painting in Northeast Florida?</h3>
        <p>Sunset Home Painting offers free estimates for interior and exterior projects in Saint Augustine, Jacksonville, and nearby communities.</p>
        <a href="{pre}schedule-appointment.html" class="btn-primary-custom">Schedule Free Estimate</a>
        <a href="{pre}contact.html" class="btn-secondary-custom ms-2 mt-2 mt-md-0">Contact Us</a>
      </div>"""


POSTS = [
    {
        "slug": "painting-st-augustine-fl-guide",
        "title": "Painting St Augustine FL: Homeowner's Guide | Sunset Home Painting",
        "desc": "Everything you need to know about painting St Augustine FL homes—interior, exterior, costs, and hiring local painters in Saint Augustine 32084.",
        "h1": "Painting St Augustine FL: What Homeowners Should Know",
        "paras": [
            "Searching for <strong>painting St Augustine</strong> brings up dozens of contractors—but not every crew understands historic homes, coastal humidity, or the difference between downtown Saint Augustine and the beaches. Sunset Home Painting is a family-owned team based in Saint Augustine, FL 32084, focused on interior and exterior painting that lasts in Northeast Florida weather.",
            "Whether you need a full exterior repaint, fresh interior walls, or cabinet refinishing, local experience matters. Salt air, intense sun, and summer storms affect how paint adheres and how long finishes hold up. We use premium coatings and thorough prep so your investment pays off for years.",
            "Our <a href=\"../interior-painting-st-augustine.html\">interior painting St Augustine</a> services cover walls, ceilings, trim, and more with low-VOC options. For curb appeal and protection, see our <a href=\"../exterior-painting-st-augustine.html\">exterior painting St Augustine</a> process—from power washing to final walkthrough.",
            "We serve Saint Augustine, St. Augustine Beach, and surrounding communities. Ready to start? <a href=\"../schedule-appointment.html\">Schedule a free estimate</a> or call <a href=\"tel:3864053015\">(386) 405-3015</a>.",
        ],
    },
    {
        "slug": "interior-painting-st-augustine-tips",
        "title": "Interior Painting St Augustine: Tips & Process | Sunset Home Painting",
        "desc": "Expert interior painting St Augustine tips—prep, paint selection, timelines, and why homeowners trust Sunset Home Painting for Saint Augustine FL homes.",
        "h1": "Interior Painting St Augustine: Tips for a Flawless Finish",
        "paras": [
            "<strong>Interior painting St Augustine</strong> projects succeed or fail in the prep stage. Furniture protection, hole repair, sanding, and primer choice determine how smooth walls look and how well paint resists Florida humidity indoors.",
            "Sunset Home Painting follows a clear process: consultation, color help, surface prep, premium application, and cleanup. We use eco-friendly, low-odor paints when possible so families can return to rooms quickly.",
            "Popular requests include living rooms, bedrooms, kitchens, and accent walls in historic downtown homes and newer builds in Nocatee and World Golf Village. We match sheen to each space—matte for bedrooms, scrubbable satin for kitchens and hallways.",
            "Compare our full <a href=\"../interior-painting-st-augustine.html\">interior painting services in St Augustine</a> or browse the <a href=\"../gallery.html\">gallery</a> for recent projects.",
        ],
    },
    {
        "slug": "exterior-painting-st-augustine-coastal-homes",
        "title": "Exterior Painting St Augustine for Coastal Homes | Sunset Home",
        "desc": "Exterior painting St Augustine FL for coastal and historic homes. Salt air prep, durable coatings, and professional painters in Saint Augustine.",
        "h1": "Exterior Painting St Augustine for Coastal & Historic Homes",
        "paras": [
            "<strong>Exterior painting St Augustine</strong> requires more than a ladder and a brush. Coastal UV, moisture, and salt accelerate peeling if surfaces are not cleaned, repaired, and primed correctly.",
            "We inspect siding, stucco, trim, and fascia; caulk gaps; and apply coatings rated for Florida exteriors. From Vilano Beach to Davis Shores, we've helped homeowners protect and beautify their properties.",
            "Choosing colors? Lighter palettes reflect heat; quality trim contrast boosts curb appeal for resale in the Saint Augustine market. Our team documents the scope up front so timelines and expectations stay clear.",
            "Learn more on our <a href=\"../exterior-painting-st-augustine.html\">exterior painting St Augustine</a> page or request a <a href=\"../contact.html\">free quote</a>.",
        ],
    },
    {
        "slug": "house-painters-st-augustine-how-to-choose",
        "title": "How to Choose House Painters St Augustine FL | Sunset Home Painting",
        "desc": "How to choose the best house painters St Augustine FL—licensing, reviews, estimates, and what to ask before hiring a painting contractor in Saint Augustine.",
        "h1": "How to Choose House Painters in St Augustine FL",
        "paras": [
            "Hiring <strong>house painters St Augustine</strong> homeowners can trust means checking reviews, verifying insurance, and getting a written scope—not just the lowest bid.",
            "Ask about prep, paint brands, crew size, and warranty. A professional painting service St Augustine should explain surface repairs, primer use, and how weather affects scheduling.",
            "Sunset Home Painting is family-owned with 10+ years serving Saint Augustine, FL 32084, Jacksonville, Palm Coast, Ponte Vedra, and Fleming Island. We provide detailed estimates and communicate throughout your project.",
            "See <a href=\"../about.html\">about us</a> and <a href=\"../faq.html\">FAQs</a>, or <a href=\"../schedule-appointment.html\">book a consultation</a>.",
        ],
    },
    {
        "slug": "painting-jacksonville-fl-services",
        "title": "Painting Jacksonville FL | Interior & Exterior | Sunset Home",
        "desc": "Professional painting Jacksonville FL—interior and exterior house painting across Jacksonville. Sunset Home Painting serves all of Jacksonville from Saint Augustine.",
        "h1": "Painting Jacksonville FL: Interior & Exterior Services",
        "paras": [
            "Sunset Home Painting provides full <strong>painting Jacksonville</strong> coverage—from Riverside and San Marco to Mandarin, Jacksonville Beach, and the Westside. We bring the same prep standards and premium coatings used on Saint Augustine projects.",
            "Jacksonville's mix of brick, stucco, and wood siding needs tailored prep. Our crews handle residential repaints, accent updates, and exterior refreshes with minimal disruption.",
            "Whether you're in Jacksonville or Saint Augustine, you get one accountable team, clear pricing, and a local phone number: <a href=\"tel:3864053015\">(386) 405-3015</a>.",
            "Details: <a href=\"../painting-jacksonville.html\">Painting Jacksonville service page</a>.",
        ],
    },
    {
        "slug": "palm-coast-painting-contractors",
        "title": "Palm Coast Painting Contractors | Sunset Home Painting",
        "desc": "Palm Coast painting contractors for interior and exterior house painting. Sunset Home Painting serves Palm Coast FL from Saint Augustine.",
        "h1": "Palm Coast Painting Contractors You Can Trust",
        "paras": [
            "Looking for <strong>Palm Coast painting</strong> experts? Sunset Home Painting serves Palm Coast communities with interior and exterior repaints, trim work, and detailed prep.",
            "Coastal Flagler County homes face similar challenges to St. Augustine—humidity, sun, and storm exposure. We specify durable exterior systems and moisture-aware interior products.",
            "We're based in Saint Augustine, FL 32084, with crews traveling to Palm Coast regularly. <a href=\"../service-areas.html\">View all service areas</a>.",
        ],
    },
    {
        "slug": "ponte-vedra-house-painting",
        "title": "Ponte Vedra House Painting | Interior & Exterior | Sunset Home",
        "desc": "Ponte Vedra house painting for luxury homes and coastal properties. Professional interior and exterior painters serving Ponte Vedra from St Augustine.",
        "h1": "Ponte Vedra House Painting: Interior & Exterior",
        "paras": [
            "<strong>Ponte Vedra house painting</strong> often means high-end finishes, careful protection of landscaping, and coordination with HOAs. Our team delivers crisp lines, premium paints, and respectful job sites.",
            "From Marsh Landing to Sawgrass, we handle full repaints, cabinet-friendly interior updates, and exterior refreshes that stand up to coastal conditions.",
            "Explore <a href=\"../services.html\">all services</a> or schedule an estimate for your Ponte Vedra home.",
        ],
    },
    {
        "slug": "fleming-island-painters",
        "title": "Fleming Island Painters | House Painting Services | Sunset Home",
        "desc": "Fleming Island painters for residential interior and exterior painting. Sunset Home Painting serves Fleming Island FL from Saint Augustine.",
        "h1": "Fleming Island Painters for Your Home",
        "paras": [
            "Sunset Home Painting is a go-to choice for <strong>Fleming Island painters</strong> when homeowners want reliable scheduling and quality finishes without a Jacksonville mega-firm runaround.",
            "We paint interiors, exteriors, and trim throughout Fleming Island and Orange Park, with free estimates and clear communication.",
            "Contact us at <a href=\"mailto:sunsethomepainting@gmail.com\">sunsethomepainting@gmail.com</a> or call <a href=\"tel:3864053015\">(386) 405-3015</a>.",
        ],
    },
    {
        "slug": "local-painting-company-st-augustine",
        "title": "Local Painting Company St Augustine | Sunset Home Painting",
        "desc": "Local painting company St Augustine FL—family-owned interior and exterior painters in Saint Augustine 32084. Free estimates.",
        "h1": "Why Hire a Local Painting Company in St Augustine?",
        "paras": [
            "A <strong>local painting St Augustine</strong> company knows neighborhood architecture, permit norms, and weather windows. Sunset Home Painting lives and works in Saint Augustine, FL 32084—not a call center states away.",
            "We support our community with fair pricing, eco-conscious paint options, and crews who treat your home like their own. That's why reviews mention professionalism, punctuality, and detail.",
            "For <strong>painting service St Augustine</strong> you can trust, <a href=\"../contact.html\">get in touch today</a>.",
        ],
    },
    {
        "slug": "residential-painting-st-augustine-fl",
        "title": "Residential Painting St Augustine FL | Sunset Home Painting",
        "desc": "Residential painting St Augustine FL for homes, townhomes, and condos. Interior and exterior house painting in Saint Augustine.",
        "h1": "Residential Painting St Augustine FL",
        "paras": [
            "<strong>Residential painting St Augustine</strong> is our core focus—whole-home repaints, single-room updates, and exterior facelifts for families across Northeast Florida.",
            "We coordinate around your schedule, protect floors and furniture, and leave job sites clean daily. Services include walls, ceilings, doors, trim, siding, and stucco.",
            "Pair interior and exterior projects for cohesive curb-to-foyer results. <a href=\"../services.html\">See residential services</a>.",
        ],
    },
    {
        "slug": "commercial-painting-st-augustine",
        "title": "Commercial Painting St Augustine | Sunset Home Painting",
        "desc": "Commercial painting St Augustine for offices, retail, and small businesses. Professional painters in Saint Augustine FL 32084.",
        "h1": "Commercial Painting in St Augustine",
        "paras": [
            "Need <strong>commercial painting St Augustine</strong>? We paint offices, retail spaces, and light commercial properties with after-hours scheduling when needed to reduce downtime.",
            "Brand colors, durable finishes, and neat crews matter for business impressions. We document scopes and stick to timelines.",
            "Ask about combining commercial exterior touch-ups with interior refresh packages.",
        ],
    },
    {
        "slug": "painting-service-st-augustine-estimates",
        "title": "Painting Service St Augustine: Free Estimates | Sunset Home",
        "desc": "Painting service St Augustine with free estimates. Interior, exterior, and whole-home painting in Saint Augustine and Northeast FL.",
        "h1": "Painting Service St Augustine: What's Included",
        "paras": [
            "Our <strong>painting service St Augustine</strong> includes consultation, surface prep, premium paint, application, cleanup, and final walkthrough. No surprise add-ons when scope is agreed upfront.",
            "We also serve as your <strong>paint service Saint Augustine</strong> partner for touch-ups, accent walls, and seasonal maintenance.",
            "<a href=\"../schedule-appointment.html\">Book online</a> for a free estimate in Saint Augustine, Jacksonville, Palm Coast, Ponte Vedra, or Fleming Island.",
        ],
    },
    {
        "slug": "best-exterior-house-painting-florida-coast",
        "title": "Best Exterior House Painting on Florida's Coast | St Augustine",
        "desc": "Best practices for exterior house painting on Florida's coast—St Augustine, Jacksonville, Palm Coast. Salt air, sun, and storm-ready finishes.",
        "h1": "Exterior House Painting on Florida's Coast",
        "paras": [
            "The best <strong>exterior house painting</strong> on Florida's coast starts with washing, scraping failing paint, sealing wood, and choosing 100% acrylic systems rated for masonry and siding.",
            "In <strong>St Augustine</strong> and nearby beaches, we recommend regular maintenance cycles before bare substrate exposure leads to costly repairs.",
            "Sunset Home Painting specializes in <a href=\"../exterior-painting-st-augustine.html\">exterior painting St Augustine</a> and coastal Northeast FL.",
        ],
    },
    {
        "slug": "eco-friendly-painting-st-augustine",
        "title": "Eco-Friendly Painting St Augustine | Low-VOC | Sunset Home",
        "desc": "Eco-friendly painting St Augustine with low-VOC and low-odor paints. Safe interior painting for families in Saint Augustine FL.",
        "h1": "Eco-Friendly Painting in St Augustine",
        "paras": [
            "Families ask about <strong>eco-friendly painting St Augustine</strong> options—low-VOC latex, low odor, and fast return to occupied rooms.",
            "Sunset Home Painting uses modern coatings that perform in humidity without harsh fumes. Ideal for nurseries, bedrooms, and seniors' homes.",
            "Ask about green product lines during your <a href=\"../interior-painting-st-augustine.html\">interior painting</a> estimate.",
        ],
    },
    {
        "slug": "free-painting-estimate-northeast-florida",
        "title": "Free Painting Estimate Northeast Florida | Sunset Home Painting",
        "desc": "Free painting estimate in Northeast Florida—St Augustine, Jacksonville, Palm Coast, Ponte Vedra, Fleming Island. Call (386) 405-3015.",
        "h1": "Free Painting Estimate in Northeast Florida",
        "paras": [
            "Get a <strong>free painting estimate</strong> for your Saint Augustine, Jacksonville, Palm Coast, Ponte Vedra, or Fleming Island project. We measure scope on-site or virtually, explain prep, and provide clear pricing.",
            "Whether you need <strong>interior painting St Augustine</strong>, <strong>exterior painting St Augustine</strong>, or whole-home work, one call connects you with Sunset Home Painting.",
            "<a href=\"../schedule-appointment.html\">Schedule online</a> or phone <a href=\"tel:3864053015\">(386) 405-3015</a>.",
        ],
    },
]


def blog_body(post):
    paras = "\n".join(f"        <p>{p}</p>" for p in post["paras"])
    return f"""  <main class="page-section page-top-section blog-article">
    <div class="container">
      <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <a href="../index.html">Home</a> &rsaquo; <a href="index.html">Blog</a> &rsaquo; {post['h1'][:40]}…
      </nav>
      <h1>{post['h1']}</h1>
      <p class="blog-meta">Sunset Home Painting &bull; Saint Augustine, FL &bull; Painting Tips</p>
      <div class="content-prose">
{paras}
{cta_block(1)}
      </div>
    </div>
  </main>"""


def blog_index_cards():
    cards = []
    for post in POSTS:
        cards.append(f"""        <article class="blog-card">
          <h3><a href="{post['slug']}.html">{post['h1']}</a></h3>
          <p>{post['desc'][:140]}…</p>
          <a href="{post['slug']}.html">Read more &rarr;</a>
        </article>""")
    return "\n".join(cards)


def main():
    blog_dir = os.path.join(ROOT, "blog")
    os.makedirs(blog_dir, exist_ok=True)

    for post in POSTS:
        path = f"blog/{post['slug']}.html"
        html = page_html(
            post["title"],
            post["desc"],
            path,
            blog_body(post),
            "blog",
            depth=1,
            article=True,
            h1=post["h1"],
        )
        out = os.path.join(blog_dir, post["slug"] + ".html")
        with open(out, "w") as f:
            f.write(html)
        print("Wrote", out)

    index_body = f"""  <main class="page-section page-top-section">
    <div class="container">
      <h1>Painting Tips &amp; Local Guides</h1>
      <p class="text-center mb-5" style="max-width:720px;margin:0 auto 2rem;">Expert advice on <strong>painting St Augustine</strong>, <strong>interior painting St Augustine</strong>, <strong>exterior painting St Augustine</strong>, Jacksonville, and Northeast Florida from Sunset Home Painting.</p>
      <motion class="blog-grid">
{blog_index_cards()}
      </motion>
    </div>
  </main>""".replace("<motion", "<motion").replace("<motion class", "<div class").replace("</motion>", "</motion>")

    index_body = index_body.replace("<motion class=\"blog-grid\">", '<div class="blog-grid">').replace("</motion>", "</motion>").replace("</motion>", "</div>")

    index_html = page_html(
        "Blog | Painting St Augustine & Northeast FL | Sunset Home Painting",
        "Painting tips for St Augustine, Jacksonville, Palm Coast—interior & exterior painting guides from local painters in Saint Augustine FL.",
        "blog/index.html",
        index_body,
        "blog",
        depth=1,
    )
    with open(os.path.join(blog_dir, "index.html"), "w") as f:
        f.write(index_html)
    print("Wrote blog index")

    urls = [
        "", "index.html", "about.html", "services.html",
        "interior-painting-st-augustine.html", "exterior-painting-st-augustine.html",
        "painting-jacksonville.html", "service-areas.html", "faq.html",
        "gallery.html", "contact.html", "schedule-appointment.html", "blog/index.html",
    ]
    for post in POSTS:
        urls.append(f"blog/{post['slug']}.html")

    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = SITE if u == "" else f"{SITE}/{u}"
        if u == "":
            loc = SITE + "/"
        priority = "1.0" if u in ("", "index.html") else "0.8"
        if u.startswith("blog/") and u != "blog/index.html":
            priority = "0.7"
        sm.append(f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{priority}</priority></url>")
    sm.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write("\n".join(sm))
    print("Wrote sitemap.xml")


def service_main(h1, intro, sections_html, active):
    return f"""  <main class="page-section page-top-section">
    <motion class="container">
      <h1>{h1}</h1>
      <div class="content-prose">
        <p class="lead">{intro}</p>
{sections_html}
{cta_block(0)}
      </div>
    </motion>
  </main>""".replace("<motion class=\"container\">", '<div class="container">').replace("</motion>", "</motion>").replace("</motion>", "</motion>").replace("</motion>", "</motion>").replace("</motion>", "</div>")


def write_service(filename, title, desc, path, body, active):
    html = page_html(title, desc, path, body, active, depth=0)
    with open(os.path.join(ROOT, filename), "w") as f:
        f.write(html)
    print("Wrote", filename)


def generate_services():
    interior = service_main(
        "Interior Painting in St. Augustine &amp; Saint Augustine, FL",
        "Sunset Home Painting delivers professional <strong>interior painting St Augustine</strong> homeowners rely on—from historic downtown homes to new construction in World Golf Village and Nocatee. Based in Saint Augustine, FL 32084, we combine careful prep, premium paints, and respectful crews.",
        """
        <h2>Interior Painting Services We Provide</h2>
        <ul>
          <li>Walls, ceilings, and accent features</li>
          <li>Trim, doors, and baseboards</li>
          <li>Low-VOC and eco-friendly coating options</li>
          <li>Color consultation and sheen recommendations</li>
          <li>Furniture and floor protection with daily cleanup</li>
        </ul>
        <h2>Our Interior Painting Process</h2>
        <p>Every <strong>interior painting St Augustine</strong> project starts with a walkthrough and written scope. We repair minor drywall issues, sand glossy areas, prime stains, and apply two finish coats for uniform color. Rooms are ventilated and left ready to use as soon as coatings cure.</p>
        <h2>Why Local Homeowners Choose Us</h2>
        <p>As a family-owned <strong>painting service St Augustine</strong> company with 10+ years of experience, we prioritize communication and detail. Read our <a href="gallery.html">gallery</a> and <a href="blog/interior-painting-st-augustine-tips.html">interior painting tips</a>, or compare <a href="exterior-painting-st-augustine.html">exterior painting St Augustine</a> if you need both.</p>
        <p>We also serve Jacksonville, Palm Coast, Ponte Vedra, and Fleming Island. See <a href="service-areas.html">service areas</a>.</p>
        """,
    )
    write_service(
        "interior-painting-st-augustine.html",
        "Interior Painting St Augustine FL | Saint Augustine | Sunset Home Painting",
        "Professional interior painting St Augustine & Saint Augustine FL. Rooms, trim, ceilings, eco-friendly paint. Free estimates—call (386) 405-3015.",
        "interior-painting-st-augustine.html",
        interior,
        "interior",
    )

    exterior = service_main(
        "Exterior Painting in St. Augustine &amp; Saint Augustine, FL",
        "Protect and beautify your home with expert <strong>exterior painting St Augustine</strong> from Sunset Home Painting. Coastal sun, salt, and storms demand proper prep and Florida-rated coatings—we deliver both for Saint Augustine and Northeast FL properties.",
        """
        <h2>Exterior Painting St Augustine: What We Paint</h2>
        <ul>
          <li>Siding, stucco, and masonry</li>
          <li>Trim, fascia, soffits, and shutters</li>
          <li>Front doors, porches, and railings</li>
          <li>Power washing, scraping, caulking, and priming</li>
        </ul>
        <h2>Built for Coastal Florida</h2>
        <p><strong>Exterior painting St Augustine</strong> homes means addressing mildew, chalking paint, and wood rot before new color goes on. Our crews use high-quality acrylic systems designed for humidity and UV exposure common from St. Augustine Beach to Palm Coast.</p>
        <h2>Pair With Interior Painting</h2>
        <p>Many clients book <a href="interior-painting-st-augustine.html">interior painting St Augustine</a> and exterior work together for a coordinated refresh. Explore our <a href="blog/exterior-painting-st-augustine-coastal-homes.html">coastal exterior guide</a> or view the <a href="gallery.html">project gallery</a>.</p>
        """,
    )
    write_service(
        "exterior-painting-st-augustine.html",
        "Exterior Painting St Augustine FL | Saint Augustine | Sunset Home",
        "Exterior painting St Augustine FL for coastal & historic homes. Power wash, prep, premium paint. Saint Augustine painters—free estimates.",
        "exterior-painting-st-augustine.html",
        exterior,
        "exterior",
    )

    services_body = service_main(
        "Painting Services in St. Augustine, FL",
        "Sunset Home Painting is your full-service <strong>painting St Augustine</strong> partner for residential and light commercial projects. From a single room to a whole-home exterior, we provide the same attention to prep, protection, and finish quality.",
        """
        <div class="service-card-grid">
          <article class="service-card">
            <h3><a href="interior-painting-st-augustine.html">Interior Painting St. Augustine</a></h3>
            <p>Walls, ceilings, trim, and eco-friendly options for homes in Saint Augustine, FL 32084 and nearby communities.</p>
            <a href="interior-painting-st-augustine.html">Learn more &rarr;</a>
          </article>
          <article class="service-card">
            <h3><a href="exterior-painting-st-augustine.html">Exterior Painting St. Augustine</a></h3>
            <p>Coastal-ready exterior repaints with thorough prep for lasting curb appeal and protection.</p>
            <a href="exterior-painting-st-augustine.html">Learn more &rarr;</a>
          </article>
          <article class="service-card">
            <h3><a href="painting-jacksonville.html">Painting Jacksonville</a></h3>
            <p>We serve all of Jacksonville, FL with interior and exterior house painting.</p>
            <a href="painting-jacksonville.html">Learn more &rarr;</a>
          </article>
        </motion>
        <h2>Local Painting Service You Can Trust</h2>
        <p>Searching for a <strong>painting service St Augustine</strong> or <strong>paint service Saint Augustine</strong>? We offer free estimates, clear timelines, and 5-star craftsmanship. Read the <a href="blog/index.html">blog</a> or <a href="faq.html">FAQ</a>.</p>
        """.replace("<motion>", "").replace("</motion>", "").replace('<motion class="service-card-grid">', '<motion class="service-card-grid">').replace(
            "<motion class=\"service-card-grid\">", '<motion class="service-card-grid">'
        ),
        "services",
    )
    services_body = services_body.replace(
        "</article>\n        </motion>",
        "</article>\n        </div>",
    )
    if "<motion" in services_body:
        services_body = services_body.replace("<motion class=\"service-card-grid\">", '<div class="service-card-grid">')

    write_service(
        "services.html",
        "Painting Services St Augustine FL | Interior & Exterior | Sunset Home",
        "Full painting services St Augustine FL—interior painting, exterior painting, residential & commercial. Saint Augustine painting company. Free estimates.",
        "services.html",
        service_main(
            "Painting Services in St. Augustine, FL",
            "Sunset Home Painting is your full-service <strong>painting St Augustine</strong> partner for residential and light commercial projects.",
            """
        <div class="service-card-grid">
          <article class="service-card">
            <h3><a href="interior-painting-st-augustine.html">Interior Painting St. Augustine</a></h3>
            <p>Walls, ceilings, trim, and eco-friendly options for Saint Augustine, FL 32084.</p>
            <a href="interior-painting-st-augustine.html">Learn more &rarr;</a>
          </article>
          <article class="service-card">
            <h3><a href="exterior-painting-st-augustine.html">Exterior Painting St. Augustine</a></h3>
            <p>Coastal-ready exterior repaints with thorough prep.</p>
            <a href="exterior-painting-st-augustine.html">Learn more &rarr;</a>
          </article>
          <article class="service-card">
            <h3><a href="painting-jacksonville.html">Painting Jacksonville</a></h3>
            <p>Interior and exterior painting across all of Jacksonville, FL.</p>
            <a href="painting-jacksonville.html">Learn more &rarr;</a>
          </article>
        </div>
        <h2>Residential &amp; Commercial</h2>
        <p>As a leading <strong>painting service St Augustine</strong> provider, we handle homes, townhomes, condos, offices, and retail spaces. See <a href="service-areas.html">where we work</a>.</p>
            """,
        ),
        "services",
    )

    write_service(
        "painting-jacksonville.html",
        "Painting Jacksonville FL | Interior & Exterior | Sunset Home Painting",
        "Painting Jacksonville FL—interior and exterior house painting. Sunset Home Painting serves all of Jacksonville from Saint Augustine. Free estimates.",
        "painting-jacksonville.html",
        service_main(
            "Painting Jacksonville, FL",
            "Sunset Home Painting provides complete <strong>painting Jacksonville</strong> services—interior and exterior—for homeowners across the city. We're headquartered in Saint Augustine, FL 32084, with crews serving Jacksonville daily.",
            """
        <h2>Jacksonville Areas We Serve</h2>
        <p>We paint in Riverside, San Marco, Mandarin, Jacksonville Beach, Arlington, Southside, and throughout Duval County. Same quality prep and coatings as our <strong>painting St Augustine</strong> projects.</p>
        <h2>Services in Jacksonville</h2>
        <ul>
          <li><a href="interior-painting-st-augustine.html">Interior house painting</a></li>
          <li><a href="exterior-painting-st-augustine.html">Exterior house painting</a></li>
          <li>Trim, doors, and accent updates</li>
        </ul>
        <p>Read our <a href="blog/painting-jacksonville-fl-services.html">Jacksonville painting guide</a> or schedule a free estimate today.</p>
            """,
        ),
        "services",
    )

    areas_body = service_main(
        "Service Areas: Northeast Florida",
        "Sunset Home Painting is a <strong>local painting St Augustine</strong> company proud to serve homeowners throughout Northeast Florida from our base in Saint Augustine, FL 32084.",
        """
        <h2>Primary Service Areas</h2>
        <div class="service-areas-list">
          <span class="service-area-tag">Saint Augustine, FL</span>
          <span class="service-area-tag">St. Augustine, FL</span>
          <span class="service-area-tag">Jacksonville, FL</span>
          <span class="service-area-tag">Palm Coast, FL</span>
          <span class="service-area-tag">Ponte Vedra, FL</span>
          <span class="service-area-tag">Fleming Island, FL</span>
          <span class="service-area-tag">St. Augustine Beach</span>
          <span class="service-area-tag">Nocatee</span>
        </div>
        <p>Whether you need <strong>interior painting St Augustine</strong>, <strong>exterior painting St Augustine</strong>, or <strong>painting Jacksonville</strong>, one team handles your project start to finish.</p>
        <p><a href="interior-painting-st-augustine.html">Interior services</a> &bull; <a href="exterior-painting-st-augustine.html">Exterior services</a> &bull; <a href="contact.html">Contact</a></p>
        """,
    )
    write_service(
        "service-areas.html",
        "Service Areas | St Augustine, Jacksonville, Palm Coast | Sunset Home Painting",
        "Painting service areas: Saint Augustine, Jacksonville, Palm Coast, Ponte Vedra, Fleming Island. Local painters FL 32084.",
        "service-areas.html",
        areas_body,
        "services",
    )

    faq_body = """  <main class="page-section page-top-section">
    <div class="container">
      <h1>Frequently Asked Questions</h1>
      <p class="text-center mb-4">Common questions about <strong>painting St Augustine</strong>, <strong>interior painting St Augustine</strong>, and <strong>exterior painting St Augustine</strong>.</p>
      <div class="content-prose">
        <div class="faq-item"><h3>Do you offer free estimates?</h3><p>Yes. We provide free estimates for interior and exterior painting in Saint Augustine, Jacksonville, Palm Coast, Ponte Vedra, and Fleming Island. <a href="schedule-appointment.html">Schedule online</a> or call (386) 405-3015.</p></div>
        <motion class="faq-item"><h3>What areas do you serve?</h3><p>We serve all of Jacksonville, Saint Augustine (FL 32084), Palm Coast, Ponte Vedra, and Fleming Island. See our <a href="service-areas.html">service areas page</a>.</p></motion>
        <div class="faq-item"><h3>How long does interior painting take?</h3><p>Most single-room projects take 1–2 days; whole-home interior painting St Augustine projects may take several days depending on prep and square footage.</p></motion>
        <div class="faq-item"><h3>How do you prep for exterior painting in coastal Florida?</h3><p>We wash surfaces, scrape failing paint, repair wood, caulk gaps, and prime bare areas before applying Florida-rated exterior coatings.</p></div>
        <div class="faq-item"><h3>Do you use eco-friendly paint?</h3><p>Yes. We offer low-VOC interior options ideal for families and occupied homes.</p></div>
        <motion class="faq-item"><h3>Are you a local painting company?</h3><p>Sunset Home Painting is family-owned and based in Saint Augustine, FL 32084—not a national franchise.</p></motion>
        <div class="faq-item"><h3>Do you paint commercial properties?</h3><p>Yes, we handle light commercial painting in St. Augustine and nearby cities. Contact us for details.</p></div>
      </div>
      {cta_block(0)}
    </div>
  </main>""".replace("<motion", "<div").replace("</motion>", "</motion>").replace("</motion>", "</motion>").replace("</motion>", "</div>")
    faq_body = faq_body.format(cta_block=cta_block)
    write_service(
        "faq.html",
        "FAQ | Painting St Augustine FL | Sunset Home Painting",
        "FAQ about painting St Augustine—estimates, service areas, interior & exterior painting timelines, eco-friendly paint. Saint Augustine FL 32084.",
        "faq.html",
        faq_body,
        "services",
    )


if __name__ == "__main__":
    main()
