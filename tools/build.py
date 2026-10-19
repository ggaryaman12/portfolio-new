#!/usr/bin/env python3
"""Generates every page of the site. Run from repo root: python3 tools/build.py
Content sources: Radhika's Framer site + Behance profile (see CONTENT-NOTES.md)."""
import os, glob, html
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SITE = "https://radhikaatolia.vercel.app"
EMAIL = "radhikaselement@gmail.com"
GMAIL = ("https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=radhikaselement@gmail.com"
         "&amp;su=Hii%20Radhika%2C%20we%20would%20like%20to%20discuss%20your%20availability!")
BEHANCE = "https://www.behance.net/radhikaselement"
LINKEDIN = "https://www.linkedin.com/in/radhikaatolia/"
RESUME_NAV = "https://drive.google.com/file/d/1pv8k1CAcRjwX_YjblszEcznRyadkhXmi/view?usp=sharing"
RESUME_DL = "https://drive.google.com/file/d/1mn57kZrvQAOB5N5ocv-0fnTCIip-mqVM/view?usp=drive_link"

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
for p in PROJECTS:
    p["deck"] = sorted(glob.glob(f"assets/behance/{p['slug']}/*"))

# --------------------------------------------------------------- shared
CURTAIN = '''<div class="curtain" aria-hidden="true"><span class="curtain__tag">Radhika Atolia · Product Designer</span><p class="curtain__q"></p><span class="curtain__sub"></span><i class="curtain__bar"></i></div>
<script>(function(){var Q=[["Pixels are just tiny opinions.","— a designer, probably"],["Ctrl+Z works on designs. Not on Mondays.","— every designer, Monday"],["No users were harmed in the making of this portfolio.","— legal, unofficially"],["Lorem ipsum dolor sit… hire me.","— the placeholder text"],["Hold on, let me ChatGPT this.","— a sticker I own"],["final_final_v7 is a design methodology.","— my Figma files"],["Making messy problems simple. On purpose.","— Radhika"],["This button was 2px off. I fixed it. You’re welcome.","— nobody noticed"],["Kerning is my cardio.","— Radhika, mid-sprint"],["Hiring a designer: 10/10 would recommend.","— everyone who did"],["It’s not a bug. It’s an unresearched feature.","— a developer, nervous"],["Good design is invisible. Great design buys you coffee.","— boba, actually"],["I put the ‘fun’ in ‘functional requirements’.","— LinkedIn, humbly"],["Loading… still faster than a 5-step signup.","— drivers, unanimously"],["Two attempts a day. Zero excuses. One streak.","— the Jugnoo system"]];var k='rq',l=+sessionStorage.getItem(k);var i;do{i=Math.floor(Math.random()*Q.length)}while(i===l&&Q.length>1);try{sessionStorage.setItem(k,i)}catch(e){}window.__Q=Q;var c=document.currentScript.previousElementSibling;c.querySelector('.curtain__q').textContent=Q[i][0];c.querySelector('.curtain__sub').textContent=Q[i][1];})();</script>'''

def head(title, desc, page="", og=None):
    og = og or f"{SITE}/assets/og.jpg"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#F8F6F3">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Fragment+Mono&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400;1,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{CURTAIN}
<div class="progress"><i></i></div>
'''

def nav(active=""):
    def a(href, label, k):
        ac = ' class="active"' if active == k else ""
        return f'<a href="{href}"{ac}>{label}</a>'
    return f'''<header class="nav"><div class="nav__inner">
  <a href="index.html" class="nav__brand"><img src="assets/favicon.png" alt="" width="26" height="26">Radhika</a>
  <nav class="nav__links">{a("work.html","Work","work")}{a("about.html","About","about")}<a href="{RESUME_NAV}" target="_blank" rel="noopener">Resume</a><a class="cta" href="#contact">Let’s talk</a></nav>
  <button class="nav__toggle" aria-label="Menu">☰</button>
</div></header>
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
      <div><ul class="tags">{tags}</ul><a class="btn btn--orange" href="{p['page']}"><span>View case study</span><span class="arr">→</span></a></div>
    </div>
    <a class="scard__media" href="{p['page']}" aria-label="{html.escape(p['title'])}">{img(p['cover'], p['title'], extra='style="object-fit:contain"')}<span class="badge">Open <span>↗</span></span></a>
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
    out = head("Radhika Atolia — Product Designer", "Hi, I am a Product designer - I design digital experiences", "home") + nav()
    out += f'''
<section class="hero" id="top"><div class="hero__bg"><i class="blob b1" data-speed=".08"></i><i class="blob b2" data-speed=".14"></i><i class="blob b3" data-speed=".05"></i></div>
 <div class="wrap hero__grid">
  <div>
    <div class="hero__hi"><span class="wave">👋</span>Hello! <a class="avail" href="#contact"><i></i>Open to new roles</a></div>
    <h1 data-split>I’m <span class="hl">Radhika,<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 14 C 60 2, 110 20, 160 9 S 260 4, 297 12"/></svg></span> a product designer.</h1>
    <p class="hero__sub" data-reveal="up" style="--i:5">I enjoy figuring out what isn't working, making sense of messy problems, and turning them into simple, useful experiences.</p>
    <div class="hero__cta" data-reveal="up" style="--i:7"><a class="btn" href="work.html"><span>See my work</span><span class="arr">→</span></a><a class="btn btn--ghost" href="about.html"><span>About me</span></a></div>
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
  <a class="ilink" href="work.html" data-reveal="up">All projects →</a></div>
  <div class="stack">{cards}</div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">{bh_strip()}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap about-tz">
  <div class="portrait" data-tilt="7" data-reveal="left"><div class="portrait__card" data-tilt-in>{img(F('EwWAE1s8zDBKUvnxB2yL0X7hWgc'), 'Radhika on a mountain')}</div><span class="tag3d t1">Sunset walks</span><span class="tag3d t2">Designing Jugnoo</span></div>
  <div><span class="eyebrow" data-reveal="up">About me</span>
   <h2 class="serif-title" style="margin:18px 0 24px" data-split>Hii! I’m Radhika.</h2>
   <p class="lead" data-reveal="up" style="--i:2">A product designer focused on creating thoughtful, well structured digital experiences. With 2.5+ years of experience designing scalable B2B SaaS products. Skilled in AI-assisted design workflows to accelerate exploration and iteration. Currently designing Jugnoo.</p>
   <p style="margin-top:28px;--i:3" data-reveal="up"><a class="btn" href="about.html"><span>More about me</span><span class="arr">→</span></a></p></div>
</div></section>
''' + contact()
    open("index.html", "w", encoding="utf8").write(out)

# ---------------------------------------------------------------- work
def build_work():
    cards = ""
    for p in PROJECTS:
        tags = "".join(f"<li>{t}</li>" for t in p["tags"])
        cards += f'''<a class="pcard" href="{p['page']}" data-cat="{p['cat']}" data-reveal="up" data-tilt="6">
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
def case_page(p, i, sections, subtitle, tags_extra=None):
    prev = PROJECTS[(i - 1) % len(PROJECTS)]; nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    tags = "".join(f"<li>{t}</li>" for t in p["tags"])
    labels = [(sid, lab) for sid, lab, _ in sections] + [("deck", "Full case study (HD)")]
    toc_links = "".join(f'<a href="#{sid}"><em>{n+1:02d}</em><span>{lab}</span></a>' for n, (sid, lab) in enumerate(labels))
    toc = (f'<aside class="toc" aria-label="On this page"><p class="toc__t">On this page</p>'
           f'<div class="toc__list"><i class="toc__bar"><b></b></i>{toc_links}</div>'
           f'<div class="toc__foot"><a href="work.html">← All work</a><a href="{p["behance"]}" target="_blank" rel="noopener">View on Behance ↗</a></div></aside>')
    tocbar = '<nav class="tocbar" aria-label="Sections">' + "".join(f'<a href="#{sid}">{lab}</a>' for sid, lab in labels) + '</nav>'
    body = "".join(f'<section class="cs-sec" id="{sid}" data-no="{n+1:02d}">{h}</section>' for n, (sid, _, h) in enumerate(sections))
    slabs = "".join(shot(d, f"{p['cs_title']} — {n+1}", p["slug"], "bare" if False else "") for n, d in enumerate(p["deck"]))
    mbg = edge_color(p["cover"])
    out = head(f"{p['cs_title']} — Radhika Atolia", p["blurb"], og=f"{SITE}/{p['cover']}") + nav("work")
    out += f'''<article>
<section class="cs-hero" style="--pc:{p['bg']}"><div class="wrap">
 <span class="eyebrow" data-reveal="up">Case study · {p['year']}</span>
 <h1 data-split>{html.escape(p['cs_title'])}</h1>
 <p class="lead" data-reveal="up" style="--i:3">{subtitle}</p>
 <ul class="tags" data-reveal="up" style="--i:4;margin-top:22px">{tags}</ul>
 <p data-reveal="up" style="--i:5;display:flex;gap:12px;flex-wrap:wrap;margin:26px 0 0"><a class="btn" href="#deck"><span>Jump to the HD boards</span><span class="arr">↓</span></a><a class="btn btn--ghost" href="{p['behance']}" target="_blank" rel="noopener"><span>View on Behance</span><span class="arr">↗</span></a></p>
 <div class="cs-cover" data-tilt="3" data-reveal="scale"><div class="cs-cover__in" data-tilt-in style="background:{mbg}">{img(p['cover'], p['cs_title'], eager=True)}</div></div>
 <div class="meta" data-reveal="up"><div><small>My role</small><b>{p['role']}</b></div><div><small>Timeline</small><b>{p['timeline']}</b></div><div><small>Team</small><b>{p['team']}</b></div><div><small>Tools</small><b>{p['tools']}</b></div></div>
</div></section>
<div class="wrap">{tocbar}<div class="cs-layout">
 {toc}
 <div class="cs-body">{body}
  <section class="cs-sec slabs" id="deck" data-no="{len(sections)+1:02d}"><span class="eyebrow">Full case study</span><h2>The whole story, in HD</h2>
   <p>Every board from the Behance case study — tap any image to open it full screen, then use ← → to move through.</p>{slabs}
   <p style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px"><a class="btn btn--orange" href="{p['behance']}" target="_blank" rel="noopener"><span>View on Behance</span><span class="arr">↗</span></a><a class="btn btn--ghost" href="{BEHANCE}" target="_blank" rel="noopener"><span>All projects on Behance</span></a></p>
   <p style="font-family:var(--mono);font-size:12px;color:var(--muted);letter-spacing:.06em">Published {p['pub']} · {p['fields']} · {p['stats'][0]} appreciations · {p['stats'][1]} views on Behance</p>
  </section>
  <div class="next"><a href="{prev['page']}"><small>← Previous</small><b>{html.escape(prev['cs_title'])}</b></a><a class="r" href="{nxt['page']}"><small>Next →</small><b>{html.escape(nxt['cs_title'])}</b></a></div>
 </div>
</div></div>
</article>
''' + contact()
    open(p["page"], "w", encoding="utf8").write(out)

def cards(items, cls="cards3"):
    return f'<div class="{cls}" data-stagger>' + "".join(
        f'<div class="card"><span class="n">{n}</span><b>{t}</b><p>{d}</p></div>' for n, t, d in items) + "</div>"

def build_cases():
    P = {p["slug"]: p for p in PROJECTS}

    # ---------------- Jugnoo (Framer text + assets)
    p = P["jugnoo-vehicle-branding"]
    g = "jug"
    mocks = f'''<div class="mockrow" data-stagger>
 <div class="mock"><div class="grab"></div><h5>Select Upload Options</h5><span class="mb o">Upload from Camera</span><span class="mb o">Upload from Gallery</span><span class="mb o">Cancel</span></div>
 <div class="mock"><h5>Please Wait !</h5><div class="spin"></div><p><b>We are Verifying Your Video</b><br>Our AI is checking your branding video. This usually takes a few seconds.</p><p style="color:#F37F3B!important;margin:0!important">Do not close the app</p></div></div>'''
    mocks2 = f'''<div class="mockrow" data-stagger>
 <div class="mock"><div class="ok">✓</div><h5>Branding Approved</h5><p>Your vehicle branding has been approved. ₹10 has been credited to your Jugnoo wallet.</p><span class="mb">View Wallet</span></div>
 <div class="mock"><div class="earn"><small>Total Earnings</small><b>₹100</b><span style="display:block;background:#fff;color:#111;border-radius:8px;padding:8px;text-align:center;margin-top:8px;font-weight:600">Start Recording</span></div>
  <p style="text-align:left;margin:12px 0 4px!important"><b style="color:#111">Rewards</b><br>Complete 30 days consecutively to get an additional ₹100 reward.</p><div class="bar"><i></i></div><small style="color:#6b7280">14 /30 Days</small></div></div>'''
    s_intro = f'''<span class="eyebrow">Introduction</span><h2>Turning every rickshaw into a moving ad.</h2>
<p class="big">Jugnoo is a ride-hailing platform operating across India, connecting everyday commuters with rides.</p>
<p>As part of its marketing, Jugnoo pays Auto drivers to display Jugnoo posters on their vehicles, turning every rickshaw into a moving ad at a fraction of the cost of traditional advertising.</p>
<div class="row c3 top float3d" style="margin-top:40px" data-stagger>{img(F('Kv5zh9kddZr9EqL8J6ZhDrRgQ'),'Jugnoo auto, front')}{img(F('24Jhcv3uglkdCAlLRUKbvdcBTo'),'Jugnoo auto, side')}{img(F('m4Gc35DGjsKbrlpBQLFX1pws588'),'Jugnoo auto, back')}</div>
<div class="callout"><h3>My Role — Product Designer</h3><p>Problem framing, User Research, Flow design, Strategy, Prototyping, High-fidelity design. · Timeline — 6 weeks</p></div>'''
    s_app = f'''<span class="eyebrow">Our Approach</span><h2>Phases, not a grand plan.</h2>
<p class="big">The branding verification system evolved through phases.</p>
<p>Each phase solved the specific gap the previous one exposed, rather than trying to design a complete solution upfront.</p>
<h3>Design Goals</h3>
{cards([("01","Fairness","Rules were designed around realistic driver scenarios like vehicle downtime, emergencies, rejected videos so the system penalizes non-compliance, not bad luck."),("02","Consistency","Daily rewards and streak incentives were designed to work together. This keeps both short-term and long-term motivation aligned."),("03","Simplicity","Verification, rewards, and activity history were kept in one clear flow. Drivers can easily understand their current status without checking multiple screens.")])}'''
    s_first = f'''<span class="eyebrow">The first idea</span><h2>Just upload a photo, every day.</h2>
<p class="big">The most straightforward fix seemed obvious: have drivers upload a photo of their vehicle every day, so branding could be verified consistently.</p>
{mocks}
<h3>Why would they?</h3>
<p>Drivers already go through sign-in and ride-related steps every single day. Adding one more unpaid task with no clear benefit to them was just friction and friction pushes drivers away from the platform. We needed drivers to want to do this.</p>
<div class="row c2" style="margin-top:30px">{shot(F('OJcIac7IoWZmsBplOEhu3aWww'),'Branding instructions screen',g)}{shot(F('YtgeEH2Eqn4PAdvwH7fBD135TY'),'Try again tomorrow dialog',g)}</div>'''
    s_paid = f'''<span class="eyebrow">01 — Verification + a base incentive</span><h2>So we paid them.</h2>
<p class="big">We set up daily verification and gave drivers an actual reason to comply.</p>
<p>Every time a driver submitted a branding video that passed AI verification, ₹10 was credited directly to their Jugnoo Wallet. This gave drivers a reason to participate.</p>
<h3>But one day isn’t enough</h3><p>Jugnoo needed drivers to maintain branding continuously, not just submit once and disengage.</p>
<div class="callout"><h3>Consistency Streak</h3><p>A streak reward was layered on top of the daily payout: every 30 consecutive days of approved submissions unlocks an additional ₹100 credited directly to their Jugnoo Wallet. This gave drivers a reason to participate.</p></div>
{mocks2}
<div class="row c2 top">{shot(F('vWZW90JnfKFrkO5RA8mXkV8w14I'),'Branding history',g)}{shot(F('CjyburaFjhnoWupTIqVhTVHDUrE'),'Branding history, all states',g)}</div>'''
    s_edge = f'''<span class="eyebrow">02 — A Fair Edge Case</span><h2>What if a driver genuinely couldn’t submit?</h2>
<p class="big">A vehicle could break down. A driver could take a day off for a personal emergency.</p>
<p>If we treated a genuine miss the same way as someone simply not bothering, drivers would stop trusting the system and stop caring about branding altogether.</p>
{cards([("Skip","Skip for Today","A skip is allowed once every 15 days, so a genuine miss doesn't feel like a punishment."),("Retry","Two attempts a day","A driver gets two attempts to submit a video. If both get rejected, they can try again the next day instead of losing the day entirely."),("Reset","Two missed days resets the streak","Branding stays active even after a missed day — a driver isn't cut off from the program. Two consecutive missed days reset the streak back to Day 1, and the driver becomes ineligible for the ₹100 they'd have earned at 30 days.")])}
<div class="quote">Only 1 Attempt Left — Your video was rejected twice today. You can skip today or try again tomorrow.</div>
<p>If you miss two days in a row, your streak will reset and you'll need to start over from the beginning. <i>Skip can be used once every 15 days.</i></p>
<div class="row c2 float3d" style="margin-top:30px">{img(F('6tSnG38U4gmmu2Y94TIjD51S3J0'),'Jugnoo auto, side')}{img(F('TOPCniumVDt7uZwYcVgXgEln4Yo'),'Jaipur Adventures auto')}</div>'''
    s_instr = f'''<span class="eyebrow">Transparency</span><h2>A dedicated Branding Instructions section</h2>
<p>To keep the experience transparent and reduce confusion - key instructions and streak rules are shown clearly, so drivers always know what is expected and what happens next. It gives quick access to video guidelines and FAQs for any additional questions. This helps drivers make the right decision without leaving the flow.</p>
<h3>Every approved submission and every streak milestone shows up as real money</h3>
<p>Visible in the driver’s wallet, explained on a dedicated rewards page, and recorded in a history they can look back on anytime.</p>
<p>This was more about making the system work in real situations. Each decision came from questioning what could go wrong, how a driver might respond, and what would still feel fair. The final experience was shaped by following those questions until the flow felt clear and practical.</p>
<div class="float3d" style="max-width:520px;margin:34px auto 0">{img(F('k8rrrQppw5ORf6fqJT0TgFFSk'),'Jugnoo auto, back')}</div>'''
    s_learn = f'''<span class="eyebrow">Reflection</span><h2>My Learnings</h2>
{cards([("01","Incentives are part of the experience.","The ₹10 daily reward, 30-day streak, and ₹100 bonus directly affect how drivers respond to the feature. These numbers needed as much thought as the screens themselves."),("02","Driver feedback helped shape the solution.","Early conversations made one thing clear: drivers needed a strong reason to participate. This helped define the reward system and overall flow."),("03","Usability testing improved the retry and skip flow.","Some rules looked fair during planning but felt frustrating during testing. This led to changes such as retrying the next day and allowing skips in specific situations."),("04","A good flow does not always guarantee adoption.","Even if the experience is simple and fair, drivers still need to trust the system and see value in using it. Real usage will show how well the feature performs over time.")], "cards3").replace('cards3','cards3" style="grid-template-columns:1fr 1fr')}
<p class="big" style="margin-top:50px">Thank You! Let’s Connect — <a class="ilink" href="mailto:{EMAIL}">{EMAIL}</a></p>'''
    case_page(p, 0, [("intro","Introduction",s_intro),("approach","Our approach",s_app),("first","The first idea",s_first),("paid","So we paid them",s_paid),("edge","A fair edge case",s_edge),("instructions","Instructions",s_instr),("learnings","Learnings",s_learn)],
              "A system that verifies vehicle branding daily through AI and rewards consistency through a series of incentive structure, designed to balance business compliance needs with driver trust and retention.")

    # ---------------- PlantParents (Framer text + assets)
    p = P["plant-parents"]; g = "plant"
    pl_intro = f'''<span class="eyebrow">The problem</span><h2>Buying plants online has become easy, but keeping them alive?</h2>
<p class="big">Not so much.</p>
<p>Most people in cities either gift plants or try to bring greenery into their homes, but they don’t know how to take care of them. Once the plant starts drooping or getting yellow, there's panic. They Google things, call their parents, or just give up. Online platforms sell plants, pots, and tools, but they stop there.</p>
<div class="quote">What if people could actually get help from someone who knows how to save your plants?</div>
<div class="row c3 top float3d" data-stagger>{img(F('hYJBXWNlQj0CCdqNH3eH5IHRaG0'),'Plant')}{img(F('15nDy43wsXPAcGBtCy1tR3s'),'Plant')}{img(F('VKhaTjnITRtY7FYmpZSmGiYCH8M'),'Rubber plant')}</div>
<h3>Design Process</h3>
{cards([("01 · Empathize","Empathize","Listened to plant lovers & new buyers to deeply understand struggles with plant care, slow delivery, and the absence of expert support."),("02 · Define","Define","Narrowed these insights into clear user problems like confusing online shopping, lack of quick help, and missing local shop connections."),("03 · Ideate","Ideate","Brainstormed unique solutions like same-day plant delivery, easy-to-use filters, and the ability to book visits from local plant experts."),("04 · Prototype","Prototype","Built interactive flows to test every step from shopping for plants to booking an expert home visit ensuring a smooth user journey.")], "cards4")}'''
    pl_emp = f'''<span class="eyebrow">01 · Empathize</span><h2>Problem statement & solution</h2>
<h3>Problem Statement</h3>
<p>Buying plants online should be easy but it rarely is. You end up browsing five different websites, most of them showing the same few plants. Delivery takes too long, there’s no proper guidance, and if your plant starts dying later, you have no clue whom to ask.</p>
<p>For people who genuinely want to keep plants at home and struggle to keep them alive it becomes more stress than joy. Especially when all they really want is something simple, quick, and reliable.</p>
<h3>Solution</h3>
<p>What we’re building is a website that connects people to local plant shops around them so they can buy fresh, healthy plants, pots, and tools, and get them delivered the same day or next.</p>
<p>And if someone’s plant is struggling, they can ask for help and a local plant expert will visit their home to take a look. This way the process always stays simple, warm, and trustworthy. Just how plant shopping should feel.</p>
<div class="row c2 float3d" style="margin:34px 0">{img(F('yImS7lBzlERjaoxZY0cTKq6i4'),'Watering plants')}{img(F('sK5aQgap2UCgzQdLHoEDk1XlRs'),'Nurseries and experts')}</div>
<h3>User Pain Points</h3>{shot(F('bJnExjameQ1jkcnScm4mTIHgfU'),'User pain points',g)}'''
    pl_def = f'''<span class="eyebrow">02 · Define</span><h2>User personas & empathy mapping</h2>
<div class="row c2 top">{shot(F('wjJC7v6kBzmmJHzvztC4fhCwnoE'),'Persona: Nisha Kumar',g)}{shot(F('6vmsudAUc5AXHmyStg6iHuuyR8k'),'Persona: Rahul Mehta',g)}</div>
<h3>Empathy Mapping</h3>
<div class="row c2 top">{shot(F('bDRPmXqCxxDao4XFyfRjvzSLjjk'),'Empathy map: Nisha',g)}{shot(F('YezLwgcys9ryFVYa5LHsPKtdU'),'Empathy map: Rahul',g)}</div>'''
    pl_ide = f'''<span class="eyebrow">03 · Ideate</span><h2>Site maps, colour & type</h2>
<h3>Site Maps</h3>{shot(F('9BPJwDvnJBQ3sHBLgjGoEBtUaRA'),'Site map',g)}
<h3>Colour</h3>
<div class="palette" data-stagger><div style="background:#003324;color:#E7F4EE">#003324</div><div style="background:#E7F4EE">#E7F4EE</div><div style="background:#A8E919">#A8E919</div><div style="background:#fff">#FFFFFF</div></div>
<h3>Typeface — Manrope & Inter</h3>{shot(F('sauHs3GyhMExhjLOslEID3qiTOo'),'Typography',g)}
<div class="row c2 float3d" style="margin-top:30px">{img(F('AoLBVGVPzT121NDoJVWabVbBfg'),'PlantParents laptop and logo')}{img(F('zSCFtDKWAjTe0l45jo6NMng'),'Choose your expert')}</div>'''
    pl_pro = f'''<span class="eyebrow">04 · Prototype</span><h2>From shopping to booking an expert</h2>
<h3>Information Architecture</h3>{shot(F('Mz4XeAdkisu19eMgUhdr0LXHL1g'),'Information architecture',g)}
<h3>Home Page</h3>{shot(F('cHmxcCb10uzXQthfeHiYkmM6ZIE'),'Home page, laptop',g)}
<div class="row c3 top" style="margin-top:22px">{shot(F('93C45hEzLXiY35JimSmtsmaiSM'),'Home page full',g)}{shot(F('1lS3Mh2Rl7DSyNI1qs1L5wsNO0'),'Home page, mobile',g)}{shot(F('gV583FqybOx3LhoggrNovQnSbU'),'Home page, dark theme',g)}</div>
<h3>Dark Theme</h3><div class="row c2" style="align-items:center">{shot(F('O4iqmzQYmdo8NrLCpSc7VvI6cFI'),'Favorites, dark',g)}{img(F('fWKpx6ETVJsH8QAvDfAqgYUdU'),'Phone mock','float3d')}</div>
<h3>Shop Page</h3><div class="row c2 top">{shot(F('5AQOGsPcYrnYPwcU7giOXDRO9E'),'Shop page',g)}{shot(F('7g7keQfwSrJTtTXH0j81UHuJvAc'),'Shop page, mobile',g)}</div>
<h3>Plant Expert Page</h3><div class="row c2 top">{shot(F('m3wG0fY4ps1koqOcRBQHS7Bl8E'),'Plant expert page',g)}{shot(F('hQ6j0Kt4euMiCT0MeVft50ekgA'),'Plant expert page, mobile',g)}</div>'''
    pl_con = f'''<span class="eyebrow">Reflection</span><h2>Conclusion & Learnings</h2>
<p>Working on PlantParents was about solving a very real problem that plant lovers face every day. From the very beginning, the idea of connecting local nurseries and plant experts to people’s homes felt close to heart, and that guided every design decision.</p>
<p>Through user research, I realized how personal plant care is, people don’t just want to buy a product, they want reassurance, guidance, and a feeling of success with their plants. That insight shaped the focus on same-day delivery and booking plant helpers, which became the core differentiators of the project.</p>
{shot(F('UXKKTdUhPeTT6S75h2znSdNPq3s'),'Thank you for watching',g)}'''
    case_page(p, 1, [("problem","The problem",pl_intro),("empathize","Empathize",pl_emp),("define","Define",pl_def),("ideate","Ideate",pl_ide),("prototype","Prototype",pl_pro),("learnings","Conclusion",pl_con)],
              "Designed an end-to-end marketplace experience for discovering plants, shopping from nurseries, and booking plant-care experts — across user flows, information architecture, wireframes, and responsive high-fidelity UI.")

    # ---------------- Connect (Behance)
    p = P["connect-b2b-feedback"]
    c1 = '''<span class="eyebrow">The project</span><h2>Growth Score, and the questions ratings can’t ask.</h2>
<p class="big">Connect is a feature within Growth Score that lets businesses create personalised feedback forms and distribute them through email campaigns.</p>
<p>Growth Score is a B2B customer feedback and reputation management platform that helps businesses understand how customers feel about their products and services. Through features like NPS, CSAT, reviews, referrals, and testimonials, businesses can collect feedback, measure satisfaction, and build stronger customer relationships.</p>
<p>But customer feedback isn't always about ratings. Sometimes, businesses need to ask specific questions to understand what their customers really want. Teams can customise their questions, apply scoring, and collect responses in one place, making it easier to turn feedback into insight.</p>'''
    c2 = cards([("Customer Retention","10–15%","Potential churn reduction"),("Revenue Expansion","5–15%","Potential annual revenue uplift")], "cards3").replace('cards3', 'cards3" style="grid-template-columns:1fr 1fr')
    c2 = f'''<span class="eyebrow">Impact</span><h2>What it could unlock</h2>{c2}
<h3>Here is what this project taught me</h3>
{cards([("01","Balance Business Goals with User Needs","This project taught me to think from both a business and a user perspective. I learned how to simplify complex processes without limiting flexibility, while building a product structure that can scale and adapt to future features. Thinking beyond the immediate interface helped me understand how design decisions can support both business goals and user needs."),("02","Make Complex Workflows Easier to Navigate","I learned that showing too many options on one screen can overwhelm users and increase decision-making effort. Breaking a process into smaller, guided steps makes it easier to follow. I also realized how important editing, deleting, and going back are when designing forms, as users need the freedom to correct mistakes without starting over.")], "cards3").replace('cards3','cards3" style="grid-template-columns:1fr 1fr')}'''
    case_page(p, 2, [("project","The project",c1),("impact","Impact & learnings",c2)],
              "Helping businesses collect more meaningful feedback, faster — a B2B feedback-form builder with email campaigns, scoring and response collection.")

    # ---------------- Wellspring (Behance)
    p = P["wellspring-healthcare"]
    w1 = '''<span class="eyebrow">About the project</span><h2>A healthier, happier you — in one hub.</h2>
<p class="big">Through this project I wanted to solve a real life problem of taking care of our health in today's fast-paced world.</p>
<p>Managing our health often takes a backseat. Wellspring was born from the desire to tackle this challenge. This project aims to empower individuals by providing a central hub for all their healthcare needs. By simplifying tasks like tracking symptoms, scheduling appointments, and managing medications, Wellspring hopes to make proactive health management more accessible and convenient, ultimately leading to a healthier and happier you.</p>
<h3>Design process</h3><p>Discover · Empathize · Define · Ideation · Prototype · Testing</p>'''
    w2 = f'''<span class="eyebrow">Key takeaways</span><h2>What I took away</h2>
{cards([("1","User needs over Aesthetics","I used to think design was all about aesthetics, but this project showed me the importance of prioritizing the user. By understanding their needs, frustrations, and goals, I wanted to create a design that works for them."),("2","The power of iteration","This project taught me the power of iteration. I constantly tested my ideas with users, gathered feedback, and then refined my designs based on their input. It's a cycle of learning and improvement that leads to a much stronger final product."),("3","Less is more","I understood the concept of Less is more and the importance of clear and concise design. Simplicity is the way to go, by focusing on intuitive navigation, easy-to-understand visuals, and user-friendly interactions.")])}
<p style="margin-top:30px">As a student, I'm constantly eager to learn and grow, and this project opened my eyes to the fascinating world of user experience design. There's so much more to discover, and I can't wait to put these learnings into practice on future projects!</p>
<p class="big">Let’s build a Project together — <a class="ilink" href="mailto:{EMAIL}">{EMAIL}</a></p>'''
    case_page(p, 3, [("about","About the project",w1),("takeaways","Key takeaways",w2)],
              "Manage your health effortlessly — track symptoms, make appointments, take meds, and record it all in one place.")

    # ---------------- Blue Pottery (Behance)
    p = P["blue-pottery"]
    b1 = '''<span class="eyebrow">The idea</span><h2>Beautiful and practical.</h2>
<p class="big">Blue pottery is often categorized solely as delicate showpieces.</p>
<p>But there is potential to do so much with this stunning art form. That’s why I decided to focus on creating <b>beautiful and practical</b> blue pottery products for everyday use.</p>
<h3>In this journey I discovered…</h3><p>Motifs and patterns drawn from the craft, a palette of six core colours, and a set of products made with them — a jewelry box, a camel table clock, a peacock table clock, coffee mugs, and gifting boxes in traditional Jaipur architectural motifs.</p>
<div class="palette" data-stagger style="grid-template-columns:repeat(6,1fr)"><div style="background:#2236d6"></div><div style="background:#4fc3ea"></div><div style="background:#c1481a"></div><div style="background:#f5d90f"></div><div style="background:#3a6b25"></div><div style="background:#0c1a9c"></div></div>'''
    case_page(p, 4, [("idea","The idea",b1)], "Beautiful and practical blue pottery products for everyday use — motifs, patterns, and objects inspired by the Jaipur tradition.")

    # ---------------- Elementals (Behance)
    p = P["elementals-poster"]
    e1 = '''<span class="eyebrow">The poster</span><h2>Opposites react.</h2>
<p class="big">A fan poster for Disney Pixar’s Elemental — water and fire, meeting in the middle.</p>
<p>Illustrated in Adobe Illustrator, with the film’s title lettered in Devanagari: एलीमेंटल.</p>'''
    case_page(p, 5, [("poster","The poster",e1)], "A fan poster for Disney Pixar’s Elemental — “Opposites react”.")

def main():
    build_index(); build_work(); build_about(); build_cases()
    print("built:", ", ".join(sorted(glob.glob("*.html"))))

if __name__ == "__main__":
    main()
