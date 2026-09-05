# CMMC Level 2 Assessor Preparation — 5-Day Workshop

A self-contained static site modelled on the CISA 5-day workshop at
`jjirik77.github.io/cisa`, built from the 8-week CMMC course in `../CMMC/`.
No build step, no dependencies, no backend. Open `index.html`.

## What is here

| | |
|---|---|
| `index.html` | Hero, 11 lesson cards, the case thread, the 5-day schedule, CAP phase bars, 12 tool cards, about |
| `lesson00–09.html` | The ten sessions, two per day |
| `lesson10.html` | Bonus — faculty and facilitator guide |
| 9 tool pages | One per threaded case-study segment (see below) |
| `transfer-test.html` | Piedmont Textile Finishing — 30-minute cold scope determination |
| `onepager.html` | Printable exam-day cram sheet |
| `threadbridge.html` | The case workbench, copied from `../CMMC/` and re-skinned |

**Tools:** `clause-trace` · `cui-determination` · `ethics-gate` · `scope-matrix` ·
`evidence-triage` · `domain-worksheet` · `sprs-calculator` · `poam-builder` · `transfer-test`

## Deploying

Copy the `.html` files to any static host. For GitHub Pages, push them to the repo root or
`/docs`. Nothing loads from a CDN and nothing calls out to a network, so it also works from a
USB stick or a local folder.

## Editing

Pages are generated. Edit the source and rebuild:

```
cd build && python3 build.py
```

| File | Holds |
|---|---|
| `build/theme.py` | The design system, page shells, and **`REG_STATUS`** — the regulatory banner |
| `build/render.py` | Lesson page renderer and the manuscript dump |
| `build/index.py` | The index page |
| `build/content_a/b/c.py` | **All lesson prose** — the authoritative manuscript source |
| `build/toolkit.py` | The shared tool engine (save, reveal, progress codes, print) |
| `build/tools*.py` | The nine tools, the transfer test, and the one-pager |

Editing the HTML directly works too, but a rebuild overwrites it.

## Before you teach

**Re-verify the regulatory position within seven days of any run.** Update `REG_STATUS` in
`build/theme.py` and rebuild — that one constant drives the dated banner everywhere. See
`lesson10.html` for the full maintenance checklist.

Three instruments must be withheld until issued in session: the Day 5 evidence package, the
interview role cards (both in `../CMMC/`), and the Piedmont transfer test.

## Handoff documents

`00_evaluation_brief.md` · `01_content_blueprint.md` · `02_learning_design_spec.md` ·
`03_manuscript.md` (generated) · `04_visual_spec.md` · `06_review_findings.md`

## Status

23 pages, ~1.6 MB. All JavaScript parses; all 23 pages load without runtime errors; 58
functional assertions pass in jsdom; 100 knowledge-check questions with 400 rationales; 84
auto-checked tool determinations; 0 broken links.

**Not yet verified:** rendering in a real browser at real viewports, and a WCAG contrast audit.
See `06_review_findings.md` L-4 and L-5.
