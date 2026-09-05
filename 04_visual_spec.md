# Stage 4 — Visual Specification
## CMMC Level 2 Assessor Preparation — 5-Day Workshop

The system is implemented once, in `build/theme.py`, and every page inherits it. Editing that
file and rebuilding restyles all 22 generated pages.

---

## 1. The design system

### Palette — navy and defense amber

Distinct from the CISA site (ISACA red on navy) and the CISM materials (teal), so the three read
as a family without collision. Every colour is defined as a token on bare `:root`; only the
tokens are redefined under `[data-theme="dark"]`.

| Token | Light | Dark | Role |
|---|---|---|---|
| `--navy` | `#12233a` | `#12233a` | Headers, day columns, case blocks, table heads |
| `--navy-mid` | `#0d1a2b` | — | Day-theme strip |
| `--navy-light` | `#24425f` | — | In-practice accents, hover states |
| `--gold` | `#c8862a` | `#c8862a` | Primary accent, rules, CTAs, numerals |
| `--gold-light` | `#e0a244` | — | Hover on amber |
| `--gold-pale` | `#fbf1e0` | `#2b1d09` | Exam-tip callout ground |
| `--body-bg` | `#eef1f5` | `#071320` | Page ground |
| `--card-bg` | `#ffffff` | `#0f2537` | Cards, panels, nav |
| `--section-alt` | `#e3e8ee` | `#0b1d2c` | Alternating sections, option rows |
| `--blue-pale` | `#e9eef4` | `#0d2436` | Hero, callouts |
| `--text-primary` | `#10202f` | `#e8eef5` | Body |
| `--text-secondary` | `#2b4258` | `#a3b6c9` | Prose |
| `--text-muted` | `#5c7086` | `#748a9e` | Metadata |
| `--border` | `#c2ccd8` | `#1e3a52` | Rules, table lines |
| `--ok` / `--warn` / `--bad` | `#2f6f4f` / `#9a5b12` / `#9d3427` | `#6fbf90` / `#e0a244` / `#e0796a` | Determination states |

**No DoD, Cyber AB, or ISACA seal or wordmark is used anywhere.** The nav seal is a plain amber
disc reading `CMMC / L2` — a workshop mark, not an imitation of an authority.

### Type

- **Georgia** for headings, card titles, and body prose — the CISA site's serif, retained so the
  two read as siblings.
- **Arial / Arial Narrow** for UI: eyebrows, chips, table headers, buttons, metadata, numerals.
- Scale: hero `clamp(2.2rem, 5vw, 3.6rem)`; section titles `clamp(1.5rem, 3vw, 2rem)`; lesson h2
  `1.45rem`; body `0.9rem` at `1.85` line-height; metadata `0.68–0.78rem` with `0.06–0.2em`
  tracking, uppercase.

### Spacing and geometry

Sections `4rem 2rem`, max width `1200px`. Cards `1.5rem` padding, `4px` radius, `1px` border, a
`3px` amber top rule. Buttons `2px` radius — deliberately squarer than the cards, so actions
read as distinct from content. The 48×3px amber `.rule` under every section title is the single
most repeated motif and is what makes the pages scan as one system.

---

## 2. Figure inventory

Every figure earns its place by doing something the caption cannot. Nothing here restates its
own heading.

| # | Figure | Form | What it makes clear |
|---|---|---|---|
| 1 | Instrument table (L1) | 3-column reference | Which kinds of document change a requirement and which do not. Replaced the dated status banner in the 2026-09-05 amendment. |
| 2 | Framework comparison | 4-column comparison | That mandatory/voluntary and *how conformity is shown* are the axes, not control content |
| 3 | Nine-link chain | Numbered sequence table | Order and joins — and that links 1–5 predate CMMC |
| 4 | DFARS clause family | 3-column table | That four clauses routinely conflated do different work |
| 5 | FCI vs CUI consequences | Side-by-side | The asymmetry in obligation size |
| 6 | Contractor may / may not | Two-column opposition | Designation authority, by what a contractor cannot do |
| 7 | Registry categories | 4-column reference | The four things every determination must produce |
| 8 | 252.204-7012 obligations | Obligation / requirement / paragraph | That each obligation has a locatable paragraph |
| 9 | Consultant vs assessor | 6-row opposition | That the governing document differs, which is the row that matters |
| 10 | Eight CoPC principles | Principle → *question it asks* | Principles as decision rules rather than a list |
| 11 | Three-year bar: covers / does not say | Two-column opposition | The two directions in which the rule is misquoted |
| 12 | Preliminary proceedings & Phase 1 | Activity → what it settles | That conflicts are handled *before* Phase 1 |
| 13 | Five asset categories | Category / test / obligation / how assessed | That two carry conditions — set apart in a following callout |
| 14 | ESP vs CSP | 3-row comparison | That classification and obligation are separate answers |
| 15 | Contested calls | Asset / tempting answer / why the test says otherwise | Where the arguments actually arise |
| 16 | Justifications that work / do not | Two-column opposition | The difference between citing the test and naming the asset |
| 17 | Adequacy vs sufficiency | Artifact-type matrix | That these are different questions, not degrees |
| 18 | Methods and objects | Method / establishes / **cannot establish** | The fourth column is the point |
| 19 | Fourteen domains | Domain → characteristic failure | Where to look first |
| 20 | Three determinations | Determination / meaning / what it requires | That N/A carries a justification burden |
| 21 | Scoring weights + partial credit | Two stacked tables | That partial credit is a closed set of two |
| 22 | Gap-by-gap scoring | 5-column working table | The arithmetic, the three mapping disputes, and the practice that does not exist in Rev 2 |
| 23 | Evidence package register | Document / what it says / **what to notice** | That the package is internally inconsistent |
| 24 | POA&M rules | Rule → practice | Threshold and list as independent gates |
| 25 | Revised assessment | Requirement / points / **deferrable?** | That the two cheapest items are the barriers |
| 26 | Case thread (index) | Session / action / tool | That one company is carried end to end |
| 27 | CAP phase bars | Horizontal bars | That the week's shape is the assessment's shape |
| 28 | Delivery models (L10) | 3-column comparison | Which model fits which cohort |

No decorative illustration, no stock imagery, no icon set beyond the small emoji used as
resource-card glyphs. The subject is documentary; the visual work is making dense comparative
material scannable.

---

## 3. Interactive widget specifications

All five widget types were built to spec and verified in jsdom (58 assertions, all passing, re-run after the 2026-09-05 amendment).

### W1 — Vocabulary flip card
**States:** front (term + "Click to reveal") / flipped (definition).
**Manipulates:** click or Enter/Space on a real `<button>`.
**Teaches:** retrieval practice on terms the exams use precisely.
**Viewport:** fixed `170px` height, definition scrolls internally if long — the card never grows
and never pushes the grid. 6–13 cards per lesson in a `230px`-minimum auto-fill grid.

### W2 — Knowledge check
**States:** unanswered / answered-correct / answered-wrong; per-question and page-level.
**Manipulates:** clicking one option.
**Changes:** the chosen option takes a correct/wrong border and ground; the correct option is
always revealed; all options disable; the rationale panel opens carrying the rationale for the
chosen option *and*, when wrong, the correct answer with its rationale; the page counter updates.
**Teaches what static text cannot:** it forces commitment before disclosure. Reading a rationale
after choosing is a different cognitive event from reading it alongside.
**Guards:** re-clicking cannot double-count (verified).
**Viewport:** each question is a self-contained block; nothing expands beyond the flow.

### W3 — Tool item with model answer
**States:** unanswered / revealed-correct / revealed-incorrect / revealed-ungraded.
**Manipulates:** free-text and select fields, then a reveal button.
**Changes:** where the item has an auto-checkable select, the verdict panel takes a good/bad
state and its heading changes to "Correct — and here is the full reasoning" or "Not this one —
here is why". The model answer opens in full. The button disables.
**Special case:** items with a *what would change it* field show an inline warning if that field
is empty on reveal. This is the one place the tool refuses to let a learner call an incomplete
verdict finished.
**Viewport:** the reveal is in-flow, not a modal. Nothing overlays; nothing needs to fit a
viewport because nothing expands over the page.

### W4 — Live score meter (SPRS Calculator)
**States:** partial (eligibility shows `—`) / complete-below-threshold / complete-above-threshold.
**Manipulates:** 14 deduction selects.
**Changes:** deductions total, score, ratio to two decimals, an eligibility pill that switches
between neutral / red / green, a progress count, and a horizontal bar whose width tracks the
score and whose fill switches from amber to green at 0.8.
**Teaches what static content cannot:** the threshold as a *cliff*. Watching 110 fall past 88 and
the pill turn red does something a printed table does not.
**Verified:** all-key values → 51 deductions, score 59, ratio 0.54, red pill. Changing GAP-01 from
5 to 3 → 61. All zeroes → 110, green pill.
**Viewport:** the meter is a single row above a 28px bar, inside the same panel as the table.

### W5 — Countdown (Transfer Test)
**States:** pre-start (profile hidden, key locked, reveal buttons disabled) / running / expired
or manually unlocked.
**Manipulates:** a start button, then a deliberate unlock.
**Changes:** starting reveals the profile and answer sheet and scrolls to them; the sticky clock
counts down and turns red under five minutes; expiry auto-unlocks the key; manual unlock
requires a confirm.
**Teaches what static content cannot:** cold, timed conditions. A key that is one scroll away is
not a transfer test.
**Verified:** all six state transitions.
**Viewport:** the clock is a 44px sticky strip below the nav. The profile and key are page flow.

### Cross-cutting
- **Persistence:** every field saves to `localStorage` on change, keyed per tool. A base64
  progress code exports and restores all answers across devices. Every access is
  try/catch-wrapped and the page renders correctly with no stored value.
- **No-scroll constraint:** met by construction. Nothing in this build expands into an overlay,
  modal, or fixed-height revealed region. The only fixed-height element is the flip card, which
  scrolls internally.
- **Print:** nav, save bar, buttons, TOC, and pager are suppressed; panels and tables avoid
  breaking across pages.

---

## 4. Responsive behaviour

| Breakpoint | Change |
|---|---|
| ≥ 980px | Two-column lesson layout, sticky sidebar TOC; 5-column schedule grid |
| < 980px | Single column, TOC collapses to the top; schedule to 2 columns; nav links hidden (anchors remain reachable from the index) |
| < 560px | Schedule to 1 column; section padding reduced |

Tables never reflow — they scroll inside their own `overflow-x:auto` wrapper, because a
comparison table that reflows into stacked cells stops being a comparison.

**BUILD COMPLETE — READY FOR REVIEW**
