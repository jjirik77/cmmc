# Stage 1 — Content Blueprint
## CMMC Level 2 Assessor Preparation — 5-Day Workshop
**Verified:** 2026-09-04 · **Amended:** 2026-09-05
**Source corpus:** `/Users/jirik/Downloads/CMMC/` (8-week course, 12 documents) plus the CMMC 2.0 Training Portal
case library at `sands-mvcc.github.io/CMMC/` (Meridian: `casestudyjs1.html`)

---

## 1. Audience and scope

Working professionals in the defense industrial base and the assessor pipeline: compliance
officers, IT and security leads at DIB contractors, RPs and RPO staff, and CCP/CCA candidates.
Assumes 3+ years IT or security experience and basic DFARS familiarity; assumes no prior
assessment experience.

**In scope.** CMMC Level 2 in depth — the 110 NIST SP 800-171 Rev 2 requirements and their
~320 assessment objectives, the CMMC Assessment Process v2.0 through all four phases, the Code
of Professional Conduct v2.0, 32 CFR Part 170 scoping and POA&M rules, the DoD Assessment
Methodology, and DFARS 252.204-7012 incident reporting.

**Contextual only.** Levels 1 and 3. NIST SP 800-171 Rev 3 as horizon-scanning.

---

## 2. Durable vs perishable

**As of the 2026-09-05 amendment there is no dated policy layer at all.** The workshop teaches
32 CFR Part 170, the DFARS clause family and NIST SP 800-171 Rev 2 as published, and teaches
separately how to tell whether an announcement has changed any of it. That is the strongest
available answer to perishability: not a banner that must be updated, but a method that does not
go stale.

| Durable — will outlast several rule cycles | Perishable — verify before each run |
|---|---|
| The assessor/consultant distinction and why it exists | Which body holds the CAICO role |
| Adequacy vs sufficiency; the three-part standard | CAP / CoPC / Assessment Guide version numbers |
| Objective-level determination; no partial credit | NARA Registry category authorities |
| The five asset categories and the *conditional* logic of two of them | CAP / CoPC / Assessment Guide version numbers |
| Examine / interview / test, and what each cannot establish | NARA Registry category authorities |
| Reading a policy change against primary sources | CCP/CCA exam mechanics |
| Source-authority ranking | Specific POA&M and scoring numbers, if Rev 3 is ever adopted |
| Policy announcement vs. instrument | Which specific instruments have issued at any given moment |

---

## 3. Verified claims

Verified against primary sources or against `sources.docx` (48-entry annotated register,
link-checked 25 Aug 2026), plus a live web check on 4 Sep 2026 for the regulatory position.

| Claim | Status | Source |
|---|---|---|
| Meridian scenario facts — contracts, systems, gaps, personnel, suppliers, incidents | Verified against the source | CMMC 2.0 Training Portal, `casestudyjs1.html`, retrieved 2026-09-04 |
| Portal maps its supply-chain gap to practices 3.17.1 / 3.17.2 | **Verified as an error to teach** — SR family exists only in Rev 3 | NIST SP 800-171 Rev 2 (14 families, no SR); Rev 3 |
| Portal describes 3.4.2 as "component inventory" | **Verified as an error to teach** — Rev 2 3.4.1 covers inventories; 3.4.2 is configuration settings | NIST SP 800-171 Rev 2 |
| Point values used in the SPRS tool | Restricted to requirements whose values are traceable to the source course's instructor key | `module06_instructor.docx` §5; DoD Assessment Methodology §5 and Annex A |
| DFARS 252.204-7012/-7019/-7020, FAR 52.204-21, 800-171 Rev 2, self-assessments, SPRS, affirmation all in force | **Verified** | Same; 32 CFR Part 170 unrepealed |
| ISACA holds the CAICO role from Dec 2025; transition completed Apr 2026 | Verified | `sources.docx` §1.1; ISACA credentialing pages |
| Cyber AB accredits organizations; ISACA certifies individuals | Verified | 32 CFR Part 170; Cyber AB; ISACA |
| Level 1 = 15 requirements, not 17 | Verified | 32 CFR 170.14(c)(2) incorporating FAR 52.204-21(b)(1)(i)–(xv) |
| Level 2 = 110 requirements, ~320 objectives | Verified | NIST SP 800-171 Rev 2; SP 800-171A |
| Scoring 110 max, deductions 5/3/1, floor −203 | Verified | DoD Assessment Methodology §5 and Annex A |
| Partial credit for exactly two requirements (3.5.3, 3.13.11) | Verified | Same |
| POA&M threshold 0.8; six requirements never deferrable | Verified | 32 CFR §170.21 |
| The six: AC.L2-3.1.20, AC.L2-3.1.22, CA.L2-3.12.4, PE.L2-3.10.3/.4/.5 | Verified | 32 CFR §170.21 |
| 180-day closeout from Conditional CMMC Status Date | Verified | 32 CFR §170.17, §170.21; CAP v2.0 Phase 4 |
| 72-hour report from *discovery*; 90-day preservation; medium assurance certificate required | Verified | DFARS 252.204-7012(c), (e) |
| CSP: FedRAMP Moderate *plus* reporting/preservation/access obligations; GCC High not named in the clause | Verified | DFARS 252.204-7012(b)(2)(ii)(D) |
| Three-year consulting bar covers any type of CMMC assessment; binds the C3PAO | Verified | 32 CFR §170.8(b)(17)(ii)(G); CoPC v2.0 §2.2(d) |
| Phase 1 concludes on Pre-Assessment Form upload to eMASS | Verified | CAP v2.0 |
| Out-brief QA reviewer must be a CCA not on the team, no contact during the assessment | Verified | CAP v2.0 Phase 3 |
| CAP v2.0 phase names (not the CMMC 1.0 names) | Verified | CAP v2.0 |
| CCP 170 questions / 6 domains; CCA 150 / 4 domains; weightings as published | Verified | ISACA exam content outlines |
| CCP/CCA **exam duration and passing scores** | **UNVERIFIED — not published** | Flagged in L0, L9, and the one-pager; no figure stated anywhere |

**Not fabricated anywhere:** no exam durations, no pass marks, no pricing, no benchmark
statistics, no citation that was not traced to an instrument.

---

## 4. Responsible-use content (mandatory, and it is genuinely on-topic here)

CoPC v2.0's eighth guiding principle is **Proper Use of Technology and AI**, and Module 3
Scenario 4 in the source course is literally an assessor pasting SSP extracts into a public AI
assistant. This is not a bolt-on.

Delivered in three places:
- **L0 §9** — the two standing questions (is a tool making a determination that is mine to
  make; is customer data leaving the boundary), what never leaves the engagement boundary, and
  the fabricated-citation risk in a findings report.
- **L3** — the scenario adjudicated formally, naming *two* breaches (Confidentiality and Proper
  Use of Technology and AI), with Information Integrity arguable as a third, and the disposition
  belonging to the C3PAO.
- **L0 and L3 knowledge checks** — one item each, both testing that candidates identify the
  second breach rather than stopping at the obvious one.

Also carried throughout: confidentiality of engagement material, the prohibition on advising,
the prohibition on speculating about outcome, and the personal False Claims Act exposure of the
Affirming Official.

---

## 5. Target tasks

What a learner must be able to *do*, each mapped to the tool that exercises it:

| Task | Tool |
|---|---|
| Trace the regulatory authority binding a contractor, from a solicitation | Clause Trace |
| Determine FCI / CUI / neither, cited to the NARA Registry | CUI Determination |
| Identify and dispose of engagement conflicts; make a Phase 1 readiness call | Engagement & Ethics Gate |
| Categorize assets and defend a boundary against a hostile reader | Scope & Asset Matrix |
| Evaluate an artifact for adequacy and sufficiency, and say what would change the verdict | Evidence Triage |
| Render objective-level determinations and detect mis-mapped gaps | Domain Worksheet |
| Compute and defend a DoD Assessment score; rule on an incident | SPRS Calculator |
| Run an assessment and write defensible findings | Case workbench |
| Determine POA&M eligibility and build a compliant plan | POA&M Builder |
| Scope an unfamiliar environment under time pressure | Piedmont transfer test |

---

## 6. Known limits

- Content is derived from the existing 8-week course, which was itself researched to 25 Aug 2026.
  No new subject-matter research was conducted beyond verifying the perishable regulatory claims.
- The NARA Registry authorities cited for CTI, PROCURE, EXPT, and PERS/PRVCY are as recorded in
  the source course. NARA updates continuously; re-verify before each run.
- CAP, CoPC, Assessment Guide, and Scoping Guide version numbers move. The material cites v2.0
  for CAP and CoPC as current at time of writing.

**HANDOFF TO INSTRUCTIONAL DESIGNER**
