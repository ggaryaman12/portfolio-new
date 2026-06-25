# Radhika Atolia — Portfolio

Static single-page-ish portfolio site. **No build step.** Plain HTML + CSS + JS.
Visual design follows a warm "cutting-mat" aesthetic (teal panels, Libre Baskerville
serif + DM Sans + Fragment Mono, scattered sticker doodles, playful motion).
All copy and artwork here are original placeholders — swap freely.

## Live
- Production: https://radhikaatolia.vercel.app
- Auto-deploys on every push to `main` (GitHub → Vercel are connected).

## Run locally
```bash
cd portfolio-new
python3 -m http.server 5173
# open http://127.0.0.1:5173
```
No npm install, no bundler. Just open the files.

## Files
| File | What |
|------|------|
| `index.html` | Home: hero (cutting-mat + jumping stickers), works marquee, skill-pill cloud, FAQ, contact |
| `about.html` | About: 3D tilt portrait card, bio, verse panel |
| `works.html` | Works grid |
| `side-quests.html` | Side-quest projects (alternating media rows) |
| `styles.css` | All styles + design tokens (`:root`) + animations |
| `script.js` | Cursor, scroll-reveal, marquee auto-scroll, 3D tilt, parallax, mobile menu, ruler |
| `vercel.json` | Static config (clean URLs) |

## Design tokens (edit in `styles.css` `:root`)
- Colors: blue `#0000EE`, teal `#1B6B6F`, orange `#FF5900`, burgundy `#26150B`, cream body `#F8F6F3`, light-blue `#CADCFC`
- Fonts: Libre Baskerville (serif headings), DM Sans (body/UI), Fragment Mono (labels)
- Radius: pills `99px`, cards `8px`, panels `24px`
- Spacing scale: `--s4`…`--s100` (4px base)

## Key interactions (in `script.js`)
- Custom cursor (dot + magnify ring) · scroll-reveal (`.reveal`) · hero sticker spring-jump + parallax
- Works marquee: native scroll + JS auto-scroll (`#universeMarquee`)
- 3D tilt: `.card`, `.tilt3d`, `#contactPanel` · mobile full-screen overlay menu · cutting-mat ruler numbers

## Deploy
Connected to Vercel — **just push**:
```bash
git add -A && git commit -m "your change" && git push
```
Production updates automatically in ~20s. (Manual fallback: `npx vercel --prod --yes`.)

## Placeholders to replace with real content
- Project images use `https://picsum.photos/...` — swap for real screenshots.
- Bio, project blurbs, FAQ answers, social links (`index.html` footer), resume link (nav `Resume`), email `hello@radhika.design`.
- Contact form is a front-end demo — wire to a backend (Formspree etc.) to receive messages.
