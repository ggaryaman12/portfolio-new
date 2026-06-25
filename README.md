# Radhika Atolia — Portfolio

Static single-page portfolio. No build step. Plain HTML + CSS + JS.

Design system follows `ipshitasingh.com-DESIGN.md` (warm teal-grid aesthetic,
Libre Baskerville + DM Sans, pill buttons, hover-lift cards, scroll-reveal).
Content is original placeholder copy for Radhika Atolia — swap freely.

## Files
- `index.html` — page structure + inline SVG doodles
- `styles.css` — full design-system tokens + components
- `script.js` — mobile nav, scroll reveal, scroll-spy, form demo
- `vercel.json` — clean URLs config

## Preview locally
```bash
cd ~/radhika-portfolio
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy to Vercel (free)

### Option A — drag & drop (no git)
1. Go to https://vercel.com → sign in (free).
2. Add New → Project → "deploy a static folder" / or use Vercel CLI below.

### Option B — Vercel CLI (fastest)
```bash
npm i -g vercel
cd ~/radhika-portfolio
vercel        # first run: log in + link, accept defaults
vercel --prod # promote to production URL
```
Framework preset: **Other** (static). No build command. Output dir: `.`

### Option C — GitHub + Vercel (auto-deploy on push)
```bash
cd ~/radhika-portfolio
git init && git add . && git commit -m "init portfolio"
gh repo create radhika-portfolio --public --source=. --push
```
Then in Vercel: Add New → Project → import the repo → Deploy.

## Customize
- Name/links: edit text in `index.html`.
- Colors/spacing/type: edit `:root` tokens in `styles.css`.
- Replace SVG doodles with your own illustrations (same `.doodle` classes).
- Wire the contact form to a real backend (Formspree, Vercel Functions, etc).
