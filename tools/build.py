#!/usr/bin/env python3
"""Generates the case-study pages. Run from repo root: python3 tools/build.py

IMPORTANT — DO NOT RUN THIS WITHOUT READING THIS NOTE.

As of 2026-10-23 the case-*.html pages are ALSO hand-maintained: they were
redesigned directly in the repo (dark mode, new layout, lowercase type) and
this script's case template no longer matches them. Running it would discard
that redesign. The SEO/social tags on the live pages were likewise patched in
place, not generated here.

index.html, work.html and about.html are hand-maintained too.
They were edited directly in the repo and this script's templates for them are
stale, so a full build would REVERT that work. Those three are therefore opt-in:

Nothing regenerates by default any more. You must opt in explicitly:

    python3 tools/build.py              -> refuses, explains, exits
    python3 tools/build.py --cases      -> overwrite case-*.html  (loses redesign)
    python3 tools/build.py --all        -> overwrite all 9 pages  (loses more)

If you only need robots.txt/sitemap.xml, use --seo, which touches nothing else.

Content sources: Radhika's Framer site + Behance profile (see CONTENT-NOTES.md)."""
import os, sys, glob, html
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import INTRO, IMPACT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# Must be the host that serves 200 directly: the bare domain 308-redirects to
# www, and social scrapers do not follow redirects when fetching og:image.
SITE = "https://www.radhikaatolia.website"
EMAIL = "radhikaselement@gmail.com"
GMAIL = ("https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=radhikaselement@gmail.com"
         "&amp;su=Hii%20Radhika%2C%20we%20would%20like%20to%20discuss%20your%20availability!")
BEHANCE = "https://www.behance.net/radhikaselement"
LINKEDIN = "https://www.linkedin.com/in/radhikaatolia/"
RESUME_NAV = "https://drive.google.com/file/d/1EbfWYlFSqeKG8F6jiqInrfgAG0uC05uF/view?usp=sharing"
RESUME_DL = "https://drive.google.com/file/d/1EbfWYlFSqeKG8F6jiqInrfgAG0uC05uF/view?usp=sharing"

def F(i, ext="webp"): return f"assets/framer/{i}.{ext}"
def B(slug, n, ext="webp"): return f"assets/behance/{slug}/{n:02d}.{ext}"

_dims = {}
def dims(p):
    if p not in _dims:
        if p.endswith(".svg"):
            import re
            s = open(p, encoding="utf8").read(2000)
            m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', s)
            _dims[p] = (int(float(m.group(1))), int(float(m.group(2)))) if m else (550, 405)
        else:
            _dims[p] = Image.open(p).size
    return _dims[p]

def img(p, alt, cls="", eager=False, extra=""):
    w, h = dims(p)
    c = f' class="{cls}"' if cls else ""
    lz = "" if eager else 'loading="lazy" '
    ex = (" " + extra) if extra else ""
    return f'<img{c} src="{p}" width="{w}" height="{h}" alt="{html.escape(alt)}" {lz}decoding="async"{ex}>'

def shot(p, alt, grp, cls=""):
    return f'<a class="shot {cls}" href="{p}" data-lb="{grp}" data-reveal="up">{img(p, alt)}</a>'

def edge_color(p):
    im = Image.open(p).convert("RGB")
    r, g, b = im.getpixel((4, 4))
    return f"#{r:02x}{g:02x}{b:02x}"

# ---------------------------------------------------------------- data
PROJECTS = [
 dict(slug="jugnoo-vehicle-branding", page="case-jugnoo.html", n="01",
      title="Verification and Incentive System", cs_title="Jugnoo — Vehicle Branding",
      blurb="A system that verifies vehicle branding daily through AI and rewards consistency through a series of incentive structure, designed to balance business compliance needs with driver trust and retention.",
      cat="product", tags=["Product design", "Mobile app", "UX research", "Case study"], year="2026",
      cover=F("rKOe2JHnERPyvkVrDf6527gXQ20"), bg="#FFE9DC", fg="#1E1109",
      behance="https://www.behance.net/gallery/255879977/Vehicle-Branding-Jugnoo", pub="September 18, 2026",
      fields="Interaction Design · Product Design · UI/UX", stats=(5, 41),
      role="Product Designer", timeline="6 weeks", team="Jungleworks · Jugnoo", tools="Figma"),
 dict(slug="plant-parents", page="case-plantparents.html", n="02",
      title="E-Commerce & Expert-Booking Platform", cs_title="PlantParents — E-Commerce Platform",
      blurb="Designed an end-to-end marketplace experience for discovering plants, shopping from nurseries, and booking plant-care experts. I worked across user flows, information architecture, wireframes, and responsive high-fidelity UI.",
      cat="product web", tags=["Web design", "E-commerce", "UX research", "Case study"], year="2025",
      cover=F("kE8fw0AakCNkQWW83Ua9I9Aoc8I"), bg="#003324", fg="#E7F4EE",
      behance="https://www.behance.net/gallery/233636525/Plant-Parents-Plant-and-Expertise-at-your-doorstep", pub="August 31, 2025",
      fields="UI/UX · Web Design · Interaction Design", stats=(21, 237),
      role="Product Designer", timeline="End-to-end", team="Concept project", tools="Figma"),
 dict(slug="connect-b2b-feedback", page="case-connect.html", n="03",
      title="Connect — B2B customer feedback management", cs_title="Connect — B2B customer feedback management platform",
      blurb="A feature within Growth Score that lets businesses create personalised feedback forms and distribute them through email campaigns — customise questions, apply scoring, and collect responses in one place.",
      cat="product", tags=["B2B SaaS", "UX / UI", "NPS", "Figma"], year="2026",
      cover=B("connect-b2b-feedback", 1), bg="#E8F3FF", fg="#1E1109",
      behance="https://www.behance.net/gallery/257163815/Connect-A-B2B-customer-feedback-management-platform", pub="October 15, 2026",
      fields="Interaction Design · Product Design · UI/UX", stats=(6, 20),
      role="Product Designer", timeline="8 weeks", team="1 Team Lead, 2 Developers, 1 Product Designer", tools="Figma, Claude Design, ChatGPT"),
 dict(slug="wellspring-healthcare", page="case-wellspring.html", n="04",
      title="Wellspring — a healthcare app", cs_title="Wellspring — A Healthcare UI/UX project",
      blurb="A central hub for all healthcare needs — tracking symptoms, scheduling appointments and managing medications, to make proactive health management more accessible and convenient.",
      cat="product", tags=["Mobile app", "Healthcare", "UI / UX", "Figma"], year="2024",
      cover=B("wellspring-healthcare", 1), bg="#D5EEF2", fg="#0b2c3a",
      behance="https://www.behance.net/gallery/200805151/Wellspring-A-Healthcare-UIUX-project", pub="June 12, 2024",
      fields="UI/UX", stats=(14, 249),
      role="UI/UX Designer", timeline="Case study", team="Solo project", tools="Figma"),
 dict(slug="blue-pottery", page="case-blue-pottery.html", n="05",
      title="Blue Pottery Products", cs_title="Blue Pottery Products",
      blurb="Beautiful and practical blue pottery for everyday use — motifs, patterns and products inspired by Jaipur's blue pottery tradition and its architecture.",
      cat="craft", tags=["Product design", "Motifs & patterns", "Craft"], year="2024",
      cover=B("blue-pottery", 1), bg="#2C44DB", fg="#ffffff",
      behance="https://www.behance.net/gallery/200571291/Blue-Pottery-Products", pub="June 8, 2024",
      fields="Product Design", stats=(20, 239),
      role="Designer", timeline="Personal project", team="Solo project", tools="Illustration, product design"),
 dict(slug="elementals-poster", page="case-elementals.html", n="06",
      title="Disney's Elementals Poster", cs_title="Disney's Elementals Poster",
      blurb="A fan poster for Disney Pixar's Elemental — “Opposites react” — illustrated in Adobe Illustrator with a Hindi-lettered title.",
      cat="illustration", tags=["Illustration", "Poster", "Adobe Illustrator"], year="2024",
      cover=B("elementals-poster", 1), bg="#140A0A", fg="#ffffff",
      behance="https://www.behance.net/gallery/200146141/Disneys-Elementals-Poster", pub="June 8, 2024",
      fields="Graphic Design · Illustration", stats=(17, 170),
      role="Illustrator", timeline="Personal project", team="Solo project", tools="Adobe Illustrator"),
]
TLDR = {'jugnoo-vehicle-branding': ('Verify auto-rickshaw branding every day without losing driver trust.', 'AI video verification, a ₹10 daily payout, a ₹100 reward for every 30-day streak, and fair edge cases (2 attempts a day, 1 skip per 15 days).', 'Incentives are part of the experience — the numbers deserve as much design as the screens.'), 'plant-parents': ('Buying plants online is easy. Keeping them alive isn’t.', 'An end-to-end marketplace: same-day delivery from local nurseries plus bookable plant-care experts — research, personas, IA, responsive hi-fi UI.', 'People don’t just want a product, they want reassurance and a feeling of success.'), 'connect-b2b-feedback': ('Star ratings can’t ask the specific questions a business actually needs answered.', 'A feedback-form builder inside Growth Score: reusable templates, scoring, and email campaigns — in 8 weeks with 2 developers and a team lead.', 'Estimated potential: 10–15% churn reduction and 5–15% annual revenue uplift.'), 'wellspring-healthcare': ('Managing your health takes a backseat in a fast-paced life.', 'A single hub to track symptoms, schedule appointments and manage medications — taken from discovery through to testing.', 'User needs over aesthetics. Iterate. Less is more.'), 'blue-pottery': ('Blue pottery is treated as a delicate showpiece.', 'Motifs, patterns and a six-colour palette turned into everyday objects: jewelry box, table clocks, coffee mugs, gifting boxes.', 'Beautiful and practical can be the same thing.'), 'elementals-poster': ('A fan poster for Disney Pixar’s Elemental.', '“Opposites react” — water meets fire, illustrated in Adobe Illustrator with a Devanagari title.', 'A small, fun craft piece.')}
for p in PROJECTS:
    p["tldr"] = TLDR[p["slug"]]
    p["impact"] = IMPACT[p["slug"]]
    p["intro"] = INTRO[p["slug"]]
    p["deck"] = sorted(glob.glob(f"assets/behance/{p['slug']}/*"))
    # the cover is reused as board 01 on some projects; don't show it twice
    p["boards"] = [d for d in p["deck"] if d != p["cover"]]

# --------------------------------------------------------------- shared
CURTAIN = '''<div class="curtain" aria-hidden="true"><span class="curtain__tag">Radhika Atolia</span><p class="curtain__q"></p><i class="curtain__bar"></i></div>
<script>(function(){var Q=["Pixels are just tiny opinions.","Ctrl+Z works on designs. Not on Mondays.","Lorem ipsum dolor sit… hire me.","Hold on, let me ChatGPT this.","final_final_v7 is a design methodology.","Making messy problems simple. On purpose.","This button was 2px off. Fixed it. You’re welcome.","Kerning is my cardio.","Hiring a designer: 10/10, would recommend.","It’s not a bug. It’s an unresearched feature.","Loading… still faster than a 5-step signup.","I put the ‘fun’ in ‘functional requirements’.","No users were harmed making this portfolio.","Two attempts a day. Zero excuses."];var l=+sessionStorage.getItem('rq'),n=sessionStorage.getItem('nq'),i;if(n!==null&&Q[+n]){i=+n}else{do{i=Math.floor(Math.random()*Q.length)}while(i===l)}try{sessionStorage.setItem('rq',i);sessionStorage.removeItem('nq')}catch(e){}window.__Q=Q;document.currentScript.previousElementSibling.querySelector('.curtain__q').textContent=Q[i];})();</script>'''

def og_card(p):
    """A 1200x630 JPEG preview per project.

    The project covers are webp, and WhatsApp/LinkedIn do not reliably render
    webp previews, so flatten each cover onto its brand colour once at build
    time and point og:image at the jpeg instead."""
    os.makedirs("assets/og", exist_ok=True)
    out = f"assets/og/{p['slug']}.jpg"
    if (not os.path.exists(out)
            or os.path.getmtime(out) < os.path.getmtime(p["cover"])):
        W, H = 1200, 630
        canvas = Image.new("RGB", (W, H), p["bg"])
        im = Image.open(p["cover"]).convert("RGBA")
        im.thumbnail((W - 90, H - 90), Image.LANCZOS)
        canvas.paste(im, ((W - im.width) // 2, (H - im.height) // 2), im)
        canvas.save(out, "JPEG", quality=86, optimize=True)
    return out

def head(title, desc, page="", og_path="assets/og.jpg"):
    """`page` is the clean URL path: "" for home, "work", "case-jugnoo"."""
    og = f"{SITE}/{og_path}"
    w, h = dims(og_path)
    url = f"{SITE}/{page}" if page else f"{SITE}/"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#F8F6F3">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Radhika Atolia"><meta property="og:url" content="{url}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{og}"><meta property="og:image:secure_url" content="{og}"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="{w}"><meta property="og:image:height" content="{h}"><meta property="og:image:alt" content="{html.escape(title)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{og}">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="96x96" href="/assets/favicon-96.png"><link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;500;600;700&family=Parkinsans:wght@400;500;600;700&family=Fragment+Mono&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="progress"><i></i></div>
'''

def url_of(page):
    """Canonical path for a page file. cleanUrls means "work.html" 308-redirects
    to "/work", so links must use the destination, never the .html form."""
    return "/" if page == "index.html" else "/" + page.replace(".html", "")

def nav(active=""):
    def a(href, label, k):
        ac = ' class="active"' if active == k else ""
        return f'<a href="{href}"{ac}>{label}</a>'
    return f'''<header class="nav"><div class="nav__inner">
  <a href="/" class="nav__brand">Radhika</a>
  <nav class="nav__links">{a("/work","Work","work")}{a("/about","About","about")}<a href="{RESUME_NAV}" target="_blank" rel="noopener">Resume</a></nav>
  <button class="nav__toggle" aria-label="Menu">☰</button>
</div></header>
'''

def footer():
    """Matches the hand-maintained footer on index/work/about.
    Copy-email behaviour lives in script.js, so there is no inline script here."""
    return f'''<footer class="footer"><div class="wrap">
  <h2 class="footer__title">Let's Connect</h2>
  <div class="footer__email">
    <span class="email-text">{EMAIL}</span>
    <button class="email-copy" title="Copy email" aria-label="Copy email">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
      </svg>
    </button>
  </div>
  <div class="footer__links">
    <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
    <span class="dot">•</span>
    <a href="{BEHANCE}" target="_blank" rel="noopener">Behance</a>
    <span class="dot">•</span>
    <a href="{RESUME_NAV}" target="_blank" rel="noopener">Resume</a>
  </div>
  <p class="footer__note">Radhika Atolia · © <span id="yr"></span></p>
</div></footer>
<button class="totop" aria-label="Back to top">↑</button>
<div class="toast" role="status"></div>
<script src="script.js"></script>
</body></html>
'''

def contact():
    return f'''<section class="contact" id="contact"><div class="wrap">
  <div class="cpanel" data-reveal="flip" data-tilt="2">
    <span class="eyebrow">Let’s talk</span>
    <h2 data-split>Have a messy problem? <em>Let’s untangle it.</em></h2>
    <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
    <div class="cpanel__btns">
      <a class="btn" href="{GMAIL}" target="_blank" rel="noopener"><span>Say hello</span><span class="arr">→</span></a>
      <a class="btn btn--ghost" href="{RESUME_DL}" target="_blank" rel="noopener"><span>Download Resume</span></a>
      <a class="btn btn--ghost" href="{BEHANCE}" target="_blank" rel="noopener"><span>Behance</span></a>
      <a class="btn btn--ghost" href="{LINKEDIN}" target="_blank" rel="noopener"><span>LinkedIn</span></a>
    </div>
    <img class="sk float" src="{F('33oMeuZudc2ErkmciG1owvxt8k')}" alt="" width="300" height="300" loading="lazy">
  </div>
</div></section>
<footer class="footer"><div class="wrap">
  <span>© <span id="yr">2026</span> Radhika Atolia · Product designer</span>
  <span><a href="{BEHANCE}" target="_blank" rel="noopener">Behance</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a><a href="mailto:{EMAIL}">Email</a><a href="{RESUME_NAV}" target="_blank" rel="noopener">Resume</a></span>
</div></footer>
<div class="hire"><button class="hire__b" aria-expanded="false"><i></i>Hire Radhika</button>
 <div class="hire__m"><p>Let’s make something clear &amp; kind.</p>
  <button class="copy" data-copy="{EMAIL}">{EMAIL} <span>copy</span></button>
  <a href="{RESUME_DL}" target="_blank" rel="noopener">Download resume ↓</a>
  <a href="{BEHANCE}" target="_blank" rel="noopener">Behance ↗</a>
  <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a></div></div>
<div class="toast" role="status"></div>
<button class="totop" aria-label="Back to top">↑</button>
<script src="script.js"></script>
</body></html>
'''

def card(p, n):
    tags = "".join(f"<li>{t}</li>" for t in p["tags"])
    mbg = edge_color(p["cover"])
    return f'''<article class="scard" style="--n:{n};--bg:{p['bg']};--fg:{p['fg']};--mbg:{mbg}">
  <div class="scard__in">
    <div class="scard__txt">
      <div><span class="scard__no">{p['n']} / 06 · {p['year']}</span><h3>{html.escape(p['title'])}</h3><p>{html.escape(p['blurb'])}</p></div>
      <div><ul class="tags">{tags}</ul><a class="btn btn--orange" href="{url_of(p["page"])}"><span>View case study</span><span class="arr">→</span></a></div>
    </div>
    <a class="scard__media" href="{url_of(p["page"])}" aria-label="{html.escape(p['title'])}">{img(p['cover'], p['title'], extra='style="object-fit:contain"')}<span class="badge">Open <span>↗</span></span></a>
  </div>
</article>'''

def bh_strip():
    rows = "".join(
        f'<li><a href="{p["behance"]}" target="_blank" rel="noopener"><em>{p["n"]}</em><span>{html.escape(p["cs_title"])}</span><small>{p["stats"][1]} views ↗</small></a></li>'
        for p in PROJECTS)
    return f'''<div class="bh" data-reveal="up"><div class="bh__grid">
  <div><span class="eyebrow">Also on Behance</span>
    <h2 class="serif-title" style="margin:16px 0 0;color:#fff;font-size:clamp(34px,4.6vw,64px)">Every project, <em class="hl">in full.</em></h2>
    <div class="bh__nums"><div><b data-count="96">96</b><small>Appreciations</small></div><div><b data-count="1050">1050</b><small>Project views</small></div><div><b data-count="23">23</b><small>Followers</small></div></div>
    <a class="btn btn--orange" href="{BEHANCE}" target="_blank" rel="noopener"><span>Open my Behance</span><span class="arr">↗</span></a></div>
  <ul class="bh__list">{rows}</ul>
</div></div>'''

# ---------------------------------------------------------------- index
def build_index():
    cards = "\n".join(card(p, i) for i, p in enumerate(PROJECTS))
    ticker = ["Product Design", "B2B SaaS", "User Research", "Flow Design", "Wireframes", "Prototyping", "High-fidelity UI", "Usability Testing", "Illustration", "Figma"]
    tk = "".join(f"<span>{t}</span>" for t in ticker * 2)
    out = head("Radhika Atolia — Product Designer", "Hi, I am a Product designer - I design digital experiences") + nav()
    out += f'''
<section class="hero" id="top"><div class="hero__bg"><i class="blob b1" data-speed=".08"></i><i class="blob b2" data-speed=".14"></i><i class="blob b3" data-speed=".05"></i></div>
 <div class="wrap hero__grid">
  <div>
    <div class="hero__hi"><span class="wave">👋</span>Hello! <a class="avail" href="#contact"><i></i>Open to new roles</a></div>
    <h1 data-split>I’m <span class="hl">Radhika,<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 14 C 60 2, 110 20, 160 9 S 260 4, 297 12"/></svg></span> a product designer.</h1>
    <p class="hero__rot" data-reveal="up" style="--i:4">Lately I’ve been <b class="rot" data-words="shipping across 5 live products|turning driver rules into fair incentives|making plant care less panicky|designing feedback forms people finish|drawing stickers on the side"></b></p>
    <p class="hero__sub" data-reveal="up" style="--i:5">I enjoy figuring out what isn't working, making sense of messy problems, and turning them into simple, useful experiences.</p>
    <div class="hero__cta" data-reveal="up" style="--i:7"><a class="btn" href="/work"><span>See my work</span><span class="arr">→</span></a><a class="btn btn--ghost" href="/about"><span>About me</span></a></div>
  </div>
  <div class="stage" aria-hidden="true"><div class="stage__in">
    <div class="layer panel-back"></div><div class="layer panel-ring"></div>
    <div class="layer me" data-depth="40">{img(F('1HD21IDvVg0u5qWNxtKJqbgues'), 'Radhika', eager=True)}</div>
    <div class="layer polaroid p1 float" data-depth="90" style="--t:6.5s">{img(F('Xep7AL0114mm5hafmjMNYUKfVRg'), '')}<span>oil pastels</span></div>
    <div class="layer polaroid p2 float" data-depth="70" style="--t:7s;--d:-1s">{img(F('1oBUwEkinIyPIHAH5ORt99Q7mfQ'), '')}<span>boba tea</span></div>
    <div class="layer polaroid p3 float" data-depth="110" style="--t:6s;--d:-2s">{img(F('cPLMoAh4X12bc6mZceBm4EI8uQ'), '')}<span>sunset walks</span></div>
    <div class="layer polaroid p4 float" data-depth="120" style="--t:8s;--d:-3s">{img(F('DaV8kbaZk6IeuLTkaIp42t6XUv8'), '')}<span>avocado toast</span></div>
    <div class="layer polaroid p5 float" data-depth="60" style="--t:7.5s;--d:-.5s">{img(F('KC80iCPjWvtdPz54VskWxuOo4kI'), '')}<span>sad songs</span></div>
    <div class="layer stk float" data-depth="140" style="--t:5.5s">{img(F('Kv5zh9kddZr9EqL8J6ZhDrRgQ'), '')}</div>
    <span class="chip3d c1" data-depth="150">Product designer</span><span class="chip3d c2" data-depth="170">Designing Jugnoo</span>
  </div></div>
 </div>
 <div class="scroll-cue"><span>Scroll</span><i></i></div>
</section>

<div class="ticker" aria-hidden="true"><div class="ticker__track">{tk}</div></div>

<section class="sec statement"><div class="wrap">
  <span class="eyebrow" data-reveal="up">What I do</span>
  <p class="serif-title" style="margin-top:22px" data-scrub>I enjoy figuring out what isn’t working, making sense of messy problems, and turning them into <span class="hl">simple, useful experiences.</span></p>
  <div class="stats" data-stagger>
    <div class="stat"><b data-count="2.5" data-suffix="+">2.5+</b><small>years designing scalable B2B SaaS products</small></div>
    <div class="stat"><b data-count="5">5</b><small>live products shipped in the Jugnoo ecosystem</small></div>
    <div class="stat"><b data-count="6">6</b><small>case studies, end-to-end</small></div>
    <div class="stat"><b data-count="3">3</b><small>teams: Jungleworks · Leapforge · Sheshya</small></div>
  </div>
</div></section>

<section class="sec" id="work" style="padding-top:0"><div class="wrap">
  <div class="work-head"><div><span class="eyebrow" data-reveal="up">Selected work</span><h2 class="serif-title" style="margin-top:18px" data-split>Projects I’ve <em>worked on</em></h2></div>
  <a class="ilink" href="/work" data-reveal="up">All projects →</a></div>
  <div class="stack">{cards}</div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">{bh_strip()}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap about-tz">
  <div class="portrait" data-tilt="7" data-reveal="left"><div class="portrait__card" data-tilt-in>{img(F('EwWAE1s8zDBKUvnxB2yL0X7hWgc'), 'Radhika on a mountain')}</div><span class="tag3d t1">Sunset walks</span><span class="tag3d t2">Designing Jugnoo</span></div>
  <div><span class="eyebrow" data-reveal="up">About me</span>
   <h2 class="serif-title" style="margin:18px 0 24px" data-split>Hii! I’m Radhika.</h2>
   <p class="lead" data-reveal="up" style="--i:2">A product designer focused on creating thoughtful, well structured digital experiences. With 2.5+ years of experience designing scalable B2B SaaS products. Skilled in AI-assisted design workflows to accelerate exploration and iteration. Currently designing Jugnoo.</p>
   <p style="margin-top:28px;--i:3" data-reveal="up"><a class="btn" href="/about"><span>More about me</span><span class="arr">→</span></a></p></div>
</div></section>

<section class="sec why"><div class="wrap">
  <span class="eyebrow" data-reveal="up">Why me</span>
  <h2 class="serif-title" style="margin:18px 0 0" data-split>What your team gets <em>on day one</em></h2>
  <div class="cards4" style="margin-top:40px" data-stagger>
   <div class="card" data-tilt="6"><span class="n">01</span><b>Simpler complex flows</b><p>Breaks multi-step processes into guided, reversible steps — like the Connect form builder, where users can edit, delete and go back without starting over.</p></div>
   <div class="card" data-tilt="6"><span class="n">02</span><b>Fairness &amp; trust by design</b><p>Rules built around real scenarios, not ideal ones — at Jugnoo a genuine miss doesn’t feel like a punishment, so drivers stay.</p></div>
   <div class="card" data-tilt="6"><span class="n">03</span><b>Consistency at scale</b><p>Led UX across On-Demand, Driver, Carpool and Car Rental — five live products that feel like one ecosystem.</p></div>
   <div class="card" data-tilt="6"><span class="n">04</span><b>Faster exploration, with AI</b><p>AI-assisted workflows for exploration and iteration, with human judgement kept on the decisions that matter.</p></div>
  </div>
</div></section>
''' + contact()
    open("index.html", "w", encoding="utf8").write(out)

# ---------------------------------------------------------------- work
def build_work():
    cards = ""
    for p in PROJECTS:
        tags = "".join(f"<li>{t}</li>" for t in p["tags"])
        cards += f'''<a class="pcard" href="{url_of(p["page"])}" data-cat="{p['cat']}" data-reveal="up" data-tilt="6">
 <div class="pcard__img" data-tilt-in style="background:{edge_color(p['cover'])}">{img(p['cover'], p['title'], extra='style="object-fit:contain"')}<span class="go">↗</span></div>
 <div class="pcard__meta"><h3>{html.escape(p['title'])}</h3><span class="yr">{p['n']} · {p['year']}</span></div>
 <p>{html.escape(p['blurb'])}</p><ul class="tags">{tags}</ul></a>'''
    out = head("Work — Radhika Atolia", "Selected product design case studies by Radhika Atolia: Jugnoo, PlantParents, Connect, Wellspring, Blue Pottery and more.") + nav("work")
    out += f'''<section class="page-hero"><div class="wrap">
 <span class="eyebrow" data-reveal="up">Work</span>
 <h1 class="serif-title" style="margin-top:18px" data-split>Projects I’ve <em>worked on</em></h1>
 <p class="lead" style="margin-top:22px" data-reveal="up" style="--i:3">Six projects across B2B SaaS, mobile, e-commerce, craft and illustration — each one a messy problem turned into something simple.</p>
 <div class="filters" data-reveal="up"><button class="on" data-f="all">All</button><button data-f="product">Product</button><button data-f="web">Web</button><button data-f="craft">Craft</button><button data-f="illustration">Illustration</button></div>
</div></section>
<section class="sec" style="padding-top:20px"><div class="wrap"><div class="pgrid">{cards}</div>
 <div style="margin-top:clamp(60px,9vw,120px)">{bh_strip()}</div></div></section>
''' + contact()
    open("work.html", "w", encoding="utf8").write(out)

# ---------------------------------------------------------------- about
def build_about():
    likes = [("Sad Songs", "KC80iCPjWvtdPz54VskWxuOo4kI", "sad", -4), ("Creating new Stickers", "33oMeuZudc2ErkmciG1owvxt8k", "", 3),
             ("Avocado sandwich", "DaV8kbaZk6IeuLTkaIp42t6XUv8", "", -3), ("Going on sunset walks", "cPLMoAh4X12bc6mZceBm4EI8uQ", "", 4),
             ("Drawing with oil pastels", "Xep7AL0114mm5hafmjMNYUKfVRg", "", -4), ("Boba tea", "1oBUwEkinIyPIHAH5ORt99Q7mfQ", "", 3)]
    lk = "".join(f'<div class="like {c}"><div class="like__card" style="--r:{r}deg">{img(F(i), t)}<h4>{t}</h4><span class="no">0{n+1}</span></div></div>' for n, (t, i, c, r) in enumerate(likes))
    jobs = [
     ("Nov 2025 – Present", "Product Designer", "Jungleworks",
      ["Designing and shipping experiences across 5 live products in the Jugnoo ecosystem, focused on reducing friction and improving task completion.",
       "Led UX across On-Demand, Driver, Carpool, and Car Rental, creating consistent and seamless experiences across product verticals."]),
     ("July 2024 – Oct 2025", "User Experience Designer", "LeapforgeDigital",
      ["Designed responsive web and mobile experiences across multiple client products, focusing on usability, interaction, and cross-platform consistency.",
       "Collaborated with developers on UX handoff, ensuring implementation accuracy and reducing UI-related rework."]),
     ("Oct 2023 – Apr 2024", "UI/UX Design Intern", "Sheshya",
      ["Designed the end-to-end Teacher Management module for a cloud-based school management platform.",
       "Conducted user research and usability analysis to shape intuitive user flows."]),
    ]
    jb = "".join(f'<div class="job"><span class="job__date">{d}</span><h3>{co}</h3><h4>{role}</h4><ul>{"".join(f"<li>{b}</li>" for b in bl)}</ul></div>' for d, role, co, bl in jobs)
    tools = ["Figma", "Claude Design", "ChatGPT", "Adobe Illustrator", "User research", "Problem framing", "Flow design", "Wireframes", "Information architecture", "Personas & empathy maps", "Prototyping", "High-fidelity UI", "Usability testing", "Design strategy", "AI-assisted workflows", "Design handoff"]
    tk = "".join(f"<span>{t}</span>" for t in tools)
    out = head("About — Radhika Atolia", "Radhika is a product designer with 2.5+ years of experience designing scalable B2B SaaS products. Currently designing Jugnoo.") + nav("about")
    out += f'''<section class="page-hero"><div class="wrap about-tz">
  <div class="portrait" data-tilt="8" data-reveal="scale"><div class="portrait__card" data-tilt-in>{img(F('EwWAE1s8zDBKUvnxB2yL0X7hWgc'), 'Radhika', eager=True)}</div><span class="tag3d t1">Product designer</span><span class="tag3d t2">India 🇮🇳</span></div>
  <div><span class="eyebrow" data-reveal="up">About</span>
   <h1 class="serif-title" style="margin:18px 0 24px" data-split>Hii ! <em>I’m Radhika,</em> a product designer.</h1>
   <p class="lead" data-reveal="up" style="--i:3">focused on creating thoughtful, well structured digital experiences. With 2.5+ years of experience designing scalable B2B SaaS products. Skilled in AI-assisted design workflows to accelerate exploration and iteration. Currently designing Jugnoo.</p>
   <p data-reveal="up" style="--i:4;color:var(--ink-2);max-width:60ch">A resilient and diligent designer, with a deep passion for crafting user experiences that leave a lasting impression. Believing that design has the power to elevate lives. Skilfully weave creativity and problem-solving abilities to construct digital interfaces that are not only aesthetically pleasing but also intuitively designed.</p>
   <div class="hero__cta" data-reveal="up" style="--i:5;margin-top:26px"><a class="btn" href="{RESUME_DL}" target="_blank" rel="noopener"><span>Download Resume</span><span class="arr">↓</span></a><a class="btn btn--ghost" href="{BEHANCE}" target="_blank" rel="noopener"><span>Behance</span></a><a class="btn btn--ghost" href="{LINKEDIN}" target="_blank" rel="noopener"><span>LinkedIn</span></a></div></div>
</div></section>

<section class="hscroll" style="--n:6"><div class="hscroll__pin">
  <div class="wrap hscroll__head"><span class="eyebrow" data-reveal="up">Off the clock</span><h2 class="serif-title" style="margin-top:16px" data-split>Things I am into <em>recently</em></h2></div>
  <div class="hscroll__track">{lk}</div>
</div></section>

<section class="sec"><div class="wrap">
  <span class="eyebrow" data-reveal="up">Experience</span>
  <h2 class="serif-title" style="margin-top:18px" data-split>Where I have <em>worked before</em></h2>
  <div class="tl"><div class="tl__line"><i></i></div>{jb}</div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <span class="eyebrow" data-reveal="up">Toolkit</span>
  <h2 class="serif-title" style="margin:18px 0 34px;font-size:clamp(30px,4.2vw,56px)" data-split>What I bring along</h2>
  <div class="toolkit" data-stagger>{tk}</div>
  <div style="margin-top:clamp(60px,9vw,110px)">{bh_strip()}</div>
</div></section>
''' + contact()
    open("about.html", "w", encoding="utf8").write(out)

# ---------------------------------------------------------------- case pages
def more_projects(i):
    """The other five projects, starting from the one after this, in a
    horizontally scrollable row of cover + name."""
    others = [PROJECTS[(i + k) % len(PROJECTS)] for k in range(1, len(PROJECTS))]
    fit = 'style="object-fit:contain"'
    cards = "".join(
        '<a class="mcard" href="' + url_of(o["page"]) + '">'
        '<span class="mcard__img">' + img(o["cover"], o["cs_title"], extra=fit) + '</span>'
        '<h3>' + html.escape(o["cs_title"]) + '</h3>'
        '<small>' + o["year"] + ' · ' + o["tags"][0] + '</small></a>'
        for o in others)
    return f'''<section class="more"><div class="wrap">
  <div class="more__head"><h2 class="serif-title" data-split>More <em>projects</em></h2><a class="ilink" href="/work">All projects →</a></div>
  <div class="more__row">{cards}</div>
</div></section>'''

def case_page(p, i, subtitle):
    tags = "".join(f"<li>{t}</li>" for t in p["tags"])
    # Her Behance boards are finished artboards that already carry their own
    # headings and body copy, so they flow in her order with no added captions.
    boards = "".join(shot(d, f"{p['cs_title']} — board {n+1}", p["slug"])
                     for n, d in enumerate(p["boards"]))
    mbg = edge_color(p["cover"])
    out = head(f"{p['cs_title']} — Radhika Atolia", p["blurb"],
               page=p["page"].replace(".html", ""), og_path=og_card(p)) + nav("work")
    out += f'''<article>
<section class="cs-hero" style="--pc:{p['bg']}"><div class="wrap">
 <span class="eyebrow" data-reveal="up">Case study · {p['year']}</span>
 <h1 data-split>{html.escape(p['cs_title'])}</h1>
 <p class="lead" data-reveal="up" style="--i:3">{subtitle}</p>
 <ul class="tags" data-reveal="up" style="--i:4;margin-top:22px">{tags}</ul>
 <div class="cs-cover" data-reveal="scale"><div class="cs-cover__in" style="background:{mbg}">{img(p['cover'], p['cs_title'], eager=True)}</div></div>
 <div class="cs-sum" data-reveal="up">
  <div class="cs-sum__facts"><div><small>My role</small><b>{p['role']}</b></div><div><small>Timeline</small><b>{p['timeline']}</b></div></div>
  <dl class="cs-sum__list">
   <div><dt>The problem</dt><dd>{p['tldr'][0]}</dd></div>
   <div><dt>What I did</dt><dd>{p['tldr'][1]}</dd></div>
   <div><dt>Takeaway</dt><dd>{p['tldr'][2]}</dd></div>
   <div><dt>Impact it created</dt><dd>{p['impact']}</dd></div>
  </dl>
 </div>
 <div class="cs-intro" data-reveal="up"><p>{p['intro']}</p></div>
</div></section>
<section class="cs-boards"><div class="wrap">{boards}</div></section>
</article>
{more_projects(i)}
''' + footer()
    open(p["page"], "w", encoding="utf8").write(out)

def build_cases():
    """One template for all six: cover, role + timeline, problem, what I did,
    takeaway, impact, a short intro, then her Behance boards in order."""
    SUBTITLE = {
     "jugnoo-vehicle-branding": "A system that verifies vehicle branding daily through AI and rewards consistency through a series of incentive structure, designed to balance business compliance needs with driver trust and retention.",
     "plant-parents": "An end-to-end marketplace for discovering plants, shopping from local nurseries, and booking plant-care experts.",
     "connect-b2b-feedback": "Helping businesses collect more meaningful feedback, faster — a B2B feedback-form builder with email campaigns, scoring and response collection.",
     "wellspring-healthcare": "Manage your health effortlessly — track symptoms, make appointments, take meds, and record it all in one place.",
     "blue-pottery": "Beautiful and practical blue pottery products for everyday use — motifs, patterns, and objects inspired by the Jaipur tradition.",
     "elementals-poster": "A fan poster for Disney Pixar’s Elemental — “Opposites react”.",
    }
    for i, p in enumerate(PROJECTS):
        case_page(p, i, SUBTITLE[p["slug"]])

def build_seo():
    """robots.txt + sitemap.xml.

    The sitemap is derived from the pages that are actually linked from the
    site, not a hardcoded list. Listing a page nothing links to tells Google
    "index this" while the site says it does not exist, and such orphans get
    reported as crawled-but-not-indexed. Deriving it means the sitemap stays
    truthful on its own: link a page and it appears, unlink it and it goes.
    """
    import glob as _glob
    pages = {p["page"] for p in PROJECTS} | {"work.html", "about.html"}
    linked = set()
    for f in _glob.glob("*.html"):
        if f in ("header.html", "footer.html"):
            continue  # partials, noindexed in vercel.json
        html_src = open(f, encoding="utf8").read()
        for pg in pages:
            slug = pg.replace(".html", "")
            if f'href="/{slug}"' in html_src or f'href="{pg}"' in html_src:
                linked.add(pg)

    orphans = sorted(pages - linked)
    if orphans:
        print("  note: omitted from sitemap, nothing links to them:",
              ", ".join(orphans))

    ordered = ["index.html", "work.html", "about.html"] + [p["page"] for p in PROJECTS]
    urls = ""
    for pg in ordered:
        if pg != "index.html" and pg not in linked:
            continue
        path = "" if pg == "index.html" else pg.replace(".html", "")
        urls += (f"  <url><loc>{SITE}/{path}</loc><changefreq>monthly</changefreq>"
                 f"<priority>{'1.0' if path == '' else '0.8'}</priority></url>\n")

    open("sitemap.xml", "w", encoding="utf8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}</urlset>\n")
    open("robots.txt", "w", encoding="utf8").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

def main():
    args = set(sys.argv[1:])
    if not args & {"--cases", "--all", "--seo"}:
        print(__doc__)
        print("Refusing to run: no target flag given. See the options above.")
        return 2
    if "--seo" in args and not args & {"--cases", "--all"}:
        build_seo(); print("built: robots.txt, sitemap.xml"); return 0
    print("WARNING: this overwrites hand-edited pages. Ctrl-C now if unsure.")
    if "--all" in args:
        build_index(); build_work(); build_about()
    build_cases(); build_seo()
    print("built:", ", ".join(p["page"] for p in PROJECTS)
          + (", index.html, work.html, about.html" if "--all" in args else "")
          + ", robots.txt, sitemap.xml")
    return 0

if __name__ == "__main__":
    sys.exit(main())
