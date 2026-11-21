# CMMC 5-Day Faculty Workshop (CMMC Level 2 and the CCP)

A self-contained static site for a live, five-day faculty professional-development workshop. It is built on the same template as the CISM 5-day workshop. No build step, no dependencies, no backend. Open `index.html`.

**Rebuilt 2026-11-16** as plain HTML on the CISM template (light theme only). The previous Python-generated version is backed up at `../CMMC_5Day-backup-2026-11-16/`. The `build/` folder is kept as an archive only. Do not run `build/build.py`, because it would overwrite this site with the old design.

## What is here

| | |
|---|---|
| `index.html` | Hero, regulatory notice, 10 lesson cards, Practice, schedule, CCP domain weights, Exam Resources, Faculty Tools, About, feedback |
| `lesson00–09.html` | Ten sessions, two per day. Each has objectives, flashcards, content, the Meridian case, a **faculty teaching segment**, practice links, and a 10-question knowledge check. The former Lesson 10 faculty guide is folded into Lesson 9 (original in `build/retired/`). |
| `practices.html`, `activity01–09.html` | CMMC Practices: 9 self-checking activities (`practice.js`, `practice.css`) |
| `labs.html` | CMMC Assessment Lab hub |
| Lab tools | `clause-trace`, `cui-determination`, `ethics-gate`, `scope-matrix`, `evidence-triage`, `domain-worksheet`, `sprs-calculator`, `poam-builder` |
| `meridian.html` | The Meridian case workbench (fictional company) |
| `transfer-test.html` | Acuitas Machining: a 30-minute cold scope determination |
| `gen-test.html` | CCP practice exam, weighted to the six CCP domains |
| `onepager.html` | Printable review sheet |
| `gen-activity/case/content/graphics/podcast.html` | AI prompt builders for faculty |
| `cmmc-lesson.css`, `cmmc-lesson.js` | Shared lesson styles and quiz script |
| `case-window.js` | "Keep the case in view" bar on the 8 tool pages: opens `meridian.html#<section>` in one reusable side window. Not used on the transfer test. |

## Before you teach

1. **Re-verify the regulatory position** within seven days of any run. The dated notice ("Regulatory status as of 16 November 2026") appears on `index.html`, `lesson00.html`, `lesson01.html`, and `onepager.html`, and is linked from the other lessons. Edit it directly in those files.
   - As of 2026-11-16, **Phase 2 (Level 2 C3PAO certification) is suspended** (13 July 2026; DFARS Class Deviation 2026-O0025 Rev. 3), with no restart date announced.
   - Research notes and sources: `../ID_Studio/projects/cmmc-workshop-template-fit/02-research/`.
2. **Withhold until issued in session:** the Day 5 evidence package and the interview role cards (from the source 8-week course), and the Acuitas transfer test.
3. Exam duration, passing score, and fees are deliberately not stated. Check ISACA.

## Editing

Edit the HTML directly. To regenerate all ten lessons or the index from the archived lesson data, use the generator scripts kept with the project: `../ID_Studio/projects/cmmc-workshop-template-fit/04-build/convert.py` and `build_index.py`. They overwrite the lesson and index pages, so re-apply any hand edits afterward.

## Handoff documents (from the previous version)

`00_evaluation_brief.md` · `01_content_blueprint.md` · `02_learning_design_spec.md` · `03_manuscript.md` · `04_visual_spec.md` · `06_review_findings.md`. These describe the earlier professional-audience design. The current design and decisions are in `../ID_Studio/projects/cmmc-workshop-template-fit/`.
