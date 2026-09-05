# -*- coding: utf-8 -*-
"""Manuscript source — Lessons 3, 4."""

L3 = dict(
 file="lesson03.html", short="L3 — Ethics, Independence & Planning", num_label="Lesson 3",
 eyebrow="Day 2 &middot; Afternoon &middot; CAP Phase 1 &middot; CCP Domains 2 &amp; 5",
 title="Ethics, Independence, and Assessment Planning",
 lead=("This is where you stop being a practitioner. An assessor who is excellent at evaluating controls and "
       "careless about independence is worse than useless &mdash; the finding is unreliable, the certificate is "
       "unsafe, and the whole verification regime is worth less for their having participated in it. Most people "
       "find this the hardest session, and not because the material is difficult."),
 chips=["Day 2 &mdash; PM","~3 hours","<strong>CCP 5% + 25%</strong>","Tool: Engagement &amp; Ethics Gate"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Apply","Apply the eight guiding principles of the CMMC Code of Professional Conduct as decision rules to concrete engagement situations, rather than recite them."),
  ("Identify","Identify conflicts of interest and impartiality threats, and distinguish those that can be mitigated from those that must be avoided."),
  ("State","State the three-year consulting prohibition accurately &mdash; what it covers, what it does not, and who it binds."),
  ("Execute","Execute the CAP preliminary proceedings and Phase 1 activities: framing, conflict management, scope validation, evidence confirmation, team composition, and the readiness determination."),
  ("Produce","Produce a defensible assessment plan with an independence declaration &mdash; including, where warranted, a determination that the engagement may not proceed."),
 ],
 vocab=[
  ("CoPC","CMMC Code of Professional Conduct v2.0. Article II carries the eight guiding principles; the practices beneath each are the operative text. Article III covers conflicts of interest."),
  ("Preliminary proceedings","The CAP activities that occur <em>before</em> Phase 1, including conflict identification and contract execution. Two of them decide whether there will be an assessment at all."),
  ("CAP Phase 1","Conduct the Pre-Assessment. Asks one question: is this organization ready to be assessed? Concludes on successful upload of the Pre-Assessment Form to CMMC eMASS."),
  ("Three-year bar","32 CFR 170.8(b)(17)(ii)(G), carried into CoPC 2.2(d). Prohibits participating in the Level 2 certification process where you consulted to prepare the organization for any CMMC assessment within three years."),
  ("Impartiality","The CoPC principle requiring freedom from undue commercial, personal, financial, or other pressure. The core of what makes a certificate mean anything."),
  ("Mitigate vs avoid","Some conflicts can be managed by removing a person from the team. Some have no available mitigation and require the C3PAO to decline the engagement entirely."),
  ("Lead CCA","The credentialed individual who validates scope, determines readiness, runs the in-brief, and owns the determination. Several CAP activities are assigned specifically to this role."),
  ("Pre-Assessment Form","CAGE code, SSP title, contacts, team, dates, readiness determination. Reviewed by a C3PAO quality assurance individual and uploaded to CMMC eMASS. Not shared outside the engagement."),
  ("Adverse readiness determination","A legitimate Phase 1 outcome. The Lead CCA may find the OSC not sufficiently prepared &mdash; and no one affiliated with the C3PAO may then help it get ready."),
  ("Customer Responsibility Matrix","The document allocating security responsibilities between an OSC and an External Service Provider. Required where an ESP is in scope."),
 ],
 sections=[
  dict(title="The shift, stated plainly", html="""
<p>For two sessions you have been learning what the requirements are. Now your judgment about them has consequences
for another company.</p>
<p>That change carries obligations with nothing to do with technical skill. If you currently work as a consultant,
some of what you do routinely is prohibited to you as an assessor, and it is better to confront that now than to
discover it mid-engagement.</p>
<div class="in-practice"><div class="ip-label">The distinction to carry into every remaining session</div>
<p>A consultant is paid to make an organization better. An assessor is paid to say accurately what is true about
it. Those are different jobs, and doing the first inside the second destroys the value of both.</p></div>"""),
  dict(title="The eight principles, as decision rules", html="""
<p>The CoPC lists eight guiding principles in Article II, each with practices beneath it. The practices are the
operative text. Learn the principles as questions you ask yourself, not as a list you recite.</p>
<div class="tw"><table>
<thead><tr><th>Principle</th><th>The question it asks</th></tr></thead>
<tbody>
<tr><td><strong>Professionalism</strong></td><td>Am I representing myself, my credentials, and my services accurately &mdash; and refraining from guarantees, low-balling, and disparagement?</td></tr>
<tr><td><strong>Impartiality</strong></td><td>Is there anything about my relationships, interests, or history that could compromise this determination, or reasonably appear to?</td></tr>
<tr><td><strong>Confidentiality</strong></td><td>Is this information leaving a boundary it was entrusted to me inside?</td></tr>
<tr><td><strong>Information Integrity</strong></td><td>Is what I am recording accurate, complete, and traceable to evidence?</td></tr>
<tr><td><strong>Lawful and Ethical Behavior</strong></td><td>Does this comply with the law and the regulation, and not merely with the contract?</td></tr>
<tr><td><strong>Equal Opportunity</strong></td><td>Am I applying the same standard I would apply to a larger, smaller, friendlier, or more difficult OSC?</td></tr>
<tr><td><strong>Proper Use of CMMC Methods</strong></td><td>Am I staying inside my role and using approved methods and materials &mdash; a CCP not encroaching on a CCA's responsibilities, for instance?</td></tr>
<tr><td><strong>Proper Use of Technology and AI</strong></td><td>Is a tool making a determination that is mine to make &mdash; and is customer data leaving the boundary to reach that tool?</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>CoPC content is only about 5% of the CCP exam and produces a disproportionate share of the failures, precisely
because candidates assume ethics is intuition and skip the document. &ldquo;Impartiality&rdquo; alone is not a
citation; &sect;2.2(g) is.</p></div>"""),
  dict(title="Impartiality and the three-year bar", html="""
<p>Impartiality carries the most operative detail and ends the most careers. The CoPC is blunt about why: the
ecosystem must operate free of undue commercial, personal, financial, or other pressures, because impartiality is
the core of what makes a certificate mean anything.</p>
<div class="warnbox"><div class="warn-label">State the prohibition precisely</div>
<p>32 CFR &sect;170.8(b)(17)(ii)(G), carried into CoPC &sect;2.2(d), prohibits ecosystem members from participating
in the Level 2 certification process for an assessment in which they previously served as a consultant to prepare
the organization for <strong>any type</strong> of CMMC assessment within <strong>three years</strong>.</p></div>
<div class="tw"><table>
<thead><tr><th>It does cover</th><th>It does not say</th></tr></thead>
<tbody>
<tr><td>Preparatory, advisory, or consulting activity of any kind, for any type of CMMC assessment</td>
<td>That every prior relationship with an OSC is barred for three years</td></tr>
<tr><td>Consulting for a Level 1 self-assessment two years ago, which bars you from a Level 2 certification assessment today</td>
<td>That the bar is the only conflict rule &mdash; most conflicts arise from other relationships entirely</td></tr>
<tr><td>The C3PAO as an organization, not only the individual assessors</td>
<td>That being clear of the three-year bar means you are clear to proceed</td></tr>
<tr><td>Supplying templates, workbooks, or tools that guide implementation &mdash; this is advisory activity</td>
<td>That you get to decide your own eligibility</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">The rule underneath the rule</div>
<p>The <strong>C3PAO</strong> owns impartiality and conflict management. The CAP says so twice, and says the
responsibility cannot be delegated to the assessment team or to the OSC. Your obligation is to disclose, in
writing, as soon as a conflict is known or reasonably should be known. The decision about whether it can be
mitigated is not yours. Assessors get into trouble far more often for deciding a conflict was fine than for having
one.</p></div>
<h3>Mitigate or avoid</h3>
<p>Some conflicts can be managed; some cannot. The CoPC's own worked examples set the pattern: a family
relationship is mitigated by removing the assessor from the team, while a C3PAO assessing an environment shaped by
its own products has no available mitigation and must decline entirely. If the conflict cannot be sufficiently
mitigated, the C3PAO does not proceed.</p>"""),
  dict(title="What happens before Phase 1", html="""
<p>An assessment does not begin with Phase 1. The CAP places preliminary proceedings ahead of it, and two of them
decide whether there will be an assessment at all.</p>
<div class="tw"><table>
<thead><tr><th>Preliminary activity</th><th>What it settles</th></tr></thead>
<tbody>
<tr><td><strong>Receive the assessment request</strong></td><td>The OSC approaches an authorized or accredited C3PAO listed in the Marketplace. Neither the Cyber AB, the CAICO, nor DoD may recommend or introduce a C3PAO.</td></tr>
<tr><td><strong>Confirm the entity</strong></td><td>The precise legal entity and the CAGE code or codes. A certification attaches to an identified information system owned and operated by an identified OSC. No CAGE code, no assessment.</td></tr>
<tr><td><strong>Frame the assessment</strong></td><td>Schedule, size, personnel, logistics, contractual requirements, and the prospective scope, worked out with the Affirming Official or OSC point of contact.</td></tr>
<tr><td><strong>Identify and manage conflicts</strong></td><td>The C3PAO proposes the Lead CCA and coordinates with the OSC to establish whether conflicts exist. Documented mitigation plan required; where a conflict cannot be sufficiently mitigated, the C3PAO does not proceed.</td></tr>
<tr><td><strong>Execute the contractual agreement</strong></td><td>A written contract and a mutual NDA. The contract may not include guarantees, promises of outcome, or any incentive or bonus contingent on a certificate being issued.</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">Two things students routinely get backwards</div>
<p>Conflicts are managed <strong>before</strong> Phase 1, not during it &mdash; and the responsibility sits with the
C3PAO, which cannot delegate it to the assessment team or to the OSC.</p>
<p>A contract that pays a bonus on certification, or refunds a fee if certification is not achieved, is prohibited.
If you see one in an engagement letter, that is a finding about the C3PAO, not a commercial detail.</p></div>"""),
  dict(title="Phase 1: Conduct the Pre-Assessment", html="""
<p>Phase 1 asks one question: is this organization ready to be assessed? Not whether it will pass &mdash; the CAP is
explicit that the team may not speculate about or intimate a likely outcome. Only whether the evaluative work of
Phase 2 can sensibly begin.</p>
<div class="tw"><table>
<thead><tr><th>Phase 1 activity</th><th>What it involves</th></tr></thead>
<tbody>
<tr><td><strong>Review the SSP</strong></td><td>A cursory review for completeness, accuracy, and consistency &mdash; enough to form a reasonable expectation that the requirements have been addressed. Not an evaluation of adequacy or sufficiency; that is Phase 2.</td></tr>
<tr><td><strong>Validate the scope</strong></td><td>The Lead CCA validates scope under 32 CFR &sect;170.19(c). Disagreements about scope must be resolved before Phase 2 may begin.</td></tr>
<tr><td><strong>Address ESPs</strong></td><td>Confirm a Customer Responsibility Matrix will be available and that ESP personnel will participate. If the ESP handles CUI, confirm the OSC can produce FedRAMP Moderate authorization, documented equivalency, or a Level 2 certificate.</td></tr>
<tr><td><strong>Confirm evidence availability</strong></td><td>Satisfy yourself that enough evidence and enough people will actually be accessible to support accurate determinations.</td></tr>
<tr><td><strong>Determine readiness</strong></td><td>The Lead CCA makes the call and conveys which assessment methods will be used, at a depth and coverage drawn from NIST SP 800-171A and SP 800-53A.</td></tr>
<tr><td><strong>Compose the team</strong></td><td>The C3PAO composes the team under 32 CFR &sect;170.11(b)(10) and ISO/IEC 17020 personnel procedures, proposes names to the OSC, and manages conflicts before Phase 2 begins.</td></tr>
<tr><td><strong>Complete the Pre-Assessment Form</strong></td><td>CAGE code, SSP title, contacts, team, dates, readiness determination. Not shared outside the engagement.</td></tr>
<tr><td><strong>QA review, then upload</strong></td><td>A C3PAO quality assurance individual reviews the form and uploads it into CMMC eMASS. <strong>Phase 1 concludes on that successful upload &mdash; not on a meeting.</strong></td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">And if the OSC is not ready</div>
<p>The Lead CCA may determine that it is not. That is a legitimate Phase 1 outcome and the paperwork is still
completed. Under no circumstances does the C3PAO, the team, or anyone affiliated with it then help the OSC get
ready &mdash; the consulting bar arriving at the moment it is hardest to honour.</p></div>"""),
  dict(title="Applied: the Meridian engagement", html="""
<p>Marcus Ellison contacted <strong>Tidewater Assurance Group, LLC</strong> directly, requesting a Level 2
certification assessment. The AMCOM recompete is 18 months out and the company has never submitted an SPRS score.
Fieldwork requested within 120 days; she has asked twice whether it can be sooner.</p>
<div class="tw"><table>
<thead><tr><th>Why the engagement looks straightforward</th><th>What Phase 1 actually finds</th></tr></thead>
<tbody>
<tr><td>There is a CISO who owns the SSP, the policies and the POA&amp;M</td><td>She keeps the POA&amp;M in a personal OneDrive outside the authorised CUI boundary, and it has not been AO-reviewed in 18 months.</td></tr>
<tr><td>A System Security Plan exists &mdash; version 2.1</td><td>Dated October 2023 and marked &ldquo;needs update&rdquo; in the company's own register. It does not describe the MSP relationship, two CUI-handling suppliers, or the data flow into AWS GovCloud.</td></tr>
<tr><td>Ten written policies, four of them current</td><td>The Incident Response Plan is three years stale and names a departed employee. Media Protection is four years stale. The Contingency Plan has been a 0.9 draft since it was written.</td></tr>
<tr><td>A network diagram exists, and it is accurate</td><td>It accurately depicts three subnets routing freely through one switch with no VLAN enforcement. The diagram is not the problem; what it shows is.</td></tr>
<tr><td>Eight gaps are already documented and rated</td><td>Documented by whom &mdash; and what does that do to this engagement?</td></tr>
<tr><td>Cloud is done properly &mdash; GCC High and AWS GovCloud, both FedRAMP High</td><td>And the GCC High tenant excludes its most privileged account from the MFA policy. The procurement decision was right; the configuration was never finished.</td></tr>
<tr><td>147 people, one domain, two sites &mdash; a manageable environment</td><td><strong>No asset inventory exists.</strong> Scope cannot be validated against a list of assets that has never been written.</td></tr>
</tbody></table></div>
<h3>The readiness question is genuinely close</h3>
<p>Meridian is a harder Phase 1 than a company with nothing, and harder in the direction that matters. The artifacts
the CAP requires Phase 1 to review mostly <em>exist</em>. An SSP can be reviewed for completeness, accuracy and
consistency. Policies can be read. A network diagram can be examined. On a checklist reading, this company is
ready.</p>
<p>Phase 1 asks whether the evaluative work of Phase 2 can sensibly begin, and the answer turns on one thing the
checklist has no line for. <strong>Scope cannot be validated under 32 CFR &sect;170.19(c), because no asset
inventory exists.</strong> The Lead CCA is required to validate scope; scope disagreements must be resolved before
Phase 2 may begin; and there is no enumeration of assets against which to do either.</p>
<p>An assessor who reaches &ldquo;not ready&rdquo; here has to earn it with a specific reason rather than a general
impression of disorder &mdash; which is exactly the discipline the determination demands.</p>
<h3>The proposed team</h3>
<ul>
<li><strong>Dana Whitfield</strong> &mdash; proposed Lead CCA. Eleven Level 2 assessments as Lead. No prior
relationship with Meridian; did not participate in the gap assessment.</li>
<li><strong>Marcus Reyes</strong> &mdash; CCA. Employed by Meridian 2019&ndash;2022, where he built the Active
Directory group structure and the file server permission model <em>still in use, including on the /CUI tree</em>.
Participated in the gap assessment.</li>
<li><strong>Priya Raghunathan</strong> &mdash; CCP. Two years alongside Meridian's IT Manager on their local
professional association chapter board; they see each other monthly. Participated in the gap assessment.</li>
<li><strong>Thomas Blalock</strong> &mdash; CCA. Holds roughly $30,000 of stock in Cardinal Industrial Group, the
parent company of ClearPath IT Solutions, the vendor with standing remote access to Meridian's PLM. Disclosed on joining.</li>
<li><strong>Nadia Farhat</strong> &mdash; quality assurance. Not on the team; reviews and uploads the Pre-Assessment
Form.</li>
</ul>
<h3>The engagement letter</h3>
<p>Two terms are worth reading twice. An <strong>outcome provision</strong>: &ldquo;In the event a Certificate of
CMMC Status is not issued, thirty percent of the fee shall be credited against a subsequent assessment.&rdquo; And
a <strong>support provision</strong>: &ldquo;Tidewater will make its assessors available to answer implementation
questions arising from the assessment for a period of 60 days following the out-brief.&rdquo;</p>
<div class="warnbox"><div class="warn-label">And then the part that tests you</div>
<p>Ellison has asked whether Tidewater can &ldquo;take a pass at the inventory and tidy up the SSP first, so we are
not wasting your people's time.&rdquo; It is a reasonable-sounding request from a company that has genuinely tried
and is short of one artifact. Being able to say why the answer is no &mdash; without being prompted, and without
lecturing him &mdash; is what this session has been building toward.</p></div>"""),
 ],
 case=dict(tag="Meridian &middot; Day 2 Afternoon &middot; Deliverable D3",
   title="Rule on the engagement, then plan it",
   html="""
<p>You are now Tidewater. The <strong>Engagement &amp; Ethics Gate</strong> puts the packet in front of you and
asks the question Phase 1 exists to answer &mdash; twice.</p>
<p><strong>First:</strong> may this engagement proceed at all? Work every conflict in the packet individually.
For each: name the principle and the specific practice, decide <em>disclose</em>, <em>mitigate</em>, or
<em>avoid</em>, and say who decides. Some are in the team biographies. At least one is not.</p>
<p><strong>Then:</strong> on the stated assumption that a conflict-free team and organization have been
substituted, build the plan &mdash; engagement scope, team composition, independence declaration, evidence request
approach, interview schedule, and readiness risks.</p>
<p>The tool also runs the eight ethics scenarios, from the former employer through the drafted finding produced by
a public AI assistant, and adjudicates each against the text.</p>
<p><strong>No remediation advice anywhere</strong>, including in the readiness risks. Naming a risk is assessment;
naming its fix is consulting. And a plan that quietly ignores a disqualifying conflict in order to have something
to plan is the exact failure this session exists to prevent.</p>""",
   actions=[("Open the Engagement &amp; Ethics Gate &rarr;","ethics-gate.html",False),
            ("Case workbench","meridian.html",True)]),
 kc=[
  dict(stem="Marcus Reyes worked at Meridian from 2019 to 2022 building the file server permission model still in use, and participated in Tidewater's gap assessment ten months ago. What is the correct disposition?", opts=[
   ("Disclose and proceed &mdash; he left on good terms",False,"Good terms are irrelevant. Two separate problems exist here, and neither is addressed by disclosure alone."),
   ("Mitigate by having another assessor review his determinations",False,"Peer review does not cure either problem. He would still be assessing a control environment he personally built, and he still participated in the prior advisory engagement."),
   ("Avoid &mdash; remove him from the team",True,"He would be assessing his own work, and he participated in an engagement that produced a Recommended Remediation Sequence. Both are impartiality failures; the second engages the three-year bar. Removal is the available mitigation for the individual, and the C3PAO decides."),
   ("No conflict &mdash; the gap assessment was non-certification work",False,"The bar covers preparatory or advisory activity for any type of CMMC assessment. Calling it non-certification does not remove it from scope."),
  ]),
  dict(stem="The engagement letter provides that 30% of the fee is credited against a future assessment if no certificate issues. What is this?", opts=[
   ("A normal commercial risk-sharing term",False,"It is a prohibited outcome-contingent term, and reading it as ordinary commerce is exactly how it survives review."),
   ("A prohibited term &mdash; a financial interest contingent on the outcome",True,"The contract may not include guarantees, promises of outcome, or any incentive or bonus contingent on a certificate being issued. If you see one in an engagement letter, that is a finding about the C3PAO."),
   ("Acceptable if disclosed to the OSC",False,"The OSC is party to the contract; it already knows. Disclosure does not cure a term that creates a financial stake in the determination."),
   ("Acceptable because it penalises rather than rewards certification",False,"It rewards certification: the firm keeps the full fee only if the certificate issues. That is a financial interest in the outcome."),
  ]),
  dict(stem="Tidewater's prior gap assessment report included Appendix C, a \"Recommended Remediation Sequence\" with suggested tooling and cost estimates. What is the consequence for this engagement?", opts=[
   ("None &mdash; a gap assessment is not a CMMC assessment",False,"The activity, not the label, governs. Recommending a remediation sequence with tooling is advisory work to prepare the organization."),
   ("It engages the three-year bar at the organizational level",True,"The bar binds the C3PAO as an organization, not only individual assessors. Tidewater consulted to prepare Meridian within three years, and Meridian built its POA&M directly from that report."),
   ("It is cured by using assessors who did not write the report",False,"Substituting personnel addresses the individual conflicts. It does not address a firm-level bar."),
   ("It is acceptable if Tidewater discloses it in the Pre-Assessment Form",False,"Disclosure is necessary and not sufficient. Where a conflict cannot be sufficiently mitigated, the C3PAO does not proceed."),
  ]),
  dict(stem="Who decides whether an identified conflict can be sufficiently mitigated?", opts=[
   ("The individual assessor concerned",False,"Nobody decides their own eligibility. Assessors get into trouble far more often for deciding a conflict was fine than for having one."),
   ("The OSC, since it bears the consequence",False,"The OSC is coordinated with, and it does not hold the decision. Its commercial interest is precisely why it cannot."),
   ("The C3PAO",True,"The C3PAO owns impartiality and conflict management, and the CAP states that the responsibility cannot be delegated to the assessment team or to the OSC."),
   ("The Cyber AB",False,"The Cyber AB accredits C3PAOs and would review conduct after the fact. It does not adjudicate individual engagement conflicts in advance."),
  ]),
  dict(stem="Meridian has an SSP v2.1, ten written policies and an accurate network diagram, but no asset inventory. What does Phase 1 conclude?", opts=[
   ("Ready &mdash; the artifacts Phase 1 reviews all exist",False,"The checklist reading, and it misses what Phase 1 is for. An SSP that can be reviewed is necessary and not sufficient."),
   ("Not ready &mdash; scope cannot be validated under §170.19(c) without an enumeration of assets",True,"The Lead CCA must validate scope, and scope disagreements must be resolved before Phase 2 may begin. Neither is possible against a list that has never been written. This is a harder call than a company with nothing, and it turns on one specific absence rather than a general impression of disorder."),
   ("Not ready &mdash; the SSP is marked \"needs update\"",False,"Closer, and it is a Phase 2 problem rather than a Phase 1 one. Phase 1's SSP review is cursory: completeness, accuracy and consistency, not currency of every control description."),
   ("Ready, provided the OSC produces an inventory during Phase 2",False,"Scope validation is a Phase 1 activity and disagreements must be resolved before Phase 2 begins. Deferring it inverts the process."),
  ]),
  dict(stem="When does CAP Phase 1 conclude?", opts=[
   ("At the Phase 1 closing meeting with the OSC",False,"A meeting is not the trigger. This is a favourite exam distinction because it feels like it should be."),
   ("When the Lead CCA signs the readiness determination",False,"The determination is one activity within Phase 1, not its conclusion."),
   ("On successful upload of the quality-reviewed Pre-Assessment Form into CMMC eMASS",True,"A C3PAO quality assurance individual reviews the form and uploads it. Phase 1 concludes on that upload."),
   ("When the OSC countersigns the assessment plan",False,"The OSC is not the gatekeeper of phase completion."),
  ]),
  dict(stem="An assessment team member pastes SSP paragraphs and an access-control screenshot into a public AI assistant to draft finding language, edits the output, and enters it as their determination. What is the disposition?", opts=[
   ("Acceptable &mdash; the assessor reviewed and edited the output",False,"Editing addresses neither breach. The data has already left the boundary and the reasoning did not originate with the assessor."),
   ("A Confidentiality breach only",False,"Confidentiality is engaged, and so is Proper Use of Technology and AI &mdash; a tool produced reasoning that is the credentialed assessor's to produce. Information Integrity is arguably a third."),
   ("Breaches of Confidentiality and Proper Use of Technology and AI, reportable to the C3PAO",True,"Engagement-confidential information describing how to attack the OSC left the boundary, and a determination was outsourced. Disclose to the C3PAO; the disposition is not the assessor's to decide."),
   ("Acceptable if the AI provider offers a no-training guarantee",False,"A vendor's data-handling terms do not make the disclosure authorised by the OSC, and they say nothing at all about who rendered the determination."),
  ]),
  dict(stem="Priya Raghunathan has served two years on a professional association chapter board with Meridian's IT Manager, seeing him monthly. No financial or family relationship exists. What is the best response?", opts=[
   ("No conflict &mdash; professional association service is not a relationship of interest",False,"An ongoing personal relationship with a key interviewee is exactly the kind of thing that could reasonably appear to compromise impartiality."),
   ("Disclose in writing; the C3PAO determines whether it can be mitigated",True,"The test is whether something could compromise the determination <em>or reasonably appear to</em>. Disclosure is the assessor's obligation; disposition is the C3PAO's decision. Note she also participated in the gap assessment, which is the more serious problem."),
   ("Avoid &mdash; any social relationship is disqualifying",False,"Overcorrecting is its own error. Not every relationship is unmitigable, and the CoPC contemplates mitigation by removal where warranted."),
   ("Mitigate by having her avoid interviewing the IT Manager",False,"Plausible on its face, and it addresses only the narrowest version of the problem. The decision is not hers to make in any event."),
  ]),
  dict(stem="Thomas Blalock holds $30,000 of stock in the parent company of ClearPath, the vendor with standing remote access to Meridian's PLM. He disclosed it when he joined Tidewater. What now?", opts=[
   ("Nothing further &mdash; he already disclosed it",False,"A general disclosure on joining is not disclosure of a conflict in this engagement. The relationship only becomes a conflict when ClearPath appears in an assessment, and it has."),
   ("It must be disclosed for this engagement and dispositioned by the C3PAO",True,"ClearPath is an ESP evaluated inside this assessment. A financial interest in its parent is a live impartiality threat, and the obligation is to disclose as soon as it is known or reasonably should be known."),
   ("No conflict &mdash; his interest is in the parent, not ClearPath",False,"An interest in the parent is an interest in the subsidiary's performance. Formal corporate separation does not neutralise the incentive."),
   ("He may serve provided he does not assess the ClearPath relationship",False,"Carving out part of the scope is not a disposition the assessor may choose, and the C3PAO decides whether any mitigation suffices."),
  ]),
  dict(stem="In the readiness risks section of an assessment plan, which sentence is permissible?", opts=[
   ("\"Meridian should implement MFA on the PLM before fieldwork begins.\"",False,"A direct instruction. Naming the fix is consulting, and it is still consulting when it appears in a risk register."),
   ("\"We recommend engaging an RPO to prepare the SSP.\"",False,"Worse &mdash; it is remediation advice plus a referral, and the referral has its own CoPC exposure."),
   ("\"No System Security Plan exists; Phase 1 cannot review the artifact the CAP requires.\"",True,"States what is true and what follows procedurally. It names a risk without naming a fix. That an OSC could act on it is fine &mdash; you never told them what to do."),
   ("\"The environment is close to ready; a few weeks of work should suffice.\"",False,"Two failures: it speculates about outcome, which the CAP prohibits, and it implies a remediation timeline."),
  ]),
 ],
)

L4 = dict(
 file="lesson04.html", short="L4 — Scoping & Asset Categorization", num_label="Lesson 4",
 eyebrow="Day 3 &middot; Morning &middot; CCA Domain 2 (20%) &middot; CCP Scoping (15%)",
 title="Scoping and Asset Categorization",
 lead=("The highest-leverage decision an assessor makes. Everything downstream inherits it: the evidence you "
       "request, the interviews you schedule, the requirements you evaluate, the score you compute, and the "
       "findings you can defend. It is also where the pressure lives &mdash; scope is the one part of an "
       "assessment an organization has a direct financial interest in shrinking."),
 chips=["Day 3 &mdash; AM","~3 hours","<strong>CCA 20%</strong>","Tool: Scope &amp; Asset Matrix"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Categorize","Categorize every asset in an environment into the five CMMC Level 2 asset categories and justify each against the defining test."),
  ("Apply","Apply the two conditional categories &mdash; Contractor Risk Managed Assets and Specialized Assets &mdash; including the conditions each depends on."),
  ("State","State the assessment boundary and document what places each asset inside or outside it."),
  ("Analyse","Analyse External Service Provider relationships under 32 CFR &sect;170.19, distinguish an ESP from a Cloud Service Provider, and say when a Customer Responsibility Matrix is required and when FedRAMP Moderate or documented equivalency is triggered."),
  ("Trace","Trace flowdown obligations to subcontractors and suppliers."),
 ],
 vocab=[
  ("CUI Asset","An asset that processes, stores, or transmits CUI. Documented in the asset inventory and the SSP; assessed against all Level 2 requirements."),
  ("Security Protection Asset","Provides security functions or capabilities to the assessment scope, whether or not it touches CUI. Assessed against the requirements relevant to the function it provides."),
  ("Contractor Risk Managed Asset","Can, but is not intended to, process, store, or transmit CUI <em>because of security policy, procedures, and practices in place</em>. Conditional. SSP review primarily."),
  ("Specialized Asset","Can process, store, or transmit CUI but is unable to be fully secured. Closed list: IoT, IIoT, OT, Government Furnished Equipment, Restricted Information Systems, Test Equipment. Conditional."),
  ("Out-of-Scope Asset","Cannot process, store, or transmit CUI and provides no security protection for CUI Assets. The contractor must be prepared to justify the inability."),
  ("External Service Provider","A non-cloud provider that processes, stores, or transmits CUI, or handles Security Protection Data. Evaluated inside the OSC's assessment; a Customer Responsibility Matrix is required."),
  ("Cloud Service Provider","A provider that processes, stores, or transmits CUI via cloud services. Triggers FedRAMP Moderate authorization or documented equivalency under DFARS 252.204-7012."),
  ("Security Protection Data","Data used to protect the assessment scope &mdash; configuration, log, and administrative data. A provider handling it falls inside the ESP rule even without touching CUI."),
  ("Assessment boundary","The stated line around what will and will not be assessed. Named systems, with the basis for each. \"The network\" is not a boundary."),
 ],
 sections=[
  dict(title="Where this sits in the Meridian story", html="""
<p>Day 2 ended with a determination that Meridian was not ready and that the C3PAO could not proceed. That was
the correct outcome and it stands.</p>
<p>Today and tomorrow are not that assessment. They are the work that makes you capable of conducting one: scoping
an environment, planning what evidence would prove what, and rendering determinations against it. You are building
instruments and judgment on a company you now know well. Day 5 morning is where an assessment actually runs
&mdash; eight months later, against a Meridian that has had time to do the work.</p>"""),
  dict(title="The five categories", html="""
<p>Each category answers one question: <strong>what does this asset do with CUI?</strong> Everything else follows.</p>
<div class="tw"><table>
<thead><tr><th>Category</th><th>The defining test</th><th>What the contractor must do</th><th>How it is assessed</th></tr></thead>
<tbody>
<tr><td><strong>CUI Assets</strong></td><td>Processes, stores, or transmits CUI</td><td>Asset inventory; SSP</td><td>Against all Level 2 security requirements</td></tr>
<tr><td><strong>Security Protection Assets</strong></td><td>Provides security functions or capabilities to the assessment scope, whether or not it touches CUI</td><td>Inventory; SSP; network diagram</td><td>Against the requirements relevant to the security function provided</td></tr>
<tr><td><strong>Contractor Risk Managed Assets</strong></td><td>Can, but is not intended to, process, store, or transmit CUI <em>because of security policy, procedures, and practices in place</em></td><td>Inventory; SSP; network diagram</td><td>SSP review primarily; further checks if documentation raises concerns</td></tr>
<tr><td><strong>Specialized Assets</strong></td><td>Can process, store, or transmit CUI but is unable to be fully secured</td><td>Inventory; SSP; network diagram; demonstrate management through risk-based security policies</td><td>SSP review only; not assessed against the other requirements</td></tr>
<tr><td><strong>Out-of-Scope Assets</strong></td><td>Cannot process, store, or transmit CUI, and provides no security protection for CUI Assets</td><td>Be prepared to justify the inability</td><td>Not assessed</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">Specialized Assets are a closed list</div>
<p>Internet of Things and Industrial Internet of Things devices, Operational Technology, Government Furnished
Equipment, Restricted Information Systems, and Test Equipment. That is the list. An asset that is inconvenient to
secure, old, or owned by somebody else does not become a Specialized Asset because it would be helpful if it were.</p></div>
<div class="tip"><div class="tip-label">The condition that decides most of this session</div>
<p>Read the Contractor Risk Managed test again: can, but is not intended to, handle CUI &mdash; <em>because of
security policy, procedures, and practices in place</em>. The relief depends on those existing.</p>
<p>Now read the Specialized Asset obligation: documented in the inventory and the SSP, shown on the network
diagram, and <em>demonstrably managed through risk-based security policies</em>.</p>
<p><strong>Both categories are earned, not claimed.</strong> And note how little it takes to lose them. Meridian
has an SSP, ten policies and an accurate network diagram &mdash; it fails the condition on one artifact, the asset
inventory, which does not exist. One missing document closes both categories to every asset in the environment.</p>
<p>That is a more instructive failure than a company with nothing, because it is the one you will actually meet:
organisations that have done most of the work and cannot claim the relief because of the piece they skipped.</p></div>"""),
  dict(title="External Service Providers and Cloud Service Providers", html="""
<p>Most organizations of any size have handed part of their environment to somebody else. The regulation treats
that in two different ways depending on what the provider is.</p>
<div class="tw"><table>
<thead><tr><th></th><th>External Service Provider (non-cloud)</th><th>Cloud Service Provider</th></tr></thead>
<tbody>
<tr><td><strong>What triggers the rule</strong></td><td>The ESP processes, stores, or transmits CUI, or handles Security Protection Data</td><td>The CSP processes, stores, or transmits CUI</td></tr>
<tr><td><strong>What is required</strong></td><td>The relationship, services, and responsibility matrix documented in the SSP. A Customer Responsibility Matrix is required.</td><td>FedRAMP Moderate authorization, or documented equivalency, under DFARS 252.204-7012</td></tr>
<tr><td><strong>Effect on the assessment</strong></td><td>The ESP is evaluated inside the OSC's assessment. Its personnel are expected to participate.</td><td>The authorization or equivalency is evidence the OSC must produce. The assessment does not evaluate the cloud service itself.</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">Two answers, not one</div>
<p>Categorizing a provider and stating its obligation are separate steps, and teams routinely collapse them and
answer neither properly. Microsoft 365 is a <em>CUI Asset</em> by category and a <em>CSP question</em> by
obligation. Both belong in your matrix.</p></div>
<h3>Meridian's providers</h3>
<div class="tw"><table>
<thead><tr><th>Provider</th><th>Service</th><th>Classification</th><th>Obligation, and what exists</th></tr></thead>
<tbody>
<tr><td><strong>ClearPath IT Solutions</strong></td><td>MSP &mdash; remote administration, help desk, firewall administration. Standing domain admin.</td>
<td>ESP (non-cloud) handling CUI <em>and</em> Security Protection Data</td>
<td>SSP documentation and a Customer Responsibility Matrix required; evaluated inside the assessment; personnel expected to participate. <strong>None exists</strong> &mdash; month-to-month, no DFARS flow-down, no right to audit, no background-check verification. Note the separate nonlocal maintenance requirement at MA.L2-3.7.5.</td></tr>
<tr><td><strong>Microsoft &mdash; M365 GCC High</strong></td><td>Email, Teams, SharePoint, OneDrive holding CUI</td>
<td>CSP processing and storing CUI</td>
<td>FedRAMP High &mdash; the baseline obligation is <em>satisfied</em>. What remains is whether the agreement establishes the reporting, preservation and access obligations, and whether the tenant is configured to protect what is in it. It is not: Conditional Access is partial and a shared Global Admin account is excluded from MFA.</td></tr>
<tr><td><strong>AWS GovCloud</strong></td><td>Compute and S3 for SBIR analysis</td><td>CSP processing and storing CUI</td>
<td>FedRAMP High, root MFA enabled, Meridian owns the IAM configuration. The best-run service in the environment &mdash; and the manual upload path into it is still an uncontrolled CUI flow the SSP does not describe.</td></tr>
<tr><td><strong>Acuitas Machining</strong></td><td>Sub-tier machining overflow; receives CUI drawings by SharePoint link</td>
<td>ESP handling CUI &mdash; and a flow-down obligation</td>
<td><strong>No formal agreement at all.</strong> Whether Acuitas is best analysed as a subcontractor requiring flow-down under 252.204-7012(m), an ESP requiring a CRM, or both is genuinely arguable. Say which you chose and why.</td></tr>
<tr><td><strong>AeroComp Composites</strong></td><td>Composite parts; receives 2D drawings by encrypted email</td>
<td>ESP handling CUI</td>
<td>Flow-down referenced in the purchase order and never verified. Ask what evidence shows the clause reached the subcontract and was accepted &mdash; &ldquo;partial&rdquo; flow-down is not a category the regulation recognises.</td></tr>
<tr><td><strong>Secure Shred AL</strong></td><td>Offsite paper shredding for Huntsville; takes custody of hard-copy CUI</td>
<td>ESP handling CUI</td>
<td><strong>The one most teams miss</strong>, because it handles paper rather than data. No NDA, no CUI handling agreement. Contrast Dayton, where shredding is in-house to DIN 66399 P-4 and is compliant &mdash; the same obligation met at one site and not the other.</td></tr>
<tr><td><strong>Whitmore &amp; Associates</strong></td><td>External CPA, read-only QuickBooks</td><td>Neither</td>
<td>No CUI. Say what you checked before concluding it &mdash; and note the company's own third-party register contradicts itself here, which is a records problem rather than a scoping one.</td></tr>
<tr><td><strong>FastenerTech Supply</strong></td><td>Precision hardware components</td><td>Neither</td>
<td>No CUI reaches them. Included so the matrix is not simply a list of failures.</td></tr>
</tbody></table></div>"""),
  dict(title="The contested calls", html="""
<p>Five categorizations at Meridian attract argument every time. Work each against the defining test, not
against what the asset is for.</p>
<div class="tw"><table>
<thead><tr><th>Asset</th><th>The tempting answer</th><th>Why the test says otherwise</th></tr></thead>
<tbody>
<tr><td><strong>The CORP-LAN workstations</strong></td>
<td>Contractor Risk Managed &mdash; no CUI is stored on them by design</td>
<td>The relief requires the asset to be documented in the asset <em>inventory</em>, the SSP, and the network diagram. Meridian has an SSP and a network diagram and <strong>no asset inventory at all</strong>. One missing artifact closes the category. They route freely to SYS-003 and SYS-004 with domain credentials. <strong>CUI Assets.</strong></td></tr>
<tr><td><strong>The Xerox AltaLink C8045</strong></td>
<td>IoT, therefore Specialized</td>
<td>It produces hard-copy CUI from the PLM and the file server, so it processes CUI. The Specialized argument requires the device to be <em>unable to be fully secured</em> &mdash; an enterprise MFP with a management interface generally is securable, which defeats it. Ask separately what it retains on internal storage. <strong>CUI Asset.</strong></td></tr>
<tr><td><strong>The domain controllers</strong></td>
<td>Out of scope &mdash; they hold no CUI</td>
<td>They provide authentication, group policy and access control to the entire scope, including Huntsville over the tunnel. <strong>Security Protection Assets.</strong></td></tr>
<tr><td><strong>The Cisco Catalyst 2960-X</strong></td>
<td>Just plumbing</td>
<td>It carries CORP-LAN, ENG-LAN and MGMT-LAN with no VLAN enforcement, which is the single fact that makes almost nothing scopable out. <strong>Security Protection Asset</strong> &mdash; and the most consequential asset in the environment.</td></tr>
<tr><td><strong>The Huntsville utility closet equipment</strong></td>
<td>Someone else's building, someone else's problem</td>
<td>The Cisco RV345 terminates the IPsec tunnel carrying CUI between the sites. That Meridian does not control the building access system is a serious physical finding, not a reason to scope the device out. <strong>Security Protection Asset.</strong></td></tr>
</tbody></table></div>
<h3>The second site</h3>
<p>Huntsville has six engineering workstations, a Cisco RV345, and a UPS, on an always-on IPsec tunnel back to the
Dayton domain controllers. The workstations authenticate against Dayton AD and reach the same CUI stores. There is
no local IT staff, the site is a commercial office lease, and Meridian does not control the building access system
&mdash; the switch and UPS sit in an unlocked utility closet accessible to building maintenance.</p>
<p>Huntsville is inside the boundary and the six workstations are CUI Assets on the same reasoning as the Dayton
fourteen. The physical exposure is a serious PE finding that does not change the category. A team that also flags
&ldquo;we cannot tell whether the tunnel is the only path between the sites, or whether the Huntsville machines
store CUI locally&rdquo; as open items has done the better piece of work.</p>"""),
  dict(title="Justifications that work", html="""
<p>Every categorization needs a basis that references the defining test rather than restating what the asset is.</p>
<div class="tw"><table>
<thead><tr><th>A justification that works</th><th>A justification that does not</th></tr></thead>
<tbody>
<tr><td>&ldquo;Stores CUI: the /CUI contract folder resides on this volume.&rdquo;</td><td>&ldquo;File server.&rdquo;</td></tr>
<tr><td>&ldquo;Provides the access control boundary for the assessment scope.&rdquo;</td><td>&ldquo;It is a firewall, so it is a security thing.&rdquo;</td></tr>
<tr><td>&ldquo;Can reach the PLM through a browser on the same flat subnet; no policy prevents it.&rdquo;</td><td>&ldquo;Production floor device, not used for CUI.&rdquo;</td></tr>
<tr><td>&ldquo;Cannot reach any CUI asset; on a physically separate circuit with no route to the LAN.&rdquo;</td><td>&ldquo;Nobody uses it for CUI.&rdquo;</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">Build the inventory before you categorize</div>
<p>An inventory built while categorizing becomes an argument. Assets that would be inconvenient to scope in quietly
fail to get listed, and nobody notices, because the list looks complete. List every asset first, recording what it
<em>can reach</em> &mdash; then categorize. It is also how you find the assets the organization forgot to mention.</p></div>"""),
  dict(title="Where scope errors go", html="""
<p>A scoping error does not announce itself. It surfaces on Day 4 as a requirement nobody evaluated, on Day 5 as a
finding that cannot be supported, and in practice as a certificate that covers less than the organization believes
it does.</p>
<div class="warnbox"><div class="warn-label">The asymmetry matters</div>
<p>Scoping an asset <em>in</em> that did not need to be in costs the organization time. Scoping an asset
<em>out</em> that should have been in produces an assessment result that is wrong. Those are not equivalent errors,
and when you are genuinely uncertain, the direction to err is not the comfortable one.</p></div>
<h3>The boundary at Meridian, stated correctly</h3>
<p>Everything at both sites is inside the boundary except Whitmore &amp; Associates and FastenerTech. Two specific
absences put it there: <strong>no enforced segmentation</strong>, so every CORP-LAN machine reaches the CUI stores
on ENG-LAN; and <strong>no asset inventory</strong>, which closes both conditional categories to the entire
environment at once.</p>
<p>Note what makes this different from a company with nothing. Meridian has an SSP, ten policies, and a network
diagram. It still cannot claim the conditional treatments, because the one artifact those treatments depend on is
the one it does not have. Saying that precisely &mdash; rather than &ldquo;they have no documentation&rdquo; &mdash;
is the difference between a Competent and an Assessor-Ready boundary statement.</p>"""),
 ],
 case=dict(tag="Meridian &middot; Day 3 Morning &middot; Deliverable D4",
   title="Categorize every asset and draw the boundary",
   html="""
<p>The <strong>Scope &amp; Asset Matrix tool</strong> loads the Meridian environment asset by asset. For each
one you record what it can reach, assign a category, and write a one-line basis referencing the defining test. The
tool checks each call and tells you why &mdash; including on the five that are genuinely contested.</p>
<p>Then five parts, in order, because the boundary has to follow from the matrix rather than the other way round:</p>
<ul>
<li><strong>The matrix</strong> &mdash; every asset, categorized, justified.</li>
<li><strong>The boundary</strong> &mdash; named systems in and out, and what places each there.</li>
<li><strong>ESP and CSP analysis</strong> &mdash; each provider classified, the resulting obligation named, and
whether a Customer Responsibility Matrix is required and exists.</li>
<li><strong>Flowdown</strong> &mdash; which suppliers must receive DFARS 252.204-7012, and on what basis.</li>
<li><strong>Open items</strong> &mdash; what you could not determine, and what evidence would settle it. There are
at least two.</li>
</ul>
<p>Where a category is unavailable to Meridian because a condition is unmet, say so explicitly and name the
condition. And no remediation anywhere: &ldquo;this asset is in scope because there is no segmentation&rdquo; is
assessment; &ldquo;they should segment the network&rdquo; is not yours to write.</p>""",
   actions=[("Open the Scope &amp; Asset Matrix &rarr;","scope-matrix.html",False),
            ("Case workbench &middot; Technology tab","meridian.html",True)]),
 kc=[
  dict(stem="Meridian's CORP-LAN workstations store no CUI by design, but route freely to the ENG-LAN file server. The company has an SSP, policies and a network diagram — but no asset inventory. How are they categorized?", opts=[
   ("Contractor Risk Managed Assets &mdash; the documentation condition is substantially met",False,"Substantially is not the test. The treatment requires the asset to be documented in the inventory, the SSP <em>and</em> the network diagram. One of the three does not exist, so the category is unavailable."),
   ("Out-of-Scope Assets &mdash; the company states they hold no CUI",False,"Out-of-scope requires the contractor to justify the asset's <em>inability</em> to process, store or transmit CUI. With unsegmented routing and domain credentials, no such justification exists."),
   ("CUI Assets &mdash; the conditional category is closed by the missing inventory, so they fall back to what they can reach",True,"One missing artifact closes both conditional categories to the entire environment. This is the failure you will actually meet: an organisation that has done most of the work and cannot claim the relief because of the piece it skipped."),
   ("Security Protection Assets &mdash; they sit on the corporate segment",False,"They provide no security function to the scope. Being on a particular subnet is not a category."),
  ]),
  dict(stem="Which is a complete statement of the Specialized Asset list?", opts=[
   ("Any asset the contractor cannot fully secure",False,"That is the defining test, not the list. Both must be satisfied: the asset type must be on the list <em>and</em> it must be unable to be fully secured."),
   ("IoT, IIoT, Operational Technology, Government Furnished Equipment, Restricted Information Systems, Test Equipment",True,"A closed list. An asset that is inconvenient to secure, old, or owned by someone else does not join it."),
   ("OT and IoT only",False,"Incomplete &mdash; it omits GFE, Restricted Information Systems, and Test Equipment."),
   ("Any asset located outside the primary facility",False,"Location has no bearing on the category."),
  ]),
  dict(stem="Secure Shred AL collects hard-copy CUI from Meridian's Huntsville site for offsite destruction, under a standard shredding contract with no NDA. How does the regulation treat it?", opts=[
   ("Out of scope &mdash; paper is not an information system",False,"The most commonly missed provider in the case. CUI in hard copy is still CUI, and taking custody of it is handling it."),
   ("An ESP handling CUI, requiring a Customer Responsibility Matrix and evaluation inside the assessment",True,"It takes physical custody of CUI. Contrast the Dayton arrangement, where shredding is in-house to DIN 66399 P-4 and is compliant &mdash; the same obligation, met at one site and not the other."),
   ("A Cloud Service Provider",False,"No cloud service is involved at any point."),
   ("Neither &mdash; destruction services are governed by MP requirements, not the ESP rule",False,"The media protection requirements govern how destruction must be done. They do not remove a provider that handles CUI from the ESP rule; both apply."),
  ]),
  dict(stem="What does classifying Microsoft 365 as a CSP oblige Meridian to produce?", opts=[
   ("A Customer Responsibility Matrix",False,"The CRM belongs to the non-cloud ESP rule. Applying it to a CSP is the most common way the two rules get mixed up."),
   ("FedRAMP Moderate authorization or documented equivalency",True,"Under DFARS 252.204-7012(b)(2)(ii)(D) &mdash; plus compliance with the reporting, preservation, and access requirements, which a commercial subscription does not impose."),
   ("A Level 2 certificate for Microsoft",False,"The assessment does not evaluate the cloud service itself. A Level 2 certificate is one route for an ESP handling CUI, not the CSP obligation."),
   ("Nothing &mdash; the tenant is Microsoft's responsibility",False,"The authorization or equivalency is evidence <em>the OSC</em> must produce. Responsibility for producing it does not transfer with the workload."),
  ]),
  dict(stem="A team categorizes Meridian's backup NAS as Out-of-Scope because \"it only stores backups.\" What is wrong?", opts=[
   ("Nothing &mdash; backup media are treated separately under MP requirements",False,"Media protection requirements apply to media in scope. They do not remove an asset from the scope."),
   ("Backups of CUI are CUI; the NAS stores CUI and is a CUI Asset",True,"The asset organizations forget and an experienced assessor asks about first. It also has a shared local account and no offsite copy, both of which become findings once it is properly in scope."),
   ("It should be a Specialized Asset as storage infrastructure",False,"Storage infrastructure is not on the closed Specialized list."),
   ("It should be a Security Protection Asset because backups protect data",False,"Backups protect against loss; they do not provide a security function to the assessment scope in the sense the category means. It stores CUI, so it is a CUI Asset."),
  ]),
  dict(stem="Which justification for a categorization would survive challenge?", opts=[
   ("\"Production floor device, not used for CUI.\"",False,"States what the asset is for. The test asks what it <em>can do</em> with CUI."),
   ("\"It is a firewall, so it is a security thing.\"",False,"Names the asset type and gestures at a category. It does not reference the defining test."),
   ("\"Can reach the PLM through a browser on the same flat subnet; no policy prevents it.\"",True,"References capability and the absence of the condition that would earn relief. A hostile reader wanting the boundary smaller cannot move it."),
   ("\"Nobody uses it for CUI.\"",False,"Usage is not the test, and it is an assertion by the party being assessed."),
  ]),
  dict(stem="Meridian's own inventory labels the domain controller \"CUI Indirect.\" What should the assessor do?", opts=[
   ("Accept it &mdash; the label describes the situation accurately",False,"It describes it loosely, and there is no such category. Accepting invented vocabulary lets the contractor define the scope."),
   ("Recategorize it as a Security Protection Asset and note the invented category",True,"It handles no CUI directly but provides authentication, group policy, and access control to the whole scope. \"CUI Indirect\" is not one of the five categories &mdash; a contractor inventing vocabulary, which is itself worth recording."),
   ("Recategorize it as a CUI Asset because it controls access to CUI",False,"Defensible only if argued from what it stores rather than from importance. The cleaner call is Security Protection Asset."),
   ("Leave it uncategorized pending the contractor's clarification",False,"Categorization is the assessor's determination, not something the contractor clarifies."),
  ]),
  dict(stem="Under what circumstances does the Contractor Risk Managed Asset category become available to an OSC?", opts=[
   ("When the OSC states the asset is not intended to handle CUI",False,"Intention alone is not the test. The relief is earned, not claimed."),
   ("When security policy, procedures, and practices are in place that keep CUI off the asset",True,"The condition is in the definition itself. Where nothing exists to show, the category is unavailable and the asset falls back to what it is capable of doing."),
   ("When the asset is on a separate VLAN",False,"Segmentation is strong evidence and it is not the stated condition. The definition speaks to policy, procedures, and practices."),
   ("When the asset is owned by a third party",False,"Ownership is irrelevant to this category, and third-party involvement raises the ESP rule instead."),
  ]),
  dict(stem="Which of Meridian's relationships clearly requires DFARS 252.204-7012 flowdown?", opts=[
   ("Whitmore &amp; Associates, because it processes employee financial data",False,"The external CPA holds read-only QuickBooks access and no CUI &mdash; consistent with the Day 2 determination that payroll and ESOP records are neither CUI nor FCI."),
   ("ClearPath, because performance involves covered defense information",True,"Paragraph (m) requires the clause in subcontracts for operationally critical support or where performance will involve CDI. ClearPath maintains the PLM, which holds CUI, with standing remote access."),
   ("FastenerTech Supply, because it supplies parts for a CUI-bearing programme",False,"Supplying commodity hardware is not handling covered defense information. No drawing or specification reaches them &mdash; say what you checked before concluding it."),
   ("Only ClearPath, because it is the only party with system access",False,"ClearPath certainly requires it. So do Acuitas, AeroComp and Secure Shred, all of which receive or take custody of CUI. The obligation follows the information, not the level of system access."),
  ]),
  dict(stem="A team cannot determine whether Huntsville is on the same network as Dayton. What is the best treatment?", opts=[
   ("Assume separation and scope Huntsville out",False,"Assuming the convenient answer is exactly the failure mode. Scoping out an asset that should be in produces an assessment result that is wrong."),
   ("Assume no separation and say nothing further",False,"Reaching the right conclusion by assumption is better than the alternative, and it still hides that the determination rests on absent evidence."),
   ("Treat Huntsville as inside the boundary and record the question as an open item with the evidence that would settle it",True,"Absent evidence of separation, the flat-LAN description governs. Naming what you could not determine, and what would resolve it, is the stronger piece of work."),
   ("Defer the question to the OSC's IT Manager",False,"He is the sole source of undocumented knowledge and the subject of several gaps. What one person remembers is not evidence."),
  ]),
 ],
)

L5 = dict(
 file="lesson05.html", short="L5 — Evidence: Adequacy & Sufficiency", num_label="Lesson 5",
 eyebrow="Day 3 &middot; Afternoon &middot; CAP Phase 2 &middot; CCP 35% / CCA 40%",
 title="Evidence: Adequacy, Sufficiency, and Collection",
 lead=("The conceptual hinge of the workshop. Everything so far has been about what applies and where. This is "
       "about proof &mdash; specifically the gap between an organization having a document and an organization "
       "doing the thing. Most people entering CMMC work close that gap without noticing. Anyone who leaves this "
       "session still equating documentation with compliance does not recover tomorrow."),
 chips=["Day 3 &mdash; PM","~3 hours","<strong>Highest exam weight</strong>","Tool: Evidence Triage"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Distinguish","Distinguish adequacy from sufficiency and apply both tests to a real artifact."),
  ("Decompose","Decompose a NIST SP 800-171 requirement into its assessment objectives and identify what each objective actually demands."),
  ("Select","Select the appropriate assessment method &mdash; examine, interview, or test &mdash; and the assessment object for a given objective, and say what each method can and cannot establish."),
  ("Apply","Apply the CMMC sampling requirements for depth and coverage."),
  ("Construct","Construct an evidence request list specific enough that an organization could act on it without asking a question."),
  ("Evaluate","Evaluate an artifact and state, with reasons, whether it is adequate, sufficient, both, or neither &mdash; and what would change the verdict."),
 ],
 vocab=[
  ("Assessment objective","The unit of determination. NIST SP 800-171A decomposes the 110 requirements into roughly 320 objectives. Every one must be MET or NOT APPLICABLE for the parent requirement to be MET."),
  ("Adequate","The evidence exists and matches what the requirement intends. A property of the artifact, not of the organization."),
  ("Sufficient","The evidence shows the control is implemented, consistently followed, and operating &mdash; across the scope, and currently."),
  ("Examine","Review, inspect, study, or analyze an object. Establishes that something exists and what it says or how it is configured. Cannot establish that anyone follows it."),
  ("Interview","Discuss with individuals or groups. Generates leads, not conclusions. Establishes what people understand and where practice diverges from documentation."),
  ("Test","Exercise an object under specified conditions and compare actual to expected behaviour. Establishes that the control operates as intended, right now."),
  ("Assessment object","What a method is applied to: specifications, mechanisms, activities, or individuals. A method is paired with an object &mdash; \"we will examine\" is half an answer."),
  ("Depth and coverage","The CAP requires a nonstatistical sampling approach and the FOCUSED value for both depth and coverage across Level 2 requirements, increased where evidence is questionable, insufficient, or inadequate."),
  ("Final-form evidence","Evidence in its completed state, as opposed to drafts or verbal assurances. What a MET determination must rest on."),
 ],
 sections=[
  dict(title="Objectives, not requirements", html="""
<p>You do not assess 110 requirements. You assess the assessment objectives those requirements decompose into
&mdash; roughly 320 across Level 2, enumerated in NIST SP 800-171A &mdash; and the arithmetic is unforgiving.</p>
<div class="warnbox"><div class="warn-label">There is no partial credit</div>
<p>Every assessment objective under a requirement must be MET, or NOT APPLICABLE, for the parent requirement to be
MET. One objective unmet makes the whole requirement NOT MET.</p>
<p>This is the single most consequential mechanic in Level 2 assessment. It is why an organization that has
&ldquo;mostly&rdquo; implemented a control has not implemented it, and why an assessor who evaluates at the
requirement level rather than the objective level produces determinations that cannot be defended.</p></div>
<p>Take AC.L2-3.1.1 &mdash; <em>limit system access to authorized users, processes acting on behalf of authorized
users, and devices</em>. It looks like one idea. It is not: authorized users are identified; processes acting on
behalf of authorized users are identified; devices authorized to connect are identified; and system access is
limited to each of the three. Evidence that establishes the first three and nothing about the fourth leaves the
requirement NOT MET.</p>"""),
  dict(title="Adequacy and sufficiency", html="""
<div class="in-practice"><div class="ip-label">The sentence this session is built on</div>
<p>Adequate evidence shows the thing <strong>exists and matches what the requirement intends</strong>. Sufficient
evidence shows it is <strong>implemented, consistently followed, and operating</strong>.</p>
<p>A policy stating that multi-factor authentication is required is adequate. A configuration export plus a sample
of enrolled accounts is sufficient. Someone telling you it is enforced is neither.</p></div>
<div class="tw"><table>
<thead><tr><th></th><th>Adequacy</th><th>Sufficiency</th></tr></thead>
<tbody>
<tr><td><strong>The question</strong></td><td>Does this evidence exist, and does it match what the requirement intends?</td><td>Does it show the control is implemented, consistently followed, and operating?</td></tr>
<tr><td><strong>A policy document</strong></td><td>Usually adequate &mdash; it exists and states the intent</td><td>Almost never sufficient on its own</td></tr>
<tr><td><strong>A configuration export</strong></td><td>Adequate if it addresses the objective</td><td>Sufficient if it covers the assets in scope and is current</td></tr>
<tr><td><strong>A screenshot</strong></td><td>Adequate for what is on screen</td><td>Sufficient only if the scope of what it shows matches the scope of the requirement</td></tr>
<tr><td><strong>A verbal assurance</strong></td><td>Neither</td><td>Neither</td></tr>
<tr><td><strong>What to ask next</strong></td><td>&ldquo;What is this a document about?&rdquo;</td><td>&ldquo;How would I know this is still true, and true everywhere?&rdquo;</td></tr>
</tbody></table></div>
<h3>The three failures you will see most</h3>
<ol>
<li><strong>The artifact exists but does not address the objective</strong> &mdash; a policy about passwords offered
for a requirement about session termination.</li>
<li><strong>The artifact addresses the objective but covers only part of the scope</strong> &mdash; real evidence for
one system, offered for an environment containing seven.</li>
<li><strong>The artifact is a claim rather than a record</strong> &mdash; an email saying the thing happens, a
spreadsheet built from memory, a person of unquestioned competence saying &ldquo;yes, we do that.&rdquo;</li>
</ol>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>Adequacy is a property of the <em>artifact</em>, not of the organization. A well-drafted policy in a
non-compliant company is still adequate, and being able to say so is the discrimination that separates a Competent
assessor from one who marks everything &ldquo;neither&rdquo; because the company is a mess.</p></div>"""),
  dict(title="Methods and objects", html="""
<p>Three methods, and each pairs with the kind of object it can actually speak to.</p>
<div class="tw"><table>
<thead><tr><th>Method</th><th>What it does</th><th>What it establishes</th><th>What it cannot establish</th></tr></thead>
<tbody>
<tr><td><strong>Examine</strong></td><td>Review, inspect, study, or analyze an object &mdash; specifications, mechanisms, activities, or documents</td><td>That something exists, and what it says or how it is configured</td><td>That anyone follows it, or that it was true yesterday</td></tr>
<tr><td><strong>Interview</strong></td><td>Discuss with individuals or groups</td><td>What people understand, what they say they do, and where practice diverges from documentation</td><td>Anything, on its own. An interview generates leads, not conclusions</td></tr>
<tr><td><strong>Test</strong></td><td>Exercise an object under specified conditions and compare actual to expected behaviour</td><td>That the control operates as intended, right now</td><td>That it operated last quarter, or across assets you did not test</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">Depth and coverage</div>
<p>The CAP requires a nonstatistical sampling approach, and requires the assessment team to apply the
<strong>FOCUSED</strong> value for both depth and coverage across all Level 2 security requirements, as applicable.
The team should increase the sample when it encounters questionable, insufficient, or inadequate evidence.</p>
<p>Two practical consequences. Where an organization has multiple CAGE codes, all of them must be accounted for in
the sampling approach. Where it has multiple physical locations &mdash; as Meridian does &mdash; the sampling
should consider whether the locations use different physical controls and whether scans and boundaries cover all
of them.</p></div>
<p>Note the word the Assessment Guide uses: <em>potential</em> assessment methods and objects. The guide lists what
<em>could</em> establish an objective, not what must. Choosing among them is your judgment, and exercising it is
what you are being trained to do.</p>"""),
  dict(title="Five artifacts, evaluated", html="""
<p>These are the artifacts Meridian supplied. Nothing has been edited to make them better or worse than they
are. Work each one before reading the verdict.</p>
<h3>Artifact 1 &mdash; Access control policy excerpt</h3>
<p><em>Supplied by Trevor Nakamura as a PDF. Document properties: created 14 March 2021, last modified 14 March 2021.
Four clauses on need-to-know, account creation and disablement, administrative privilege restriction, and periodic
review by the IT Manager. Approved by the CEO.</em></p>
<p><strong>Adequate. Not sufficient.</strong> It exists, it is approved, and clauses 4.1 and 4.3 address the intent
of AC.L2-3.1.1, 3.1.2, and 3.1.5. It is not sufficient because there is no access control matrix, access is managed
from the IT Manager's memory, a QuickBooks administrator account belonging to a departed employee has been active
for fourteen months, and the Contracts Manager does not know who can reach the folder she asked to be restricted.
Clause 4.4 promises periodic review; no record of a review exists.<br>
<em>What would change it:</em> an access control matrix; an account listing with privilege levels reconciled
against it; dated review records naming the reviewer; termination records showing accounts disabled on separation.</p>
<h3>Artifact 2 &mdash; Conditional Access configuration</h3>
<p><em>A screenshot of the Microsoft 365 admin centre. Policy &ldquo;Require MFA for all users,&rdquo; State: On,
Users: All users (163), Cloud apps: All, Conditions: Any location, Grant: Require MFA &mdash; with the shared
service account <code>mpds-admin@</code> listed under Excluded. Tenant identifier visible and matching. Exported
three days before the request.</em></p>
<p><strong>The hardest artifact in the set.</strong> This is genuinely good evidence &mdash; current, scoped,
attributable, recent. And it does not carry IA.L2-3.5.3, because the requirement applies across the assessment
scope and the scope is not Microsoft 365. The PLM, the file server, domain controller RDP, the SSL VPN, QuickBooks,
and the backup NAS all authenticate with single-factor credentials. Evidence covering one system out of seven
establishes the objective for one system out of seven.<br>
<em>Two secondary observations:</em> a screenshot shows the policy exists and is enabled; it does not show
exclusions, which is where Conditional Access policies usually leak &mdash; the full policy export is the better
artifact. And the assessor should test with a sample account rather than rely on configuration alone.</p>
<div class="warnbox"><div class="warn-label">Hold this distinction</div>
<p>The artifact is excellent and the requirement is still NOT MET. An assessor who cannot praise good evidence and
still find the requirement unmet will be argued out of findings in the field.</p></div>
<h3>Artifact 3 &mdash; Email from the IT Manager</h3>
<p><em>&ldquo;Logging is turned on across the board &mdash; Windows event logs on all the servers and the FortiGate
firewall logs everything. I check them regularly and we have not seen anything unusual. If something looked wrong I
would know about it. I have been doing this here for nine years.&rdquo;</em></p>
<p><strong>Neither.</strong> It is an assertion that arrived by email, which does not make it a record. An interview
response is a lead to be corroborated, not a conclusion, and this is an interview response in written form.</p>
<p>Two rhetorical moves are worth naming. &ldquo;I have been doing this here for nine years&rdquo; is an appeal to
authority. &ldquo;We have not seen anything unusual&rdquo; is an appeal to the absence of evidence &mdash; and with
no review records, no aggregation, and no SIEM, Meridian has no capability to have seen anything unusual. The
absence of observed events is not evidence of absence when nothing is looking.</p>
<h3>Artifact 4 &mdash; Risk Assessment Report (POL-006)</h3>
<p><em>Supplied by Diana Kowalczyk. The document register records it as last performed June 2023 and flags it
&ldquo;Overdue.&rdquo; Six risks, each with likelihood, impact, a level, a remediation state and an owner.</em></p>
<p><strong>Adequate. Not sufficient.</strong> Unlike most artifacts in this case it is the right kind of document,
it identifies real risks specific to this environment, and it assigns ownership. Meridian has genuinely done a risk
assessment. But the requirement is to assess risk <em>periodically</em>, and this was performed once, 19 months ago,
with no next review scheduled &mdash; so there is no periodicity to evidence. Two of the six risks record no
remediation at all and one records &ldquo;planned&rdquo; with no date.</p>
<p><strong>The observation that separates Competent from Assessor-Ready:</strong> read the register against your own
findings. RISK-01, RISK-02 and RISK-03 describe, in the company's own words, three of the failures you are about to
write up &mdash; unpatched workstations, MSP privileged access, stale VPN accounts. Meridian identified them, rated
them Critical and High, assigned owners, and did nothing for 19 months. That is not an unknown risk. It is an
accepted one that nobody was authorised to accept.</p>
<h3>Artifact 5 &mdash; The POA&amp;M</h3>
<p><em>Supplied by Diana Kowalczyk as an .xlsx attachment. Six items. Four carry no target date, none carries a
named individual owner &mdash; the owner column reads &ldquo;IT&rdquo; or &ldquo;Contracts&rdquo; &mdash; none
records resources, and no item has ever been closed. No version history. No AO signature. Last modified 18 months
ago. Asked where the master copy lives, she states it is in her OneDrive.</em></p>
<p><strong>Neither &mdash; and the artifact is itself a finding.</strong> A plan of action must identify the
weakness, the corrective action, the resources required, the milestones and the completion dates. This does not
match what the requirement intends, so it is not adequate.</p>
<div class="warnbox"><div class="warn-label">Where an artifact lives can be worse than what it says</div>
<p>The master copy is in a <strong>personal OneDrive on a commercial tenant</strong>, not in the authorised GCC High
environment. A document enumerating every unremediated security weakness in a defense contractor is precisely what
an adversary would target, and it is being kept outside the accredited boundary &mdash; which also contradicts the
SSP's own boundary statement.</p>
<p>This is the clearest example in the case of a finding that has nothing to do with the content of the document.
Ask where evidence lives, not only what it says.</p></div>
<div class="tip"><div class="tip-label">Consistency check</div>
<p>You will need the POA&amp;M again on Friday, when the eligibility rules in 32 CFR &sect;170.21 turn on what a
plan of action may and may not carry. Note now that a POA&amp;M is a regulated instrument with a defined content
standard, not a spreadsheet of intentions &mdash; and that an assessor who accepts this one as evidence of anything
will have a difficult Friday.</p></div>"""),
  dict(title="Building the request list", html="""
<p>An evidence request list is a working instrument, not a wish list. Each line names four things.</p>
<div class="tw"><table>
<thead><tr><th>Element</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td><strong>The artifact</strong></td><td>Specific enough to be retrieved. &ldquo;Access control documentation&rdquo; is not a request; &ldquo;the current Conditional Access policy export from the Microsoft 365 tenant&rdquo; is.</td></tr>
<tr><td><strong>The method</strong></td><td>Examine, interview, or test. This tells the organization what form the evidence has to take.</td></tr>
<tr><td><strong>The objective it serves</strong></td><td>Which assessment objective this is meant to establish. If you cannot name one, delete the line.</td></tr>
<tr><td><strong>The custodian</strong></td><td>Who holds it. At Meridian this is frequently one person, which is itself a finding.</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">Where assessments go wrong quietly</div>
<p>A vague request produces a pile of documents, a week of delay, and an assessment team that starts accepting
whatever arrived because the schedule is slipping. Nobody decides to lower the standard; it lowers itself.
Specificity up front is the control.</p></div>"""),
  dict(title="The verdict is the least interesting part", html="""
<p>Most assessors reach similar verdicts on these five artifacts. What separates them is the last clause &mdash;
<strong>what would change it</strong>.</p>
<p>An assessor who can say &ldquo;this is adequate but not sufficient, and here is precisely what would make it
sufficient&rdquo; has given an organization something it can act on, without ever telling it what to do. That is the
line you will walk for the rest of your career, and it is the reason every verdict in this workshop carries a
<em>what would change it</em> field.</p>
<div class="in-practice"><div class="ip-label">The habit</div>
<p>Naming what evidence is missing is assessment. Telling Meridian how to produce it is not. Name the gap
precisely enough that the fix is obvious without ever being stated.</p></div>"""),
 ],
 case=dict(tag="Meridian &middot; Day 3 Afternoon &middot; Deliverable D5",
   title="Triage five artifacts and build the request list",
   html="""
<p>The <strong>Evidence Triage tool</strong> presents the five artifacts one at a time, in full, exactly as they
were supplied. For each you name the assessment objective it is offered against, render a verdict &mdash;
<em>adequate</em>, <em>sufficient</em>, <em>both</em>, or <em>neither</em> &mdash; give the reasoning, and say what
would change the verdict. The tool then shows the model evaluation with the reasoning exposed, including the
observations that separate a Competent verdict from an Assessor-Ready one.</p>
<p>Part B is the request list: fifteen requirements, from AC.L2-3.1.1 through SC.L2-3.13.1, each needing one or
more lines naming a retrievable artifact, a method, the objective it serves, and the custodian. The tool rejects
lines that name a topic rather than an artifact.</p>
<p><strong>Every verdict must say what would change it.</strong> A verdict without that clause is incomplete, and
the tool will tell you so.</p>""",
   actions=[("Open the Evidence Triage tool &rarr;","evidence-triage.html",False),
            ("Case workbench &middot; Documents","meridian.html",True)]),
 kc=[
  dict(stem="A requirement has five assessment objectives. Evidence establishes four; the fifth is not addressed by anything supplied. What is the determination?", opts=[
   ("MET, with the fifth objective noted as a weakness",False,"There is no MET-with-weakness determination. A noted weakness at objective level is what NOT MET means."),
   ("NOT MET",True,"Every objective must be MET or NOT APPLICABLE for the parent requirement to be MET. Four out of five is NOT MET, and the finding names the objective that failed."),
   ("MET, since the preponderance of objectives is satisfied",False,"Preponderance has no place in this determination. Importing it from other assurance regimes is a reliable way to produce findings that collapse."),
   ("Deferred pending additional evidence",False,"Deferral is not a determination. You may request more evidence during the assessment; at determination time the answer is MET, NOT MET, or NOT APPLICABLE."),
  ]),
  dict(stem="Meridian supplies a current Conditional Access export showing MFA enforced for all 163 users on all cloud apps, with one shared Global Admin service account excluded. The SSL VPN has no MFA. How do you evaluate the artifact against IA.L2-3.5.3?", opts=[
   ("Adequate and sufficient &mdash; it is current, scoped, and attributable",False,"It is all of those things for Microsoft 365. The requirement applies across the assessment scope, and the scope is not Microsoft 365."),
   ("Neither &mdash; the requirement is NOT MET",False,"Rejecting good evidence because the requirement fails is the mirror-image error. Adequacy is a property of the artifact."),
   ("Adequate, and sufficient only for the Microsoft 365 boundary; the requirement is NOT MET",True,"Evidence covering one system out of seven establishes the objective for one system out of seven. Praising the artifact and finding the requirement unmet are not in tension &mdash; an assessor who cannot do both will be argued out of findings."),
   ("Adequate and sufficient, with the other systems handled as a separate finding",False,"The other systems are not a separate requirement. They are within the scope of this one, and the determination has to reflect that."),
  ]),
  dict(stem="Which best describes what an interview can establish on its own?", opts=[
   ("That a control is implemented, if the interviewee is credible and knowledgeable",False,"Competence and honesty are not evidence. The assessments that go wrong go wrong with likeable people."),
   ("Nothing on its own &mdash; it generates leads to be corroborated",True,"An interview establishes what people understand and where practice diverges from documentation. It is a lead, not a conclusion."),
   ("That a policy exists",False,"Existence of a document is established by examining it, not by being told about it."),
   ("That a control operated during the assessment period",False,"Nothing establishes past operation from a conversation. Even a test only establishes current operation."),
  ]),
  dict(stem="An IT manager emails: \"Logging is on everywhere and I check them regularly. If something looked wrong I would know. I've been doing this nine years.\" Evaluate against AU.L2-3.3.1 and 3.3.5.", opts=[
   ("Adequate &mdash; it is a written record from the system owner",False,"An assertion in writing is still an assertion. The medium does not convert a claim into a record."),
   ("Adequate but not sufficient &mdash; it needs supporting review records",False,"Close, and it misses that the artifact does not meet the adequacy test at all. It is not a document about log review; it is a statement that log review happens."),
   ("Neither &mdash; it is an interview response in written form, resting on an appeal to authority and an appeal to absence of evidence",True,"With no review records, no aggregation, and no SIEM, the organization has no capability to have seen anything unusual. Absence of observed events is not evidence of absence when nothing is looking."),
   ("Sufficient for 3.3.1 but not 3.3.5",False,"It is not evidence for either. 3.3.1 requires records created and retained; 3.3.5 requires correlation across sources."),
  ]),
  dict(stem="Which evidence request line would you accept?", opts=[
   ("\"Access control documentation\"",False,"A topic, not an artifact. It produces a pile of documents and a week of delay."),
   ("\"Evidence that MFA is enforced\"",False,"Names an objective, not a retrievable artifact, and does not say what form the evidence should take."),
   ("\"The current Conditional Access policy export from the Microsoft 365 tenant, including exclusions &mdash; Examine &mdash; IA.L2-3.5.3[a] &mdash; T. Nakamura\"",True,"Artifact, method, objective, custodian. An OSC could satisfy it without a phone call, and the mention of exclusions closes the gap a screenshot leaves open."),
   ("\"Anything you have on vulnerability management\"",False,"The request that guarantees you receive a management summary of a report the organization does not hold."),
  ]),
  dict(stem="Meridian's POA&M is a spreadsheet held in the CISO's personal OneDrive rather than in the GCC High tenant. Beyond its content, what does the assessor record?", opts=[
   ("Nothing further &mdash; storage location is an IT preference, not a compliance matter",False,"It is a boundary violation. The authorised environment for this company's sensitive material is the GCC High tenant, and this is not in it."),
   ("That a document enumerating every unremediated weakness is being held outside the authorised CUI boundary, contradicting the SSP's own boundary statement",True,"Two findings in one: the storage location itself, and the inconsistency with the SSP. Where an artifact lives can be a more serious finding than what it says &mdash; ask where evidence lives, not only what it says."),
   ("That the CISO should move it immediately",False,"That is remediation advice. Naming the gap is assessment; specifying the fix is not."),
   ("That the POA&M is invalid and cannot be considered",False,"It can and must be considered &mdash; as evidence about the company. Refusing to look at it would lose the finding."),
  ]),
  dict(stem="What sampling values does the CAP require for Level 2 assessments?", opts=[
   ("A statistically valid random sample sized to a 95% confidence interval",False,"The CAP requires a nonstatistical approach. Statistical sampling language is imported from financial audit."),
   ("A nonstatistical approach applying the FOCUSED value for both depth and coverage",True,"Increased where the team encounters questionable, insufficient, or inadequate evidence. Multiple CAGE codes must all be accounted for, and multiple locations considered for differing physical controls."),
   ("100% coverage of all in-scope assets",False,"Not required and not feasible. The sampling requirement exists precisely because full coverage is not the standard."),
   ("Whatever depth the Lead CCA considers proportionate",False,"Judgment applies to method selection, not to the depth and coverage values, which the CAP specifies."),
  ]),
  dict(stem="An asset inventory lists \"Laptops / desktops 41; Service accounts 3.\" Against CM.L2-3.4.1, this is:", opts=[
   ("Adequate &mdash; an inventory is the right kind of document",False,"The category of document is right and the content does not address the objective. That distinction is the whole of adequacy."),
   ("Adequate but not sufficient &mdash; it needs dates and owners",False,"Dates and owners would not fix it. It omits every asset that holds CUI."),
   ("Neither &mdash; a two-line list of quantities is not an inventory of system components, and it omits every CUI-bearing asset",True,"Not adequate because it does not match the intent; not sufficient because it was compiled from memory, is undated, and carries no baseline configurations, which is the other half of the requirement."),
   ("Sufficient for the endpoint portion of the requirement",False,"It does not even establish the endpoint portion &mdash; there is no identification of components, only a count."),
  ]),
  dict(stem="A policy is well drafted, approved by the CEO, and directly addresses the requirement's intent, but the organization demonstrably does not follow it. How is the artifact evaluated?", opts=[
   ("Neither, because the organization is non-compliant",False,"The most common error in the set. Adequacy is a property of the artifact, not of the organization."),
   ("Adequate but not sufficient",True,"It exists and matches what the requirement intends &mdash; adequate. It does not show the control is implemented, consistently followed, and operating &mdash; not sufficient. The requirement is NOT MET and the artifact is still adequate."),
   ("Sufficient but not adequate",False,"This combination is close to impossible. Sufficiency presupposes the evidence addresses the objective."),
   ("Adequate and sufficient, with a separate finding for non-compliance",False,"Non-compliance is not a separate finding. It is what makes the evidence insufficient."),
  ]),
  dict(stem="What must every verdict in an evidence log include beyond the verdict itself?", opts=[
   ("The severity of the associated finding",False,"Severity attaches to findings, and it follows from the requirement and the exposure, not from the evidence evaluation."),
   ("A recommendation for how the OSC could produce better evidence",False,"That is remediation advice. Naming what is missing is assessment; telling the OSC how to produce it is not."),
   ("What would change the verdict",True,"An assessor who can say precisely what would make an artifact sufficient has given the organization something it can act on without ever telling it what to do. A verdict without that clause is incomplete."),
   ("The name of the assessor who evaluated it",False,"Useful for records, and not the substantive element the evaluation turns on."),
  ]),
 ],
)

L6 = dict(
 file="lesson06.html", short="L6 — Assessing the 14 Domains", num_label="Lesson 6",
 eyebrow="Day 4 &middot; Morning &middot; CAP Phase 2 &middot; CCP 35% / CCA 40%",
 title="Assessing the Fourteen Domains",
 lead=("Everything you have built &mdash; the boundary, the evidence discipline, the objective-level thinking "
       "&mdash; gets pointed at fourteen families of requirements and turned into determinations. Every small "
       "contractor fails in roughly the same places. Knowing the pattern tells you where to look first. It does "
       "not tell you what you will find."),
 chips=["Day 4 &mdash; AM","~3 hours","<strong>Highest exam weight</strong>","Tool: Domain Worksheet"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Assess","Assess requirements across the fourteen NIST SP 800-171 Rev 2 families using the CMMC Assessment Guide for Level 2."),
  ("Render","Render and justify MET, NOT MET, and NOT APPLICABLE determinations at the assessment-objective level."),
  ("Recognize","Recognize the characteristic failure pattern of each domain in a small-contractor environment."),
  ("Defend","Defend a determination against challenge, arguing from the objectives rather than from experience or seniority."),
  ("Detect","Detect where a gap has been mapped to the wrong requirement, and argue the correct mapping."),
 ],
 vocab=[
  ("MET","All applicable assessment objectives are satisfied by final-form evidence. An enduring exception with documented mitigation, or a temporary deficiency covered by an operational plan of action, can still be MET."),
  ("NOT MET","One or more objectives is not satisfied. The finding must name which objective and what is missing."),
  ("NOT APPLICABLE","The requirement does not apply to the assessment scope. Treated as MET for scoring purposes, which is exactly why it attracts pressure."),
  ("Enduring exception","A special circumstance where remediation is not feasible &mdash; documented in the SSP with a mitigation. Not the same as a deficiency."),
  ("Operational plan of action","An OSC-managed plan covering a temporary deficiency, documented in the SSP. Distinct from the POA&amp;M used for conditional status."),
  ("AC / AU / CM / IA","Access Control, Audit and Accountability, Configuration Management, Identification and Authentication &mdash; four of the fourteen families, and where the heaviest point values cluster."),
 ],
 sections=[
  dict(title="The three determinations", html="""
<div class="tw"><table>
<thead><tr><th>Determination</th><th>What it means</th><th>What it requires of you</th></tr></thead>
<tbody>
<tr><td><strong>MET</strong></td><td>All applicable assessment objectives are satisfied by final-form evidence. An enduring exception with a documented mitigation, or a temporary deficiency covered by an operational plan of action, can still be MET.</td><td>Cite the evidence for each objective. &ldquo;The control is in place&rdquo; is not a determination.</td></tr>
<tr><td><strong>NOT MET</strong></td><td>One or more objectives is not satisfied.</td><td>Document the nonconformance &mdash; which objective, and what is missing. A NOT MET with no named objective cannot be defended or remediated.</td></tr>
<tr><td><strong>NOT APPLICABLE</strong></td><td>The requirement does not apply to the assessment scope.</td><td>Justify it. N/A is treated as MET for scoring purposes, which is exactly why it attracts pressure.</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>Candidates reliably miss that a requirement can be MET while a deficiency exists, provided the deficiency is
temporary and covered by an operational plan of action documented in the SSP &mdash; or is an enduring exception
with a documented mitigation. Note that this is a different instrument from the POA&amp;M that supports conditional
status, which you meet on Friday.</p></div>"""),
  dict(title="The fourteen domains and how they fail", html="""
<div class="tw"><table>
<thead><tr><th>Domain</th><th>Characteristic small-contractor failure</th></tr></thead>
<tbody>
<tr><td><strong>AC</strong> &mdash; Access Control</td><td>Shared accounts, administrative rights used for daily work, no access matrix, accounts that outlive their owners.</td></tr>
<tr><td><strong>AT</strong> &mdash; Awareness and Training</td><td>A generic annual campaign with partial completion, and no role-based training for the people who actually handle CUI.</td></tr>
<tr><td><strong>AU</strong> &mdash; Audit and Accountability</td><td>Logging enabled and never reviewed. Retention undefined. No correlation across sources.</td></tr>
<tr><td><strong>CA</strong> &mdash; Security Assessment</td><td>No SSP, or an SSP written once and never maintained. No cadence for reassessment.</td></tr>
<tr><td><strong>CM</strong> &mdash; Configuration Management</td><td>No baseline configurations, no authorized software list, changes made on request without review.</td></tr>
<tr><td><strong>IA</strong> &mdash; Identification and Authentication</td><td>Multi-factor on the easy system and nothing else. Legacy systems exempted by silence.</td></tr>
<tr><td><strong>IR</strong> &mdash; Incident Response</td><td>No written plan, incidents handled by email, and a reporting decision made by whoever happened to be in the room.</td></tr>
<tr><td><strong>MA</strong> &mdash; Maintenance</td><td>Third-party maintenance with standing remote access, no escort, no session records, no sanitization requirement.</td></tr>
<tr><td><strong>MP</strong> &mdash; Media Protection</td><td>No removable media policy, no sanitization record, and paper nobody thought of as media.</td></tr>
<tr><td><strong>PE</strong> &mdash; Physical Protection</td><td>Visitor logs unmaintained, secondary sites uncontrolled, physical access to the server room undocumented.</td></tr>
<tr><td><strong>PS</strong> &mdash; Personnel Security</td><td>Offboarding that happens eventually, with no record that it happened at all.</td></tr>
<tr><td><strong>RA</strong> &mdash; Risk Assessment</td><td>A scan report with no remediation trail, and no recurring schedule.</td></tr>
<tr><td><strong>SC</strong> &mdash; System and Communications Protection</td><td>Flat networks, commercial cloud holding CUI, and no boundary anyone can draw on paper.</td></tr>
<tr><td><strong>SI</strong> &mdash; System and Information Integrity</td><td>Unsupported operating systems still in production because replacing them is expensive.</td></tr>
</tbody></table></div>
<p>Read that table against Meridian and you have most of the gap list before anyone opens a document. That is
useful for knowing where to look. It is not a substitute for looking.</p>"""),
  dict(title="Working a requirement objective by objective", html="""
<p>Take <strong>AC.L2-3.1.5 &mdash; employ the principle of least privilege</strong>, and work it against
Meridian as the company stood before its remediation year.</p>
<div class="tw"><table>
<thead><tr><th>Objective</th><th>Evidence available</th><th>Determination</th></tr></thead>
<tbody>
<tr><td>Privileged accounts are identified</td><td>No access control matrix exists; the IT Manager manages permissions from memory</td><td>NOT MET</td></tr>
<tr><td>Access to privileged accounts is authorized in accordance with least privilege</td><td>Two domain administrators, both using those accounts for daily work; three shared service accounts, one of them domain admin</td><td>NOT MET</td></tr>
<tr><td>Security functions are identified</td><td>Not documented anywhere</td><td>NOT MET</td></tr>
<tr><td>Access to security functions is authorized in accordance with least privilege</td><td>Same</td><td>NOT MET</td></tr>
</tbody></table></div>
<p>Requirement determination: <strong>NOT MET</strong>, and the finding names all four objectives rather than
asserting &ldquo;least privilege is not implemented.&rdquo; The difference matters when the OSC challenges it: a
finding that names objectives can be verified or overturned without redoing the assessment.</p>
<div class="in-practice"><div class="ip-label">Citing evidence</div>
<p>&ldquo;Interview with the IT Manager, 14 March, on privileged account inventory&rdquo; is a citation.
&ldquo;Discussion&rdquo; is not. Every MET must name the evidence relied on; every NOT MET must name the objective
that fails and what was missing.</p></div>"""),
  dict(title="When the gap list maps to the wrong requirement", html="""
<p>Meridian's own documentation maps thirteen gaps to requirements. Two of those mappings are worth arguing
with, and noticing them is a specific assessable skill.</p>
<div class="tw"><table>
<thead><tr><th>Gap</th><th>Company mapping</th><th>The argument</th></tr></thead>
<tbody>
<tr><td><strong>GAP-04</strong> &mdash; No asset inventory; unpatched engineering workstations</td><td>3.4.2, described by the company as &ldquo;component inventory&rdquo;</td>
<td>The company's <em>description</em> of 3.4.2 is wrong. In Rev 2, <strong>3.4.1</strong> covers baseline configurations <em>and inventories</em>; <strong>3.4.2</strong> is establishing and enforcing security configuration settings. This is really two gaps against two requirements. The correction does not move the score &mdash; both are 5 points &mdash; which is exactly why it is worth catching: it changes <em>what evidence closes it</em>.</td></tr>
<tr><td><strong>GAP-05</strong> &mdash; No formal POA&amp;M; informal spreadsheet, not AO-approved</td><td>3.12.4</td>
<td>3.12.4 is the <strong>System Security Plan</strong> requirement. A deficient plan of action is <strong>CA.L2-3.12.2</strong>. The consequence is not academic: 3.12.4 is one of the six that may never be placed on a POA&amp;M and 3.12.2 is not, so the mapping helps decide whether Meridian is blocked outright.</td></tr>
<tr><td><strong>GAP-08</strong> &mdash; No segmentation between CORP-LAN and ENG-LAN</td><td>3.13.3</td>
<td>3.13.3 separates user functionality from system management functionality &mdash; arguably engaged by the policy-only MGMT-LAN separation, but not what the finding describes. What is described is failure to protect communications at a key internal boundary: <strong>SC.L2-3.13.1</strong>, worth 5 points rather than 1.</td></tr>
<tr><td><strong>GAP-06</strong> &mdash; No supply chain risk management programme</td><td>3.17.1 / 3.17.2</td>
<td><strong>These practices do not exist in Rev 2.</strong> The SR family belongs to NIST SP 800-171 <em>Rev 3</em>. CMMC Level 2 is anchored to Rev 2, which has fourteen families and no SR family. There is nothing to deduct under the methodology &mdash; and the gap is real: it is a DFARS 252.204-7012(m) flow-down violation and an ESP failure under 32 CFR &sect;170.19.</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>Three of these are mapping errors and one is a category error. The GAP-06 line is the one to dwell on: a gap
mapped to a requirement <em>that does not exist in the applicable revision</em> cannot be scored, cannot be
remediated against a stated objective, and cannot be defended &mdash; yet the underlying failure is one of the most
serious in the company. Catching it requires knowing which revision governs, which is a fact about the programme
rather than about this contractor.</p></div>"""),
  dict(title="N/A discipline", html="""
<p>NOT APPLICABLE scores as MET. That makes it the determination an OSC has the strongest incentive to invite, and
the one you should be slowest to grant.</p>
<p>Meridian's own SPRS submission claimed three:</p>
<ul>
<li><strong>3.13.3 &mdash; &ldquo;Not applicable, single site network.&rdquo;</strong> The company has two sites,
in different states, on one flat LAN. The premise is false on the company's own facts.</li>
<li><strong>3.2.2 &mdash; &ldquo;Not applicable, training is delivered by a third party.&rdquo;</strong> Who delivers
training has no bearing on whether the requirement applies. Outsourcing execution does not outsource the
obligation.</li>
<li><strong>3.10.3 &mdash; &ldquo;Not applicable, no visitors access the server room.&rdquo;</strong> An assertion by
the party being assessed, contradicted by a warehouse with no visitor log where delivery drivers come and go.</li>
</ul>
<div class="warnbox"><div class="warn-label">Recognize when N/A is being invited</div>
<p>None of these three is a considered determination. Each is a reason not to do work, written by someone who
needed a number. An assessor who accepts them has allowed the OSC to score itself.</p></div>"""),
  dict(title="Defending a determination", html="""
<p>Challenges are arbitrated against the Assessment Guide text, not by assertion and not by seniority. If a
determination cannot be defended from the objectives, it changes.</p>
<p>This cuts both ways, and the second direction is the one people find harder. A team that never concedes anything
has stopped assessing and started defending. Distinguish <strong>new information</strong>, which should change your
call, from <strong>pressure</strong>, which should not.</p>
<div class="in-practice"><div class="ip-label">Lead with the call you are least sure of</div>
<p>The instinct is to present your best work. That wastes the exercise: nobody learns anything from a determination
everyone agrees with. A categorization or determination that cannot survive a peer challenge will not survive an
organization that stands to save money by defeating it.</p></div>"""),
 ],
 case=dict(tag="Meridian &middot; Day 4 Morning &middot; Deliverable D6",
   title="Render objective-level determinations",
   html="""
<p>The <strong>Domain Determination Worksheet</strong> loads fifteen requirements spanning eight of the fourteen
families, decomposed into their assessment objectives, with the Meridian evidence attached to each.</p>
<p>For every requirement: determine each objective, cite the evidence relied on, and give the reasoning where the
call was not obvious. Where you dispute the company's mapping of a gap to a requirement, say so and give your
mapping &mdash; the tool checks both G-08 and G-09 specifically.</p>
<ul>
<li><strong>Objective level, not requirement level.</strong> A worksheet that determines at the requirement level
has not done the work.</li>
<li><strong>Every MET cites named evidence.</strong> &ldquo;Interview with the IT Manager&rdquo; is a citation;
&ldquo;discussion&rdquo; is not.</li>
<li><strong>Every NOT MET names the failing objective</strong> and what is missing.</li>
<li><strong>Every N/A carries a justification.</strong> N/A scores as MET, so it will be challenged.</li>
<li><strong>No remediation.</strong> State what is missing; do not state what to do about it.</li>
</ul>
<p>Your determinations must stay consistent with the scope you drew this morning and the evidence you triaged
yesterday. The tool flags contradictions.</p>""",
   actions=[("Open the Domain Worksheet &rarr;","domain-worksheet.html",False),
            ("Evidence Triage","evidence-triage.html",True)]),
 kc=[
  dict(stem="Meridian's SPRS submission marks 3.2.2 \"Not applicable — training is delivered by a third party.\" What is the assessor's response?", opts=[
   ("Accept it &mdash; the requirement is satisfied by the provider",False,"That would be a MET determination on the provider's evidence, not an N/A. And no such evidence was offered."),
   ("Reject it &mdash; who delivers training has no bearing on whether the requirement applies",True,"Outsourcing execution does not outsource the obligation. This is not a determination; it is a reason not to do work, written by someone who needed a number."),
   ("Accept it if the provider holds its own CMMC certification",False,"A training vendor's certification, if it existed, would say nothing about whether Meridian's people received role-based training."),
   ("Defer it to the provider's assessment",False,"There is no provider assessment, and the requirement is Meridian's."),
  ]),
  dict(stem="Meridian maps \"No System Security Plan exists\" to requirement 3.12.1. What is the strongest correction?", opts=[
   ("The mapping is right; 3.12.1 covers security assessment planning",False,"3.12.1 is periodic assessment of security controls. It is a different obligation."),
   ("It should map to CA.L2-3.12.4, which is worth 1 point and may never be placed on a POA&M",True,"Two consequences follow the correction: the deduction falls from 5 to 1, and the requirement becomes an absolute barrier to any CMMC status regardless of score. The cheapest requirement on the sheet is the one that stops the company."),
   ("It should map to both 3.12.1 and 3.12.4",False,"Defensible as an argument, and it raises total deductions rather than lowering them. The cleaner correction is 3.12.4, which is the requirement that actually addresses the SSP."),
   ("It should map to CA.L2-3.12.3, continuous monitoring",False,"Monitoring is a separate obligation and does not describe the absence of an SSP."),
  ]),
  dict(stem="Which statement about NOT APPLICABLE is correct?", opts=[
   ("It is scored as a deduction, since the control is not implemented",False,"N/A is not a failure. It means the requirement does not apply to the scope."),
   ("It is treated as MET for scoring purposes and must be justified",True,"Which is precisely why it attracts pressure from an OSC and why an assessor should be slow to grant it."),
   ("It may only be used where the OSC has documented the exclusion in its SSP",False,"SSP documentation supports the justification, and the determination is the assessor's regardless of what the SSP says."),
   ("It is unavailable at Level 2",False,"It is available and used. What is unavailable at Level 2 is partial credit at the objective level."),
  ]),
  dict(stem="An assessor writes: \"AC.L2-3.1.5 NOT MET — least privilege is not implemented.\" What is deficient about this finding?", opts=[
   ("Nothing &mdash; it states the requirement and the determination",False,"It states a conclusion. A reader cannot verify or overturn it without redoing the assessment."),
   ("It does not name the failing objectives or what was missing",True,"A NOT MET with no named objective cannot be defended or remediated. The finding should name each objective that failed, the evidence examined, and what was absent."),
   ("It should include a recommended remediation",False,"It should not. Naming the fix is consulting, and it is still consulting in a findings report."),
   ("It should state a severity of Critical",False,"Severity follows from the requirement and the exposure, and it does not cure the absence of objective-level detail."),
  ]),
  dict(stem="A requirement's evidence shows a temporary deficiency that the OSC has documented in its SSP with an operational plan of action. Can the requirement be MET?", opts=[
   ("No &mdash; any deficiency makes the requirement NOT MET",False,"Too absolute. The Assessment Guide contemplates both enduring exceptions with documented mitigations and temporary deficiencies covered by operational plans of action."),
   ("Yes, if the deficiency is temporary and covered by an operational plan of action documented in the SSP",True,"Note that this instrument is distinct from the POA&M supporting conditional status &mdash; the two are routinely conflated, and they operate at different points in the process."),
   ("Only if the requirement is worth 1 point",False,"Point values belong to the DoD Assessment score and have nothing to do with the MET determination."),
   ("Only with the Contracting Officer's written concurrence",False,"No such concurrence is contemplated in the determination process."),
  ]),
  dict(stem="Meridian maps its unsegmented CORP-LAN / ENG-LAN routing to 3.13.3. What is the better mapping?", opts=[
   ("3.13.5, publicly accessible subnetworks",False,"That addresses separating publicly accessible components, which is not what is described."),
   ("SC.L2-3.13.1 &mdash; monitor, control, and protect communications at external and key internal boundaries",True,"What is described is a failure of boundary protection at a key internal boundary. It is also worth 5 points rather than 1, so the correction raises the deduction."),
   ("3.13.3 is correct &mdash; it addresses network separation",False,"3.13.3 separates user functionality from system management functionality. That is a different idea from segmenting untrusted endpoints from CUI servers."),
   ("3.1.3, control the flow of CUI",False,"Arguable, and it addresses information flow enforcement rather than boundary protection. 3.13.1 is the cleaner call on these facts."),
  ]),
  dict(stem="During a cross-presentation an opposing team challenges your determination and produces evidence you had not seen. What should happen?", opts=[
   ("Hold the determination &mdash; changing it undermines the team's credibility",False,"A team that never concedes anything has stopped assessing and started defending."),
   ("Change the determination &mdash; new information should move a call",True,"Distinguish new information, which should change your call, from pressure, which should not. Conceding to evidence is the discipline; conceding to insistence is the failure."),
   ("Refer it to the instructor to arbitrate",False,"Arbitration happens against the Assessment Guide text, and here there is nothing to arbitrate &mdash; new evidence has been produced."),
   ("Record both determinations and let the report note the disagreement",False,"A report carries a determination, not a disagreement between assessors about what the evidence shows."),
  ]),
  dict(stem="Which is a proper evidence citation supporting a MET determination?", opts=[
   ("\"Discussion with IT\"",False,"Names neither the person, the date, nor the subject. It is not a citation."),
   ("\"Interview with T. Nakamura, 14 March, on privileged account inventory; access control matrix v1.2 §3\"",True,"Names the method, the individual, the date, the subject, and the corroborating artifact. A reader could go and check it."),
   ("\"The control is in place per the SSP\"",False,"\"It is in the SSP\" is the belief that having a document means the control is implemented. The SSP is a claim about the environment, not evidence of it."),
   ("\"Observed during the walkthrough\"",False,"No object, no date, no detail of what was observed. It cannot be verified or overturned."),
  ]),
  dict(stem="Meridian claims 3.10.3 (escort visitors) is N/A because \"no visitors access the server room.\" What defeats this?", opts=[
   ("Nothing &mdash; if no visitors enter, the requirement does not apply",False,"The premise is an assertion by the party being assessed, and it is contradicted elsewhere in the environment."),
   ("The Huntsville site has no visitor log and delivery drivers come and go",True,"The claim also confines itself to the server room, while the requirement concerns the organization's facilities within the scope. And an unlogged site cannot evidence who did or did not enter."),
   ("3.10.3 may never be N/A under any circumstances",False,"Overstated. What is true is that 3.10.3 is on the list that may never be placed on a POA&M, which is a different rule."),
   ("The requirement is automatically MET where a facility is small",False,"No size exemption exists anywhere in the model."),
  ]),
  dict(stem="Why does knowing each domain's characteristic small-contractor failure pattern help an assessor?", opts=[
   ("It allows determinations to be made efficiently without collecting evidence",False,"The opposite of what an assessor does. A pattern is a hypothesis, not a determination."),
   ("It tells you where to look first, without telling you what you will find",True,"Useful for planning evidence requests and interview questions. It becomes dangerous the moment it substitutes for looking."),
   ("It establishes the severity of any finding in that domain",False,"Severity follows from the requirement and the exposure in the specific environment."),
   ("It identifies which requirements may be scoped out",False,"Scoping follows the asset categories, not the likelihood of failure."),
  ]),
 ],
)
