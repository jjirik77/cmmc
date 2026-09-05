# Stage 6 — Review Findings
## CMMC Level 2 Assessor Preparation — 5-Day Workshop
**Reviewed:** 2026-09-04 · Three perspectives: accuracy, pedagogy, learner experience.

This is a report of checks actually performed, not an assertion of quality. Where something was
not checked, it says so.

---

## What was verified, and how

| Check | Method | Result |
|---|---|---|
| Regulatory currency | Live web search, 4 Sep 2026 | Phase 2 suspension confirmed; Task Force report confirmed **still pending** |
| JavaScript syntax | `node --check` on every inline script in all 23 pages | Clean |
| Runtime errors | jsdom load of all 23 pages, capturing `jsdomError` | 0 pages with errors |
| Interactive behaviour | jsdom harness, 58 assertions across 8 pages | 58 pass, 0 fail |
| Internal links | Every non-anchor `href` resolved against the file list | 0 broken |
| HTML structure | Tag-balance check on div/section/table/main/details/script | Balanced on all pages |
| Answer-key integrity | Every knowledge-check question parsed | 100 questions, exactly one correct option each |
| Feedback completeness | Every option rationale measured | 400 rationales, 0 placeholder or short |
| Tool auto-grading | Every `data-ok` value matched against its own `<option>` list | 84 selects, 0 mismatches |
| Model answers | Every tool item's verdict panel measured | 78 items, 0 empty |
| Objective decompositions | Compared against NIST SP 800-171A | **1 defect found and fixed** — see A-1 |

**Specific behaviours verified in jsdom:** knowledge-check grading and no-double-count;
correct-answer reveal; flip cards; SPRS live scoring (key values → 66 deductions, score 44,
ratio 0.40, red pill; one changed value → 46; all zero → 110, green pill); tool reveal with
correct/incorrect styling; the *what-would-change-it* enforcement warning; transfer-test timer,
key lock, and unlock; `localStorage` save, progress-code export, and restore; theme toggle and
persistence; index structure counts.

---

## Accuracy

**A-1 · Assessment-objective decompositions were paraphrased — FIXED.**
*Severity: high (now resolved).* Three of the eight requirements in the Domain Worksheet listed
approximate objective sets rather than the NIST SP 800-171A decompositions: 3.5.3 showed 3
objectives instead of 5 (omitting both "accounts are identified" objectives), 3.3.1 showed 4
instead of 6, and 3.12.4 showed 6 instead of 8. Since the entire pedagogical claim of that tool
is objective-level fidelity, this was the most serious defect in the build. All three corrected
to the 800-171A structure; the affected model answers rewritten to match; and a provenance
callout added stating that the listed objectives are a study aid reproduced from 800-171A, not
the authority, and must be verified against the current published version. Counts now
6 / 4 / 5 / 6 / 8 / 7 / 2 / 2.

**A-2 · Unverified claims are flagged, not guessed — CONFIRMED.**
CCP and CCA exam duration and passing scores were not publicly stated by ISACA at time of
research. No figure appears anywhere in the build. The gap is explicitly marked in three places
(L0, L9, the one-pager) with instructions to confirm with ISACA.

**A-3 · Two widely-repeated errors are corrected explicitly — CONFIRMED.**
Level 1 is 15 requirements, not 17 (32 CFR 170.14(c)(2)); ISACA certifies individuals while the
Cyber AB accredits organizations. Both are taught as corrections, with the reason the wrong
version circulates. L10 notes that a module in the user's own existing portal carries the second
error, and recommends using the discrepancy to teach source authority.

**A-4 · Perishable content is isolated to one constant — CONFIRMED.**
`REG_STATUS` in `build/theme.py` drives the dated banner on the index and Lesson 1. A maintainer
updates one place and rebuilds. L10 carries the standing seven-day re-verification obligation and
a table of what to check.

**A-5 · Residual risk: NARA Registry authorities.** *Severity: low, unresolved by design.*
The authorities cited for CTI, PROCURE, EXPT, and PERS/PRVCY are as recorded in the source
course (link-checked 25 Aug 2026). NARA updates the Registry continuously and without
announcement. These were not independently re-verified in this build. L10 flags the check.

**A-6 · Residual risk: document versions.** *Severity: low, unresolved by design.*
CAP v2.0 and CoPC v2.0 are cited as current. Version numbers move; L10 requires re-verification
against the DoD CIO and Cyber AB libraries before each run.

---

## Pedagogy

**P-1 · Every outcome has an activity and a check — CONFIRMED.**
27 outcomes mapped in `02_learning_design_spec.md` §2, each to at least one activity and at
least one check. Coverage: 100 knowledge-check items, 84 auto-checked tool determinations, 78
tool items with model answers.

**P-2 · Items test judgment, not recall — CONFIRMED by inspection of all 100.**
No item asks for a version number, a date, a price, or a name. Every item presents an artifact,
an environment, a determination, or a professional situation and asks whether to accept it and
why. The distractors are drawn from things practitioners assert confidently in the field, and
each carries a rationale explaining *why it is attractive* rather than merely that it is wrong.

**P-3 · Conditional knowledge is taught with its condition and tested without it — CONFIRMED.**
The three highest-value conditional rules each have a knowledge-check item where the naive
answer drops the condition: the conditional asset categories (L4 Q8, L9 Q6), the MFA
partial-credit conjunction (L7 Q1), and POA&M threshold-plus-list (L9 Q1). The Acuitas printer
controller — the single hardest judgment in the workshop — turns entirely on this.

**P-4 · The fade is real and stated — CONFIRMED.**
L5 models three artifacts with reasoning exposed, the tool works five with the model answer one
click away, and L8 supplies nine documents with no model answer at all. The learner is told the
scaffolding is being removed.

**P-5 · The transfer test is genuinely cold — CONFIRMED by test.**
The profile is hidden until the clock starts, the determination key is hidden and all reveal
buttons disabled on load, and unlocking requires either timer expiry or an explicit confirm.
Verified in jsdom.

**P-6 · Weakness: the mock assessment is the least-scaffolded deliverable and has no in-tool
check.** *Severity: medium, accepted.* Day 5 morning runs in the existing case workbench, which
has no model findings report. A solo learner completes D8 with no comparison point beyond the
rubric. This was a deliberate consequence of the approved decision to reuse the workbench rather
than rebuild it, and it is the one place where a facilitated cohort has a real advantage over a
solo learner. **Offer:** a `findings-key.html` giving a model findings report and the
determination key for the nine documents would close it. Roughly one further tool's worth of work.

**P-7 · Weakness: no cumulative practice exam.** *Severity: low, accepted.*
The CISA site carries a standalone timed practice exam; this build does not. The 100 knowledge-check
items are distributed per-lesson and per-domain rather than mixed. A candidate rehearsing under
exam conditions has no single instrument. **Offer:** a mixed-domain, CCP-weighted timed exam
drawing on the existing 100 items plus new ones.

---

## Learner experience

**L-1 · Pacing.** Ten sessions at roughly 3 hours. Lesson pages run 63–73 KB of rendered HTML,
10–12 content sections, 6–13 vocabulary cards, one case segment, and 10 questions. Reading time
per lesson is roughly 35–50 minutes, leaving the balance for the tool work — which is where the
time should go. L10 (faculty) is deliberately lighter at 47 KB.

**L-2 · Cognitive load.** The heaviest single page is the Scope & Asset Matrix at 22 items. That
is a real load, and it is the correct one — the whole point of the session is that categorization
is a per-asset determination, and shortening the list would teach the opposite. It is also the
most mechanical of the tools, so items go quickly once the rule is understood.

**L-3 · Accessibility — verified by construction and inspection.**
Every interactive element is a real `<button>`, `<select>`, `<input>`, `<textarea>`, `<a>`, or
`<details>`, so tab order and keyboard activation come free; there is no div-with-onclick
anywhere. Every field has a `<label for>`; flip cards carry `aria-label`. Correct/incorrect
states carry text ("Correct." / "Not this one.") as well as colour. Both themes define the full
token set. All tables sit in `overflow-x:auto` wrappers so the body never scrolls horizontally.

**L-4 · Not verified: contrast ratios were not measured with a tool.** *Severity: low.*
The palette was chosen for high contrast and reads correctly in both themes on inspection, but
no automated WCAG contrast audit was run. **Offer:** run one and adjust the two or three muted
tokens if any fall short.

**L-5 · Not verified: rendering in a real browser at real viewports.** *Severity: medium.*
Everything was tested in jsdom, which executes JavaScript and builds a DOM but **does not lay
out or paint**. Media queries, the sticky TOC, the flip-card 3D transform, the schedule grid
collapse, and print output have not been seen. The CSS is conventional and modelled closely on a
site already in production, so the risk is low — but it is not zero, and I have not looked at
these pages. **This is the one thing I would check first**, and it takes about ten minutes:
open `index.html`, one lesson, the SPRS calculator, and the transfer test; resize; toggle dark
mode; print one tool to PDF.

**L-6 · Interactions do work static content could not — CONFIRMED for four of five widget types.**
The knowledge check forces commitment before disclosure. The SPRS meter makes the eligibility
threshold felt as a cliff. The countdown creates the conditions the transfer test measures. The
enforcement warning refuses to let an incomplete verdict be called finished. The flip cards are
the weakest case — they are retrieval practice, which is a real function, but they are close to
an accordion and are labelled as vocabulary rather than as a simulation.

**L-7 · The case workbench is visually adjacent, not identical.** *Severity: low, accepted.*
`threadbridge.html` was copied and given a palette overlay plus a return bar rather than being
rebuilt in the new design system, per the approved decision. It shares the navy-and-amber colours
but retains its own layout and typography. It will read as a companion application rather than as
another page of the site.

---

## Summary

| | Count |
|---|---|
| Defects found and fixed during review | 1 (A-1, high) |
| Accepted limitations, documented | 5 (A-5, A-6, P-6, P-7, L-7) |
| Not verified, with offers to close | 2 (L-4 contrast audit, L-5 browser rendering) |

**Nothing is left as a placeholder.** No empty feedback text, no unwritten model answer, no
fabricated citation, no guessed number.

The highest-value next action is **L-5**: ten minutes in a browser. After that, P-6 (a findings
key for the mock assessment) is the largest genuine gap in the learner experience for anyone
working the material alone.

---

## Amendment review — 2026-09-05

Three changes were made after the initial review: the dated regulatory layer was removed, the case study changed to
Meridian Precision Defense Systems, and self-check rubrics were added. Everything below was re-verified after those
changes.

| Check | Result |
|---|---|
| Runtime errors across all 23 pages (jsdom) | 0 |
| Functional assertions | **80 pass, 0 fail** (was 58; 22 new, covering rubrics and the dropdown fixes) |
| Knowledge-check questions / option rationales | 100 / 400, one correct answer each, none short |
| Auto-checked tool selects | 85, all answer keys present in their own option lists |
| Tool items with model answers | 82, none empty |
| Self-check rubrics | 69 across 9 tools, all with 3+ checks and a live tally |
| Internal links | 0 broken |
| Stale-reference sweep (18 terms) | 0 hits |

### Defects found and fixed in this pass

**A-7 · Answer-shape cues in three bespoke dropdowns — FIXED.** *Severity: high.* The user asked whether
deliverables should become dropdowns, and working through the answer exposed the mirror-image problem in what was
already built. Three option lists let a student score correct on shape alone:

- **Transfer test, CNC controllers.** The option list contained *"Specialized Asset — but the treatment is
  unavailable"* — which is the answer, and the pivot the whole transfer test exists to measure. Replaced with the
  plain category; the conditional reasoning moved to a free-text basis field whose label now asks explicitly whether
  the condition is met, and the model answer states that picking the category without addressing the condition is a
  right-looking answer for the wrong reason.
- **Domain worksheet, mapping disputes.** The correct option ran 59 characters against a 12-character shortest.
  Options are now uniform requirement identifiers; the reasoning moved to free text.
- **POA&M eligibility.** The correct option ran 62 characters against a 3-character shortest. Rebalanced to four
  parallel options, with the correct one now the *shortest*.

A length-cue audit was added to the checks. It groups selects by option signature and ignores shared taxonomies
(where length cannot identify *which* item an answer belongs to), flagging only bespoke lists. It now reports none.

**A-8 · Ethics dispositions were graded by wordiness — FIXED.** *Severity: medium.* The five disposition options
ranged 8–37 characters, with the strongest-worded consistently correct. Rewritten as five parallel phrases of 21–23
characters. The engagement gate was also rebalanced from three affirmative / one negative to two and two, with the
new fourth option ("the engagement letter terms are disqualifying") a genuinely plausible near-miss — it identifies a
real prohibited term that is nonetheless *curable*, where the firm-level bar is not. That distinction is now the
substance of the item.

**A-9 · `tools2.py` was truncated to zero bytes by a build script error — FIXED.** *Severity: high, transient.* A
patch script opened the file for writing and then raised before writing. Caught by a file-size sweep, reconstructed
in full, and verified: 6 conflicts, 8 scenarios, 5 dispositions, both gates, all rubrics. No other source file was
affected.

### Added

**Self-check rubrics — 69 across 9 tools.** Each appears *with* the model answer, never before it, as three or four
tickable statements with a live tally that turns amber when partially met and green when complete. Seven standard
sets (determination, verdict, category, citation, ethics, scoring, incident) plus bespoke sets for the POA&M items.
Each statement names a specific thing to do differently rather than a quality judgement, and the footer says so:
*"an unticked box is worth more to you than a ticked one."*

This addresses the real weakness behind the dropdown question — not that there was too much writing, but that
free-text answers had no feedback mechanism beyond passively reading a model answer. Checkbox state persists to
`localStorage` and travels in the progress code; it is excluded from the "items answered" counter so ticking boxes
cannot inflate progress.

### Retired

Currency risk **D-4** and rows 1–2 of the Stage 1 currency table are gone with the dated regulatory layer. The
workshop now teaches the rule as published and, separately, how to tell whether an announcement has changed it —
which is a method rather than a fact, and does not go stale.

### Still not verified

**L-4 and L-5 stand.** No WCAG contrast audit has been run, and these pages have still never been rendered in a real
browser — jsdom executes JavaScript and builds a DOM but does not lay out or paint. The rubric checkboxes are new
visual elements and are the most likely thing to need a nudge (spacing, accent colour in dark mode). Ten minutes in a
browser remains the highest-value next action.
