# Radhika Atolia — Portfolio

Static site (plain HTML/CSS/JS, **no bundler**). Content pulled from Radhika's Framer site + Behance profile — see `CONTENT-NOTES.md` for the full inventory and source links.

## Run
```bash
python3 -m http.server 5173   # then open http://localhost:5173
```

## Regenerate pages
All `.html` files are generated from `tools/build.py` (content + templates live there):
```bash
python3 tools/build.py        # needs: pip install pillow
```
Edit copy/links/projects in `tools/build.py`, rebuild, commit.

## Structure
| Path | What |
|---|---|
| `index.html` | Home: 3D hero, ticker, statement, stacked work cards, Behance strip, about teaser, contact |
| `work.html` | All 6 projects with filters |
| `about.html` | Bio, "things I'm into" horizontal scroller, experience timeline, toolkit |
| `case-*.html` | Jugnoo, PlantParents (full Framer write-ups) + Connect, Wellspring, Blue Pottery, Elementals (Behance boards) — each with HD full-screen lightbox |
| `styles.css` / `script.js` | Design tokens, scroll reveals, split/scrub text, parallax, 3D tilt, pinned horizontal scroll, lightbox |
| `assets/framer`, `assets/behance` | Optimised HD webp (originals kept outside repo) |

## Deploy
Vercel, auto-deploys on push to `main`. `vercel.json` redirects the old `/works`, `/side-quests`, and Framer-style `/jugnoo-project`, `/plant-parents-2` URLs.
