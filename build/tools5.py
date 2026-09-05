# -*- coding: utf-8 -*-
"""Tool pages: POA&M Builder, Acuitas Transfer Test, Exam-Day One-Pager."""
from toolkit import tool_page, item
from theme import head, nav, FOOT, THEME_JS, CSS

NEVER = ["AC.L2-3.1.20","AC.L2-3.1.22","CA.L2-3.12.4","PE.L2-3.10.3","PE.L2-3.10.4","PE.L2-3.10.5"]

POAM_ROWS = [
 ("AC.L2-3.1.5","Employ the principle of least privilege",3,True,
  "Deferrable. Not on the enumerated list, and the score threshold is met."),
 ("AU.L2-3.3.2","Ensure actions can be traced to individual users",3,True,
  "Deferrable. Note the dependency: actions cannot be traced to individuals while a shared Global Admin service "
  "account and shared MSP credentials remain, so sequence it after 3.1.5."),
 ("CM.L2-3.4.1","Establish and maintain baseline configurations and inventories",5,True,
  "Deferrable, and the heaviest item at 5 points. It is also a dependency for several others &mdash; you cannot "
  "enforce a configuration you have not defined, and you cannot categorize assets you have not inventoried. "
  "Sequence it first."),
 ("MA.L2-3.7.5","MFA for nonlocal maintenance sessions; terminate them on completion",5,True,
  "Deferrable. Depends on a contractual change with ClearPath as well as a technical one, which is worth reflecting "
  "in the milestone and the owner &mdash; this is the one item where Contracts, not IT, holds the critical path."),
 ("CA.L2-3.12.4","Develop, document, and periodically update the System Security Plan",1,False,
  "<strong>May never be deferred.</strong> One of the six enumerated in &sect;170.21. Worth one point and an "
  "absolute barrier &mdash; it must be MET before any status can issue."),
 ("PE.L2-3.10.3","Escort visitors and monitor visitor activity",1,False,
  "<strong>May never be deferred.</strong> Also one of the six, also worth one point. The Dayton escort policy for "
  "MSP technicians is informal and undocumented, and Huntsville has no visitor control Meridian operates at all."),
]

def poam_builder():
    never = " &middot; ".join(f"<code>{x}</code>" for x in NEVER)
    intro = f"""<div class="panel">
<h2>The rules, before you build anything</h2><div class="rule"></div>
<div class="tw"><table><thead><tr><th>Rule</th><th>What it means</th></tr></thead><tbody>
<tr><td><strong>The score threshold</strong></td><td>A POA&amp;M may be used only where the assessment score divided
by the total number of Level 2 requirements is at least <strong>0.8</strong>. For 110 requirements that is
<strong>88</strong>. Below that there is no plan of action available at all &mdash; the answer is no issuance.</td></tr>
<tr><td><strong>The six that may never be deferred</strong></td><td>{never}. These must be MET.</td></tr>
<tr><td><strong>The encryption exception</strong></td><td>SC.L2-3.13.11 may be placed on a POA&amp;M only where
encryption is employed but is not FIPS validated. Where no encryption is employed, it may not.</td></tr>
<tr><td><strong>The window</strong></td><td>180 days from the Conditional CMMC Status Date, closed out by a closeout
assessment. Miss it and the conditional status expires.</td></tr>
<tr><td><strong>Who closes it out</strong></td><td>An authorized or accredited C3PAO &mdash; and it need not be the
firm that ran Phases 1 through 3. It assumes responsibility for the Final status determination after its own
conflict-of-interest review.</td></tr>
</tbody></table></div>
<div class="verdict show"><h4>Notice what the point values do not tell you</h4>
<p><strong>CA.L2-3.12.4</strong> &mdash; the System Security Plan &mdash; is worth one point.
<strong>PE.L2-3.10.3</strong> &mdash; escorting visitors &mdash; is worth one point. Both are on the never-defer
list.</p>
<p>A company can be one point from a perfect score and still be unable to obtain any status at all. Scoring weight
measures exploitability; POA&amp;M eligibility measures something else entirely, and conflating the two is the most
expensive mistake available in this area.</p></div>
<p style="font-size:.82rem;color:var(--text-muted)"><strong>Throughout:</strong> every deferral justified against
&sect;170.21 by requirement identifier. &ldquo;Low risk&rdquo; is not a basis for deferral; eligibility is. And no
remediation design &mdash; naming what must be remediated and by when is the plan; specifying how is consulting, and
it is still consulting on the last afternoon.</p></div>"""

    items = item("pa", 1, "Part A &mdash; Eligibility, for Meridian as you assessed it",
      '<p>Work from your own findings and your own score. You will reach the conclusion quickly.</p>',
      [dict(label="Your assessed score", type="text", name="sc", ph="From your D7 worksheet"),
       dict(label="Is Meridian eligible for a POA&M?", type="select", name="e",
            options=["Yes","No — score below threshold","No — score below threshold AND ineligible requirements failing",
                     "Yes, with the ineligible items excluded"],
            ok="No — score below threshold AND ineligible requirements failing"),
       dict(label="What CMMC status, if any, may issue — and under what provision?", type="area", name="st"),
       dict(label="What it means for the company, commercially", type="area", name="cons",
            ph="The AMCOM recompete, the clause it already holds, and the affirmation its CEO has already signed.")],
      """<p><strong>Not eligible, on two independent grounds.</strong></p>
<p><strong>The threshold.</strong> An assessed score around 44 gives 0.40 &mdash; half the 0.8 threshold. And 44 is
an optimistic ceiling, since it derives from a thirteen-item gap list rather than an assessment of all 110
requirements.</p>
<p><strong>The enumerated list.</strong> Even at a score above 88 it would fail, because two of the six requirements
that may never be deferred are NOT MET: <code>CA.L2-3.12.4</code> and <code>PE.L2-3.10.3</code>. These bind
<em>independently of the score</em>.</p>
<p><strong>Status:</strong> none. No Conditional and no Final CMMC Status may issue.</p>
<p><strong>Saying the consequence out loud.</strong> A determination of no issuance is not the end of the sentence.
Meridian must win a AMCOM recompete that requires a current assessment of record it does not have. It is in breach
today of the DFARS 252.204-7012 clause in the contracts it already holds &mdash; an obligation that exists
independently of CMMC entirely. And its chief executive has already affirmed a score of 88 in SPRS, in a federal system, under penalty,
on the basis that other people told her the number was right.</p>
<p><em>Assessors do not decide what happens to companies. They do have to be able to say plainly what their
determination means, without softening it and without enjoying it.</em></p>""")

    rows = ""
    for i, (rid, title, pts, ok, note) in enumerate(POAM_ROWS, 1):
        okv = "May be deferred" if ok else "May never be deferred"
        rows += item(f"pb{i}", i+1, f"{rid} &mdash; {title}",
          f'<p style="font-family:Arial,sans-serif;font-size:.86rem;color:var(--text-secondary)">'
          f'<strong>{pts} point{"s" if pts != 1 else ""}</strong> &middot; NOT MET in the revised assessment.</p>',
          [dict(label="Eligibility — work this column before anything else", type="select", name="el",
                options=["May be deferred","May never be deferred"], ok=okv),
           dict(label="Basis in §170.21", type="text", name="b",
                ph="Cite by requirement identifier, not by risk level."),
           dict(label="Milestone / target date / owner", type="area", name="m",
                ph="A milestone with no owner is a wish. Dates must fall inside the window.")],
          f"<p><strong>{okv}.</strong> {note}</p>")
    items += rows
    n = len(POAM_ROWS) + 1

    items += item("pconc", n+1, "The conclusion that follows",
      '<div class="in-practice"><div class="ip-label">The revised assessment</div>'
      '<p>Nine months later Meridian engages a closeout-capable C3PAO for a fresh Level 2 certification '
      'assessment. This time the company has <em>implemented</em> rather than documented. Every requirement is MET '
      'except the six above. Total deductions <strong>18</strong>. Assessment score <strong>92</strong>. '
      '92 &divide; 110 = <strong>0.836</strong>.</p></div>',
      [dict(label="Does the score alone permit a POA&M?", type="select", name="q1",
            options=["Yes","No"], ok="Yes"),
       dict(label="Can every NOT MET requirement go on it?", type="select", name="q2",
            options=["Yes","No"], ok="No"),
       dict(label="What status may the Lead CCA recommend, and when?", type="area", name="q3")],
      """<p><strong>The score alone: yes.</strong> 0.836 clears 0.8 comfortably, and a company reading only the
threshold rule would expect a Conditional status.</p>
<p><strong>Every requirement on the plan: no.</strong> <code>CA.L2-3.12.4</code> and <code>PE.L2-3.10.3</code> are on
the never-defer list &mdash; and they are the two cheapest items on the sheet, at one point each.</p>
<p><strong>What may issue:</strong> nothing yet. Both ineligible requirements must be brought to MET
<em>before</em> any status can issue. Once they are, the remaining four &mdash; AC.L2-3.1.5, AU.L2-3.3.2,
CM.L2-3.4.1, and MP.L2-3.8.7, totalling 16 points against a score that would then stand at 94 &mdash; may go on a
POA&amp;M supporting a <strong>Conditional Level 2 status</strong>, closed out within 180 days of the Conditional
CMMC Status Date.</p>
<p><strong>The lesson, stated plainly:</strong> the score alone never answers the question. Work the eligibility
column before anything else &mdash; it determines whether the rest of the row exists.</p>
<p><strong>Sequencing worth credit:</strong> CM.L2-3.4.1 first, because baseline configurations are a dependency for
enforcing least privilege; AU.L2-3.3.2 after AC.L2-3.1.5, because tracing actions to individuals is not achievable
while shared service accounts persist.</p>""")

    items += item("pc", n+2, "Part C &mdash; Closeout and sustainment",
      '<p>How the conditional status becomes final, and what carries afterward.</p>',
      [dict(label="Closeout: window, coverage, who may conduct it, and what happens on expiry", type="area", name="c"),
       dict(label="Sustainment: the certification period, the affirmation, and who carries the exposure", type="area", name="s"),
       dict(label="What would you say to Marcus Ellison about the affirmation she has already signed?",
            type="area", name="h", ph="Plainly, without softening it and without lecturing her.")],
      """<div class="tw"><table><tbody>
<tr><td style="width:210px"><strong>Window</strong></td><td>180 days from the Conditional CMMC Status Date.</td></tr>
<tr><td><strong>Coverage</strong></td><td>The requirements on the POA&amp;M, assessed to confirm they are now MET.</td></tr>
<tr><td><strong>Who may conduct it</strong></td><td>An authorized or accredited C3PAO &mdash; and it may be a
different firm from the one that ran Phases 1&ndash;3.</td></tr>
<tr><td><strong>What that firm must do first</strong></td><td>Its own conflict-of-interest review. It then assumes
responsibility for the Final status determination and issues the Final certificate.</td></tr>
<tr><td><strong>On expiry</strong></td><td>The Conditional status expires.</td></tr>
<tr><td><strong>Certification period</strong></td><td>Three years from the CMMC Status Date.</td></tr>
<tr><td><strong>Annual affirmation</strong></td><td>Submitted in SPRS by the Affirming Official &mdash; a senior
official of the OSC with authority to bind it. Not the IT manager, not the consultant, not the assessor.</td></tr>
<tr><td><strong>What it attests</strong></td><td>That the organization continues to meet the requirements. A
present-tense statement, not a memory of the assessment.</td></tr>
<tr><td><strong>The exposure</strong></td><td>An affirmation that is not true is a false statement in a federal
system, with False Claims Act consequences attaching <em>personally</em> to the official who signed.</td></tr>
</tbody></table></div>
<p style="margin-top:1rem"><strong>On Ellison.</strong> She affirmed 88 because Dennis and the consultant said that
was the number. She did not verify it and would not know how, and she does not know what an Affirming Official is
personally liable for. Nobody at Meridian behaved dishonestly. The number is still wrong, and she is still the
person who attested to it in a federal system.</p>
<p>What you say is what is true: what the affirmation is, what it attests, who carries it, and that a submitted
score which overstates the position is a false statement. What you do <em>not</em> say is what she should do about
it. That remains consulting, and it remains consulting on the last afternoon of the week.</p>
<p>The practical answer to sustainment &mdash; and the reason the question matters beyond this case &mdash; is
continuous monitoring, so that the affirmation reports something known rather than something assumed.</p>""")
    return tool_page("poam-builder","POA&amp;M Builder","Tool &middot; Deliverable D9 &middot; Lesson 9",
      "POA&amp;M Builder, Closeout, and Sustainment",
      "Eligibility first: the 0.8 threshold, then the six that may never be deferred. Then milestones, owners, and "
      "dates inside the window &mdash; and what the Affirming Official is carrying.",
      ["&sect;170.21","6 never-defer","180-day window","Prints as D9"], intro, items,
      back=("Lesson 9 &mdash; POA&amp;M, Closeout &amp; Roadmap","lesson09.html"))


# ---------------------------------------------------------------- TRANSFER TEST
PIED_ASSETS = [
 ("Commercial cloud tenant and shared drive",
  "A <strong>commercial</strong> Microsoft 365 Business Standard subscription &mdash; email and OneDrive. Not a "
  "government or high-assurance tenant. MFA is enabled on the owner&rsquo;s account only. One folder structure: "
  "Meridian drawings land in a folder named &ldquo;MPDS jobs,&rdquo; commercial customers&rsquo; work sits in "
  "sibling folders, and all fourteen staff accounts can read every folder.",
  "CUI Asset",
  "It stores and transmits CUI, so it is a CUI Asset. Then the separate obligation: because it is an external cloud "
  "service processing CUI, Acuitas must produce FedRAMP Moderate authorisation or documented equivalency under "
  "DFARS 252.204-7012(b)(2)(ii)(D) &mdash; and a commercial Business Standard tenant does not carry one.<br><br>"
  "<strong>Note the contrast with Meridian.</strong> Meridian&rsquo;s GCC High tenant <em>passes</em> the "
  "authorisation and fails on configuration. Acuitas fails at the authorisation itself. Same rule, two entirely "
  "different findings &mdash; and only the second one can be fixed by configuration. Credit students who separate "
  "the categorization from the authorisation question rather than collapsing them."),
 ("Office PCs (2)",
  "Owner and office manager. Used for email, quoting, scheduling, and opening drawings.",
  "CUI Asset","They open and store CUI drawings. Straightforward; nearly everyone gets this."),
 ("Shop floor PC",
  "Opens drawings and generates the tool paths sent to the machines. Shared login used by whoever is on shift; the "
  "password is taped inside the cabinet door.",
  "CUI Asset",
  "Processes CUI. The shared login is a <em>finding</em>, not a categorization question &mdash; watch for students "
  "who confuse a control failure with a scoping decision."),
 ("Three CNC machining centres",
  "Each has an embedded Windows-based controller. Tool-path and drawing-derived files are transferred by USB and "
  "<strong>retained on the controller&rsquo;s internal storage until an operator clears them</strong>. The shop lead "
  "clears them &ldquo;when they get full &mdash; maybe twice a year.&rdquo;",
  "Specialized Asset — but the treatment is unavailable",
  "<strong>The pivot of the whole test.</strong> These are Operational Technology, they process and retain CUI, and "
  "OT is a listed Specialized Asset type. But the Specialized treatment is <em>conditional</em>: the contractor must "
  "document the asset in the inventory, the SSP and the network diagram, and demonstrate that it is managed using "
  "risk-based security policies. Acuitas has none of those artifacts and no policy of any kind. The category is "
  "therefore unavailable in practice, and the asset cannot simply be set aside.<br><br>"
  "<strong>Three answers appear and they separate the cohort cleanly.</strong> <em>Weakest:</em> out of scope, "
  "&ldquo;they are machine tools&rdquo; &mdash; the asset has not been read as an information system and the "
  "months-long retention has been missed. <em>Middle:</em> full CUI Assets requiring all 110 requirements &mdash; "
  "thorough, but unaware the Specialized category exists. <em>Strongest:</em> Specialized by type, treatment "
  "unavailable by condition, so they stay in the assessment. That is the difference between having read the scoping "
  "guide and being able to use it."),
 ("CMM inspection station",
  "A coordinate measuring machine with an attached PC. Inspection programs are written from the Meridian drawings "
  "and stored on the PC; measurement reports go back to Meridian with the parts.",
  "CUI Asset",
  "It holds programs derived from CUI drawings and generates inspection data referencing them. Students who scope "
  "the machine tools carefully and then forget the metrology station have found the obvious OT and missed the "
  "quieter one."),
 ("Wireless network",
  "One WPA2 network, one passphrase, unchanged since installation. Shared by staff, the two part-time programmers, "
  "and visiting customers. No guest network, no segmentation.",
  "Security Protection Asset",
  "It provides the access control boundary such as it is, and it is the reason nothing at Acuitas can be scoped "
  "out. &ldquo;In-scope infrastructure&rdquo; with sound reasoning is acceptable."),
 ("Bookkeeper (external, own laptop)",
  "Part-time, works from home on her own equipment. Holds an account on the cloud tenant with access to the full "
  "shared drive, because restricting it was never set up.",
  "External Service Provider — in scope",
  "She holds an account with access to CUI and works from her own equipment. An ESP that handles CUI is assessed "
  "<em>within</em> the OSC assessment and requires a Customer Responsibility Matrix. None exists. Watch for students "
  "who dismiss her as &ldquo;just accounting.&rdquo;"),
 ("IT contractor (tenant administrator)",
  "A local one-person firm that set up the tenant and the wireless network. Holds administrator rights on the cloud "
  "tenant. Called when something breaks; no contract beyond an hourly rate sheet.",
  "External Service Provider — Security Protection",
  "Holds tenant administrator rights, so he handles Security Protection Data. Same treatment: assessed inside the "
  "assessment, CRM required &mdash; and there is no contract beyond a rate sheet. Note the structural echo: Meridian "
  "has exactly this problem with ClearPath, one tier up. The pattern repeats down the supply chain, and nobody at "
  "either company has looked."),
]

TIMER_JS = """<script>
var SECS=30*60,_t=null,_started=false;
function fmt(s){var m=Math.floor(s/60),x=s%60;return m+':'+(x<10?'0':'')+x;}
function startTimer(){if(_started)return;_started=true;
 document.getElementById('startbtn').disabled=true;
 document.getElementById('startbtn').textContent='Clock running';
 document.getElementById('paper').style.display='block';
 document.getElementById('preamble').style.display='none';
 _t=setInterval(function(){SECS--;
  var d=document.getElementById('clock');d.textContent=fmt(SECS);
  if(SECS<=300)d.style.color='var(--bad)';
  if(SECS<=0){clearInterval(_t);d.textContent="Time";unlockKey(true);}},1000);
 window.scrollTo({top:document.getElementById('paper').offsetTop-70,behavior:'smooth'});}
function unlockKey(auto){
 if(!auto && !confirm('Reveal the determination key? Do this only when you have finished or the clock has stopped.'))return;
 if(_t)clearInterval(_t);
 document.getElementById('keywrap').style.display='block';
 document.getElementById('lockmsg').style.display='none';
 var b=document.getElementById('unlockbtn');if(b)b.disabled=true;
 document.querySelectorAll('.rvbtn').forEach(function(x){x.disabled=false;});
 if(auto){document.getElementById('clock').style.color='var(--bad)';}
 window.scrollTo({top:document.getElementById('keywrap').offsetTop-70,behavior:'smooth'});}
window.addEventListener('DOMContentLoaded',function(){
 document.querySelectorAll('.rvbtn').forEach(function(x){x.disabled=true;});});
</script>"""

def transfer_test():
    profile = """<div class="panel" id="preamble">
<h2>Before you start</h2><div class="rule"></div>
<p><strong>Thirty minutes. Individually. No notes, no Meridian material, no internet.</strong> You may use the
CMMC Assessment Scope guidance for Level 2 and 32 CFR &sect;170.19 if you have them in hard copy.</p>
<p>You will receive a profile of a company in Meridian&rsquo;s supply chain and produce a scope determination.
Budget roughly eight minutes to read and twenty to write.</p>
<div class="verdict show"><h4>What is being measured</h4>
<p>Not recall. Whether the method you have used on one company for four days works on a company you have never
seen &mdash; which is the only thing that would make you useful to the next OSC that hires you.</p>
<p><strong>A confident wrong categorization scores worse than a correctly hedged one.</strong> If a category is
genuinely arguable, say what makes it arguable and what would settle it. That is the assessor&rsquo;s answer, and it
is the answer this test is looking for.</p></div>
<p>This is not a trick. Everything you need is in the profile, and the reasoning is the reasoning you have used
since Lesson 4. The only new thing is the company.</p>
<div class="btnrow" style="justify-content:center;margin-top:1.5rem">
  <button class="btn" id="startbtn" onclick="startTimer()" style="font-size:.9rem;padding:.85rem 2rem">
    Start the 30-minute clock &rarr;</button></div>
</div>
<div id="paper" style="display:none">
<div class="panel">
<h2>Acuitas Machining Inc.</h2><div class="rule"></div>
<div class="tw"><table><tbody>
<tr><td style="width:190px"><strong>Location</strong></td><td>Springfield, Ohio &mdash; about 25 miles from Meridian&rsquo;s Dayton plant</td></tr>
<tr><td><strong>Business</strong></td><td>Precision CNC machining and inspection &mdash; a job shop taking overflow and short-run work</td></tr>
<tr><td><strong>Employees</strong></td><td>14 &mdash; the owner, an office manager, a shop lead, eight machinists, two part-time CNC programmers, plus an external bookkeeper</td></tr>
<tr><td><strong>Revenue</strong></td><td>~$3.4M annually</td></tr>
<tr><td><strong>DoD-related work</strong></td><td>~$800K, all of it as a sub-tier supplier to Meridian Precision Defense Systems</td></tr>
<tr><td><strong>Other work</strong></td><td>Automotive tooling, agricultural equipment parts, and two local fabricators. No government relationship.</td></tr>
<tr><td><strong>Facility</strong></td><td>One leased building: a shop floor, a small office, and an inspection room.</td></tr>
</tbody></table></div>
<h3>What Acuitas receives from Meridian</h3>
<p>Meridian subcontracts machining overflow on the actuator housing line. To do that work, Acuitas receives:</p>
<ul>
<li>Machining drawings for the actuator housing assemblies, extracted from the technical data package AMCOM
furnished to Meridian.</li>
<li>Geometric dimensioning and tolerancing data, material specifications, and inspection criteria.</li>
<li>Lot quantities and delivery dates for each release.</li>
</ul>
<p>Files arrive by a <strong>shared SharePoint link</strong> from Meridian&rsquo;s GCC High tenant; Acuitas saves
them down to its own commercial cloud drive. There is <strong>no formal agreement</strong> between the two companies
beyond purchase orders, and the purchase orders reference &ldquo;MPDS standard terms&rdquo; which incorporate DFARS
252.204-7012 by reference. Nobody at Acuitas has read them. The owner&rsquo;s position, stated plainly during the
walkthrough, is that <em>&ldquo;we are a job shop. We machine to a print. CMMC is Meridian&rsquo;s problem.&rdquo;</em></p>
<h3>The environment</h3>
<p>There is no server, no domain, and no IT staff. There is no system security plan, no asset inventory, no network
diagram, no written security policy of any kind, and <strong>no record of any security decision ever having been
made</strong>. What exists:</p>
<div class="tw"><table><thead><tr><th style="width:210px">Asset</th><th>Description</th></tr></thead><tbody>
<tr><td><strong>Cloud tenant</strong></td><td>A <em>commercial</em> Microsoft 365 Business Standard subscription &mdash; email and OneDrive. Not a government or high-assurance tenant. MFA enabled on the owner&rsquo;s account only.</td></tr>
<tr><td><strong>Shared drive</strong></td><td>One folder structure. Meridian drawings are saved to a folder named &ldquo;MPDS jobs.&rdquo; Commercial customers&rsquo; work sits in sibling folders. All fourteen staff accounts can read every folder.</td></tr>
<tr><td><strong>Office PCs (2)</strong></td><td>Owner and office manager. Email, quoting, scheduling, and opening drawings.</td></tr>
<tr><td><strong>Shop floor PC (1)</strong></td><td>Opens drawings and generates the tool paths sent to the machines. Shared login used by whoever is on shift; the password is taped inside the cabinet door.</td></tr>
<tr><td><strong>CNC machining centres (3)</strong></td><td>Each has an embedded Windows-based controller. Tool-path and drawing-derived files are transferred by USB and retained on the controller&rsquo;s internal storage until an operator clears them. The shop lead clears them &ldquo;when they get full &mdash; maybe twice a year.&rdquo;</td></tr>
<tr><td><strong>CMM inspection station</strong></td><td>A coordinate measuring machine with an attached PC. Inspection programs are written from the Meridian drawings and stored on the PC; measurement reports go back to Meridian with the parts.</td></tr>
<tr><td><strong>Wireless network</strong></td><td>One WPA2 network, one passphrase, unchanged since installation. Shared by staff, the two part-time programmers, and visiting customers. No guest network, no segmentation.</td></tr>
<tr><td><strong>Bookkeeper</strong></td><td>External, part-time, works from home on her own laptop. Holds an account on the cloud tenant with access to the full shared drive, because restricting it was never set up.</td></tr>
<tr><td><strong>IT contractor</strong></td><td>A local one-person firm that set up the tenant and the wireless network. Holds administrator rights on the cloud tenant. Called when something breaks; no contract beyond an hourly rate sheet.</td></tr>
</tbody></table></div>
</div>
<div class="panel">
<h2>Answer sheet</h2><div class="rule"></div>
<h3>Question 1 &mdash; Level and authority <span style="font-weight:400;color:var(--text-muted)">(about 4 minutes)</span></h3>
<p>What CMMC level applies to Acuitas, and what makes it apply? Answer the owner&rsquo;s objection directly, in no
more than four sentences, and name the instrument you are relying on.</p>
<label for="q1">Your answer</label><textarea id="q1" data-f="q1" style="min-height:120px"></textarea>
<h3 style="margin-top:1.6rem">Question 3 &mdash; The consequential unknown <span style="font-weight:400;color:var(--text-muted)">(about 4 minutes)</span></h3>
<p>Name the single fact you would most want resolved before finalizing this scope, say why it matters, and say what
evidence would settle it.</p>
<label for="q3">Your answer</label><textarea id="q3" data-f="q3" style="min-height:110px"></textarea>
<p style="font-size:.8rem;color:var(--text-muted);margin-top:1rem">Question 2 &mdash; asset categorization, about
14 minutes &mdash; is below, one asset at a time.</p>
</div>
</div>"""
    items = ""
    for i, (name, desc, ok, model) in enumerate(PIED_ASSETS, 1):
        items += item(f"pt{i}", i, name, f'<p>{desc}</p>', [
            dict(label="Category", type="select", name="c",
                 options=["CUI Asset","Security Protection Asset","Contractor Risk Managed Asset",
                          "Specialized Asset — but the treatment is unavailable","Specialized Asset",
                          "Out-of-Scope Asset","External Service Provider — in scope",
                          "External Service Provider — Security Protection"], ok=ok),
            dict(label="Basis — one line", type="text", name="b"),
        ], f"<p><strong>{ok}.</strong> {model}</p>", ok_label="Show the key for this asset")
    items = f"""<div class="panel" id="lockmsg" style="text-align:center;background:var(--gold-pale);border-color:var(--gold)">
  <p style="margin:0"><strong>The determination key is locked</strong> until the clock stops or you unlock it
  deliberately. Answer first.</p>
  <div class="btnrow" style="justify-content:center"><button class="btn ghost" id="unlockbtn"
    onclick="unlockKey(false)">I have finished &mdash; unlock the key</button></div>
</div>
<div id="keywrap" style="display:none">
<div class="panel"><h2>Question 1 &mdash; the key</h2><div class="rule"></div>
<div class="verdict show"><h4>Expected answer: CMMC Level 2</h4>
<p>Acuitas receives machining drawings and tolerancing data <em>extracted from the technical data package AMCOM
furnished to Meridian</em>. That is Controlled Technical Information &mdash; CUI &mdash; and it
reaches Acuitas through a subcontract that incorporates DFARS 252.204-7012, which flows down under paragraph (m) to
subcontractors whose performance will involve covered defense information. <strong>The obligation follows the
information, not the tier.</strong></p>
<p>The owner&rsquo;s objection is answered directly: the clause is in his subcontract, flowdown is the mechanism by
which it got there, Meridian was required to put it there, and whether he has read it is not relevant to whether
it binds him.</p>
<p><strong>Marking notes.</strong> Full credit requires naming the flowdown mechanism, not merely asserting Level 2
&mdash; &ldquo;they handle CUI so it is Level 2&rdquo; is the conclusion without the authority. Either 252.204-7012(m)
or DFARS 252.204-7021 flowdown is acceptable as the cited instrument provided the reasoning is sound; naming both
and distinguishing them earns more. <strong>Do not accept &ldquo;Level 1, because they are a subcontractor&rdquo;</strong>
&mdash; the single most serious error available on this test, and the owner&rsquo;s own error. Noting that
Acuitas&rsquo;s commercial work carries no federal obligation at all, and that only the Meridian work triggers
this, is worth extra credit.</p></div></div>
""" + items + """
<div class="panel"><h2>Question 3 &mdash; the key</h2><div class="rule"></div>
<div class="verdict show"><h4>No single required answer &mdash; three are strong</h4>
<ul>
<li><strong>What the CNC controllers retain, and for how long.</strong> The best answer. It decides whether the
controllers are information systems holding CUI or transient devices, and it is the difference between the hardest
categorization on the sheet and an easy one. Settled by examining the controller storage directly &mdash; an
inspection, not an interview.</li>
<li><strong>Whether the cloud tenant can meet FedRAMP Moderate or documented equivalency.</strong> It determines
whether the environment can be brought into conformity at all, or whether Acuitas must move tenants before an
assessment is meaningful. Settled by the provider&rsquo;s authorization record and the subscription terms.</li>
<li><strong>Whether any risk-based security policy exists in any form.</strong> The most consequential in breadth: it
is the condition on both the Specialized Asset and Contractor Risk Managed treatments. If nothing exists, two
categories collapse into CUI Assets at once. Settled by asking for the document and accepting only a document.</li>
</ul>
<p><strong>Weak answers.</strong> &ldquo;Whether they will fix the wifi&rdquo; &mdash; a remediation question, not an
assessment one, and the consulting reflex arriving under time pressure. &ldquo;How much CUI there is&rdquo; &mdash;
volume does not change categorization. Anything the profile already answers &mdash; re-reading is part of the thirty
minutes.</p></div></div>
<div class="panel"><h2>What should be scoped out</h2><div class="rule"></div>
<div class="verdict show good"><h4>Nothing &mdash; and saying so explicitly is the correct answer</h4>
<p>Out-of-Scope Assets require the contractor to be prepared to justify the asset&rsquo;s <em>inability</em> to
process, store, or transmit CUI. On a single flat wireless network with a shared drive every account can read, no
such justification exists.</p>
<p>A student who scopes nothing out, <strong>and says explicitly that the absence of segmentation is what makes that
true</strong>, has produced the correct answer and should be told so.</p></div></div>
<div class="panel"><h2>Where you stand</h2><div class="rule"></div>
<div class="tw"><table><thead><tr><th style="width:150px">Level</th><th>What it looks like</th></tr></thead><tbody>
<tr><td><strong>Not Yet</strong></td><td>Level 1, or Level 2 with no authority named. Assets categorized by intuition. Printer treated as out of scope.</td></tr>
<tr><td><strong>Developing</strong></td><td>Level 2 correctly identified with the flowdown named. Most assets categorized plausibly. Printer treated as a full CUI Asset, or as Specialized without noticing the condition. ESPs missed or dismissed.</td></tr>
<tr><td><strong>Competent</strong></td><td>Level 2 with the flowdown mechanism cited and the owner&rsquo;s objection answered. All eight assets categorized with sound one-line bases. Both ESPs identified. Printer identified as a Specialized Asset. A defensible consequential unknown.</td></tr>
<tr><td><strong>Assessor-Ready</strong></td><td>All of the above, plus the conditional nature of the Specialized and Contractor Risk Managed treatments recognised explicitly &mdash; the categories exist, and Acuitas cannot claim them. States what would have to be true for the answer to change.</td></tr>
</tbody></table></div>
<p style="margin-top:1rem;font-size:.84rem;color:var(--text-muted)">This is diagnostic, not graded, and it does not
affect completion. It exists to tell you something you cannot find out any other way: whether the week gave you a
method or a familiarity. Both feel identical from the inside.</p></div>
</div>"""
    clock = """<div style="position:sticky;top:60px;z-index:70;background:var(--navy);color:#fff;
      padding:.55rem 2rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap">
      <span style="font-family:Arial,sans-serif;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;
        color:var(--gold)">Timed &middot; individual &middot; cold</span>
      <span style="font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:1.6rem"
        id="clock">30:00</span></div>"""
    return tool_page("transfer-test","Acuitas Transfer Test","Transfer Test &middot; Lesson 9 &middot; Cold",
      "Transfer Test &mdash; Acuitas Machining",
      "Thirty minutes on a company you have never seen: a supplier inside Meridian&rsquo;s own supply chain. "
      "Fourteen people, no server, no domain, and three CNC controllers that retain CUI for months.",
      ["30 minutes","Individual","No notes","Key locked until the clock stops"],
      clock + profile, items,
      back=("Lesson 9 &mdash; POA&amp;M, Closeout &amp; Roadmap","lesson09.html"),
      extra_js=TIMER_JS)


# ---------------------------------------------------------------- ONE-PAGER
def onepager():
    body = """<main class="tool-main">
<div class="panel">
<h2>The three-part standard</h2><div class="rule"></div>
<p>Every claim, every time: <strong>Requirement</strong> &mdash; what specifically is required?
<strong>Authority</strong> &mdash; what regulation, clause, or official document imposes it?
<strong>Evidence</strong> &mdash; what would demonstrate it, and would that be enough?</p>

<h3>Adequacy vs sufficiency</h3>
<p><strong>Adequate:</strong> the evidence exists and matches what the requirement intends. A property of the
artifact, not the organization. <strong>Sufficient:</strong> it shows the control is implemented, consistently
followed, and operating &mdash; across the scope, and currently. <strong>A verbal assurance is neither.</strong>
Every verdict must say <em>what would change it</em>.</p>

<h3>The three methods</h3>
<p><strong>Examine</strong> &mdash; that something exists and what it says. Cannot show anyone follows it.
<strong>Interview</strong> &mdash; leads, never conclusions. <strong>Test</strong> &mdash; that it operates now.
Cannot show it operated last quarter. Sampling: nonstatistical, <strong>FOCUSED</strong> depth and coverage,
increased on questionable evidence.</p>

<h3>The five asset categories</h3>
<div class="tw"><table><thead><tr><th>Category</th><th>Test</th><th>Assessed</th></tr></thead><tbody>
<tr><td>CUI Asset</td><td>Processes, stores, or transmits CUI</td><td>All Level 2 requirements</td></tr>
<tr><td>Security Protection Asset</td><td>Provides security functions to the scope</td><td>Relevant requirements</td></tr>
<tr><td>Contractor Risk Managed</td><td>Can but is not intended to &mdash; <strong>because policy and practices are in place</strong></td><td>SSP review</td></tr>
<tr><td>Specialized</td><td>Can, but unable to be fully secured. <strong>Closed list:</strong> IoT, IIoT, OT, GFE, Restricted IS, Test Equipment</td><td>SSP review only</td></tr>
<tr><td>Out-of-Scope</td><td>Cannot, and provides no protection. Contractor must justify the inability</td><td>Not assessed</td></tr>
</tbody></table></div>
<p><strong>Both conditional categories are earned, not claimed.</strong> No policy, no SSP, no network diagram
&rarr; neither category is available, and assets fall back to what they can do.</p>

<h3>ESP vs CSP</h3>
<p><strong>ESP</strong> (non-cloud, handles CUI or Security Protection Data): documented in the SSP,
<strong>Customer Responsibility Matrix required</strong>, evaluated inside the OSC assessment.
<strong>CSP</strong> (handles CUI): <strong>FedRAMP Moderate or documented equivalency</strong> &mdash; plus the
reporting, preservation, and access obligations. The authorization alone is not sufficient, and the clause never
names GCC High.</p>

<h3>Determinations</h3>
<p><strong>MET / NOT MET / NOT APPLICABLE</strong>, at the <strong>assessment-objective</strong> level. 110
requirements, ~320 objectives. <strong>No partial credit</strong> &mdash; one objective unmet makes the requirement
NOT MET. N/A scores as MET, so it will be challenged. A NOT MET names the objective and what is missing.</p>

<h3>Scoring &mdash; DoD Assessment Methodology</h3>
<p>Start <strong>110</strong>, deduct <strong>5 / 3 / 1</strong>. Floor <strong>&minus;203</strong>.
<strong>Partial credit exists for exactly two requirements:</strong></p>
<div class="tw"><table><thead><tr><th>Requirement</th><th>Deduct 3</th><th>Deduct 5</th></tr></thead><tbody>
<tr><td>3.5.3 &mdash; MFA</td><td>Remote <strong>and</strong> privileged users covered, general user not</td><td>No MFA for any users</td></tr>
<tr><td>3.13.11 &mdash; FIPS encryption</td><td>Encryption employed, not FIPS validated</td><td>No encryption employed</td></tr>
</tbody></table></div>

<h3>POA&amp;M &mdash; 32 CFR &sect;170.21</h3>
<p>Threshold: score &divide; total <strong>&ge; 0.8</strong> (88 of 110). <strong>Six may never be deferred:</strong>
<code>AC.L2-3.1.20</code> &middot; <code>AC.L2-3.1.22</code> &middot; <code>CA.L2-3.12.4</code> &middot;
<code>PE.L2-3.10.3</code> &middot; <code>PE.L2-3.10.4</code> &middot; <code>PE.L2-3.10.5</code>.
Two of them are worth <strong>one point each</strong>. <strong>The score alone never answers the question.</strong>
SC.L2-3.13.11 is deferrable only where encryption is employed but not FIPS validated.
Window: <strong>180 days</strong> from the Conditional CMMC Status Date. Any accredited C3PAO may close out, after
its own conflict review.</p>

<h3>Incident reporting &mdash; DFARS 252.204-7012</h3>
<p><strong>72 hours from discovery</strong>, via DIBNet, requiring a <strong>DoD-approved medium assurance
certificate</strong>. Threshold is <em>potentially</em> adverse, not confirmed. <strong>90 days</strong> media and
monitoring-data preservation from report submission. Malicious software to DC3, <em>not</em> with the report.</p>

<h3>Independence</h3>
<p>Three-year bar: no participation where you consulted to prepare the organization for <strong>any type</strong> of
CMMC assessment within three years. <strong>Binds the C3PAO as an organization</strong>, not only individuals.
Disclose in writing; <strong>the C3PAO decides</strong> whether it can be mitigated, and cannot delegate that. No
outcome-contingent fees. Never advise, never speculate about the outcome.</p>

<h3>Trap patterns</h3>
<ul>
<li>Level 1 is <strong>15</strong> requirements, not 17.</li>
<li><strong>ISACA</strong> certifies individuals; the <strong>Cyber AB</strong> accredits organizations.</li>
<li>MFA partial credit is a <strong>conjunction</strong> &mdash; remote <em>and</em> privileged &mdash; not a spectrum.</li>
<li>Not all AU requirements are 5 points. 3.3.2 is 3. 3.4.3 is 1.</li>
<li>DFARS 252.204-7019 is not a NIST requirement &mdash; <strong>no deduction</strong>.</li>
<li>The SSP requirement is <strong>3.12.4</strong> (1 point), not 3.12.1 (5 points).</li>
<li>Phase 1 concludes on <strong>upload of the Pre-Assessment Form to eMASS</strong>, not on a meeting.</li>
<li>The out-brief QA reviewer must be a CCA <strong>not on the team, with no contact during the assessment</strong>.</li>
<li>A contractor <strong>identifies and protects</strong> CUI; only the Government <strong>designates</strong> it.</li>
<li>Unmarked is not unprotected. The obligation attaches to the information, not the sticker.</li>
</ul>
<p style="margin-top:1.4rem;padding-top:1rem;border-top:2px solid var(--gold);font-size:.8rem;color:var(--text-muted)">
<strong>Unverified:</strong> CCP and CCA exam duration and passing scores. Confirm directly with ISACA.
&mdash; <strong>Currency:</strong> this sheet states the rule as published in 32 CFR Part 170, the DFARS clause
family, and NIST SP 800-171 Rev 2. Only three instruments change what a contractor owes &mdash; a class deviation, a
FAR/DFARS rule change, or an amendment to Part 170. Check whether any has issued before you sit the exam.</p>
<div class="btnrow" style="justify-content:center;margin-top:1.5rem">
  <button class="btn" onclick="window.print()">&#128424; Print / Save PDF</button>
  <a class="btn ghost" href="index.html">Back to the workshop</a></div>
</div></main>"""
    return (head("Exam-Day One-Pager | CMMC 5-Day Workshop",
                 "A one-page printable cram sheet of the highest-yield CMMC Level 2 material.") + nav() +
            """<header class="lhero"><div class="lhero-in">
  <div class="eyebrow">Reference &middot; Printable</div>
  <h1>Exam-Day One-Pager</h1>
  <p class="lead">The highest-yield material on one printable page: the three-part standard, adequacy versus
  sufficiency, the five categories with their conditions, the scoring weights and both exceptions, the six that may
  never be deferred, and the trap patterns.</p></div></header>""" +
            body + FOOT + THEME_JS + "</body></html>")

def build_all():
    return [("poam-builder.html", poam_builder()),
            ("transfer-test.html", transfer_test()),
            ("onepager.html", onepager())]
