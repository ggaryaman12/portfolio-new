# Content inventory — what was pulled in, from where

Sources (pulled Oct 2026):
- Framer: https://radhikaatoliaportfolio.framer.website/  (pages: `/`, `/about`, `/work`, `/jugnoo-project`, `/plant-parents-2`)
- Behance: https://www.behance.net/radhikaselement  (6 projects)

Originals (full-res, untouched) are kept OUTSIDE the repo at `~/radhika/originals/{framer,behance}`.
Repo ships optimized HD webp (max 2000px wide Behance, 2400px Framer) in `assets/`.

## Framer — home `/`
- [x] Hero: "Hello! I'm Radhika, a product designer." + tagline, CTAs *See my work* / *About me*
- [x] "Projects I've Worked on": Verification and Incentive System → Jugnoo case; E-Commerce & Expert-Booking Platform → PlantParents case
- [x] Contact block: "Let's talk!", email, Say hello (Gmail compose deeplink), Download Resume, Behance, LinkedIn
- [x] Assets: hero cut-out portrait, Jugnoo cover, PlantParents cover, favicons (70px light/dark)
- NOT used: Framer og:image `BzRsGroDP5cGdKYfisAanhbI.jpg` — it is the Framer *template* ("Meeko") preview, not Radhika's work.

## Framer — `/about`
- [x] "Hii! I'm Radhika…" bio (2.5+ yrs, B2B SaaS, AI-assisted workflows, currently designing Jugnoo)
- [x] Things I am into recently ×6 (Sad Songs, Creating new Stickers, Avocado sandwich, Sunset walks, Oil pastels, Boba tea) + the 6 photos
- [x] Experience ×3: Jungleworks (Nov 2025–Present), LeapforgeDigital (Jul 2024–Oct 2025), Sheshya (Oct 2023–Apr 2024) with bullets
- [x] About portrait photo

## Framer — `/work`
- Page is a CMS list that renders empty server-side; the two projects it lists are the same two on home.

## Framer — `/jugnoo-project` (Jugnoo – Vehicle Branding)
- [x] Intro, role, timeline (6 weeks), approach, 3 design goals, first idea, "Why would they?", "So we paid them", streak, fair edge case, skip rule, two-missed-days reset, instructions section, wallet/history, learnings ×2, thank-you
- [x] Images: JUGNOO banner, 5 rickshaw renders, Jaipur-adventures rickshaw, instructions/history/modal phone UIs, 4 SVG illustrations
- [x] In-page UI states (upload options sheet, "verifying" dialog, "approved" dialog, rewards card, skip card) rebuilt as HTML

## Framer — `/plant-parents-2` (PlantParents)
- [x] Problem, solution, 4-step process, pain points, personas (Nisha, Rahul) + empathy maps, site maps, colour palette (#003324 #E7F4EE #A8E919 #FFFFFF), typefaces (Manrope + Inter), IA, home / dark theme / shop / expert pages, responsive strips, conclusion & learnings, thank-you
- [x] All 28 images

## Behance — profile
- [x] Name, title "Product designer", company Jungleworks, location India
- [x] "About Me" text (verbatim), stats (appreciations / views / followers / following)
- [x] Deeplinks to profile + all 6 projects

## Behance — projects (all images pulled at max res, text lives inside the images)
| Project | Behance | Published | Images |
|---|---|---|---|
| Connect – B2B customer feedback management platform | /gallery/257163815 | Oct 15 2026 | 7 |
| Vehicle Branding – Jugnoo | /gallery/255879977 | Sep 18 2026 | 10 |
| Plant Parents – Plant and Expertise at your doorstep | /gallery/233636525 | Aug 31 2025 | 11 |
| Wellspring – A Healthcare UI/UX project | /gallery/200805151 | Jun 12 2024 | 17 (incl. 1 GIF) |
| Blue Pottery Products | /gallery/200571291 | Jun 8 2024 | 14 |
| Disney's Elementals Poster | /gallery/200146141 | Jun 8 2024 | 1 |

## Links
- Resume (nav link): https://drive.google.com/file/d/1EbfWYlFSqeKG8F6jiqInrfgAG0uC05uF/view?usp=sharing
- Download Resume (button): https://drive.google.com/file/d/1mn57kZrvQAOB5N5ocv-0fnTCIip-mqVM/view?usp=drive_link
- Behance: https://www.behance.net/radhikaselement
- LinkedIn: https://www.linkedin.com/in/radhikaatolia/
- Email: radhikaselement@gmail.com

## Rebuild
`python3 tools/build.py` regenerates every `.html` page from the data in that file.
