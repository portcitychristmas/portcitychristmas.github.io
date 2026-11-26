"""Builds the static site from src/ into the repo root.

Run from the repo root:   python src/build.py

- Shared header, footer, <head> tags and business data live here, so a phone
  number or price change is made once.
- Big page sections live in src/parts/*.html.
- Each town page is generated from the AREAS list below.
GitHub Pages serves the generated HTML files as-is (no build step on GitHub).
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = Path(__file__).resolve().parent / "parts"
SITE = "https://portcitychristmas.github.io"
PHONE_DISPLAY = "506-799-2790"
PHONE_TEL = "+15067992790"
START_PRICE = 200
# Paste your Google review link here once your Business Profile is verified
# (Business Profile > "Ask for reviews" > copy link), then run: python src/build.py
# While it's empty, the review button opens a text message instead.
REVIEW_URL = "https://g.page/r/CezxlFJ04hWNEBM/review"
GOOGLE_PROFILE = "https://g.page/r/CezxlFJ04hWNEBM"
UPDATED = date.today().strftime("%B %Y")
TODAY = date.today().isoformat()


def part(name):
    return (PARTS / f"{name}.html").read_text(encoding="utf-8").replace("{{REVIEW_CTA}}", review_cta())


STAR_ICON = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6-4.9-4.6 6.6-.8z"/></svg>'


def review_link_attrs():
    if REVIEW_URL:
        return f'href="{REVIEW_URL}" target="_blank" rel="noopener"'
    return f'href="sms:{PHONE_TEL}"'


def review_cta(town=None):
    who = f"in {town}" if town else "by Port City"
    if REVIEW_URL:
        label, note = "Leave a Google review", "It takes 30 seconds and really helps a small local business."
    else:
        label, note = "Leave a review", "Text me a few words about your experience and I'll add it here."
    return f"""        <div class="review-cta">
          <p><strong>Had your lights hung {who}?</strong> {note}</p>
          <a class="btn btn-primary" {review_link_attrs()}>{STAR_ICON} {label}</a>
        </div>"""


# ---------------------------------------------------------------- service areas
AREAS = [
    {
        "slug": "saint-john", "name": "Saint John",
        "card": "East, West, North and South End, Millidgeville, Lakewood and more.",
        "places": ["Uptown", "East Side", "West Side", "North End", "South End", "Millidgeville", "Lakewood"],
        "intro": "From the East Side to the West Side, I hang the lights you already own on homes all over Saint John.",
        "review": "Andrew B.",
    },
    {
        "slug": "rothesay", "name": "Rothesay",
        "card": "The whole town, from the Common to Wells.",
        "places": ["Renforth", "Fairvale", "East Riverside-Kingshurst", "Rothesay Common area", "Wells"],
        "intro": "Rothesay homes, from Renforth to Wells, get the same simple service: your lights, my ladder.",
        "review": "Nicole P.",
    },
    {
        "slug": "quispamsis", "name": "Quispamsis",
        "card": "Every neighbourhood, from Hammond River to Meenan's Cove.",
        "places": ["Hammond River", "Meenan's Cove", "Gondola Point", "Model Farm"],
        "intro": "I cover every neighbourhood in Quispamsis, from Gondola Point to Hammond River.",
        "review": None,
    },
    {
        "slug": "hampton", "name": "Hampton",
        "card": "Hampton and nearby Lakeside, Smithtown, Nauwigewauk and Norton.",
        "places": ["Hampton", "Lakeside", "Smithtown", "Nauwigewauk", "Norton"],
        "intro": "I'm hanging lights in Hampton this season, and I also cover nearby Lakeside, Smithtown, Nauwigewauk and Norton.",
        "review": None,
    },
    {
        "slug": "grand-bay-westfield", "name": "Grand Bay-Westfield",
        "card": "Grand Bay, Westfield and the areas around them.",
        "places": ["Grand Bay", "Westfield", "Pamdenec", "Nerepis"],
        "intro": "Grand Bay, Westfield and the communities around them are all part of my regular route.",
        "review": "Jason W.",
    },
]

STAR = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6-4.9-4.6 6.6-.8z"/></svg>'
REVIEWS = {
    "Andrew B.": ("Saint John", "Booked him to put up the lights we already owned. Communication was easy, and he left everything tidy. Glad to have it done before the cold weather."),
    "Nicole P.": ("Rothesay", "First time getting someone to hang our Christmas lights, and it was such a relief. The roofline looks great, and the kids asked if we could leave them up all year."),
    "Jason W.": ("Grand Bay-Westfield", "Just needed a hand with the higher part of the house that I couldn’t reach safely. Karan took care of it, and everything matched the lights I’d already put up. Happy with the result."),
}

PRICES = [
    ("Mini-home / small bungalow", "200"), ("Bungalow", "250"),
    ("Large bungalow / split-level", "350"), ("Two-storey", None),
]
EXTRAS = [
    ("Attached garage roofline", "75", ""), ("Bushes", "30", " each"),
    ("Small trees (up to 8 ft)", "50", " each"), ("Railings", "30", " each"), ("Windows", "25", " each"),
]

FAQS = [
    ("How much does Christmas light hanging cost in Saint John?",
     "It depends on your house: $200 for a mini-home or small bungalow, $250 for a bungalow and $350 for a large bungalow or split-level. Two-storey homes get a custom quote from a photo. Extras like a garage roofline (+$75), bushes (+$30 each), small trees (+$50 each), railings (+$30 each) and windows (+$25 each) are added on. Every job is at least $200."),
    ("Do I have to supply the lights?",
     "That's the idea. Most people already own lights, so I hang yours. If you don't have enough, or don't have any, I can bring them. They're added to your quote and you keep them."),
    ("When do you hang Christmas lights?",
     "Hanging runs from early November into December, 7 days a week from 8am to 8pm. Same-day appointments are available."),
    ("Which areas do you cover?",
     "Saint John, Rothesay, Quispamsis, Hampton and Grand Bay-Westfield, plus nearby communities like Lakeside, Smithtown, Nauwigewauk and Norton. Just outside these areas? Text me and I can often make it work."),
    ("Do you install Govee permanent lights?",
     "Yes. I install Govee and similar permanent outdoor lights along your roofline. Buy the kit yourself or I can supply it, and every install gets a custom quote from a photo. See the permanent lights page for details."),
    ("What if some of my lights don't work?",
     "I test every strand before it goes up. If one is dead, I'll let you know before I start. I can bring a replacement, or we leave that section out. Your call."),
    ("How do I get a price?",
     "Send me your address by text, phone or the quote form. I can usually measure from satellite and street view, so you'll get a fixed price within a day without a visit."),
    ("Will it damage my roof or gutters?",
     "I take care with your roof and gutters. Regular Christmas light strands go up with clips made for gutters and shingles. Permanent lights (like Govee) have to be fastened to the house with small nails or screws, so I show you exactly where they'll go before I start."),
    ("Do I need to be home?",
     "No. Leave your lights by the door or in the garage, and make sure I can reach an outdoor outlet. I'll text you a photo when it's done."),
    ("How do I pay?",
     "No deposit. You pay once your lights are up, by e-transfer or cash."),
    ("Why are you cheaper than the big companies?",
     "They rent you their lights for the season and charge for them every year. I hang the lights you already own, and I'm a one-person local business with no office or sales team."),
]

# ---------------------------------------------------------------- structured data
BUSINESS = {
    "@type": "HomeAndConstructionBusiness",
    "@id": f"{SITE}/#business",
    "name": "Port City Christmas Lights",
    "description": f"Christmas light hanging for homes in Greater Saint John, New Brunswick. Karan hangs the lights you already own, with every strand tested and a neat, secure install. Starts at ${START_PRICE}. Same-day appointments available.",
    "url": f"{SITE}/",
    "image": f"{SITE}/og-image.png",
    "logo": f"{SITE}/apple-touch-icon.png",
    "telephone": "+1-506-799-2790",
    "priceRange": f"${START_PRICE} to $350+",
    "currenciesAccepted": "CAD",
    "paymentAccepted": "Cash, Interac e-Transfer",
    "address": {"@type": "PostalAddress", "addressLocality": "Saint John", "addressRegion": "NB", "addressCountry": "CA"},
    "areaServed": [{"@type": "City", "name": f"{a['name']}, NB", "url": f"{SITE}/service-areas/{a['slug']}/"} for a in AREAS]
                  + [{"@type": "Place", "name": f"{p}, NB"} for p in ["Lakeside", "Smithtown", "Nauwigewauk", "Norton"]],
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "08:00", "closes": "20:00"}],
    "founder": {"@id": f"{SITE}/#karan"},
    "sameAs": ["https://www.facebook.com/portcitychristmaslights", "https://www.instagram.com/portcitychristmaslights/", GOOGLE_PROFILE],
    "knowsAbout": ["Christmas light installation", "Holiday lighting", "Permanent outdoor lighting installation", "Govee permanent outdoor lights"],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Christmas light hanging",
        "itemListElement":
            [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "CAD", "itemOffered": {"@id": f"{SITE}/#service"}} if p else
             {"@type": "Offer", "name": n + " home", "description": "Custom quote from a photo", "itemOffered": {"@id": f"{SITE}/#service"}}
             for n, p in PRICES]
            + [{"@type": "Offer", "name": n + (" (each)" if e else ""), "price": p, "priceCurrency": "CAD"} for n, p, e in EXTRAS]
            + [{"@type": "Offer", "name": "Permanent light installation (Govee and similar)", "description": "Custom quote from a photo", "itemOffered": {"@id": f"{SITE}/#permanent"}}],
    },
}
PERSON = {"@type": "Person", "@id": f"{SITE}/#karan", "name": "Karan", "jobTitle": "Owner and installer",
          "worksFor": {"@id": f"{SITE}/#business"}}
WEBSITE = {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "Port City Christmas Lights",
           "inLanguage": "en-CA", "publisher": {"@id": f"{SITE}/#business"}}


def service(areas):
    return {
        "@type": "Service", "@id": f"{SITE}/#service" if len(areas) > 1 else None,
        "serviceType": "Christmas light installation",
        "name": "Christmas light hanging",
        "description": "I hang your own Christmas lights on single and two-storey homes, test every strand and run cords to your outlet. Lights can be supplied if needed.",
        "provider": {"@id": f"{SITE}/#business"},
        "areaServed": [f"{a}, NB" for a in areas],
        "offers": {"@type": "Offer", "price": str(START_PRICE), "priceCurrency": "CAD", "description": "Minimum job price"},
    }


PERMANENT_SERVICE = {
    "@type": "Service", "@id": f"{SITE}/#permanent",
    "serviceType": "Permanent outdoor lighting installation",
    "name": "Govee permanent light installation",
    "description": "Installation of Govee and similar permanent outdoor lights along the roofline. Customer can supply the kit, or it can be supplied. Custom quote from a photo.",
    "provider": {"@id": f"{SITE}/#business"},
    "areaServed": [f"{a['name']}, NB" for a in AREAS],
    "url": f"{SITE}/permanent-lights/",
}


def breadcrumbs(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(trail)]}


def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def ld(nodes):
    nodes = [{k: v for k, v in n.items() if v is not None} for n in nodes]
    data = json.dumps({"@context": "https://schema.org", "@graph": nodes}, indent=2, ensure_ascii=False)
    return f'<script type="application/ld+json">\n{data}\n  </script>'


# ---------------------------------------------------------------- layout
NAV = [("Pricing", "/pricing/"), ("Permanent lights", "/permanent-lights/"), ("Service areas", "/service-areas/"), ("Reviews", "/#reviews"), ("FAQ", "/faq/")]
FB = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.5 1.6-1.5h1.7V4.4c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.1v2.4H7.7V14h2.7v8z"/></svg>'
IG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
SOCIAL = (f'<a class="social-link" href="https://www.facebook.com/portcitychristmaslights" target="_blank" rel="noopener">{FB} Facebook</a> &nbsp; '
          f'<a class="social-link" href="https://www.instagram.com/portcitychristmaslights/" target="_blank" rel="noopener">{IG} Instagram</a>')


def nav_links(path):
    return "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{n}</a>' for n, h in NAV)


def layout(*, path, title, description, body, schema, og_title=None, index=True):
    url = SITE + path
    if index:
        schema = schema + [{
            "@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": description,
            "inLanguage": "en-CA", "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": f"{SITE}/#business"},
            "dateModified": TODAY}]
    robots = "index, follow, max-image-preview:large, max-snippet:-1" if index else "noindex, follow"
    canonical = f'<link rel="canonical" href="{url}">' if index else ""
    area_links = "<br>".join(f'<a href="/service-areas/{a["slug"]}/">{a["name"]}</a>' for a in AREAS)
    return f"""<!doctype html>
<!-- Generated by src/build.py. Edit the files in src/, then run: python src/build.py -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  {canonical}
  <meta name="robots" content="{robots}">
  <meta name="google-site-verification" content="P151AKQfPSG1wQbQof6HxM4MtWVv_O-pmnW42BDxnn8">
  <meta name="author" content="Karan, Port City Christmas Lights">
  <meta name="theme-color" content="#0b1424">
  <meta name="geo.region" content="CA-NB">
  <meta name="geo.placename" content="Saint John">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Port City Christmas Lights">
  <meta property="og:title" content="{og_title or title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Port City Christmas Lights: a house lit up with Christmas lights">
  <meta property="og:locale" content="en_CA">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="sitemap" type="application/xml" href="/sitemap.xml">
  {ld(schema)}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

  <header class="nav" id="top">
    <div class="wrap nav-inner">
      <a href="/" class="logo" aria-label="Port City Christmas Lights home">
        <span class="logo-mark" aria-hidden="true">
          <i></i><i></i><i></i>
        </span>
        <span class="logo-text">Port City<small>Christmas Lights</small></span>
      </a>
      <nav class="nav-links" aria-label="Main">
{nav_links(path)}
      </nav>
      <div class="nav-cta">
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <a class="btn btn-primary" href="/quote/">Get a quote</a>
        <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
      </div>
    </div>
    <nav class="mobile-menu" id="mobile-menu" aria-label="Mobile" hidden>
{nav_links(path)}
        <a href="/quote/">Get a free quote</a>
        <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </nav>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="footer">
    <div class="wrap footer-grid">
      <div>
        <a href="/" class="logo">
          <span class="logo-mark" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="logo-text">Port City<small>Christmas Lights</small></span>
        </a>
        <p>Christmas light hanging for homes in Greater Saint John, New Brunswick. Your lights, hung right.</p>
        <p><a href="/pricing/">Pricing</a> · <a href="/permanent-lights/">Permanent lights</a> · <a href="/faq/">FAQ</a> · <a href="/quote/">Free quote</a> · <a {review_link_attrs()}>Leave a review</a></p>
      </div>
      <div>
        <h3 class="footer-h">Contact</h3>
        <p>Karan<br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>7 days a week, 8am to 8pm</p>
        <p>{SOCIAL}</p>
      </div>
      <div>
        <h3 class="footer-h"><a href="/service-areas/">Service areas</a></h3>
        <p>{area_links}</p>
      </div>
    </div>
    <p class="wrap copyright">© <span id="year">{date.today().year}</span> Port City Christmas Lights. All rights reserved. · Prices and info updated {UPDATED}.</p>
  </footer>

  <!-- Mobile sticky bar -->
  <div class="mobile-bar">
    <a href="tel:{PHONE_TEL}">Call or text</a>
    <a href="/quote/" class="hl">Get a free quote</a>
  </div>

  <script src="/script.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- reusable blocks
def page_hero(h1, lead, trail, eyebrow=None, quote="/quote/"):
    crumbs = " <span aria-hidden=\"true\">›</span> ".join(
        f'<a href="{p}">{n}</a>' for n, p in trail[:-1]) + f' <span aria-hidden="true">›</span> <span aria-current="page">{trail[-1][0]}</span>'
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    return f"""    <section class="page-hero">
      <div class="wrap">
        <nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>
        {eb}
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        <div class="hero-actions">
          <a class="btn btn-primary btn-lg" href="{quote}">Get a free quote</a>
          <a class="btn btn-secondary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
        </div>
      </div>
    </section>"""


def areas_section(heading="Where I hang Christmas lights", tag="h2"):
    cards = "\n".join(
        f'          <a class="area" href="/service-areas/{a["slug"]}/"><h3>{a["name"]}</h3><p>{a["card"]}</p><span class="area-more">Lights in {a["name"]} →</span></a>'
        for a in AREAS)
    return f"""    <section class="section night" id="areas">
      <div class="wrap">
        <div class="section-head light">
          <p class="eyebrow">Greater Saint John</p>
          <{tag}>{heading}</{tag}>
          <p>Local, so I'm close by for installs and quick fixes all season.</p>
        </div>
        <div class="areas">
{cards}
        </div>
        <p class="areas-note">Just outside these areas? <a href="sms:{PHONE_TEL}">Text me</a>. I can often make it work.</p>
      </div>
    </section>"""


def review_fig(name):
    town, text = REVIEWS[name]
    return f"""          <figure class="review">
            <div class="stars-row" role="img" aria-label="5 out of 5 stars">{STAR * 5}</div>
            <blockquote>“{text}”</blockquote>
            <figcaption><strong>{name}</strong><span>{town}</span></figcaption>
          </figure>"""


def faq_section(items, heading=None):
    head = f"""        <div class="section-head">
          <p class="eyebrow dark">Good questions</p>
          <h2>{heading}</h2>
        </div>
""" if heading else ""
    det = "\n".join(f"""          <details>
            <summary>{q}</summary>
            <p>{a}</p>
          </details>""" for q, a in items)
    return f"""    <section class="section" id="faq">
      <div class="wrap narrow">
{head}        <div class="faq">
{det}
        </div>
      </div>
    </section>"""


def price_table():
    rows = "\n".join(f'              <li><b>{n}</b><span>{"$" + p if p else "Custom quote"}</span></li>' for n, p in PRICES)
    extras = "\n".join(f'              <li><b>{n}</b><span>+${p}{e}</span></li>' for n, p, e in EXTRAS)
    return f"""          <div class="price-card">
            <div class="price-top">
              <span>Hanging from</span>
              <strong>${START_PRICE}</strong>
            </div>
            <ul class="price-list price-table">
{rows}
            </ul>
            <ul class="price-list price-table extras">
{extras}
            </ul>
            <p class="fine"><strong class="same-day">Same-day appointments available.</strong> Need lights? I can bring them, and they're added to your quote.</p>
          </div>"""


CTA = part("final-cta")


# ---------------------------------------------------------------- pages
def page_home():
    checks = ["Every strand tested before it goes up", "Single and two-storey homes",
              "Neat, secure install for your type of lights", "Cords run to your outlet, timer set up",
              "No lights? I can bring them, and you keep them", "You don't need to be home",
              "A photo texted to you when it's done", "No deposit. Pay by e-transfer or cash after"]
    checklist = "\n".join(f"            <li>{c}</li>" for c in checks)
    reviews = "\n".join(review_fig(n) for n in REVIEWS)
    area_links = "\n".join(f'            <li><a href="/service-areas/{a["slug"]}/">{a["name"]}</a></li>' for a in AREAS)
    body = "\n\n".join([
        part("hero"),
        f"""    <section class="section alt" id="services">
      <div class="wrap">
        <div class="section-head">
          <h2>Two ways I can help</h2>
          <p>Seasonal lights you already own, or permanent lights that stay up all year.</p>
        </div>
        <div class="services">
          <article class="service">
            <h3>Christmas light hanging</h3>
            <p>Bring your lights up from the basement and I'll get them on the roof. Every strand tested, hung neatly and plugged in, on single and two-storey homes.</p>
            <div class="service-meta"><span class="service-price">From ${START_PRICE}</span><a class="text-link" href="/pricing/">See prices →</a></div>
          </article>
          <article class="service">
            <h3>Permanent lights</h3>
            <p>Govee and similar permanent outdoor lights, installed cleanly along your roofline. Buy the kit yourself, or I can supply it.</p>
            <div class="service-meta"><span class="service-price">Custom quote</span><a class="text-link" href="/permanent-lights/">Learn more →</a></div>
          </article>
        </div>
      </div>
    </section>""",
        f"""    <section class="section" id="how">
      <div class="wrap">
        <div class="section-head">
          <h2>How it works</h2>
          <p>Three steps, and the only thing you carry is the bin of lights.</p>
        </div>
        <ol class="steps">
          <li><span>01</span><h3>Send your address and a photo</h3><p>Text me or use the quote form. I'll confirm a fixed price, usually within a day, without a visit.</p></li>
          <li><span>02</span><h3>Pick a date</h3><p>Same-day appointments are often available, 7 days a week from 8am to 8pm.</p></li>
          <li><span>03</span><h3>Lights go up</h3><p>Every strand tested, hung neatly and plugged in. I text you a photo when it's done.</p></li>
        </ol>
      </div>
    </section>""",
        f"""    <section class="section alt" id="about">
      <div class="wrap split">
        <div>
          <h2>One person, done properly</h2>
          <p>I'm Karan. Port City Christmas Lights is my business and I do every job myself, so when you text, you're talking to the person on the ladder.</p>
          <p>Most people already own plenty of lights. Hanging the ones you have, instead of renting you new ones, is how I keep prices low.</p>
          <div class="signature"><span class="signature-badge" aria-hidden="true">K</span><div><strong>Karan</strong><span>Owner and installer</span></div></div>
        </div>
        <ul class="checklist">
{checklist}
        </ul>
      </div>
    </section>""",
        f"""    <section class="section" id="reviews">
      <div class="wrap">
        <div class="section-head">
          <h2>What neighbours say</h2>
          <p>Five-star reviews from homes in Greater Saint John.</p>
        </div>
        <div class="reviews">
{reviews}
        </div>
{review_cta()}
      </div>
    </section>""",
        f"""    <section class="section alt" id="areas">
      <div class="wrap info-grid">
        <div class="info-card">
          <h2>Where I work</h2>
          <ul class="area-list">
{area_links}
          </ul>
          <p class="info-note">Just outside these areas? <a href="sms:{PHONE_TEL}">Text me</a>. I can often make it work.</p>
        </div>
        <div class="info-card">
          <h2>Get in touch</h2>
          <ul class="contact-lines">
            <li><span>Call or text</span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li><span>Hours</span>7 days a week, 8am to 8pm</li>
            <li><span>Follow along</span>{SOCIAL}</li>
          </ul>
        </div>
      </div>
    </section>""",
        CTA])
    schema = [WEBSITE, BUSINESS, PERSON, service([a["name"] for a in AREAS]), PERMANENT_SERVICE]
    return layout(path="/", title="Christmas Light Installation in Saint John, NB | Port City Christmas Lights",
                  description=f"Christmas light hanging and Govee permanent light installation in Saint John, Rothesay, Quispamsis, Hampton and Grand Bay-Westfield, NB. From ${START_PRICE}.",
                  og_title="Port City Christmas Lights: Your lights. My ladder.", body=body, schema=schema)


PERM_FAQS = [
    ("Do you install Govee permanent lights?",
     "Yes. I install Govee Permanent Outdoor Lights and similar permanent light kits along your roofline, on single and two-storey homes in Greater Saint John."),
    ("Can I buy the lights myself?",
     "Yes. Buy a Govee or similar kit wherever you like and I'll install it. Or I can supply the kit, and its cost is added to your quote."),
    ("How much does permanent light installation cost?",
     "It depends on the length of your roofline and the kit, so every install gets a custom quote. Send a photo of the front of your house to get yours, usually within a day."),
    ("Do permanent lights need screws or nails?",
     "Yes. Permanent lights have to be fastened to the house with small screws or nails. I show you exactly where they'll go before I start."),
    ("Do you install brands other than Govee?",
     "Yes, I install similar permanent outdoor light kits too. Tell me which one you have or are looking at."),
]


def page_permanent():
    trail = [("Home", "/"), ("Permanent lights", "/permanent-lights/")]
    checks = ["Govee Permanent Outdoor Lights and similar kits", "Bring your own kit, or I supply it",
              "Run cleanly and evenly along your roofline", "Fastening points shown to you before I start",
              "Power run neatly to your outdoor outlet", "Single and two-storey homes"]
    checklist = "\n".join(f"            <li>{c}</li>" for c in checks)
    body = "\n\n".join([
        page_hero("Govee permanent light installation in Saint John, NB",
                  "I install Govee and similar permanent outdoor lights on homes across Greater Saint John. Buy the kit yourself or I can supply it. Every install is quoted from a photo of your house.",
                  trail, "Permanent lights", quote="/quote/?service=permanent"),
        f"""    <section class="section">
      <div class="wrap split">
        <div>
          <h2>Permanent lights, installed properly</h2>
          <p>Permanent lights stay up all year and change colour from an app, so you can use them for Christmas, Halloween, game days or every night.</p>
          <p>Getting them straight, secure and neatly powered along a roofline is the hard part. That's the part I do.</p>
        </div>
        <ul class="checklist">
{checklist}
        </ul>
      </div>
    </section>""",
        f"""    <section class="section alt">
      <div class="wrap">
        <div class="section-head"><h2>How it works</h2></div>
        <ol class="steps">
          <li><span>01</span><h3>Send a photo</h3><p>Send a photo of the front of your house and tell me which kit you have, or want.</p></li>
          <li><span>02</span><h3>Get a fixed quote</h3><p>Usually within a day. If I'm supplying the kit, its cost is included.</p></li>
          <li><span>03</span><h3>Install day</h3><p>I install the lights, run the power and make sure everything lights up before I leave.</p></li>
        </ol>
      </div>
    </section>""",
        faq_section(PERM_FAQS, "Permanent light questions"),
        f"""    <section class="nearby">
      <div class="wrap narrow">
        <p class="disclaimer">Govee is a trademark of its owner. Port City Christmas Lights is an independent installer and is not affiliated with or endorsed by Govee.</p>
      </div>
    </section>""",
        CTA])
    return layout(path="/permanent-lights/", title="Govee Permanent Light Installation, Saint John NB | Port City Christmas Lights",
                  description="Govee and similar permanent outdoor light installation in Saint John, Rothesay, Quispamsis, Hampton and Grand Bay-Westfield, NB. Bring your kit or I supply it. Free quote.",
                  body=body, schema=[BUSINESS, PERMANENT_SERVICE, faq_schema(PERM_FAQS), breadcrumbs(trail)])


def page_pricing():
    trail = [("Home", "/"), ("Pricing", "/pricing/")]
    body = "\n\n".join([
        page_hero("Christmas light hanging prices",
                  f"Simple, flat prices based on your house. Starts at <strong>${START_PRICE}</strong>. No deposit, pay once your lights are up.",
                  trail, "Greater Saint John, NB"),
        part("pricing"), CTA])
    return layout(path="/pricing/", title="Christmas Light Hanging Prices | Port City Christmas Lights",
                  description=f"Christmas light hanging prices in Saint John, NB: $200 mini-home, $250 bungalow, $350 large bungalow, custom quote for two-storey. Instant online estimate.",
                  body=body, schema=[BUSINESS, breadcrumbs(trail)])


def page_quote():
    trail = [("Home", "/"), ("Free quote", "/quote/")]
    body = "\n\n".join([
        page_hero("Get your free quote",
                  "Send me your address and a photo of your house and I'll confirm your price, usually within a day. Same-day appointments are available.",
                  trail, "Free · No obligation"),
        part("quote-form")])
    return layout(path="/quote/", title="Free Christmas Light Hanging Quote | Port City Christmas Lights",
                  description=f"Get a free Christmas light hanging quote in Greater Saint John, NB. Text your address and a photo to {PHONE_DISPLAY}. From ${START_PRICE}.",
                  body=body, schema=[BUSINESS, breadcrumbs(trail)])


def page_faq():
    trail = [("Home", "/"), ("FAQ", "/faq/")]
    body = "\n\n".join([
        page_hero("Christmas light hanging FAQ",
                  "Prices, lights, timing, payment and more. Still have a question? Just text me.",
                  trail, "Good questions"),
        faq_section(FAQS), CTA])
    return layout(path="/faq/", title="Christmas Light Hanging FAQ | Port City Christmas Lights",
                  description="Answers about Christmas light hanging in Greater Saint John: cost, supplying lights, timing, roof safety, payment and service areas.",
                  body=body, schema=[BUSINESS, faq_schema(FAQS), breadcrumbs(trail)])


def page_areas():
    trail = [("Home", "/"), ("Service areas", "/service-areas/")]
    body = "\n\n".join([
        page_hero("Christmas light hanging service areas",
                  "I hang Christmas lights in Saint John, Rothesay, Quispamsis, Hampton and Grand Bay-Westfield, plus the communities around them.",
                  trail, "Greater Saint John, NB"),
        areas_section("Pick your town"), CTA])
    return layout(path="/service-areas/", title="Service Areas in Greater Saint John | Port City Christmas Lights",
                  description="Christmas light hanging in Saint John, Rothesay, Quispamsis, Hampton, Grand Bay-Westfield and nearby communities in New Brunswick.",
                  body=body, schema=[BUSINESS, service([a["name"] for a in AREAS]), breadcrumbs(trail)])


def page_town(a):
    name, slug = a["name"], a["slug"]
    path = f"/service-areas/{slug}/"
    trail = [("Home", "/"), ("Service areas", "/service-areas/"), (name, path)]
    places = "".join(f"<li>{p}</li>" for p in a["places"])
    others = " · ".join(f'<a href="/service-areas/{o["slug"]}/">{o["name"]}</a>' for o in AREAS if o is not a)
    review = f"""    <section class="section alt">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow dark">From a neighbour in {name}</p>
          <h2>What customers say</h2>
        </div>
        <div class="reviews single">
{review_fig(a["review"])}
        </div>
{review_cta(name)}
      </div>
    </section>""" if a["review"] else f"""    <section class="section alt">
      <div class="wrap">
{review_cta(name)}
      </div>
    </section>"""
    covered = ", ".join(a["places"][:-1]) + " and " + a["places"][-1]
    town_faqs = [
        (f"Which parts of {name} do you cover?",
         (f"All of {name}, plus nearby " + ", ".join(a["places"][1:-1]) + f" and {a['places'][-1]}" if a["places"][0] == name
          else f"All of {name}, including {covered}") + f". Just outside {name}? Text me at {PHONE_DISPLAY} and I can often make it work."),
        (f"How much does it cost to hang Christmas lights in {name}?",
         f"The same as everywhere I work: $200 for a mini-home or small bungalow, $250 for a bungalow and $350 for a large bungalow or split-level. Two-storey homes get a custom quote. Every job is at least ${START_PRICE}."),
        (f"How do I book in {name}?",
         f"Text your address and a photo of your house to {PHONE_DISPLAY}, or use the quote form. I'll confirm your price, usually within a day, and same-day appointments are available."),
        FAQS[1], FAQS[6], FAQS[7],
    ]
    body = "\n\n".join(x for x in [
        page_hero(f"Christmas light hanging in {name}, NB",
                  f"{a['intro']} Starts at <strong>${START_PRICE}</strong>. <strong>Same-day appointments available.</strong>",
                  trail, "Your lights. My ladder."),
        f"""    <section class="section">
      <div class="wrap town-grid">
        <div>
          <p class="eyebrow dark">Local service</p>
          <h2>Where I work in {name}</h2>
          <ul class="town-places">{places}</ul>
          <h3>What you get</h3>
          <ul class="town-points">
            <li>I hang the lights you already own, on single and two-storey homes</li>
            <li>Every strand tested before it goes up</li>
            <li>Neat, secure install: clips for regular strands, proper fastening for permanent lights</li>
            <li>Cords run neatly to your outlet, timer set up if you have one</li>
            <li>No lights? I can bring them, and you keep them</li>
            <li>You don't need to be home. I text you a photo when it's done</li>
          </ul>
        </div>
        <div>
{price_table()}
          <p class="town-est"><a class="btn btn-primary btn-block" href="/pricing/#estimator">Get an instant estimate</a></p>
        </div>
      </div>
    </section>""",
        review,
        faq_section(town_faqs, f"Questions from {name}"),
        f"""    <section class="section alt nearby">
      <div class="wrap narrow">
        <p><strong>Also serving:</strong> {others}</p>
        <p><a href="/quote/?area={name.replace(' ', '+')}">Get a free quote for your {name} home →</a></p>
      </div>
    </section>""",
        CTA] if x)
    return layout(path=path, title=f"Christmas Light Hanging in {name}, NB | Port City Christmas Lights",
                  description=(f"Christmas light hanging in {', '.join(a['places'][:-1])} and {a['places'][-1]}, NB. Your own lights hung from ${START_PRICE}. Same-day appointments: {PHONE_DISPLAY}."
                               if slug == "hampton" else
                               f"Christmas light hanging in {name}, NB. I hang your own lights, every strand tested. From ${START_PRICE}, same-day appointments. Call or text {PHONE_DISPLAY}."),
                  body=body, schema=[BUSINESS, service([name] + (a["places"][1:] if slug == "hampton" else [])),
                                     faq_schema(town_faqs), breadcrumbs(trail)])


def write(path, html):
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")
    return path


def page_404():
    body = f"""    <section class="page-hero">
      <div class="stars" aria-hidden="true"></div>
      <div class="wrap">
        <p class="eyebrow">Page not found</p>
        <h1>This page has gone dark.</h1>
        <p class="lead">The link may be old. Here's where you probably wanted to go:</p>
        <div class="hero-actions">
          <a class="btn btn-primary btn-lg" href="/">Home</a>
          <a class="btn btn-outline btn-lg" href="/pricing/">Pricing</a>
          <a class="btn btn-outline btn-lg" href="/quote/">Free quote</a>
        </div>
      </div>
    </section>

{areas_section()}"""
    return layout(path="/404.html", title="Page not found | Port City Christmas Lights",
                  description="Page not found. Christmas light hanging in Greater Saint John, NB.",
                  body=body, schema=[BUSINESS], index=False)


def llms_txt(paths):
    names = {"/": "Home: overview, what's included, how it works, reviews", "/pricing/": "Pricing and instant estimator",
             "/service-areas/": "Service areas", "/faq/": "FAQ", "/permanent-lights/": "Govee and similar permanent light installation (custom quote)", "/quote/": "Free quote: quote form, phone and text"}
    pages = []
    for p in paths:
        town = next((a["name"] for a in AREAS if p == f"/service-areas/{a['slug']}/"), None)
        pages.append(f"{'  ' if town else ''}- [{town or names[p]}]({SITE}{p})")
    prices = "\n".join(f"- {n}: {'$' + p if p else 'custom quote from a photo'}" for n, p in PRICES)
    extras = "\n".join(f"- {n}: +${p}{e}" for n, p, e in EXTRAS)
    areas = "\n".join(f"- {a['name']}: {', '.join(a['places'])}" for a in AREAS)
    faqs = "\n\n".join(f"### {q}\n{a}" for q, a in FAQS)
    return f"""# Port City Christmas Lights

> Christmas light hanging for homes in Greater Saint John, New Brunswick, Canada (Saint John, Rothesay, Quispamsis, Hampton and Grand Bay-Westfield). A one-person local business run by Karan, who hangs the lights homeowners already own. Jobs start at ${START_PRICE} CAD. Same-day appointments are available.

Last updated: {UPDATED}

## Contact

- Phone and text: {PHONE_DISPLAY} (+1-506-799-2790)
- Hours: 7 days a week, 8am to 8pm
- Website: {SITE}/
- Google Business Profile: {GOOGLE_PROFILE}
- Facebook: https://www.facebook.com/portcitychristmaslights
- Instagram: https://www.instagram.com/portcitychristmaslights/

## Service

- Hangs the customer's own Christmas lights on single and two-storey homes
- Tests every strand before it goes up
- Neat, secure install: regular strands go up with clips made for gutters and shingles; permanent lights (like Govee) are fastened with small nails or screws, and the customer is shown where first
- Runs cords neatly to the outlet and sets up the customer's timer
- Can supply lights if the customer has none or not enough; these are priced separately and the customer keeps them
- Also installs Govee and similar permanent outdoor lights (customer's own kit or supplied), custom quote from a photo
- Hanging season runs from early November into December

## Pricing (CAD)

- Minimum job: ${START_PRICE}
{prices}
{extras}

Final price is confirmed after a photo or address check, usually within a day and without a visit. No deposit. Payment by Interac e-Transfer or cash once the lights are up.

## Service areas

{areas}
- Just outside these areas: text to ask

## How to book

1. Use the instant estimator on the website, or text your address to {PHONE_DISPLAY}
2. Text a photo of the front of the house to confirm the price
3. Pick a date (same-day often available)
4. Leave the lights by the door or in the garage; the customer doesn't need to be home

## FAQ

{faqs}

## Pages

""" + "\n".join(pages) + "\n"


def main():
    paths = [
        write("/", page_home()),
        write("/pricing/", page_pricing()),
        write("/service-areas/", page_areas()),
        *[write(f"/service-areas/{a['slug']}/", page_town(a)) for a in AREAS],
        write("/permanent-lights/", page_permanent()),
        write("/faq/", page_faq()),
        write("/quote/", page_quote()),
    ]
    (ROOT / "404.html").write_text(page_404(), encoding="utf-8", newline="\n")
    (ROOT / "llms.txt").write_text(llms_txt(paths), encoding="utf-8", newline="\n")
    urls = "\n".join(f"  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>" for p in paths)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n',
        encoding="utf-8", newline="\n")
    print("Built", len(paths), "pages:", ", ".join(paths))


if __name__ == "__main__":
    main()
