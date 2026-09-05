# Stage 0 — Evaluation Brief
## CMMC Level 2 Assessor Preparation — 5-Day Workshop
**Prepared:** 2026-09-04 · **Orchestrator:** ai_orchestrator · **Output:** `/Users/jirik/Downloads/CMMC_5Day/`

---

## 1. Audience and the problem this solves

**Audience.** Working professionals in the defense industrial base and the assessor
pipeline: compliance officers, IT/security leads at DIB contractors, RPs and RPOs,
and candidates for the ISACA **CCP** and **CCA** credentials. Assumes 3+ years of
IT or security experience and basic DFARS familiarity. Not an introductory
cybersecurity audience.

**The problem.** The existing asset (`/Users/jirik/Downloads/CMMC/`) is an
excellent **8-week, 16-session academic course** — 24 contact hours delivered
twice weekly, nine graded deliverables, Canvas-oriented, `.docx`-native. It cannot
be delivered as a workshop. A conference, a faculty PD week, or a corporate cohort
needs a **self-paced, self-contained, web-delivered** artifact that a learner can
work through alone and an instructor can teach from — which is exactly what the
CISA workshop at `jjirik77.github.io/cisa` already is.

This build **re-forms** existing, verified content into the CISA delivery pattern.
It is not a new curriculum.

---

## 2. Delivery target

**Self-contained web lesson set** — a multi-page static site of single-file HTML
pages, embedded CSS and JS, zero external dependencies, hostable on GitHub Pages
exactly as the CISA site is.

**Why.** The instruction is "same structure, look, and feel" as a site that is
already built this way. Any other target breaks the mandate. It also solves the
distribution problem the source course has: nine `.docx` deliverables cannot be
handed to a workshop attendee.

---

## 3. Proposed structure — the CISA pattern, mapped

The CISA site is: `index.html` (hero, stats bar, 10 lesson cards, 5-day schedule
grid, domain-weight bars, resource grid in three groups, about, feedback, footer
disclaimer) + `lesson00–09.html` + `lesson10.html` (bonus faculty PD) + six
resource/tool pages.

The CMMC 8-week course maps onto that shape almost exactly — the source Module 6
splits into two half-days the same way CISA's Domains 2, 4, and 5 do.

| Lesson | Day / Half | Title | Source | CAP Phase |
|---|---|---|---|---|
| **L0** | Day 1 AM | CMMC Orientation & the Assessor Mindset | new + Module 3 mindset | — |
| **L1** | Day 1 PM | The Compliance Landscape & the CMMC Ecosystem | Module 1 | — |
| **L2** | Day 2 AM | FCI, CUI, and the Regulatory Stack | Module 2 | — |
| **L3** | Day 2 PM | Ethics, Independence & Assessment Planning | Module 3 | Phase 1 |
| **L4** | Day 3 AM | Scoping and Asset Categorization | Module 4 | Phase 1 |
| **L5** | Day 3 PM | Evidence: Adequacy, Sufficiency, Collection | Module 5 | Phase 2 |
| **L6** | Day 4 AM | Assessing the 14 Domains | Module 6A | Phase 2 |
| **L7** | Day 4 PM | Scoring, SPRS & the Incident Clock | Module 6B | Phase 2 |
| **L8** | Day 5 AM | Conducting the Assessment & Reporting | Module 7 | Phases 2–3 |
| **L9** | Day 5 PM | POA&M, Closeout, Transfer Test & Credential Roadmap | Module 8 | Phase 4 |
| **L10** | Bonus | Teaching CMMC — Faculty PD Guide | schedule.docx + instructor decks | — |

Ten lessons, five days, two ~3-hour sessions per day — structurally identical to
CISA. Contact time rises from 24 hours to 30, which absorbs the hands-on tool work
the workshop format adds.

**Per-lesson page anatomy** (matching the CISA lesson template exactly): sticky
topnav → lesson hero with meta chips → sidebar TOC → objectives with Bloom tags →
vocabulary flip-cards → ~10 content sections with in-practice callouts, exam tips,
and inline diagrams → **ThreadBridge case-study block** → scored knowledge check
with per-option rationale → prev/next pager.

---

## 4. The threaded case study — ThreadBridge Solutions

The source course already carries **ThreadBridge Solutions, LLC** through every
deliverable D2–D9: a fictional small manufacturer of DoD combat utility uniforms
that also sells commercial office supplies on GSA Schedule, so it sits across
Level 1 and Level 2 at once. Two sites, flat network, no VLANs, commercial M365
tenant holding CUI, unmanaged tablets reaching the ERP, a maintenance vendor with
standing remote access, and two seeded incidents — only one of which trips the
DFARS 72-hour clock.

A complete 172 KB interactive workbench for it already exists
(`threadbridge.html` / `uniforms_case_study.html`): tabbed environment briefing,
11 practitioner documents, 6 interview personas, incident records, save/restore
progress codes, print-to-PDF.

**The thread.** One ThreadBridge segment closes every lesson, and each segment is
executed **in a tool**, not on paper:

| Lesson | ThreadBridge segment | Tool the student executes it in |
|---|---|---|
| L0 | Meet the company; read the solicitation | Case Workbench — Overview tab |
| L1 | Trace the clause chain to the contract | **Clause Trace tool** |
| L2 | Sort the data inventory: FCI / CUI / neither | **CUI Determination tool** (NARA-cited) |
| L3 | Rule on the engagement; declare conflicts | **Engagement & Ethics Gate** |
| L4 | Categorize every asset; draw the boundary | **Scope & Asset Matrix tool** |
| L5 | Triage five real artifacts | **Evidence Adequacy/Sufficiency Triage** |
| L6 | Render objective-level determinations | **Domain Determination Worksheet** |
| L7 | Compute the DoD score; rule on the incidents | **SPRS Score Calculator** |
| L8 | Two-day mock assessment; interviews; findings | Case Workbench — Interviews + Findings |
| L9 | POA&M and closeout; cold transfer test | **POA&M Builder** + Piedmont Textile transfer test |

By Day 5 PM the student has executed a full CMMC Level 2 assessment on one company,
in sequence, with every intermediate artifact saved in the browser and printable.
The Day 5 cold transfer test (**Piedmont Textile Finishing**, a supplier inside
ThreadBridge's own supply chain, issued unseen and timed at 30 minutes) is the
honest check on whether the thread taught method or memorization.

---

## 5. The four decisions that change the build most

**D-1 · Visual identity — recommend deep navy + defense amber.**
CISA is ISACA red on navy; CISM is teal. CMMC needs its own so the three read as a
family without collision. Recommend charcoal-navy `#12233a` with a defense-amber
accent `#c8862a`, cream/slate neutrals, full light + dark token sets. Same
Georgia/Arial typographic pairing, same 60px sticky nav, same card and stats-bar
geometry as CISA — identical *feel*, distinct *identity*. Never DoD or Cyber AB
seals; the site is not affiliated.

**D-2 · Build the tools natively, reuse the workbench.**
Recommend authoring the eight tool pages fresh in the new design system, and
copying `threadbridge.html` into the folder re-skinned to the new palette rather
than rebuilding 172 KB of working case-study machinery. `applicability.html` is
harvested for content into the L4 Scope tool, not shipped as-is — it carries DoD
seal styling that does not belong on an unaffiliated site.

**D-3 · Deliverables become in-browser tool outputs, not `.docx` uploads.**
The source course's D1–D9 assume an instructor and a Canvas dropbox. In a workshop
neither exists. Recommend each deliverable become a tool output the learner
completes, self-checks against a revealed model answer, and prints to PDF — with
the rubric criteria shown as a self-assessment checklist. The Faculty PD Guide
(L10) retains the graded-course version for instructors who want it.

**D-4 · The regulatory disclosure is a first-class, dated component.**
The July 2026 Phase 2 suspension and the pending Reform Task Force report make
this the most perishable material in the catalogue. Recommend a dated
`REGULATORY STATUS` banner component appearing on the index and on L1, driven by a
single JS constant so a maintainer updates one line — plus a "verify before you
teach" note in L10. This is a hard requirement of Stage 1, not a nicety.

---

## 6. Explicitly out of scope

- Any change to the source 8-week course in `/Users/jirik/Downloads/CMMC/`. It is
  read-only input.
- New subject-matter research beyond verifying the perishable regulatory claims
  against `sources.docx` and primary sources. The content is already sourced.
- Canvas packaging, SCORM, LTI, or LMS import files.
- A backend. Everything persists in `localStorage` with copy-paste progress codes,
  as the existing workbench already does.
- ISACA CCP/CCA exam duration and passing scores — flagged unverified in the source
  course and will stay flagged, not guessed.

---

## 7. Known currency risks

| Risk | Horizon | Mitigation |
|---|---|---|
| CMMC Phase 2 suspension status (13 Jul 2026) may have changed | Weeks | Single-constant dated banner; verify within 7 days of any run |
| Reform Task Force report to DoW CIO, due mid-Sept 2026 | Days — imminent | L9 designed to absorb it; L10 tells the instructor to re-verify |
| 32 CFR 170 / 48 CFR acquisition rule amendments | 6–12 months | Citations carry section numbers so a diff is findable |
| NIST SP 800-171 Rev 3 adoption as assessment standard | 12–24 months | Rev 2 taught as the standard; Rev 3 as horizon-scanning only |
| ISACA CCP/CCA exam mechanics | Unknown | Held as unverified; no numbers published to learners |
| Case study currency (ThreadBridge v1.0, Jun 2025) | Stable | Fictional; no regulatory dependency beyond Rev 2 |

---

## 8. What I need from you

Four decisions above carry recommendations. Three are safe to act on. One genuinely
forks the build — **how much gets built now** — and that is the question posed
alongside this brief.

**APPROVAL GATE — awaiting go**

---

## Amendment — 2026-09-05

Two changes were approved after the initial build and applied throughout.

**1. The dated regulatory layer was removed entirely.** The CMMC Phase 2 suspension, the Reform Task Force, and the
`REG_STATUS` banner machinery are gone. Lesson 1 now teaches the durable skill the suspension was a vehicle for
— *policy announcement versus regulation*, and the three instruments that can actually change what a contractor
owes (a class deviation, a FAR/DFARS rule change, an amendment to 32 CFR Part 170). The programme is taught as
published. This removes the largest maintenance liability in the build; currency risk D-4 and rows 1–2 of the
Stage 1 currency table are retired.

**2. The threaded case study changed from ThreadBridge Solutions to Meridian Precision Defense Systems.**
Meridian is drawn from the CMMC 2.0 Training Portal case library (`casestudyjs1.html`) and is the portal's most
developed case: 147 employees, Dayton OH plus Huntsville AL, three DoD contracts worth $17.9M, eight seeded gaps,
nine audit documents, an accurate network diagram, and six named personnel with defined cybersecurity roles.
`meridian.html` replaces `threadbridge.html` as the case workbench. **Acuitas Machining Inc.** — a sub-tier supplier
inside Meridian's own supply chain — replaces Piedmont Textile Finishing as the cold transfer test.

**Why Meridian.** Structurally the closest match to ThreadBridge, so the pedagogy transferred without re-derivation
— two sites, technical data packages, flowdown. But it upgrades the workshop in four places:

- **The cloud lesson inverts.** ThreadBridge failed the FedRAMP *authorisation* on a commercial tenant. Meridian
  passes it — GCC High and AWS GovCloud, both FedRAMP High — and fails on *configuration*: partial Conditional
  Access, unrestricted SharePoint guest access, and a shared Global Admin service account excluded from the MFA
  policy. That is the harder and far more common failure, and Acuitas then supplies the authorisation-failure
  contrast one tier down.
- **The Phase 1 readiness call becomes genuinely arguable.** ThreadBridge had no SSP, so "not ready" was obvious.
  Meridian has an SSP, ten policies and a network diagram, and fails on one specific absence — no asset inventory,
  so scope cannot be validated under §170.19(c). Students must earn the determination with a reason rather than an
  impression of disorder.
- **The conditional-category lesson sharpens.** One missing artifact closes both conditional categories to the
  whole environment. That is the failure assessors actually meet: organisations that did most of the work.
- **A third mapping dispute appears, and it is the best one.** The portal maps its supply-chain gap to practices
  **3.17.1 / 3.17.2** — the SR family in NIST SP 800-171 **Rev 3**, which does not exist in Rev 2. It is scored
  zero and written up as a DFARS 252.204-7012(m) and §170.19 finding instead. A gap mapped to a requirement that
  does not exist in the applicable revision cannot be scored, remediated or defended.

**Numbers that moved.** Assessed score 44 → **59** (deductions 66 → 51, ratio 0.40 → 0.536); defensible range
40–48 → **50–59**; gap lines 17 → **14**; providers 5 → **8**; mapping disputes 2 → **3**.
