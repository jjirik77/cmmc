# -*- coding: utf-8 -*-
from theme import head, nav, FOOT, THEME_JS

CARDS = [
 ("L 0","", "Day 1 &mdash; Morning","CMMC Orientation and the Assessor Mindset","lesson00.html",
  "CMMC is not a cybersecurity test &mdash; it is a conformity regime. The ecosystem, the three levels, the "
  "credential pathway, and the change of role everything else depends on.",
  "Meet Meridian; read the solicitation"),
 ("L 1","CCP 5% + 15%","Day 1 &mdash; Afternoon","The Compliance Landscape and the CMMC Ecosystem","lesson01.html",
  "How a NIST publication became something that can cost a company a contract. Nine links from EO 13556 to a "
  "clause in a live solicitation &mdash; and how to tell a policy announcement from an instrument that actually\n  changes what a contractor owes.",
  "Clause Trace tool &middot; D1"),
 ("L 2","CCP 15%","Day 2 &mdash; Morning","FCI, CUI, and the Regulatory Stack","lesson02.html",
  "The determination everything downstream depends on. Two definitions, the NARA Registry used properly, "
  "DFARS 252.204-7012 clause by clause, and a contractor's own inventory audited against the authorities.",
  "CUI Determination tool &middot; D2"),
 ("L 3","CCP 5% + 25%","Day 2 &mdash; Afternoon","Ethics, Independence, and Assessment Planning","lesson03.html",
  "Where you stop being a practitioner. Eight principles as decision rules, the three-year bar stated precisely, "
  "and a CAP Phase 1 that may correctly conclude the engagement cannot proceed.",
  "Engagement &amp; Ethics Gate &middot; D3"),
 ("L 4","CCA 20%","Day 3 &mdash; Morning","Scoping and Asset Categorization","lesson04.html",
  "The highest-leverage decision an assessor makes. Five categories, two of them conditional and both earned "
  "rather than claimed &mdash; which decides almost every contested call in the environment.",
  "Scope &amp; Asset Matrix &middot; D4"),
 ("L 5","CCP 35% / CCA 40%","Day 3 &mdash; Afternoon","Evidence: Adequacy, Sufficiency, and Collection","lesson05.html",
  "The conceptual hinge. The gap between having a document and doing the thing &mdash; five real artifacts "
  "evaluated, including one that is excellent evidence and still does not carry the requirement.",
  "Evidence Triage tool &middot; D5"),
 ("L 6","CCP 35% / CCA 40%","Day 4 &mdash; Morning","Assessing the Fourteen Domains","lesson06.html",
  "Determinations at the objective level across fourteen families, each with its characteristic small-contractor "
  "failure &mdash; and two gaps the company has mapped to the wrong requirement.",
  "Domain Determination Worksheet &middot; D6"),
 ("L 7","110 to &minus;203","Day 4 &mdash; Afternoon","Scoring, SPRS, and the Incident Clock","lesson07.html",
  "Determinations become a number that a named official affirms under penalty. The weighting, the two "
  "partial-credit exceptions, and an account that should not exist authenticating four times.",
  "SPRS Calculator &middot; D7"),
 ("L 8","CCP 25% / CCA 25%+15%","Day 5 &mdash; Morning","Conducting the Assessment and Reporting Findings","lesson08.html",
  "The summative session. Nine documents, six interview personas, two incidents, and a chief executive who will "
  "ask you, warmly and reasonably, to tell her what she needs to do.",
  "Full mock assessment &middot; D8"),
 ("L 9","Closes CCP blueprint","Day 5 &mdash; Afternoon","POA&amp;M, Closeout, and What You Do Next","lesson09.html",
  "CAP Phase 4, a POA&amp;M whose cheapest items are absolute barriers, a cold thirty-minute transfer test on a "
  "company you have never seen, and a credential roadmap with dates on it.",
  "POA&amp;M Builder + transfer test &middot; D9"),
]

BONUS = ("Bonus","Faculty PD","Not part of the 5-day sequence","Teaching CMMC &mdash; Faculty and Facilitator Guide",
 "lesson10.html",
 "You have worked the material; this is how to deploy it. Three delivery models, the facilitation moments that "
 "make or break each session, the competency rubric, the instruments that must be issued cold, and the "
 "maintenance obligation that comes with teaching a subject in active regulatory flux.","")

SCHEDULE = [
 ("Day 1","Foundations",
  ["Understand what CMMC is and who governs which part of it",
   "Trace the chain from a 2010 executive order to a clause in a live solicitation"],
  [("Lesson 0 &mdash; AM","Orientation &amp; the Assessor Mindset","lesson00.html","~3 hrs"),
   ("Lesson 1 &mdash; PM","Compliance Landscape &amp; Ecosystem","lesson01.html","~3 hrs &middot; CCP 5%+15%")],
  "Thread: <strong>meet Meridian</strong>, then trace the clause"),
 ("Day 2","Information &amp; Independence",
  ["Determine what is FCI, what is CUI, and what is neither &mdash; cited to the Registry",
   "Apply the CoPC and run CAP Phase 1, including deciding the engagement cannot proceed"],
  [("Lesson 2 &mdash; AM","FCI, CUI &amp; the Regulatory Stack","lesson02.html","~3 hrs &middot; CCP 15%"),
   ("Lesson 3 &mdash; PM","Ethics, Independence &amp; Planning","lesson03.html","~3 hrs &middot; CCP 5%+25%")],
  "Thread: <strong>CUI determination</strong>, then the ethics gate"),
 ("Day 3","Scope &amp; Proof",
  ["Categorize every asset and draw a boundary that survives a hostile reader",
   "Separate adequacy from sufficiency on artifacts that arrive exactly as they are"],
  [("Lesson 4 &mdash; AM","Scoping &amp; Asset Categorization","lesson04.html","~3 hrs &middot; CCA 20%"),
   ("Lesson 5 &mdash; PM","Evidence: Adequacy &amp; Sufficiency","lesson05.html","~3 hrs &middot; CCP 35%")],
  "Thread: <strong>asset matrix</strong>, then evidence triage"),
 ("Day 4","Determination &amp; Score",
  ["Render objective-level determinations across the fourteen domains",
   "Compute a DoD Assessment score and rule on a live incident"],
  [("Lesson 6 &mdash; AM","Assessing the Fourteen Domains","lesson06.html","~3 hrs &middot; CCA 40%"),
   ("Lesson 7 &mdash; PM","Scoring, SPRS &amp; the Incident Clock","lesson07.html","~3 hrs &middot; 110 to &minus;203")],
  "Thread: <strong>domain worksheet</strong>, then the SPRS calculator"),
 ("Day 5","Assess, Report, Close",
  ["Run a full Level 2 assessment under time pressure and write defensible findings",
   "Close it out &mdash; then scope a company you have never seen, in thirty minutes"],
  [("Lesson 8 &mdash; AM","Conducting the Assessment &amp; Reporting","lesson08.html","~3 hrs &middot; mock assessment"),
   ("Lesson 9 &mdash; PM","POA&amp;M, Closeout &amp; Roadmap","lesson09.html","~3 hrs &middot; transfer test")],
  "Thread: <strong>the mock assessment</strong>, then Acuitas cold"),
]

THREAD = [
 ("L0","Meet the company; read the solicitation","Case workbench &mdash; Overview","meridian.html"),
 ("L1","Trace the clause chain to the contract","Clause Trace tool","clause-trace.html"),
 ("L2","Sort the data inventory: FCI / CUI / neither","CUI Determination tool","cui-determination.html"),
 ("L3","Rule on the engagement; declare every conflict","Engagement &amp; Ethics Gate","ethics-gate.html"),
 ("L4","Categorize every asset; draw the boundary","Scope &amp; Asset Matrix","scope-matrix.html"),
 ("L5","Triage five artifacts; build the request list","Evidence Adequacy Triage","evidence-triage.html"),
 ("L6","Render objective-level determinations","Domain Determination Worksheet","domain-worksheet.html"),
 ("L7","Compute the score; rule on the incident","SPRS Score Calculator","sprs-calculator.html"),
 ("L8","Two-day mock assessment; interviews; findings","Case workbench &mdash; full package","meridian.html"),
 ("L9","POA&amp;M and closeout, then the cold transfer test","POA&amp;M Builder &middot; Acuitas","poam-builder.html"),
]

PHASES = [
 ("Preliminary proceedings &mdash; conflicts, contract","Day 2 PM",14),
 ("Phase 1 &mdash; Conduct the Pre-Assessment","Day 2 PM &ndash; Day 3 AM",22),
 ("Phase 2 &mdash; Assess Conformity to Requirements","Day 3 PM &ndash; Day 5 AM",40),
 ("Phase 3 &mdash; Complete and Report Results","Day 5 AM",12),
 ("Phase 4 &mdash; Certificate and Closeout POA&amp;M","Day 5 PM",12),
]

RESOURCES = [
 ("&#9881;&#65039;","Threaded Case Tools",[
  ("Tool &middot; D1","&#128279;","Clause Trace","clause-trace.html",
   "Build the nine-link chain from EO 13556 to the clause in Meridian's solicitation, then answer the three "
   "questions D1 asks. Checks your citations against the authorities and prints as a regulatory trace memo.",
   "9 links &middot; Primary sources &middot; Level determination &middot; Print to PDF"),
  ("Tool &middot; D2","&#128269;","CUI Determination","cui-determination.html",
   "Six information types, six company classifications, and your determination on each &mdash; category, marking, "
   "Basic or Specified, and the authority. Names the kind of error where the company is wrong.",
   "NARA Registry &middot; FCI vs CUI &middot; Error typing &middot; Open items"),
  ("Tool &middot; D3","&#9878;&#65039;","Engagement &amp; Ethics Gate","ethics-gate.html",
   "Every conflict in the engagement packet, dispositioned as disclose, mitigate, or avoid with the deciding party "
   "named &mdash; plus the eight CoPC scenarios and the Phase 1 readiness call.",
   "CoPC &middot; Three-year bar &middot; CAP Phase 1 &middot; Readiness"),
  ("Tool &middot; D4","&#128506;&#65039;","Scope &amp; Asset Matrix","scope-matrix.html",
   "Every asset categorized against the defining test, with the boundary, the ESP and CSP analysis, flowdown, and "
   "the open items. Checks the five contested calls and the conditional-category trap.",
   "5 categories &middot; ESP vs CSP &middot; CRM &middot; Flowdown"),
  ("Tool &middot; D5","&#128300;","Evidence Adequacy Triage","evidence-triage.html",
   "Five artifacts exactly as supplied. Name the objective, render adequate / sufficient / both / neither, and say "
   "what would change the verdict &mdash; the clause the tool will not let you skip.",
   "Adequacy &middot; Sufficiency &middot; Methods &middot; Request list"),
  ("Tool &middot; D6","&#9989;","Domain Determination Worksheet","domain-worksheet.html",
   "Fifteen requirements decomposed into assessment objectives, with the evidence attached. Determine each "
   "objective, cite the evidence, and argue the two gaps mapped to the wrong requirement.",
   "Objective level &middot; MET / NOT MET / N/A &middot; Mapping disputes"),
  ("Tool &middot; D7","&#128290;","SPRS Score Calculator","sprs-calculator.html",
   "Fourteen gap lines, live running total, and the eligibility threshold moving against you. Flags the 3.5.3 trap, "
   "the three mapping disputes, and the practice that does not exist in Rev 2 at all.",
   "5/3/1 weighting &middot; Partial credit &middot; 0.8 threshold &middot; Floor at &minus;203"),
  ("Tool &middot; D9","&#128203;","POA&amp;M Builder","poam-builder.html",
   "Eligibility first: the threshold, then the six that may never be deferred. Refuses an ineligible deferral and "
   "says why. Then milestones, owners, dates, closeout, and sustainment.",
   "&sect;170.21 &middot; The six &middot; 180-day window &middot; Affirmation"),
 ]),
 ("&#129514;","Case Study &amp; Assessment",[
  ("Case Study","&#127981;","Meridian Precision Defense Systems &mdash; Case Workbench","meridian.html",
   "The company that carries all five days. Environment briefing, eleven practitioner documents, six interview "
   "personas, two incidents, and a save-and-restore workspace. The Day 5 mock assessment runs here.",
   "147 people &middot; 2 sites &middot; 2 contracts &middot; 11 documents &middot; 6 interviews"),
  ("Transfer Test","&#9201;&#65039;","Acuitas Machining &mdash; Cold Scope","transfer-test.html",
   "Thirty minutes, timed, on a company you have never seen &mdash; a supplier inside Meridian's own supply "
   "chain. Eight assets, three questions. The determination key opens when the timer stops.",
   "Timed &middot; Cold &middot; Flowdown &middot; OT asset &middot; Two ESPs"),
  ("Reference","&#128424;&#65039;","Exam-Day One-Pager","onepager.html",
   "One printable page of the highest-yield material: the three-part standard, adequacy versus sufficiency, the "
   "five categories with their conditions, the scoring weights and both exceptions, and the six that may never "
   "be deferred.",
   "Printable &middot; Cram sheet &middot; Thresholds &middot; Trap patterns"),
 ]),
 ("&#127891;","For Facilitators",[
  ("Faculty PD","&#128218;","Teaching CMMC &mdash; Facilitator Guide","lesson10.html",
   "Three delivery models, the facilitation moments that make or break each session, the competency rubric, the "
   "three instruments that must be issued cold, and the standing obligation to re-verify the regulatory position "
   "within seven days of any run.",
   "Delivery models &middot; Facilitation &middot; Rubric &middot; Maintenance"),
 ]),
]

def build(lessons):
    cards = ""
    for badge, weight, day, title, href, desc, thread in CARDS:
        w = f'<div class="domain-weight"><strong>{weight}</strong>exam weight</div>' if weight else ""
        cards += f"""<article class="lesson-card">
  <div class="card-header"><span class="lesson-badge">{badge}</span>{w}</div>
  <span class="card-day-tag">{day}</span>
  <h3 class="card-title">{title}</h3>
  <p class="card-desc">{desc}</p>
  <p class="card-thread"><strong>Thread &rarr;</strong> {thread}</p>
  <div class="card-footer"><a class="launch-btn" href="{href}">Launch Lesson <span class="arrow">&rarr;</span></a></div>
</article>"""
    b = BONUS
    cards += f"""<article class="lesson-card card-special">
  <div class="card-header"><span class="lesson-badge">{b[0]}</span>
  <div class="domain-weight"><strong>{b[1]}</strong>{b[2]}</div></div>
  <h3 class="card-title">{b[3]}</h3>
  <p class="card-desc">{b[5]}</p>
  <div class="card-footer"><a class="launch-btn" href="{b[4]}">Open Guide <span class="arrow">&rarr;</span></a></div>
</article>"""

    sched = ""
    for day, theme, aims, sessions, cap in SCHEDULE:
        s = ""
        for num, name, href, meta in sessions:
            s += (f'<a class="day-lesson" href="{href}"><span class="day-lesson-num">{num}</span>'
                  f'<span class="day-lesson-name">{name}</span>'
                  f'<span class="day-lesson-meta">&#128340; {meta}</span></a>')
        aimhtml = "".join(f"<li>{a}</li>" for a in aims)
        sched += f"""<div class="day-col"><div class="day-header">{day}</div>
  <div class="day-theme">{theme}</div>
  <div style="padding:.7rem .85rem 0"><ul style="margin:0 0 0 1rem;padding:0">{aimhtml}</ul></div>
  <div class="day-lessons">{s}</div>
  <div class="day-cap">{cap}</div></div>"""

    thread = ""
    for lid, what, tool, href in THREAD:
        thread += (f'<tr><td><strong>{lid}</strong></td><td>{what}</td>'
                   f'<td><a href="{href}" style="color:var(--gold);font-weight:700">{tool} &rarr;</a></td></tr>')

    bars = ""
    for label, when, pct in PHASES:
        bars += (f'<div class="bar-row"><div class="bar-label">{label}<br>'
                 f'<span style="color:var(--text-muted);font-size:.72rem">{when}</span></div>'
                 f'<div class="bar-track"><div class="bar-fill" style="width:{pct*2.2}%">{pct}%</div></div></div>')

    res = ""
    for icon, heading, items in RESOURCES:
        res += (f'<div class="resource-section-heading"><span class="rsh-icon">{icon}</span>'
                f'<h3>{heading}</h3></div><div class="resource-grid">')
        for rtype, ricon, rtitle, rhref, rdesc, rcov in items:
            res += f"""<article class="resource-card">
  <span class="rc-type">{rtype}</span>
  <div class="rc-icon-title"><span class="rc-icon">{ricon}</span><span class="rc-title">{rtitle}</span></div>
  <p class="rc-desc">{rdesc}</p>
  <p class="rc-covers"><strong>Covers:</strong> {rcov}</p>
  <div class="card-footer"><a class="launch-btn" href="{rhref}">Open <span class="arrow">&rarr;</span></a></div>
</article>"""
        res += "</div>"

    return head("CMMC Level 2 Assessor Preparation | 5-Day Workshop",
                "A five-day, ten-session workshop preparing CCP and CCA candidates to scope, assess, score, "
                "report, and close out a CMMC Level 2 assessment on one threaded case study.") + nav() + f"""
<header class="hero">
  <div class="hero-eyebrow">&#9670; CMMC Level 2 &middot; CCP and CCA Preparation &#9670;</div>
  <h1>Assess a Real Company in <span>Five Days</span></h1>
  <p class="hero-subtitle">Ten sessions, fourteen domains, one defense contractor carried end to end &mdash;
    scoped, evidenced, determined, scored, assessed, reported, and closed out. Then thirty minutes on a company
    you have never seen.</p>
  <a class="hero-cta" href="#lessons">Begin the Workshop &#9660;</a>
</header>
<div class="stats-bar">
  <div class="stat-item"><span class="stat-num">5</span><span class="stat-label">Days</span></div>
  <div class="stat-item"><span class="stat-num">10</span><span class="stat-label">Sessions</span></div>
  <div class="stat-item"><span class="stat-num">110</span><span class="stat-label">Requirements</span></div>
  <div class="stat-item"><span class="stat-num">320</span><span class="stat-label">Objectives</span></div>
  <div class="stat-item"><span class="stat-num">14</span><span class="stat-label">Domains</span></div>
  <div class="stat-item"><span class="stat-num">9</span><span class="stat-label">Case Tools</span></div>
</div>
<section class="section" id="lessons">
  <div class="section-eyebrow">Workshop Content</div>
  <h2 class="section-title">Ten Sessions. One Company. Four CAP Phases.</h2>
  <div class="rule"></div>
  <p class="section-desc">Each session carries learning objectives, key terminology, a full content outline with
    exam-tip callouts, a Meridian segment executed in a purpose-built tool, and a scored knowledge check with
    per-option rationale. Begin at Lesson 0 for the orientation and the assessor mindset.</p>
  <div class="card-grid">{cards}</div>
</section>
<div class="section-alt"><section class="section" id="thread">
  <div class="section-eyebrow">The Threaded Case Study</div>
  <h2 class="section-title">Meridian Precision Defense Systems, Carried End to End</h2>
  <div class="rule"></div>
  <p class="section-desc">One fictional 147-person precision manufacturer in Dayton, Ohio, with a second site in
    Huntsville, Alabama, holding three DoD contracts worth $17.9M &mdash; an Army AMCOM prime, a Raytheon
    subcontract, and a NAVAIR SBIR. All three carry DFARS 252.204-7012. It has a CISO, ten written policies, a
    System Security Plan, an accurate network diagram, and cloud done properly in GCC High and AWS GovCloud. It also
    has three subnets routing freely through one switch, an MSP holding standing domain admin under a month-to-month
    agreement, six VPN accounts belonging to people who left, and no asset inventory at all. Every session closes
    with a segment of its assessment, executed in a tool rather than on paper. By Friday afternoon you have run a
    complete Level 2 assessment on it.</p>
  <div class="tw"><table>
    <thead><tr><th style="width:70px">Session</th><th>What you do to Meridian</th><th style="width:34%">Where you do it</th></tr></thead>
    <tbody>{thread}</tbody></table></div>
  <div class="in-practice" style="margin-top:1.5rem"><div class="ip-label">And then the honest test</div>
    <p>Day 5 afternoon closes with <strong>Acuitas Machining</strong> &mdash; fourteen people, no server, no domain,
    a commercial cloud tenant that fails the FedRAMP question outright, and three CNC controllers that retain CUI
    for months. It is a sub-tier supplier inside Meridian's own supply chain, it is issued cold, and you get thirty
    minutes. Four days inside one company produces a real risk: learning Meridian rather than learning a method.
    This is the only instrument that tells the two apart.</p></div>
</section></div>
<section class="section" id="schedule">
  <div class="section-eyebrow">Workshop Schedule</div>
  <h2 class="section-title">Five Days, Morning and Afternoon</h2>
  <div class="rule"></div>
  <p class="section-desc">Two sessions per day, roughly three hours each, with built-in knowledge checks and a
    case-study segment in every one. Thirty contact hours in total.</p>
  <div class="schedule-grid">{sched}</div>
</section>
<div class="section-alt"><section class="section" id="cap">
  <div class="section-eyebrow">Assessment Process</div>
  <h2 class="section-title">The Week Follows the CAP</h2>
  <div class="rule"></div>
  <p class="section-desc">The workshop sequence and the assessment sequence are the same sequence. Bars show the
    approximate share of workshop time given to each stage of the CMMC Assessment Process v2.0 &mdash; Phase 2,
    where conformity is actually assessed, carries the most, which matches its weight on both exams.</p>
  {bars}
</section></div>
<section class="section" id="resources">
  <div class="section-eyebrow">Workshop Tools</div>
  <h2 class="section-title">Nine Tools, One Case, Every Deliverable</h2>
  <div class="rule"></div>
  <p class="section-desc">Each tool executes one segment of the Meridian assessment, checks your work against
    the governing authority with the reasoning exposed, saves in your browser, and prints to PDF. Facilitators
    teaching this material should start with the Faculty PD guide.</p>
  {res}
</section>
<div class="section-alt"><section class="section" id="about">
  <div class="section-eyebrow">About This Workshop</div>
  <h2 class="section-title">Built for the Work, Not Only the Exam</h2>
  <div class="rule"></div>
  <div class="about-grid">
    <div class="about-body">
      <h4>Who this is for</h4>
      <p>Compliance officers, IT and security leads at defense industrial base contractors, Registered
        Practitioners and RPO staff, and candidates for the ISACA <strong>CCP</strong> and <strong>CCA</strong>
        credentials. It assumes three or more years of IT or security experience and basic familiarity with the
        DFARS. It does not assume you have ever conducted an assessment.</p>
      <h4>How it differs from exam-only training</h4>
      <p>An exam-only course teaches you the model. This one teaches you to render a determination you can defend
        when the company that dislikes it pushes back. You will spend five days finding problems in a company and
        never once being permitted to fix one &mdash; that constraint is the subject, not an inconvenience.</p>
      <h4>How to use it</h4>
      <p>Work the sessions in order; each depends on the one before it, and the tools carry state forward. Complete
        the Meridian segment before moving on &mdash; the Day 5 mock assessment assumes you have. Do not read
        ahead to the Acuitas transfer test; a student who has seen it beforehand has taken a different test.</p>
      <h4>On sources</h4>
      <p>Requirements are stated from primary sources and cited to part, section, or clause: 32 CFR Part 170,
        32 CFR Part 2002, FAR 52.204-21, the DFARS 252.204 clause family, NIST SP 800-171 Rev 2 and SP 800-171A,
        the CMMC Assessment Process v2.0, the Code of Professional Conduct v2.0, and the NARA CUI Registry. Where a
        fact could not be verified &mdash; the CCP and CCA exam duration and passing scores &mdash; it is marked
        unverified rather than guessed.</p>
    </div>
    <div class="facts-box">
      <h4>At a glance</h4>
      <div class="facts-grid">
        <div class="fact"><div class="fv">30</div><div class="fl">Contact hours</div></div>
        <div class="fact"><div class="fv">110</div><div class="fl">Level 2 requirements</div></div>
        <div class="fact"><div class="fv">~320</div><div class="fl">Assessment objectives</div></div>
        <div class="fact"><div class="fv">88</div><div class="fl">POA&amp;M threshold</div></div>
        <div class="fact"><div class="fv">&minus;203</div><div class="fl">Score floor</div></div>
        <div class="fact"><div class="fv">72 hrs</div><div class="fl">Incident report clock</div></div>
        <div class="fact"><div class="fv">180</div><div class="fl">Days to closeout</div></div>
        <div class="fact"><div class="fv">6</div><div class="fl">Never POA&amp;M-able</div></div>
      </div>
      <p style="font-family:Arial,sans-serif;font-size:.78rem;color:var(--text-muted);line-height:1.65;margin-top:1.1rem;
        padding-top:.9rem;border-top:1px solid var(--border)">
        <strong style="color:var(--gold)">No lab, no licence, no clearance.</strong> Every artifact is fictional and
        unclassified, every primary source is free and publicly available, and every tool runs entirely in your
        browser with nothing sent anywhere.</p>
    </div>
  </div>
</section></div>
{FOOT}{THEME_JS}</body></html>"""
