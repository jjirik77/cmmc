# -*- coding: utf-8 -*-
"""Manuscript source — Lessons 0, 1, 2."""

L0 = dict(
 file="lesson00.html", short="L0 — Orientation & the Assessor Mindset", num_label="Lesson 0",
 eyebrow="Day 1 &middot; Morning &middot; Orientation",
 title="CMMC Orientation and the Assessor Mindset",
 lead=("CMMC is not a cybersecurity test. It is a conformity regime, and you are training to be the person "
       "whose determination other people rely on without knowing you. Before the first requirement, understand "
       "what the program is, who governs which part of it, what the credential pathway actually requires, and "
       "the change of role that everything else in this week depends on."),
 chips=["Day 1 &mdash; AM","~3 hours","<strong>No prerequisites</strong>","Sets up all 5 days"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Explain","State what CMMC is, what it governs, and what makes it different in kind from the frameworks you already know."),
  ("Identify","Name every body in the CMMC ecosystem and say which one governs organizations and which governs individuals."),
  ("Distinguish","Separate the assessor role from the consultant role, and name the moments where the line is easiest to cross."),
  ("Apply","Apply the three-part standard &mdash; requirement, authority, evidence &mdash; to a claim about a contractor."),
  ("Plan","Map the CCP and CCA prerequisite chains against your own position today."),
 ],
 vocab=[
  ("CMMC","Cybersecurity Maturity Model Certification. The DoD program, established by 32 CFR Part 170, that makes a stated level of cybersecurity a condition of contract award."),
  ("OSC","Organization Seeking Certification &mdash; the contractor being assessed. The term of art in 32 CFR Part 170; use it rather than &ldquo;the client.&rdquo;"),
  ("C3PAO","CMMC Third-Party Assessment Organization. An accredited firm authorized to conduct Level 2 certification assessments."),
  ("CAICO","CMMC Assessor and Instructor Certification Organization. ISACA holds this role since December 2025; the transition completed April 2026."),
  ("CCP / CCA","Certified CMMC Professional and Certified CMMC Assessor. Individual credentials issued by ISACA, not by the Cyber AB."),
  ("Affirming Official","The senior official of the OSC with authority to bind it, who submits the annual affirmation in SPRS. Personally exposed under the False Claims Act."),
  ("SPRS","Supplier Performance Risk System. Where a DoD Assessment score is posted and where the annual affirmation is filed."),
  ("CUI","Controlled Unclassified Information. Information a law, regulation, or government-wide policy requires an agency to safeguard. Level 2 exists to protect it."),
  ("FCI","Federal Contract Information. Non-public information provided by or generated for the Government under a contract. Triggers Level 1 and the 15 FAR requirements."),
  ("CAP","CMMC Assessment Process v2.0. The Cyber AB document that governs how an assessment is run: preliminary proceedings plus four numbered phases."),
  ("CoPC","CMMC Code of Professional Conduct v2.0. Eight guiding principles that govern assessor behaviour, including impartiality and the three-year consulting bar."),
  ("Assessment objective","The unit of determination. The 110 Level 2 requirements decompose into roughly 320 objectives, each of which must be MET or NOT APPLICABLE."),
 ],
 sections=[
  dict(title="What this workshop is, and what it is not", html="""
<p>Five days, ten sessions, one company. You will scope it, plan the engagement, request and triage its evidence,
render determinations against the fourteen NIST SP 800-171 Rev 2 families, compute and defend its DoD Assessment
score, run a two-day mock assessment against it, write the findings, and close it out with a plan of action.
On the final afternoon you will be handed a company you have never seen and given thirty minutes.</p>
<p>This is preparation for the ISACA <strong>CCP</strong> and <strong>CCA</strong> credentials, and it is
preparation for the work those credentials describe. Those are not the same thing, and where they diverge this
workshop follows the work. An exam-only course teaches you the model. This one teaches you to render a
determination you can defend when the company that dislikes it pushes back.</p>
<h3>What it is not</h3>
<ul>
<li><strong>Not a course in how to become compliant.</strong> You will spend five days finding problems in a
company and never once being permitted to fix one. That constraint is the subject, not an inconvenience.</li>
<li><strong>Not a technical security course.</strong> You are expected to know what a domain controller and a
Conditional Access policy are. You are not expected to configure either.</li>
<li><strong>Not a substitute for the primary sources.</strong> Everything here is traced to 32 CFR Part 170, the
FAR, the DFARS, the NIST publications, the CAP, and the NARA CUI Registry. When this material and a governing
document disagree, the governing document wins and this material is wrong.</li>
</ul>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>The single most common source of wrong answers in CMMC study is confidently remembered material that was true
two years ago. Two examples arrive in this workshop within the first day: who issues the CCP and CCA, and how many
requirements CMMC Level 1 comprises. Both are widely mis-stated in circulating training decks. Cite the rule, not
the deck.</p></div>"""),
  dict(title="Where CMMC sits among the frameworks you know", html="""
<p>Most people arriving at CMMC already know a security framework, and the instinct is to file CMMC alongside it.
That instinct produces one specific, predictable error later: the assumption that partial implementation earns
partial credit. True in a maturity model. False in CMMC.</p>
<p>The differences that matter are not about content. CMMC Level 2 <em>is</em> NIST SP 800-171 Rev 2 &mdash; the
requirements are borrowed wholesale. What differs is status, enforcement, and how conformity is demonstrated.</p>
<div class="tw"><table>
<thead><tr><th>Framework</th><th>Mandatory?</th><th>Applies to</th><th>How conformity is shown</th></tr></thead>
<tbody>
<tr><td><strong>NIST CSF 2.0</strong></td><td>No &mdash; voluntary</td><td>Any organization</td>
<td>Self-declared. No external verification exists or is expected.</td></tr>
<tr><td><strong>NIST RMF (SP 800-37)</strong></td><td>Yes, for federal systems</td><td>Federal information systems under FISMA</td>
<td>Authorization to Operate granted by a government Authorizing Official.</td></tr>
<tr><td><strong>NIST SP 800-53 Rev 5</strong></td><td>Yes, for federal systems</td><td>Federal systems; underpins FedRAMP</td>
<td>Security Assessment Report feeding an authorization decision.</td></tr>
<tr><td><strong>ISO/IEC 27001</strong></td><td>No &mdash; but certifiable</td><td>Any organization, by choice</td>
<td>Certification by an accredited certification body.</td></tr>
<tr><td><strong>CMMC Level 2</strong></td><td>Yes, when it is in the contract</td><td>DIB contractors handling CUI</td>
<td>Self-assessment or C3PAO certification, posted to SPRS, affirmed annually by a named official.</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">The distinction to carry forward</div>
<p>RMF and SP 800-53 are mandatory &mdash; but for federal agency systems, not for you as a contractor. CSF 2.0 and
ISO 27001 are voluntary. CMMC is the only one of these that a contracting officer can make a condition of your
company winning work. That is why it is assessed the way it is, and why an assessor here carries obligations an
auditor of a voluntary framework does not.</p></div>"""),
  dict(title="Three levels, and what triggers each", html="""
<p>The level is not chosen. It follows from the information the contractor will handle, and the contracting officer
inserts the clause accordingly under 32 CFR Part 170.</p>
<div class="tw"><table>
<thead><tr><th>Level</th><th>Triggered by</th><th>Requirements</th><th>Source</th><th>How assessed</th></tr></thead>
<tbody>
<tr><td><strong>Level 1</strong></td><td>Federal Contract Information</td><td>15</td>
<td>FAR 52.204-21(b)(1)(i)&ndash;(xv), incorporated by 32 CFR 170.14(c)(2)</td>
<td>Annual self-assessment and affirmation</td></tr>
<tr><td><strong>Level 2</strong></td><td>Controlled Unclassified Information</td><td>110</td>
<td>NIST SP 800-171 Rev 2</td><td>Self-assessment or C3PAO certification, per the contract</td></tr>
<tr><td><strong>Level 3</strong></td><td>CUI on the highest-priority programs</td><td>110 plus a selected subset of NIST SP 800-172</td>
<td>32 CFR 170.14(c)(4)</td><td>Government-led, by DIBCAC</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Exam tip &mdash; the counting trap</div>
<p>Level 1 is <strong>15</strong> requirements. A great deal of circulating CMMC 2.0 material says 17, because
earlier model documentation split FAR 52.204-21(b)(1)(ix) into three separate practices. That split has no basis in
the rule. 32 CFR 170.14(c)(2) incorporates fifteen paragraphs, and there are fifteen of them. Count them yourself.</p></div>
<p>Level 2 decomposes further, and this is the mechanic that decides most of your week. The 110 requirements break
into roughly <strong>320 assessment objectives</strong> in NIST SP 800-171A. Every objective under a requirement
must be MET or NOT APPLICABLE for the parent requirement to be MET. There is no partial credit at the objective
level, and an assessor who determines at the requirement level has not done the work.</p>"""),
  dict(title="The ecosystem &mdash; who governs what", html="""
<p>The ecosystem has more bodies than the names suggest, and their responsibilities do not overlap the way people
assume. Roughly one in twenty CCP questions is drawn from this table, and it is the most commonly mis-stated topic
in published CMMC material.</p>
<div class="tw"><table>
<thead><tr><th>Body or role</th><th>What it does</th></tr></thead>
<tbody>
<tr><td><strong>DoW CIO / CMMC PMO</strong></td><td>Owns the program. Issues the model, the assessment guides, and the scoping guides.</td></tr>
<tr><td><strong>DIBCAC</strong></td><td>The government assessment arm. Conducts government-led assessments, including Level 3.</td></tr>
<tr><td><strong>The Cyber AB</strong></td><td>The accreditation body. Accredits C3PAOs under ISO/IEC 17020 and operates the CMMC Marketplace. <strong>Accredits organizations &mdash; not people.</strong></td></tr>
<tr><td><strong>ISACA, as CAICO</strong></td><td>The certification body for individuals. Administers CCP, CCA, Lead CCA, and CCI. Took the role in December 2025; transition completed April 2026.</td></tr>
<tr><td><strong>C3PAO</strong></td><td>An accredited firm that conducts Level 2 certification assessments.</td></tr>
<tr><td><strong>RPO / RP</strong></td><td>Registered Provider Organizations and Registered Practitioners. Readiness consulting. They help you prepare; they may not assess you.</td></tr>
<tr><td><strong>OSC</strong></td><td>Organization Seeking Certification &mdash; the contractor being assessed.</td></tr>
<tr><td><strong>CCP / CCA</strong></td><td>Individually credentialed professionals. A CCA may serve on a certification assessment team; a CCP supports one.</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">The correction &mdash; expect this on the exam</div>
<p>The Cyber AB accredits <strong>organizations</strong>. ISACA, as CAICO, certifies <strong>individuals</strong>.</p>
<p>For years the Cyber AB did both, and an enormous amount of still-circulating material &mdash; training decks,
blog posts, vendor guides, and some published course modules &mdash; says the Cyber AB issues the CCP and CCA.
That has not been true since December 2025. If you take one fact out of this session, take this one.</p></div>"""),
  dict(title="The shift: consultant to assessor", html="""
<p>An assessor is not a better consultant. The two roles answer different questions, serve different parties, and
are held to different standards. Most students find this the hardest idea in the workshop, and it is not because
it is complicated. It is because the rules prohibit things people are used to doing: helping, advising, fixing,
recommending a vendor they trust.</p>
<div class="tw"><table>
<thead><tr><th></th><th>Consultant</th><th>Assessor</th></tr></thead>
<tbody>
<tr><td><strong>Question answered</strong></td><td>How do we get better?</td><td>What is true here?</td></tr>
<tr><td><strong>Serves</strong></td><td>The client&rsquo;s improvement</td><td>The integrity of the determination</td></tr>
<tr><td><strong>Success looks like</strong></td><td>The gap is closed</td><td>The finding is accurate and survives challenge</td></tr>
<tr><td><strong>Relationship</strong></td><td>Collaborative, ongoing</td><td>Professional, bounded, documented</td></tr>
<tr><td><strong>On finding a problem</strong></td><td>Propose a fix</td><td>Record it, evidence it, and say nothing about the remedy</td></tr>
<tr><td><strong>Governing document</strong></td><td>The engagement contract</td><td>The CoPC, the CAP, 32 CFR Part 170, and ISO/IEC 17020</td></tr>
</tbody></table></div>
<p>The last row is the one that changes your working life. As an assessor you operate inside a conformity regime
that exists precisely so that someone can rely on your determination without knowing you.</p>
<div class="in-practice"><div class="ip-label">The line, in one sentence</div>
<p>A consultant is paid to make an organization better. An assessor is paid to say accurately what is true about
it. You will feel the pull constantly &mdash; a company with obvious problems, staff who want help, an easy fix you
could name in one sentence. Noticing the pull is fine. Acting on it disqualifies you.</p></div>"""),
  dict(title="The three-part standard", html="""
<p>From this session onward, every claim you make in this workshop is held to three questions. Write them on
something you will still have on Friday.</p>
<div class="tw"><table>
<thead><tr><th></th><th>The question</th><th>What a weak answer looks like</th></tr></thead>
<tbody>
<tr><td><strong>Requirement</strong></td><td>What specifically is required?</td>
<td>&ldquo;They need to protect CUI.&rdquo; Which requirement, and at which objective?</td></tr>
<tr><td><strong>Authority</strong></td><td>What imposes it?</td>
<td>&ldquo;CMMC requires it.&rdquo; CMMC is a program. Name the clause, the section, or the Registry category.</td></tr>
<tr><td><strong>Evidence</strong></td><td>What would demonstrate it, and would that be enough?</td>
<td>&ldquo;They have a policy.&rdquo; A policy is a claim about intent, not proof of practice.</td></tr>
</tbody></table></div>
<p>Days 1 and 2 exercise the first two properly and the third lightly. Day 3 afternoon onward is almost entirely
the third, and it is the part that separates people who know CMMC from people who can assess against it.</p>"""),
  dict(title="The credential pathway", html="""
<div class="tw"><table>
<thead><tr><th></th><th>CCP</th><th>CCA</th></tr></thead>
<tbody>
<tr><td><strong>Prerequisites</strong></td>
<td>Training from an Approved Training Provider; relevant experience; a DoW Tier 3 background determination</td>
<td>An active CCP; a DoD 8140.03 Work Role 612 baseline certification at Intermediate or Advanced proficiency &mdash; CISA and CISM both qualify; ATP training; Tier 3 determination</td></tr>
<tr><td><strong>Exam</strong></td><td>170 questions across six domains</td><td>150 questions across four domains</td></tr>
<tr><td><strong>Domain weighting</strong></td>
<td>Ecosystem 5% &middot; Code of Professional Conduct 5% &middot; Governance and Source Documents 15% &middot; Model Construct and Implementation Evaluation 35% &middot; Assessment Process 25% &middot; Scoping 15%</td>
<td>Evaluating OSCs Against Level 2 15% &middot; Level 2 Assessment Scoping 20% &middot; Assessment Process 25% &middot; Assessing Level 2 Practices 40%</td></tr>
<tr><td><strong>Continuing education</strong></td><td>20 CPE annually; 120 over three years, at least 90 CMMC-related</td><td>As CCP</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">Unverified &mdash; do not rely on</div>
<p>Exam <em>duration</em> and <em>passing scores</em> for the CCP and CCA were not publicly stated by ISACA at the
time this material was researched, and no number is published here rather than guessed. Confirm both directly with
ISACA before you register. If you find a figure quoted in a study guide, ask where it came from.</p></div>
<p>Map the domain weights onto this week: Day 4 feeds the 35% and 40% blocks, Day 2 afternoon and Day 5 morning
feed the 25% Assessment Process blocks, and Day 3 morning feeds the scoping blocks. Where you find a session hard
is where your study time goes.</p>"""),
  dict(title="Responsible use, and what never leaves the boundary", html="""
<p>The CoPC's eighth guiding principle is <strong>Proper Use of Technology and AI</strong>, and it is not
decorative. It exists because two things have become easy at the same time: pasting a client's system security
plan into a chat window, and letting a tool draft a determination that is yours to make.</p>
<h3>Two questions, every time</h3>
<ul>
<li><strong>Is a tool making a determination that is mine to make?</strong> A model can summarize an artifact. It
cannot render MET or NOT MET, because it cannot be held to the CoPC, cannot be challenged at an out-brief, and
cannot sign anything. The determination is the credentialed human's, and the reasoning has to be theirs.</li>
<li><strong>Is customer data leaving the boundary to reach that tool?</strong> An SSP extract, a Conditional Access
export, a network diagram, an access control matrix, personnel names, CAGE codes, incident detail &mdash; all of it
is confidential to the engagement and much of it describes exactly how to attack the OSC. Confidentiality is a
separate CoPC principle and it does not have a convenience exception.</li>
</ul>
<div class="warnbox"><div class="warn-label">A real scenario, adjudicated on Day 2</div>
<p>To save time on a long evidence review, a team member pastes several paragraphs of the OSC's system security
plan and a screenshot of its access-control configuration into a public web-based AI assistant, and asks it to
draft finding language. They read the output, edit it, and enter it as their determination.</p>
<p>Two principles are engaged, not one, and the disposition is not &ldquo;be careful next time.&rdquo; You will rule
on this scenario, cite the practices, and say who decides.</p></div>
<h3>What this workshop asks of you</h3>
<ul>
<li>Nothing from the Meridian case needs protecting &mdash; it is fictional, and you may work it in any tool you
like. Use the week to build the habit anyway, because the habit is what transfers.</li>
<li>Every claim you write carries its authority. If an AI tool supplied a citation, open the citation. Fabricated
regulatory cites are common, confident, and career-ending in a findings report.</li>
<li>Disclose tool use where an engagement requires it, and never let a tool talk to the OSC.</li>
</ul>"""),
 ],
 case=dict(tag="The thread begins &middot; Day 1 Morning",
   title="Meet Meridian Precision Defense Systems, and read the solicitation",
   html="""
<p>One company carries all five days. <strong>Meridian Precision Defense Systems, Inc.</strong> is a 147-person
precision manufacturer and systems integrator, headquartered in Dayton, Ohio with a second site in Huntsville,
Alabama. Founded 1998, employee-owned through an ESOP, roughly $31M in annual revenue, CAGE code 7RK42. It machines
guidance system housings and actuator assemblies, and supports UAV subsystem integration.</p>
<p>It holds <strong>three active DoD contracts worth $17.9M</strong>, and all three carry DFARS 252.204-7012:</p>
<ul>
<li><strong>W58RGZ-23-C-0174</strong> &mdash; Army AMCOM prime, firm fixed price, $11.4M. Actuator housing
assemblies, technical data packages, qualification test reports. CUI//CTI, ITAR-controlled drawings. Also carries
252.204-7019, -7020 and -7021.</li>
<li><strong>RTX-SUB-2024-4489</strong> &mdash; a $4.7M cost-plus subcontract under a Raytheon prime for AFLCMC. UAV
airframe bracket design support, FEA reports, drawings to MIL-DTL-31000C. CUI//CTI and limited CUI//PRVCY.</li>
<li><strong>N68335-22-C-0552</strong> &mdash; NAVAIR SBIR Phase II, $1.85M, in its final reports phase. Composite
actuator prototype. CUI//CTI and CUI//SP-EXPT.</li>
</ul>
<p>Three contracts, three agencies, three different CUI category mixes, and one network carrying all of it. The
company has a CISO, ten written policies, and a System Security Plan &mdash; which makes it a more realistic
assessment subject than a company with nothing, and a harder one. Documents exist. Whether they describe the
environment is the question you will spend the week answering.</p>
<p>Today the Army prime contract is up for recompete as solicitation <strong>W58RGZ-26-R-0301</strong>. Open the
case workbench, read the Overview and Contracts tabs, and answer one question before Day 1 afternoon: what does this
company have to be able to demonstrate in order to keep the contract that is 64% of its DoD backlog?</p>
<p><em>You are not determining the level yet. You are noticing that the solicitation never states one in plain
language &mdash; and that somebody has to reason it out from what the contractor will actually receive.</em></p>""",
   actions=[("Open the case workbench &rarr;","meridian.html",False),
            ("See the 5-day thread","index.html#thread",True)]),
 kc_lead=("Ten questions in CCP style. The rationale is the point &mdash; several of the wrong answers are things "
          "you will hear stated confidently by working practitioners."),
 kc=[
  dict(stem="Which body certifies individuals as CCPs and CCAs?", opts=[
   ("The Cyber AB",False,"The Cyber AB is the accreditation body. It accredits C3PAOs under ISO/IEC 17020 and operates the Marketplace &mdash; organizations, not people. This was true historically, which is why so much circulating material still says it."),
   ("ISACA, acting as the CAICO",True,"ISACA took the CMMC Assessor and Instructor Certification Organization role in December 2025, and the transition completed in April 2026. It administers CCP, CCA, Lead CCA, and CCI."),
   ("The DoW CIO / CMMC PMO",False,"The PMO owns the program and issues the model, assessment guides, and scoping guides. It does not certify individuals."),
   ("DIBCAC",False,"DIBCAC is the government assessment arm and conducts government-led assessments, including Level 3. It has no credentialing role."),
  ]),
  dict(stem="A contractor holds Federal Contract Information but no CUI. What CMMC level applies?", opts=[
   ("Level 1",True,"FCI triggers FAR 52.204-21 and CMMC Level 1 &mdash; 15 requirements, annual self-assessment and affirmation."),
   ("Level 2, at reduced scope",False,"There is no reduced-scope Level 2. Level 2 is triggered by CUI, and its requirement set is not scaled down by how little CUI is present."),
   ("Level 2",False,"Level 2 is triggered by CUI. FCI alone does not reach it."),
   ("None &mdash; FCI is outside CMMC",False,"A common and expensive misreading. FCI is squarely inside CMMC at Level 1; 32 CFR 170.14(c)(2) incorporates the fifteen FAR safeguarding requirements."),
  ]),
  dict(stem="How many security requirements comprise CMMC Level 1?", opts=[
   ("15",True,"32 CFR 170.14(c)(2) incorporates FAR 52.204-21(b)(1)(i) through (xv). Fifteen paragraphs, fifteen requirements."),
   ("17",False,"The most widely repeated wrong answer in CMMC study. Earlier CMMC 2.0 model documentation split FAR 52.204-21(b)(1)(ix) into three practices. The split has no basis in the rule. If a deck says 17, the deck is out of date."),
   ("110",False,"110 is Level 2, from NIST SP 800-171 Rev 2."),
   ("320",False,"Roughly 320 is the count of Level 2 assessment objectives in NIST SP 800-171A, not requirements, and not Level 1."),
  ]),
  dict(stem="Under Level 2, a requirement has four assessment objectives. Three are MET and one is not. What is the determination for the requirement?", opts=[
   ("MET, with a noted deficiency",False,"There is no such determination. A noted deficiency at objective level is exactly what makes the requirement NOT MET."),
   ("Partially MET",False,"Partially MET does not exist in CMMC. This is the single most consequential import from maturity-model thinking, and it produces determinations that cannot be defended."),
   ("NOT MET",True,"Every assessment objective must be MET or NOT APPLICABLE for the parent requirement to be MET. One objective unmet makes the whole requirement NOT MET. There is no partial credit."),
   ("It depends on the point value of the requirement",False,"Point values belong to the DoD Assessment Methodology score, which is a different instrument. They have nothing to do with the MET / NOT MET determination."),
  ]),
  dict(stem="An assessor reviewing evidence notices an obvious, cheap fix for a gap and mentions it to the IT Manager during the walkthrough. What has happened?", opts=[
   ("Nothing &mdash; informal observations are not part of the report",False,"The prohibition is not about the report. It is about the role. Advice given verbally in a corridor is still advice, and it is still consulting."),
   ("Good practice &mdash; the assessor is adding value",False,"This is the reasoning that ends careers, and it feels helpful at the time. Adding value to the OSC is the consultant's job, and doing it inside an assessment destroys the independence the determination rests on."),
   ("The assessor has crossed from assessment into consulting",True,"An assessor records a problem, evidences it, and says nothing about the remedy. Naming a risk is assessment; naming its fix is not."),
   ("It is permitted if the OSC asked first",False,"The OSC will ask. It will ask reasonably, warmly, and repeatedly. Being asked does not change the rule &mdash; and being able to decline without lecturing is a skill this workshop assesses."),
  ]),
  dict(stem="Which of these is the correct three-part standard for a claim in an assessment finding?", opts=[
   ("Risk, impact, likelihood",False,"That is a risk-assessment triad. It is not how a conformity determination is justified."),
   ("Requirement, authority, evidence",True,"What specifically is required; what regulation, clause, or official document imposes it; and what would demonstrate it &mdash; and whether that would be enough."),
   ("Policy, procedure, practice",False,"A useful maturity heuristic, and not the standard for defending a determination. It names artifact types, not the burden of proof."),
   ("Examine, interview, test",False,"Those are the three assessment methods from NIST SP 800-171A. They are how you gather evidence, not how you justify a claim."),
  ]),
  dict(stem="Who may serve as an OSC's Affirming Official?", opts=[
   ("The IT Manager who knows the environment best",False,"Knowledge of the environment is not the criterion. Authority to bind the organization is."),
   ("The C3PAO's Lead CCA",False,"Never. The assessor does not affirm the organization's compliance; that would collapse the independence the whole regime rests on."),
   ("A senior official of the OSC with authority to bind it",True,"And the exposure attaches personally: an affirmation that is not true is a false statement in a federal system, with False Claims Act consequences for the person who signed it."),
   ("The consultant who prepared the organization",False,"A consultant cannot bind the OSC and cannot affirm on its behalf."),
  ]),
  dict(stem="An assessment team member pastes extracts from the OSC's system security plan into a public AI assistant to draft finding language. Which CoPC principles are engaged?", opts=[
   ("Proper Use of Technology and AI only",False,"It is the obvious one, and it is not the only one. Stopping here misses the more serious breach."),
   ("Confidentiality only",False,"Confidentiality is engaged, but so is the question of who is permitted to render the determination."),
   ("Proper Use of Technology and AI, and Confidentiality",True,"Two breaches, not one: engagement-confidential information left the boundary, and a tool was used to produce reasoning that is the credentialed assessor's to produce. Information Integrity is arguably a third."),
   ("None, provided the output was edited before use",False,"Editing the output addresses neither problem. The data has already left, and the reasoning still did not originate with the assessor."),
  ]),
  dict(stem="What is the relationship between CMMC Level 2 and NIST SP 800-171 Rev 2?", opts=[
   ("Level 2 is a subset of the 800-171 requirements chosen by the PMO",False,"There is no subset at Level 2. All 110 apply."),
   ("Level 2 adopts all 110 requirements of Rev 2 as its security requirements",True,"The controls are borrowed wholesale. What CMMC adds is the assessment regime, the levels, the scoping rules, affirmation, and enforceability through a contract clause."),
   ("Level 2 is based on Rev 3, with Rev 2 retained for legacy contracts",False,"Rev 3 is not the assessment standard. CMMC Level 2 remains anchored to Rev 2; Rev 3 is horizon-scanning only until future rulemaking says otherwise."),
   ("Level 2 adds requirements from NIST SP 800-172 to 800-171",False,"That describes Level 3, which layers a selected subset of 800-172 on top of the 110."),
  ]),
  dict(stem="A Registered Practitioner (RP) helped an OSC prepare for a Level 1 self-assessment two years ago. The RP is now proposed for the OSC's Level 2 certification assessment team. What applies?", opts=[
   ("Nothing &mdash; the prior work was Level 1, not Level 2",False,"The bar covers preparatory or consulting activity for <em>any type</em> of CMMC assessment. The level of the earlier work does not create an exemption."),
   ("Nothing &mdash; two years have passed",False,"The prohibition runs three years, not two. And even outside it, other conflicts may still apply."),
   ("The three-year consulting prohibition bars participation",True,"32 CFR 170.8(b)(17)(ii)(G), carried into CoPC 2.2(d), prohibits participating in the Level 2 certification process where the member consulted to prepare the organization for any CMMC assessment within three years."),
   ("Participation is permitted if the RP discloses it and the OSC consents",False,"The OSC's consent is irrelevant, and the individual does not decide their own eligibility. The C3PAO owns impartiality and conflict management, and that responsibility cannot be delegated."),
  ]),
 ],
)

L1 = dict(
 file="lesson01.html", short="L1 — Compliance Landscape & Ecosystem", num_label="Lesson 1",
 eyebrow="Day 1 &middot; Afternoon &middot; CCP Domains 1 &amp; 3",
 title="The Compliance Landscape and the CMMC Ecosystem",
 lead=("Cybersecurity standards do not become obligations on their own. Someone writes one, a government adopts "
       "it, and a contracting officer puts it in a contract. Until that happens, a standard is advice. This "
       "session is about how CMMC stopped being advice &mdash; and about reading a regulatory disruption against "
       "primary sources instead of headlines."),
 chips=["Day 1 &mdash; PM","~3 hours","<strong>CCP 5% + 15%</strong>","Tool: Clause Trace"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Trace","Trace the regulatory chain from Executive Order 13556 through 32 CFR Part 170 and the 48 CFR acquisition rule to DFARS 252.204-7021 appearing in a solicitation."),
  ("Distinguish","Distinguish a voluntary framework from a mandatory, assessed, contractually enforced requirement set."),
  ("Determine","Determine the applicable CMMC level from a solicitation that never states one in plain language."),
  ("Separate","Separate what a policy announcement does from what a regulation says, and name the instruments that can actually change the framework."),
  ("Analyse","Sort statements in a professional regulatory alert into what the source states, what the author infers, and what the author advocates."),
 ],
 vocab=[
  ("EO 13556","Executive Order 13556 (2010). Created the government-wide CUI Program and named NARA as Executive Agent. The first link in the chain."),
  ("32 CFR Part 2002","Implements the CUI Program: who may designate CUI, and how it is marked, safeguarded, disseminated, and decontrolled."),
  ("32 CFR Part 170","The CMMC Program rule. Effective 16 December 2024. Defines the model, levels, assessment types, scoping, affirmation, POA&amp;M rules, and the ecosystem."),
  ("48 CFR acquisition rule","Effective 10 November 2025. Amended the DFARS so contracting officers may insert the CMMC clause into solicitations and contracts. Phase 1 began here."),
  ("DFARS 252.204-7012","Safeguarding Covered Defense Information and Cyber Incident Reporting. In force since 2017. Makes 800-171 contractual and adds the 72-hour clock."),
  ("DFARS 252.204-7019 / -7020","Require a current DoD Assessment score posted in SPRS as a condition of award."),
  ("DFARS 252.204-7021","The CMMC clause. Makes a specific CMMC level and status a condition of award and of continued performance."),
  ("Flowdown","The mechanism by which a prime passes safeguarding and certification obligations to subcontractors that will handle covered defense information."),
  ("Covered defense information","The term DFARS 252.204-7012 actually uses. Broader than it looks: it captures information the contractor generates during performance, not only what the Government hands over."),
  ("Class deviation","A formal acquisition instrument that changes how a clause is applied across a class of contracts. One of the three things that can actually change what a contractor owes."),
 ],
 sections=[
  dict(title="Why a cybersecurity standard became a contract term", html="""
<p>NIST SP 800-171 was published in 2015 and revised in 2020. On its own it binds nobody. It is a NIST
publication: a specification of 110 security requirements for protecting CUI on nonfederal systems, with no
enforcement mechanism of any kind.</p>
<p>What made it consequential was a clause. DFARS 252.204-7012 took a NIST document and made implementing it a
term of a Department of Defense contract. From that moment a contractor that failed to implement 800-171 was not
falling short of best practice &mdash; it was in breach of contract.</p>
<p>CMMC is the layer that came next, and it answers a different question. 7012 said <em>you must implement this</em>.
It did not say <em>and someone will check</em>. Fifteen years of self-attestation produced a defense industrial
base in which the attestations and the reality had drifted a long way apart. CMMC is the verification regime built
on top of an obligation that already existed.</p>
<div class="in-practice"><div class="ip-label">Why this matters for the rest of the week</div>
<p>Hold the two apart. The <strong>obligation</strong> to protect CUI lives in DFARS 252.204-7012 and dates from
2017. The <strong>verification</strong> of that obligation lives in 32 CFR Part 170 and DFARS 252.204-7021 and
dates from 2024&ndash;2025. The two are separable, and separating them is the single most useful analytical move
available in this field &mdash; you will use it again on Friday.</p></div>"""),
  dict(title="The chain, link by link", html="""
<p>This is the sequence that turns a NIST publication into something that can cost a company a contract. The order
and the joins are what matter.</p>
<div class="tw"><table>
<thead><tr><th>#</th><th>Link</th><th>What it does</th></tr></thead>
<tbody>
<tr><td>1</td><td><strong>EO 13556</strong> (2010)</td><td>Creates the government-wide CUI Program and names NARA as Executive Agent. Before this, agencies invented their own markings.</td></tr>
<tr><td>2</td><td><strong>32 CFR Part 2002</strong> (2016)</td><td>Implements the CUI Program: who may designate CUI, how it is marked, safeguarded, disseminated, and decontrolled.</td></tr>
<tr><td>3</td><td><strong>NIST SP 800-171 Rev 2</strong> (2020)</td><td>Specifies 110 security requirements for protecting CUI on nonfederal systems. Binding on no one by itself.</td></tr>
<tr><td>4</td><td><strong>DFARS 252.204-7012</strong> (2017)</td><td>Makes 800-171 contractual for DoD contractors, and adds 72-hour cyber incident reporting.</td></tr>
<tr><td>5</td><td><strong>DFARS 252.204-7019 / -7020</strong></td><td>Require a current DoD Assessment score posted in SPRS as a condition of award.</td></tr>
<tr><td>6</td><td><strong>32 CFR Part 170</strong> (eff. Dec 2024)</td><td>Establishes the CMMC Program: three levels, assessment types, scoping rules, affirmation, the ecosystem.</td></tr>
<tr><td>7</td><td><strong>48 CFR acquisition rule</strong> (eff. Nov 2025)</td><td>Amends the DFARS so contracting officers may insert the CMMC clause into solicitations and contracts.</td></tr>
<tr><td>8</td><td><strong>DFARS 252.204-7021</strong></td><td>The clause. Makes a specific CMMC level and status a condition of award and of continued performance.</td></tr>
<tr><td>9</td><td><strong>Flowdown</strong></td><td>The prime passes the requirement to subcontractors at the level appropriate to the information each one handles.</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>Steps 1 through 5 were in force years before CMMC existed. That matters every time someone argues that a
change to the CMMC programme has changed what a contractor owes: the obligation to protect CUI lives at step 4, not
at step 8. You will meet that argument in the field. You should be able to dismantle it in one sentence.</p></div>"""),
  dict(title="The DFARS clause family, and what each one does", html="""
<p>Four clauses appear together in DoD solicitations and are routinely confused with one another. They do different
work and they were added at different times.</p>
<div class="tw"><table>
<thead><tr><th>Clause</th><th>Title</th><th>What it actually requires</th></tr></thead>
<tbody>
<tr><td><strong>FAR 52.204-21</strong></td><td>Basic Safeguarding of Covered Contractor Information Systems</td>
<td>Fifteen basic safeguarding requirements where the contractor handles FCI. The floor for almost every federal contract.</td></tr>
<tr><td><strong>DFARS 252.204-7008</strong></td><td>Compliance with Safeguarding Covered Defense Information Controls</td>
<td>A representation at proposal time that the offeror will implement 800-171, and the route by which a deviation can be requested.</td></tr>
<tr><td><strong>DFARS 252.204-7012</strong></td><td>Safeguarding CDI and Cyber Incident Reporting</td>
<td>Adequate security via 800-171 Rev 2; the 72-hour report; malicious software submission; 90-day media preservation; DoD access; cloud provider requirements; flowdown.</td></tr>
<tr><td><strong>DFARS 252.204-7019 / -7020</strong></td><td>NIST SP 800-171 DoD Assessment Requirements</td>
<td>A current assessment of record in SPRS as a condition of award, and DoD access to conduct higher-level assessments.</td></tr>
<tr><td><strong>DFARS 252.204-7021</strong></td><td>Cybersecurity Maturity Model Certification Requirements</td>
<td>A specific CMMC level and status as a condition of award and of continued performance. The clause CMMC actually rides on.</td></tr>
</tbody></table></div>"""),
  dict(title="Reading a solicitation: where the level actually comes from", html="""
<p>Solicitation <strong>W58RGZ-26-R-0301</strong> &mdash; the AMCOM recompete Meridian must win &mdash; carries
DFARS 252.204-7021 with the required CMMC status left as a fill-in, and points to Section L. Section L says the
status &ldquo;shall be that which corresponds to the categories of information identified in Section C, determined
in accordance with 32 CFR Part 170.&rdquo;</p>
<p>In other words: the solicitation does not tell you. You have to reason it out. The reasoning runs through the
Statement of Work, not the clause list.</p>
<h3>What Section C says</h3>
<ul>
<li><strong>C.3.2</strong> &mdash; on award the Government furnishes the complete Technical Data Package: engineering
drawings, pattern grading specifications, seam and stitch construction standards, flame-resistance test protocols,
the approved materials list. Portions bear <strong>Distribution Statement D</strong> and are subject to export
control provisions cited in Section I.</li>
<li><strong>C.3.3</strong> &mdash; the contractor generates and transmits production status reports, first-article
test results, lot traceability records, and deviation requests, referencing drawing numbers and revision levels
from the TDP.</li>
<li><strong>C.4.1</strong> &mdash; any subcontractor receiving any portion of the TDP must be identified to the
Contracting Officer, and the safeguarding and certification requirements of Section I must be included in that
subcontract.</li>
</ul>
<p>Technical information with military application, subject to controls on access, use, reproduction, modification,
release, or dissemination, is <strong>Controlled Technical Information</strong> &mdash; a CUI category. CUI drives
Level 2. C.3.3 matters independently: information the contractor <em>generates</em> during performance is captured
too. And C.4.1 is flowdown, stated in the Statement of Work before it appears in any clause.</p>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>Candidates look for the level in the clause list and find a blank. The level is determined by the information,
under 32 CFR Part 170, and the Statement of Work is where the information is described. Read Section C before
Section I.</p></div>"""),
  dict(title="Policy announcement versus regulation", html="""
<p>CMMC is an active programme, and active programmes generate announcements: memoranda, press releases, industry
days, testimony, and a steady stream of professional commentary interpreting all of it. Some of that changes what a
contractor owes. Most of it does not, and telling the two apart is a skill with a longer shelf life than any
particular announcement.</p>
<div class="in-practice"><div class="ip-label">Three instruments can change what is required</div>
<ul style="margin-bottom:0">
<li>A <strong>class deviation</strong> &mdash; a formal acquisition instrument changing how a clause is applied
across a class of contracts.</li>
<li>A <strong>DFARS or FAR rule change</strong> &mdash; amending the clause text itself.</li>
<li>An <strong>amendment to 32 CFR Part 170</strong> &mdash; changing the programme rule.</li>
</ul></div>
<p>Until one of those issues, the framework is what the published instruments say it is. A memorandum announcing an
intention, a schedule adjustment, a pilot, or a review does not amend a regulation, however consequential it may
turn out to be. Neither does a recommendation to an agency official, and neither does a press report about either.</p>
<div class="tw"><table>
<thead><tr><th>What you are reading</th><th>Does it change the requirement?</th><th>What to do with it</th></tr></thead>
<tbody>
<tr><td>An amendment to 32 CFR Part 170</td><td><strong>Yes</strong></td><td>Read it; re-derive anything downstream that depended on the old text</td></tr>
<tr><td>A DFARS or FAR rule change</td><td><strong>Yes</strong></td><td>Read the new clause text, not the summary of it</td></tr>
<tr><td>A class deviation</td><td><strong>Yes</strong>, for the class it names</td><td>Check whether the contract in front of you is in that class</td></tr>
<tr><td>A policy memorandum or announcement</td><td><strong>Not by itself</strong></td><td>Note it; watch for the instrument that would implement it</td></tr>
<tr><td>A task force report or recommendation</td><td>No</td><td>Track it as a leading indicator, nothing more</td></tr>
<tr><td>A law firm alert or vendor briefing</td><td>No</td><td>Use it to stay current; never cite it</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">Why an assessor in particular needs this</div>
<p>Because the question arrives as a request. A contractor reads that something has changed, concludes that an
obligation has lifted, and asks you to agree. Your answer is not a matter of opinion or of how the news was
reported &mdash; it is whether an instrument issued, and what its text says.</p>
<p>The same discipline protects you in the other direction. An announcement that sounds alarming does not create an
obligation either, and an assessor who writes findings against requirements that were never enacted is as wrong as
one who ignores requirements that were.</p></div>
<p>Note also that obligations rarely move together. The chain in the previous section has nine links from four
different bodies of law, enacted across fifteen years. A change at one link frequently leaves the others exactly
where they were &mdash; which is why &ldquo;has CMMC changed?&rdquo; is almost never a question with a single
answer, and why the useful question is always <em>which instrument, and what does its text now say?</em></p>"""),
  dict(title="Fact, inference, advice", html="""
<p>You are entering a field with a very large amount of published commentary and a very small amount of governing
text. The discipline that keeps you current without making you wrong is the ability to read a professional alert
and sort every sentence into three buckets.</p>
<div class="tw"><table>
<thead><tr><th>Bucket</th><th>What it is</th><th>Example shape</th><th>Citable?</th></tr></thead>
<tbody>
<tr><td><strong>Stated</strong></td><td>What the primary source actually says</td>
<td>&ldquo;32 CFR 170.21 permits a POA&amp;M only where the score is at least 0.8 of the total.&rdquo;</td><td>Yes &mdash; cite the source, not the alert</td></tr>
<tr><td><strong>Inferred</strong></td><td>What the author concludes from it</td>
<td>&ldquo;This suggests the Department intends to ease the burden on small suppliers.&rdquo;</td><td>No</td></tr>
<tr><td><strong>Advocated</strong></td><td>What the author recommends the reader do</td>
<td>&ldquo;Contractors should begin readiness work now rather than waiting.&rdquo;</td><td>No</td></tr>
</tbody></table></div>
<p>All three are legitimate and useful. Conflating them is not. A finding that rests on a law firm's inference is a
finding that collapses the moment someone reads the underlying memorandum.</p>
<div class="in-practice"><div class="ip-label">The habit worth building this week</div>
<p>When commentary tells you something surprising, find the primary source that supports it <em>before</em> you
accept it. On Friday you will do this across three sources that disagree with one another, on a subject where the
primary sources are incomplete and moving. It is the last analytical exercise of the workshop because it is the
one that keeps everything else current after it stops being true.</p></div>"""),
  dict(title="Source authority, ranked", html="""
<p>In an assessment, and on the exams, the correct answer is the one the governing document supports. Ranking
sources by authority is itself a professional skill.</p>
<div class="tw"><table>
<thead><tr><th>Tier</th><th>Category</th><th>Rule</th></tr></thead>
<tbody>
<tr><td>1</td><td>Governing law and regulation (CFR, FAR, DFARS)</td><td>Controlling. Cite this when a requirement is disputed. It is the law.</td></tr>
<tr><td>2</td><td>Official CMMC program documents (DoW CIO)</td><td>Controlling for assessment practice. The Assessment and Scoping Guides govern how a requirement is assessed.</td></tr>
<tr><td>3</td><td>NIST standards and guidance</td><td>Incorporated by reference. 800-171 Rev 2 and 800-171A define the requirements and objectives.</td></tr>
<tr><td>4</td><td>Ecosystem governance (Cyber AB, ISACA/CAICO)</td><td>Controlling for assessor conduct. The CAP and CoPC govern behaviour; ISACA governs the credentials.</td></tr>
<tr><td>5</td><td>CUI governance (NARA, Executive Order)</td><td>Controlling for CUI identification. Contractors do not self-designate.</td></tr>
<tr><td>6</td><td>Practitioner and legal analysis</td><td>Current-awareness only. Never citable as a requirement.</td></tr>
<tr><td>7</td><td>Training material, portals, case studies</td><td>Instructional. Useful for practice; never authority.</td></tr>
</tbody></table></div>
<p>Note where this workshop sits: tier 7. When it and a governing document disagree, the governing document wins.</p>"""),
 ],
 case=dict(tag="Meridian &middot; Day 1 Afternoon &middot; Deliverable D1",
   title="Trace the clause chain to the contract",
   html="""
<p>You have the solicitation. Now build the chain that binds Meridian to it, and be able to hand the result to
Marcus Ellison &mdash; the chief executive, who is capable, busy, and not a compliance specialist.</p>
<p>The <strong>Clause Trace tool</strong> walks you through the nine links, then asks you three questions:</p>
<ul>
<li>What legal and regulatory authority makes CMMC applicable to this solicitation?</li>
<li>What CMMC level does the offeror need, and what evidence of that level must exist at the time of award?</li>
<li>Which obligations arise independently of CMMC itself &mdash; that is, which would still bind this company if the CMMC clause were struck from the contract tomorrow?</li>
</ul>
<p>Cite primary sources only &mdash; the CFR, the FAR, the DFARS, or an official CMMC document, named to the part,
section, or clause. You may have used a law firm alert to orient yourself; it does not appear in your answer.</p>
<p>The tool checks your chain against the authorities, shows you a model answer once you have committed to your
own, and prints to PDF as your D1 Regulatory Trace Memo.</p>""",
   actions=[("Open the Clause Trace tool &rarr;","clause-trace.html",False),
            ("Case workbench","meridian.html",True)]),
 kc=[
  dict(stem="A contractor argues that a change affecting the CMMC certification requirement means it no longer needs to implement NIST SP 800-171. Where does this reasoning fail?", opts=[
   ("It does not fail &mdash; CMMC is what makes 800-171 mandatory",False,"Reversed. DFARS 252.204-7012 made 800-171 contractual in 2017, seven years before the CMMC programme rule took effect. CMMC verifies an obligation that already existed."),
   ("The 800-171 obligation arises from DFARS 252.204-7012, which is a separate instrument",True,"The obligation lives at link 4 of the chain; CMMC sits at links 6 to 8 as the verification layer. Changing how conformity is verified does not change the thing being verified. This is the single most useful analytical move in the field."),
   ("It fails only if the contract also contains DFARS 252.204-7021",False,"Backwards. The 7012 obligation is independent of 7021 &mdash; with no CMMC clause at all, 7012 still requires 800-171 implementation."),
   ("It fails because 32 CFR Part 170 cannot be amended",False,"Part 170 can be amended, and one day will be. The point is that a change there would not reach back and alter DFARS 252.204-7012."),
  ]),
  dict(stem="A solicitation includes DFARS 252.204-7021 with the required CMMC status left blank, and Section L states the status corresponds to the categories of information in Section C. How is the level determined?", opts=[
   ("It cannot be determined; the offeror must ask the Contracting Officer",False,"Asking is always available, but here the solicitation gives you what you need. An assessor who cannot reason from the Statement of Work will be unable to do the job."),
   ("Default to Level 1 until the Government states otherwise",False,"Defaulting low is the most expensive error available. The information described in Section C determines the level; a blank fill-in is not a determination of Level 1."),
   ("By reading Section C to identify the information the contractor will handle, then applying 32 CFR Part 170",True,"The level follows the information. Section C describes a Technical Data Package with Distribution Statement D and export-controlled content &mdash; Controlled Technical Information, which is CUI, which is Level 2."),
   ("By the dollar value and the NAICS code",False,"Neither has any bearing on the CMMC level. The level is a function of the information, not of contract size or industry classification."),
  ]),
  dict(stem="Which statement about the Statement of Work provision requiring subcontractors handling the Technical Data Package to be identified is most accurate?", opts=[
   ("It is a reporting formality with no CMMC consequence",False,"It is the flowdown obligation appearing in the SOW. The consequences reach every subcontractor that will touch the TDP."),
   ("It obliges the prime to flow safeguarding and certification requirements to those subcontractors",True,"Flowdown is link 9 of the chain. DFARS 252.204-7012(m) requires the clause in subcontracts where performance will involve covered defense information, and the SOW states the same obligation in plain language."),
   ("It applies only to subcontractors above the simplified acquisition threshold",False,"There is no such threshold in the flowdown rule. The obligation follows the information, not the dollar value."),
   ("It transfers the prime's CMMC obligation to the subcontractor",False,"Flowdown adds an obligation to the subcontractor; it does not discharge the prime's. Both are bound."),
  ]),
  dict(stem="Which of the following may be cited as authority in an assessment finding?", opts=[
   ("A law firm client alert analysing a recent DFARS amendment",False,"Tier 6 &mdash; current awareness only. It is how you stay current, and it is never what you cite. Cite the amendment, not the alert about it."),
   ("32 CFR 170.19(c)",True,"Tier 1: governing federal regulation. When a requirement is disputed, this is where the answer resolves."),
   ("A CMMC training portal module",False,"Tier 7 &mdash; instructional. Useful for practice, never authority. Note that a portal module in this very curriculum contains a factual error about who issues the CCP."),
   ("The OSC's own data classification inventory",False,"That is evidence about the OSC, not authority about the requirement. Treating a contractor's assertion as authority is the specific error this workshop trains out of you."),
  ]),
  dict(stem="In a law firm alert, the sentence \"contractors should treat the pause as an opportunity to close gaps before demand resumes\" belongs in which bucket?", opts=[
   ("Stated",False,"No primary source says this. It is the author speaking, not the memorandum."),
   ("Inferred",False,"Close, but inference is a conclusion about what is true. This is a recommendation about what to do."),
   ("Advocated",True,"It is advice. Legitimate, often sensible, and not citable as a requirement. The discipline is separating it from the two sentences above it that may look identical in tone."),
   ("It is not classifiable without the full document",False,"The grammatical form settles it. \"Should\" plus an action is advocacy."),
  ]),
  dict(stem="Which pair correctly describes the effect of the 48 CFR acquisition rule effective 10 November 2025?", opts=[
   ("It created the CMMC Program and defined the three levels",False,"That is 32 CFR Part 170, effective December 2024."),
   ("It amended the DFARS so contracting officers may insert the CMMC clause; Phase 1 began",True,"32 CFR Part 170 created the program; the 48 CFR rule made it operable in acquisitions. Level 1 and Level 2 self-assessment requirements began appearing in contracts from this point."),
   ("It established the CUI Program and named NARA as Executive Agent",False,"That is Executive Order 13556, link 1 of the chain, and it dates from 2010."),
   ("It replaced DFARS 252.204-7012",False,"7012 was untouched and remains in force. Nothing in the chain replaced it."),
  ]),
  dict(stem="A contractor holds a contract containing DFARS 252.204-7012 but no CMMC clause. Which obligations attach?", opts=[
   ("None until a CMMC clause is added",False,"7012 stands on its own. This is the reasoning that leaves a contractor in breach of a clause it already holds."),
   ("Adequate security via NIST SP 800-171 Rev 2, 72-hour incident reporting, media preservation, cloud conditions, and flowdown",True,"All of it, and none of it depends on CMMC. 7012 has been in force since 2017 and imposes each of these directly."),
   ("Only the incident reporting obligation",False,"Reporting is one paragraph of the clause. Adequate security under (b)(2) is the substantive obligation and applies equally."),
   ("Implementation of 800-171, but no reporting obligation without 7019 and -7020",False,"Conflates two clauses. 7019 and -7020 concern the SPRS assessment of record; the 72-hour report is 7012(c)(1)."),
  ]),
  dict(stem="What does DFARS 252.204-7012's definition of covered defense information capture that a narrow reading would miss?", opts=[
   ("Classified information held under a facility clearance",False,"CUI and covered defense information are unclassified by definition. Classified information is governed by an entirely separate regime."),
   ("Information the contractor develops at its own expense for its own purposes",False,"That is expressly outside the CUI definition &mdash; and it is the trap in Meridian's payroll and vendor-invoice entry."),
   ("Information the contractor collects, develops, receives, transmits, uses, or stores in support of contract performance",True,"The second half of the definition captures information the contractor generates itself, not only what the Government hands over. Meridian's production reports and lot traceability records land here."),
   ("Any information stored on a system that also stores CUI",False,"Co-location is a scoping consequence, not a definitional one. A system holding CUI is in scope; that does not reclassify the other data on it."),
  ]),
  dict(stem="An offeror has never calculated or submitted a SPRS score. Which clause makes that a problem at award?", opts=[
   ("DFARS 252.204-7012",False,"7012 imposes safeguarding, incident reporting, preservation, cloud, and flowdown obligations. It does not require a posted score."),
   ("FAR 52.204-21",False,"The fifteen basic safeguarding requirements for FCI. No SPRS obligation."),
   ("DFARS 252.204-7019 and -7020",True,"These require a current assessment of record in SPRS as a condition of award, and the solicitation's Section L makes verification explicit. Meridian has never submitted one and its Army prime contract requires it."),
   ("DFARS 252.204-7008",False,"7008 is a proposal-time representation about implementing 800-171 and the route for requesting a deviation. It does not create the SPRS posting requirement."),
  ]),
  dict(stem="A policy memorandum announces an intended change to how CMMC will be applied. What has changed for a contractor performing today?", opts=[
   ("Everything the memorandum describes, from its effective date",False,"A memorandum announcing an intention is not an instrument that amends a clause or a rule. Acting on it as though it were is how contractors end up out of compliance with text that never changed."),
   ("Nothing yet &mdash; a class deviation, a FAR or DFARS rule change, or an amendment to 32 CFR Part 170 is required",True,"Those three are the instruments that can change what a contractor owes. Until one issues, the framework is what the published text says. Watching for which of the three arrives is the practical form of regulatory currency."),
   ("Nothing, and nothing ever will &mdash; only Congress can change the requirement",False,"Overcorrecting. The requirement rests on regulations that agencies amend routinely; the point is which instrument does it, not that none can."),
   ("It depends on whether the contracting officer agrees the change applies",False,"A contracting officer administers a contract; they do not amend the regulation. They may, however, issue a modification &mdash; which is a different thing and applies to that contract alone."),
  ]),
 ],
)

L2 = dict(
 file="lesson02.html", short="L2 — FCI, CUI & the Regulatory Stack", num_label="Lesson 2",
 eyebrow="Day 2 &middot; Morning &middot; CCP Domain 3 (15%)",
 title="FCI, CUI, and the Regulatory Stack",
 lead=("The determination everything downstream depends on. Get this wrong and the level is wrong, the scope is "
       "wrong, the evidence plan is wrong, and every finding inherits the error. This is also the cheapest "
       "session in which to make a mistake, which is why it comes early."),
 chips=["Day 2 &mdash; AM","~3 hours","<strong>CCP 15%</strong>","Tool: CUI Determination"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Distinguish","Distinguish Federal Contract Information from Controlled Unclassified Information by definition and by consequence &mdash; not by how sensitive the information feels."),
  ("Use","Use the NARA CUI Registry to identify the category, marking, Basic/Specified status, and authorizing law for a given information type."),
  ("Audit","Audit a contractor's own data classification and say precisely where and why it is wrong."),
  ("Explain","Explain why a contractor identifies and protects CUI but does not designate it, and say who does."),
  ("Determine","Determine the DFARS 252.204-7012 obligations attaching to a contract, including the 72-hour clock, media preservation, cloud requirements, and flowdown."),
  ("Defend","State which systems fall inside the CUI boundary and defend the line."),
 ],
 vocab=[
  ("Federal Contract Information","FAR 52.204-21(a): information, not intended for public release, provided by or generated for the Government under a contract to develop or deliver a product or service. Excludes public information and simple transactional information."),
  ("Controlled Unclassified Information","32 CFR 2002.4: information the Government creates or possesses, or that an entity creates or possesses for or on behalf of the Government, that a law, regulation, or government-wide policy requires an agency to safeguard or control."),
  ("CUI Basic","A category whose handling follows the uniform CUI baseline, with no additional controls set by the authorizing authority."),
  ("CUI Specified","A category where the authorizing law, regulation, or policy itself sets handling requirements beyond the CUI Basic baseline. Marked with the SP- prefix, e.g. CUI//SP-CTI."),
  ("Designating agency","The agency that determines information is CUI under an authority. A contractor is never one."),
  ("Authorized holder","An individual, agency, organization, or group permitted to designate or handle CUI in accordance with 32 CFR Part 2002. Handling authority is not designation authority."),
  ("CTI","Controlled Technical Information. Technical information with military or space application subject to controls on access, use, reproduction, modification, release, or dissemination. CUI Specified."),
  ("PROCURE","General Procurement and Acquisition. Covers cost or pricing data, contract information, indirect costs, and direct labour rates. CUI Specified."),
  ("Medium assurance certificate","A DoD-approved certificate required to file a cyber incident report on DIBNet. Without one, a contractor cannot report at all."),
  ("DIBNet","The DoD portal through which cyber incidents are reported under DFARS 252.204-7012(c)."),
 ],
 sections=[
  dict(title="Two definitions, and what follows from each", html="""
<p>Start with the text rather than the intuition. Both definitions are short, and both turn on origin rather than
sensitivity.</p>
<div class="in-practice"><div class="ip-label">Federal Contract Information &mdash; FAR 52.204-21(a)</div>
<p>Information, not intended for public release, that is provided by or generated for the Government under a
contract to develop or deliver a product or service to the Government. It <em>excludes</em> information the
Government provides to the public &mdash; anything on a public website &mdash; and simple transactional information
such as that necessary to process payments.</p></div>
<div class="in-practice"><div class="ip-label">Controlled Unclassified Information &mdash; 32 CFR 2002.4</div>
<p>Information the Government creates or possesses, or that an entity creates or possesses for or on behalf of the
Government, that a law, regulation, or government-wide policy requires or permits an agency to handle with
safeguarding or dissemination controls. It <em>excludes</em> classified information, and information a company
develops purely at its own expense for its own purposes.</p></div>
<div class="tw"><table>
<thead><tr><th></th><th>FCI</th><th>CUI</th></tr></thead>
<tbody>
<tr><td><strong>Triggering clause</strong></td><td>FAR 52.204-21</td><td>DFARS 252.204-7012 (for DoD covered defense information)</td></tr>
<tr><td><strong>CMMC level</strong></td><td>Level 1</td><td>Level 2</td></tr>
<tr><td><strong>Requirement count</strong></td><td>15, incorporated verbatim by 32 CFR 170.14(c)(2)</td><td>110, NIST SP 800-171 Rev 2</td></tr>
<tr><td><strong>Conformity</strong></td><td>Annual self-assessment and affirmation</td><td>Self-assessment or C3PAO certification per the contract; posted to SPRS; affirmed annually</td></tr>
<tr><td><strong>Marking</strong></td><td>No CUI marking regime applies</td><td>Banner and portion marking under the CUI Marking Handbook</td></tr>
<tr><td><strong>Incident reporting</strong></td><td>No clause-imposed obligation</td><td>72-hour rapid report to DIBNet under 252.204-7012(c)</td></tr>
</tbody></table></div>
<p><strong>Meridian holds CUI under all three contracts, and FCI besides.</strong> The Army prime carries the CMMC
clause expressly; the Raytheon subcontract and the NAVAIR SBIR carry DFARS 252.204-7012 without it. All of it lives
on the same file server, in the same tenant, handled by the same people. The obligations stack; they do not
partition themselves because the contracts are separate, and a company cannot run three security postures across one
network.</p>"""),
  dict(title="Who decides", html="""
<p>This is the part practitioners get wrong most often, and the error is not subtle once you see it.</p>
<p>Under EO 13556 and 32 CFR Part 2002, information becomes CUI because a law, regulation, or government-wide
policy requires it to be controlled, and an authorized holder in the <em>designating agency</em> applies that
basis. A contractor is not a designating agency. A contractor cannot make information CUI by marking it, and cannot
make it not-CUI by declining to.</p>
<div class="tw"><table>
<thead><tr><th>A contractor may</th><th>A contractor may not</th></tr></thead>
<tbody>
<tr><td>Identify information already designated as CUI by the Government</td><td>Designate information as CUI on its own authority</td></tr>
<tr><td>Apply required markings when creating documents from CUI it holds</td><td>Decide that CUI it received is &ldquo;not really&rdquo; CUI</td></tr>
<tr><td>Ask the contracting officer for a determination when status is unclear</td><td>Mark commercial or internal information CUI &ldquo;to be safe&rdquo;</td></tr>
<tr><td>Protect the information at the level the contract requires</td><td>Decontrol CUI &mdash; only the designating agency can</td></tr>
<tr><td>Flow the requirement down to subcontractors who will handle it</td><td>Rely on the absence of markings as proof that nothing is CUI</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">Unmarked does not mean unprotected</div>
<p>You will find CUI in the field carrying no marking at all &mdash; because a government office failed to mark it,
because it was extracted from a marked document, or because it was generated during performance and nobody thought
about it. The obligation attaches to the information, not to the sticker. &ldquo;It was not marked&rdquo; is an
explanation for how a company got into trouble. It has never been a defence.</p></div>"""),
  dict(title="The Registry, used properly", html="""
<p>The NARA CUI Registry is the authoritative list of CUI categories, each tied to the authority that permits the
control. Using it well is a mechanical skill and you should be fast at it by the end of the session.</p>
<p>For any information type, produce <strong>four things</strong>:</p>
<ol>
<li>The <strong>exact category name</strong> as the Registry states it &mdash; not a paraphrase, and not a name the
company made up.</li>
<li>The <strong>category marking</strong>, and the banner marking that results.</li>
<li>Whether the category is <strong>CUI Basic or CUI Specified</strong>.</li>
<li>The <strong>authorizing law, regulation, or government-wide policy</strong> the Registry cites.</li>
</ol>
<div class="tw"><table>
<thead><tr><th>Category</th><th>Marking</th><th>Index</th><th>What it covers</th></tr></thead>
<tbody>
<tr><td><strong>Controlled Technical Information</strong></td><td>CTI</td><td>Defense</td>
<td>Technical information with military or space application subject to controls on access, use, reproduction, modification, release, or dissemination &mdash; drawings, specifications, standards, manuals, test protocols, data sets, software. Specified; the Registry cites 48 CFR 252.204-7012.</td></tr>
<tr><td><strong>General Procurement and Acquisition</strong></td><td>PROCURE</td><td>Procurement and Acquisition</td>
<td>Material relating to acquisition and procurement of goods and services, including cost or pricing data, contract information, indirect costs, and direct labour rates. Specified.</td></tr>
<tr><td><strong>Export Controlled</strong></td><td>EXPT</td><td>Export Control</td>
<td>Unclassified information concerning items subject to export control, including under the Export Administration Regulations.</td></tr>
<tr><td><strong>Personnel Records / General Privacy</strong></td><td>PERS / PRVCY</td><td>Privacy</td>
<td>Personnel and privacy information held by or for the Government. Note the boundary: an employer's own HR file is not automatically in this category.</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Exam tip &mdash; the SP- prefix</div>
<p>A banner such as <strong>CUI//SP-CTI</strong> marks a CUI <em>Specified</em> category &mdash; one where the
authorizing law, regulation, or policy itself sets handling requirements beyond the CUI Basic baseline. Some
categories are Specified under one authority and Basic under another. That is why you read the category page rather
than memorizing a list.</p></div>"""),
  dict(title="DFARS 252.204-7012, clause by clause", html="""
<p>This clause predates CMMC by seven years and stands entirely independently of it. It is the reason
Meridian, with no certification and no assessor ever having visited, is already in breach of its Army prime contract.
Know it in detail.</p>
<div class="tw"><table>
<thead><tr><th>Obligation</th><th>What the clause requires</th><th>Where</th></tr></thead>
<tbody>
<tr><td><strong>Adequate security</strong></td><td>Implement NIST SP 800-171 Rev 2 on covered contractor information systems; deviations require a written determination by the DoD CIO.</td><td>(b)(2)</td></tr>
<tr><td><strong>Rapid reporting</strong></td><td>Report a cyber incident to DoD within 72 hours of discovery, via DIBNet, using a DoD-approved medium assurance certificate.</td><td>(c)(1)</td></tr>
<tr><td><strong>Malicious software</strong></td><td>Submit malicious software discovered and isolated in connection with a reported incident to the DoD Cyber Crime Center. Do not send it with the incident report.</td><td>(d)</td></tr>
<tr><td><strong>Media preservation</strong></td><td>Preserve and protect images of known affected systems and relevant monitoring data for at least 90 days from the incident report.</td><td>(e)</td></tr>
<tr><td><strong>DoD access</strong></td><td>Provide DoD access to additional information or equipment necessary for forensic analysis on request.</td><td>(f)</td></tr>
<tr><td><strong>Cloud services</strong></td><td>Require an external cloud service provider storing, processing, or transmitting CDI to meet the FedRAMP Moderate baseline or equivalent, <em>and</em> to comply with the reporting, preservation, and access requirements above.</td><td>(b)(2)(ii)(D)</td></tr>
<tr><td><strong>Flowdown</strong></td><td>Include the clause, without alteration except to identify the parties, in subcontracts for operationally critical support or where performance will involve CDI.</td><td>(m)</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Three details worth memorizing exactly</div>
<p><strong>72 hours, from discovery</strong> of the incident &mdash; not from confirmation, not from the end of the
investigation.<br>
<strong>90 days</strong> of media and monitoring-data preservation, running from submission of the incident report.<br>
<strong>A medium assurance certificate</strong> is required to file the report at all. Meridian has never
obtained one, which means that on the day it needs to report it will discover this at hour 70 of a 72-hour clock.</p></div>
<div class="warnbox"><div class="warn-label">The cloud question at Meridian, precisely</div>
<p>Meridian keeps CUI in Microsoft 365 <strong>GCC High</strong> and runs SBIR analysis in <strong>AWS
GovCloud</strong>. Both carry FedRAMP <em>High</em> authorisations &mdash; comfortably above the Moderate baseline
the clause names. So is (b)(2)(ii)(D) satisfied?</p>
<p><strong>The authorisation is satisfied. The obligation may not be.</strong> Two things remain to check.</p>
<p>First, the clause requires the provider to comply with the cyber incident reporting, media preservation, and DoD
access requirements as well. A FedRAMP authorisation is a statement about the platform's security posture; it is not
by itself a commitment to those contractual obligations, and the assessor asks what in the agreement establishes
them.</p>
<p>Second &mdash; and this is where Meridian actually fails &mdash; <strong>an authorised platform that is
misconfigured is not a compliant environment.</strong> Conditional Access is only partially configured, guest access
to SharePoint is not fully restricted, and a shared service account holds Global Admin with no individual owner
assigned. The platform is doing its job. The tenant is not.</p>
<p>Note how this differs from the more familiar failure. A contractor keeping CUI in a commercial tenant fails at
the authorisation. Meridian passes the authorisation and fails at the configuration &mdash; which is harder to see,
easier to argue about, and far more common in companies that have spent money on the right products.</p></div>"""),
  dict(title="Auditing a contractor's own inventory", html="""
<p>Meridian maintains a data inventory, and like most contractors it produced that inventory without ever opening
the Registry. Your job is not to accept it. It is to audit it.</p>
<p>Six entries. Some of the company's calls are right. Among the wrong ones there is a category name that does not
exist, an item the company has treated as its own commercial property when the contract says otherwise, an internal
contradiction between two of the company's own records, and one item classified <em>too low</em> &mdash; the
direction that costs money.</p>
<div class="tw"><table>
<thead><tr><th>#</th><th>Information</th><th>Meridian says</th></tr></thead>
<tbody>
<tr><td>1</td><td>Actuator housing technical data packages &mdash; engineering drawings, tolerances, materials, and qualification test protocols furnished by AMCOM under W58RGZ-23-C-0174. Portions bear Distribution Statement D and are ITAR-controlled.</td><td>CUI &mdash; &ldquo;ITAR Data&rdquo;</td></tr>
<tr><td>2</td><td>UAV airframe bracket design files &mdash; FEA reports and drawings to MIL-DTL-31000C, produced by Meridian under the Raytheon subcontract and delivered to the prime</td><td>CUI &mdash; &ldquo;CTI&rdquo;</td></tr>
<tr><td>3</td><td>Personnel security submissions &mdash; SF-86 data and DISS records for staff requiring a determination, collected on behalf of the Government and held by the FSO</td><td>CUI &mdash; &ldquo;Privacy&mdash;Personnel&rdquo;</td></tr>
<tr><td>4</td><td>SBIR final technical report and composite actuator research data &mdash; export-controlled; the NAVAIR contract identifies CUI//SP-EXPT</td><td>&ldquo;Proprietary R&amp;D &mdash; company confidential&rdquo;</td></tr>
<tr><td>5</td><td>Payroll, ESOP participant records, and invoices from commercial raw-material suppliers &mdash; generated by Meridian as an employer and a business, at its own expense</td><td>Inconsistent &mdash; two company records disagree</td></tr>
<tr><td>6</td><td>Cost and pricing data under the CPFF Raytheon subcontract &mdash; indirect cost pools, negotiated labour rates, and the build-ups behind them</td><td>FCI</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">The contradiction to resolve, not average</div>
<p>Meridian's data classification page states plainly that payroll, ESOP participant records, and commercial
supplier invoices are sensitive business data that do not meet the CUI definition. Its third-party register, three
screens away, records Whitmore &amp; Associates &mdash; the external CPA with read-only QuickBooks access &mdash; as
handling &ldquo;employee PII / CUI-Privacy,&rdquo; while the same register elsewhere states the firm is
&ldquo;not in SSP scope.&rdquo;</p>
<p>Both cannot be right, and neither is <em>authority</em> &mdash; the Registry and the definition are. Saying what
distinguishes item 5 from item 3, since both concern employees, is the heart of the audit. The distinction is not
sensitivity. It is <em>who the information was created for</em>. SF-86 and DISS material is collected on the
Government's behalf under a personnel security process; a W-4 and an ESOP statement are not.</p></div>
<div class="warnbox"><div class="warn-label">The item the company has quietly reclassified as its own</div>
<p>Item 4 is the interesting one. Meridian calls the SBIR research &ldquo;proprietary R&amp;D &mdash; company
confidential,&rdquo; which is how a great many contractors think about work they performed. But the NAVAIR contract
identifies <strong>CUI//SP-EXPT</strong>, and the CUI definition expressly reaches information an entity creates or
possesses <em>for or on behalf of</em> the Government.</p>
<p>SBIR data rights are real and they are a different question entirely: a contractor may hold data rights in
technical data and that information may still be CUI. Rights govern what the Government may do with it. CUI status
governs how it must be protected. Conflating the two is the specific error here, and it is extremely common in
research-performing contractors.</p>
<p>An assessor who says &ldquo;this is CUI//SP-EXPT under the contract, and your data rights position is
unaffected by that&rdquo; has made the determination and defused the argument in one sentence.</p></div>
<div class="tip"><div class="tip-label">Where Meridian is right</div>
<p>Item 2 is correct and should be marked so. Note what makes it correct: Meridian <em>generated</em> the FEA
reports and drawings itself, and they are still CUI, because covered defense information reaches information the
contractor develops in performance. Contractors routinely assume that only what the Government hands them counts.</p></div>"""),
  dict(title="Drawing the boundary", html="""
<p>The last question is the hardest half: which systems are inside the CUI boundary, and which are outside.</p>
<p>Dayton runs three subnets &mdash; CORP-LAN (10.10.1.0/24), ENG-LAN (10.10.2.0/24) and MGMT-LAN (10.10.3.0/24)
&mdash; and all three route freely through a core Cisco Catalyst 2960-X. There is no VLAN-enforced segmentation
between them, so a compromise on CORP-LAN has direct SMB and NFS access to the CUI file stores on ENG-LAN. MGMT-LAN
is separated by policy only, not at the switch. Huntsville (192.168.5.0/24) sits behind a Cisco RV345 on an
always-on IPsec tunnel back to the Dayton domain controllers.</p>
<p>Multifactor authentication is enforced at the Microsoft 365 GCC High layer. It is <strong>not</strong> enforced
at the network access layer: the FortiGate SSL VPN authenticates against Active Directory with username and password
alone, roughly 22 users hold VPN access, and six of those accounts belong to people who no longer work here.</p>
<div class="tw"><table>
<thead><tr><th>System</th><th>What it is</th><th>Holds CUI?</th><th>Note</th></tr></thead>
<tbody>
<tr><td>SYS-001 / SYS-002</td><td>MPDS-CORP-DC01 / DC02, AD domain controllers, WS2019</td><td>Indirect</td><td>Dayton. AD, DNS, Group Policy for the whole environment.</td></tr>
<tr><td>SYS-003</td><td>MPDS-FILE-SRV01, Windows file server, WS2022</td><td><strong>Primary</strong></td><td>Dayton. The principal CUI store.</td></tr>
<tr><td>SYS-004</td><td>MPDS-APP-LNX01, Arena PLM on Ubuntu 22.04</td><td>Yes</td><td>Dayton. Drawings, BOMs, engineering change data.</td></tr>
<tr><td>SYS-005 &times;14</td><td>Engineering workstations, CAD/CAM, Win 10 Ent 22H2</td><td>Yes</td><td>Dayton. Not enrolled in any configuration management tool; about four are 90+ days behind on critical updates.</td></tr>
<tr><td>SYS-006 &times;6</td><td>Engineering workstations, Win 11 Ent</td><td>Yes</td><td>Huntsville. Reached over the IPsec tunnel; no local IT staff on site.</td></tr>
<tr><td>SYS-007</td><td>Microsoft 365 GCC High tenant</td><td>Yes</td><td>Email, Teams, SharePoint, OneDrive. FedRAMP High authorised platform; tenant configuration only partially complete.</td></tr>
<tr><td>SYS-008</td><td>AWS GovCloud (US-West), compute and S3</td><td>Yes</td><td>SBIR finite-element analysis data. FedRAMP High. Meridian manages IAM directly; root account MFA enabled.</td></tr>
<tr><td>SYS-009 / SYS-010</td><td>FortiGate 200F perimeter firewall and VPN gateway</td><td>No</td><td>Dayton. Single ISP, no DMZ. VPN authenticates against AD with no MFA.</td></tr>
<tr><td>SYS-011</td><td>Snort 3.x IDS/IPS sensor on Ubuntu 20.04</td><td>No</td><td>Dayton, on MGMT-LAN.</td></tr>
<tr><td>SYS-012</td><td>Xerox AltaLink C8045 multifunction printer</td><td>Yes</td><td>Dayton, on ENG-LAN. Hard-copy CUI output.</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">A boundary is named systems</div>
<p>&ldquo;The network&rdquo; is not a boundary. Name systems, say what puts each inside or outside, and say what
evidence would move one across the line. A strong determination also notices the shape of the answer here: the
boundary is wide <em>by default</em> rather than by design, because there is no segmentation and no policy &mdash;
and that fact is itself the most consequential finding available.</p></div>"""),
 ],
 case=dict(tag="Meridian &middot; Day 2 Morning &middot; Deliverable D2",
   title="Sort the data inventory: FCI, CUI, or neither",
   html="""
<p>Six information types, six company classifications, and your determination on each. The
<strong>CUI Determination tool</strong> gives you the Registry categories, the definitions, and a workspace, then
checks your calls one at a time with the reasoning &mdash; not just the verdict.</p>
<p>For each item you determine is CUI: the exact Registry category name, the marking, Basic or Specified, and the
authority the Registry cites. For each item you determine is FCI or neither: the element of the definition it
fails, and which definition you applied.</p>
<p>Then say what kind of error the company made where it is wrong &mdash; a category that does not exist, a
category that exists but does not fit, an internal contradiction, or an item classified too low.</p>
<p><strong>A warning about your source material.</strong> The inventory reproduces Meridian's own
classifications. Those are assertions by the party being assessed, which is precisely the kind of claim you are
being trained not to accept. If a determination in your memo can be traced only to something the contractor said
about itself, it is not yet a determination.</p>""",
   actions=[("Open the CUI Determination tool &rarr;","cui-determination.html",False),
            ("Case workbench &middot; Data tab","meridian.html",True)]),
 kc=[
  dict(stem="Who may designate information as CUI?", opts=[
   ("The contractor holding it",False,"A contractor identifies and protects CUI. It does not designate, and it cannot decontrol. Almost every bad determination in the field is a variation on a contractor believing it holds an authority it does not hold."),
   ("Any authorized holder",False,"Handling authority is not designation authority. An authorized holder may possess and handle CUI in accordance with 32 CFR Part 2002 without any power to designate it."),
   ("An agency, under a law, regulation, or government-wide policy",True,"Designation authority sits with the Government under EO 13556 and 32 CFR Part 2002, and it must rest on an authority that requires or permits the control."),
   ("The prime contractor, on behalf of its subcontractors",False,"A prime flows down obligations. It does not acquire designation authority by being higher in the supply chain."),
  ]),
  dict(stem="Meridian classifies its SBIR final technical report as \"proprietary R&D — company confidential\" rather than CUI. What is the assessor's response?", opts=[
   ("Accept it &mdash; Meridian performed the research and holds data rights in it",False,"Conflates two separate questions. Data rights govern what the Government may do with the information; CUI status governs how it must be protected. A contractor can hold data rights in information that is also CUI."),
   ("It is CUI//SP-EXPT: the contract identifies it, and CUI reaches information created for or on behalf of the Government",True,"The NAVAIR contract identifies the category, and 32 CFR 2002.4 expressly reaches information an entity creates or possesses for or on behalf of the Government. The company's data rights position is unaffected by the determination."),
   ("It is CUI only if the Government has marked the deliverable",False,"Marking is evidence, not the test. The obligation attaches to the information, and the contract identifies the category regardless."),
   ("It is neither &mdash; research performed at the contractor's own initiative is outside the definition",False,"It was not performed at the contractor's own initiative. It was performed under a $1.85M federal contract that names the CUI category."),
  ]),
  dict(stem="Meridian keeps CUI in Microsoft 365 GCC High, which holds a FedRAMP High authorization. Its Conditional Access policies are partially configured, guest access to SharePoint is unrestricted, and a shared service account holds Global Admin. What follows?", opts=[
   ("The requirement is satisfied &mdash; FedRAMP High exceeds the Moderate baseline",False,"The authorization is satisfied. It is a statement about the platform, and it says nothing about how this tenant is configured."),
   ("The authorization is met, but an authorized platform that is misconfigured is not a compliant environment",True,"This is the harder and more common failure. Meridian passed the procurement question and failed the implementation one &mdash; and the misconfigurations are findings against access control and configuration requirements in their own right."),
   ("GCC High is not acceptable; only a private government cloud satisfies the clause",False,"No such rule exists. The clause names the FedRAMP Moderate baseline or equivalent, and GCC High comfortably exceeds it."),
   ("The findings belong to Microsoft, since it operates the platform",False,"Tenant configuration is the customer's responsibility, not the provider's. That allocation is exactly what a Customer Responsibility Matrix exists to make explicit."),
  ]),
  dict(stem="Within what period must a cyber incident be reported under DFARS 252.204-7012, and from when?", opts=[
   ("24 hours from confirmation",False,"Neither the period nor the trigger is right."),
   ("72 hours from discovery",True,"Via DIBNet, and a DoD-approved medium assurance certificate is required to file at all."),
   ("72 hours from completion of the investigation",False,"The reading contractors act on in practice, and it is wrong. Meridian acted on something close to this and then never finished the investigation either."),
   ("30 days from discovery",False,"No provision of the clause supports this."),
  ]),
  dict(stem="Meridian's payroll records, production labour hours, and commercial vendor invoices are best classified as:", opts=[
   ("CUI &mdash; Privacy",False,"Sensitive and regulated, but neither is the test. Ask what law requires an <em>agency</em> to control it. Nothing does &mdash; this material was never created for or on behalf of the Government."),
   ("FCI",False,"Fails the FCI definition too: it was not provided by or generated for the Government under either contract."),
   ("Neither CUI nor FCI",True,"Created and held by Meridian as an employer and a business, at its own expense, for its own purposes. Expressly outside the CUI definition at 32 CFR 2002.4 and outside FCI at FAR 52.204-21(a)."),
   ("CUI &mdash; PROCURE, because invoices are procurement material",False,"PROCURE concerns government acquisition material. Invoices from Meridian's own commercial raw-material suppliers are not that."),
  ]),
  dict(stem="Employee clearance submissions (SF-86 data) are CUI, but ordinary payroll records are not. What distinguishes them?", opts=[
   ("Clearance data is more sensitive",False,"Sensitivity is not the test, and reasoning from it is how contractors end up over-marking everything."),
   ("Clearance data is collected for the Government under a personnel security process",True,"The distinction is who the information was created for. SF-86 material is collected on the Government's behalf; a W-4 is not. Both concern employees; only one is inside the CUI definition."),
   ("Clearance data is classified",False,"CUI is unclassified by definition, and no clearance attaches to it."),
   ("Payroll is excluded because a third party processes it",False,"Who processes it is irrelevant to whether it is CUI. The external accountant's involvement changes the scoping analysis, not the classification."),
  ]),
  dict(stem="Meridian classifies its contract pricing and cost data as FCI. What is the strongest assessor response?", opts=[
   ("Accept it &mdash; pricing is transactional information excluded from CUI",False,"The transactional exclusion in FAR 52.204-21(a) covers information necessary to process payments, not cost proposals and negotiated indirect rates."),
   ("It is arguably CUI under General Procurement and Acquisition, and at minimum is not settled",True,"PROCURE covers cost or pricing data, contract information, indirect costs, and direct labour rates on its face, and it is Specified. This is the item classified too low &mdash; the direction that costs money, because the contracts folder has been handled at the FCI standard."),
   ("It is CUI under Source Selection",False,"Source Selection covers pre-award proposal evaluation material held by the Government. Close, and not this."),
   ("It cannot be CUI because the contractor generated it",False,"Contractor-generated information is squarely inside both the CUI definition and the covered defense information definition."),
  ]),
  dict(stem="What does a banner marking of CUI//SP-CTI indicate?", opts=[
   ("The information is classified at a low level",False,"CUI is unclassified. Nothing about a CUI marking implies classification."),
   ("A CUI Specified category, whose authority sets handling controls beyond the CUI Basic baseline",True,"The SP- prefix denotes Specified. Note that some categories are Specified under one authority and Basic under another, which is why you read the category page rather than memorizing a list."),
   ("Special permission is required to access the information",False,"No clearance or special permission regime attaches to CUI as such; lawful government purpose and any limited dissemination controls govern access."),
   ("The information is subject to a DoD-only control",False,"Specified is a government-wide construct, not a DoD one."),
  ]),
  dict(stem="An assessor finds CUI in a contractor's SharePoint carrying no CUI markings at all. What follows?", opts=[
   ("Nothing &mdash; unmarked information is not CUI",False,"The obligation attaches to the information, not to the marking. This is the defence contractors reach for and it has never worked."),
   ("The contractor must mark it as CUI on its own authority",False,"A contractor applies required markings when it creates documents from CUI it holds. It does not designate, and marking something does not settle its status."),
   ("The information is still CUI, and the absence of marking may itself be a finding",True,"Government offices fail to mark; material gets extracted from marked documents; information is generated during performance and nobody thinks about it. 252.204-7012 also reaches information \"otherwise identified in the contract.\""),
   ("The assessor should ask the contractor to decontrol it",False,"Only the designating agency can decontrol CUI, and an assessor asking for anything to be changed has stopped assessing."),
  ]),
  dict(stem="ClearPath maintains Meridian's PLM, which holds CUI, with standing remote VPN access under a master services agreement containing no security terms. Under DFARS 252.204-7012, what is missing?", opts=[
   ("Nothing &mdash; ClearPath is a vendor, not a subcontractor",False,"Paragraph (m) turns on whether performance will involve covered defense information, not on what the parties call the relationship."),
   ("The clause must be flowed down under paragraph (m)",True,"Performance plainly involves CDI &mdash; the PLM holds it and ClearPath has standing access. The clause must be included without alteration except to identify the parties. There is also a separate maintenance requirement at MA.L2-3.7.5 for nonlocal maintenance sessions."),
   ("A FedRAMP Moderate authorization for ClearPath",False,"FedRAMP applies to cloud service providers. ClearPath is a non-cloud external service provider, which is a different rule with different consequences &mdash; you will separate the two on Day 3."),
   ("Nothing, provided Meridian monitors the sessions",False,"Monitoring would address a different requirement. It does not discharge the flowdown obligation, and in any event Meridian does not monitor them."),
  ]),
 ],
)
