# -*- coding: utf-8 -*-
"""Manuscript source — Lessons 7, 8, 9, 10."""

L7 = dict(
 file="lesson07.html", short="L7 — Scoring, SPRS & the Incident Clock", num_label="Lesson 7",
 eyebrow="Day 4 &middot; Afternoon &middot; DoD Assessment Methodology &middot; DFARS 252.204-7012",
 title="Scoring, SPRS, and the Incident Clock",
 lead=("Determinations become a number. The number is posted to SPRS, read by a contracting officer, and affirmed "
       "under signature by a named official. An arithmetic slip here is not a rounding error &mdash; it is a "
       "false statement in a federal system. Then a device goes missing, and you decide whether a 72-hour clock "
       "has started."),
 chips=["Day 4 &mdash; PM","~3 hours","<strong>110 to &minus;203</strong>","Tool: SPRS Calculator"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Calculate","Calculate a NIST SP 800-171 DoD Assessment score using the 5, 3, and 1 point weighting, from a maximum of 110 to a floor of &minus;203, including the two partial-credit exceptions."),
  ("Distinguish","Distinguish the DoD Assessment score from the CMMC certification determination, and say what each is for."),
  ("Explain","Explain what a posted SPRS score commits a company to, and who personally carries that commitment."),
  ("Rule","Rule on whether an incident triggers the DFARS 252.204-7012 72-hour obligation, state when the clock starts, and defend the decision against the strongest counter-argument."),
  ("Identify","Identify what a contractor must hold in order to file a report at all."),
 ],
 vocab=[
  ("DoD Assessment Methodology","The instrument that produces the SPRS score. Start at 110 and deduct 5, 3, or 1 per unimplemented requirement. A strategic assessment instrument &mdash; not the CMMC certification assessment."),
  ("Basic / Medium / High assessment","The three DoD Assessment types under DFARS 252.204-7020. Basic is a contractor self-assessment; Medium and High are government-conducted, at increasing rigour."),
  ("The floor","&minus;203. What you get by implementing nothing: the weighted deductions total far more than 110. Negative scores are not computational errors and contractors do post them."),
  ("Partial credit","Exists for exactly two requirements &mdash; 3.5.3 (multifactor authentication) and 3.13.11 (FIPS-validated encryption). Everywhere else the deduction is all or nothing."),
  ("Cyber incident","Actions that result in an actual or potentially adverse effect on an information system or the information residing in it. The threshold is <em>potentially</em> adverse."),
  ("Rapid report","The 72-hour report to DoD via DIBNet required by DFARS 252.204-7012(c)(1), running from discovery."),
  ("Assessment of record","The current DoD Assessment posted in SPRS, which DFARS 252.204-7019 and -7020 make a condition of award."),
 ],
 sections=[
  dict(title="Two different things that both look like scoring", html="""
<div class="warnbox"><div class="warn-label">Keep these separate from the first minute</div>
<p>A <strong>CMMC assessment determination</strong> is binary at the objective level. Every objective is MET or NOT
APPLICABLE, or the requirement is NOT MET. There is no partial credit.</p>
<p>The <strong>DoD Assessment Methodology score</strong> is a weighted 110-point scale with deductions of 5, 3, or 1
&mdash; and two requirements where partial credit does exist.</p>
<p>These are different instruments serving different purposes, and candidates conflate them every year.</p></div>
<p>The methodology exists because DoD needed a way to compare the security posture of thousands of contractors at
acquisition time, quickly, from self-reported data. It is a strategic risk instrument. A CMMC certification
assessment is a conformity determination about one organization at one moment. A company can hold a respectable
SPRS score and fail a certification assessment, and the reverse is arithmetically possible too.</p>"""),
  dict(title="The weighting, and why it is what it is", html="""
<p>Start at 110 and subtract. The weighting reflects what an unimplemented requirement would let an attacker do
&mdash; not how hard the requirement is to satisfy.</p>
<div class="tw"><table>
<thead><tr><th>Value</th><th>What it covers</th><th>Examples</th></tr></thead>
<tbody>
<tr><td><strong>5 points</strong></td><td>Requirements whose absence renders other controls ineffective or permits significant exploitation or exfiltration</td><td>Limiting system access to authorized users; establishing baseline configurations; incident-handling capability; controlling removable media; vulnerability scanning</td></tr>
<tr><td><strong>3 points</strong></td><td>Requirements with a specific and confined security effect</td><td>Limiting access to CUI on system media; encrypting CUI on mobile devices; least privilege; tracing actions to individual users</td></tr>
<tr><td><strong>1 point</strong></td><td>The remaining derived requirements, with limited or indirect effect</td><td>Preventing reuse of identifiers for a defined period; developing and updating the System Security Plan</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">The two partial-credit exceptions &mdash; and only these two</div>
<div class="tw"><table>
<thead><tr><th>Requirement</th><th>Deduct 3</th><th>Deduct 5</th></tr></thead>
<tbody>
<tr><td><strong>3.5.3</strong> &mdash; Multifactor authentication</td><td>MFA implemented for remote <em>and</em> privileged users, but not for the general user</td><td>MFA not implemented for any users</td></tr>
<tr><td><strong>3.13.11</strong> &mdash; FIPS-validated encryption</td><td>Encryption is employed but is not FIPS validated</td><td>Encryption is not employed</td></tr>
</tbody></table></div>
<p>Every other requirement is all or nothing. The temptation to award partial credit elsewhere, because an
organization has &ldquo;mostly&rdquo; done something, is the most common scoring error there is.</p></div>
<div class="in-practice"><div class="ip-label">The floor</div>
<p>The maximum is 110. The minimum is <strong>&minus;203</strong>, which is what you get by implementing nothing:
the weighted deductions total far more than 110. A negative score is not a computational error, and contractors do
post them.</p></div>"""),
  dict(title="The 3.5.3 trap, worked", html="""
<p>Meridian's gap G-01 reads: <em>MFA on Microsoft 365 only; PLM, file server, domain controller RDP, VPN,
QuickBooks, and the backup NAS all single-factor.</em> What is the deduction?</p>
<p>A substantial minority answer <strong>3</strong>, reasoning that MFA is partly implemented. Read the exception
precisely: the 3-point treatment requires MFA for remote <strong>and</strong> privileged users. Meridian has
neither &mdash; the SSL VPN is remote access with no MFA, and domain controller RDP is privileged access with no
MFA. Microsoft 365 alone earns nothing under the exception.</p>
<p><strong>Deduct 5.</strong></p>
<div class="tip"><div class="tip-label">Exam tip</div>
<p>The exception is a conjunction, not a spectrum. &ldquo;Some MFA exists&rdquo; is not the test. Ask specifically:
is MFA in place for remote users? Is it in place for privileged users? Both yes and the general user missing is a
3. Either one missing is a 5.</p></div>"""),
  dict(title="Scoring Meridian, gap by gap", html="""
<p>Meridian&rsquo;s eight seeded findings, expanded to the requirement lines they actually touch, as the company
maps them. Look each point value up in the methodology; do not work from memory or from a summary someone else
made.</p>
<div class="tw"><table>
<thead><tr><th>Gap</th><th>Requirement</th><th>Value</th><th>Deduct</th><th>Note</th></tr></thead>
<tbody>
<tr><td>GAP-01</td><td>3.5.3</td><td>5 / partial</td><td><strong>5</strong></td><td>The trap. Neither remote nor privileged MFA exists.</td></tr>
<tr><td>GAP-02a</td><td>3.1.1</td><td>5</td><td>5</td><td>Six accounts belonging to separated employees.</td></tr>
<tr><td>GAP-02b</td><td>3.1.2</td><td>5</td><td>5</td><td>Shared Global Admin with no individual owner.</td></tr>
<tr><td>GAP-03a</td><td>3.3.1</td><td>5</td><td>5</td><td>Basic, 5 points.</td></tr>
<tr><td>GAP-03b</td><td>3.3.2</td><td>3</td><td>3</td><td>Assuming all AU requirements are 5 over-deducts here.</td></tr>
<tr><td>GAP-04</td><td>3.4.2 <em>as mapped</em></td><td>5</td><td>5</td><td>The company describes 3.4.2 as &ldquo;component inventory.&rdquo; It is not &mdash; see the mapping disputes.</td></tr>
<tr><td>GAP-05</td><td>3.12.4 <em>as mapped</em></td><td>1</td><td>1</td><td>A POA&amp;M deficiency mapped to the SSP requirement &mdash; see the mapping disputes.</td></tr>
<tr><td><strong>GAP-06</strong></td><td>3.17.1 / 3.17.2</td><td>&mdash;</td><td><strong>0</strong></td><td><strong>These practices do not exist in Rev 2.</strong></td></tr>
<tr><td>GAP-07a</td><td>3.6.1</td><td>5</td><td>5</td><td>Basic, 5 points.</td></tr>
<tr><td>GAP-07b</td><td>3.6.2</td><td>5</td><td>5</td><td>Basic, 5 points.</td></tr>
<tr><td>GAP-08</td><td>3.13.3 <em>as mapped</em></td><td>1</td><td>1</td><td>3.13.1 would be 5 &mdash; see the mapping disputes.</td></tr>
<tr><td>GAP-09</td><td>3.2.2</td><td>5</td><td>5</td><td>No role-based training for privileged users or MSP technicians.</td></tr>
<tr><td>GAP-10</td><td>3.7.5</td><td>5</td><td>5</td><td>Derived, 5 points.</td></tr>
<tr><td>GAP-11</td><td>3.10.3</td><td>1</td><td>1</td><td>1 point &mdash; and POA&amp;M-ineligible under &sect;170.21.</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">GAP-06 is the most instructive line on the sheet</div>
<p>Practices <strong>3.17.1 and 3.17.2</strong> belong to the SR &mdash; Supply Chain Risk Management &mdash; family
in NIST SP 800-171 <strong>Rev 3</strong>. CMMC Level 2 is anchored to <strong>Rev 2</strong>, which has fourteen
families and no SR family at all.</p>
<p>So there is nothing to deduct. That does not make the gap harmless &mdash; an MSP with unaudited domain admin and
three CUI-handling suppliers with no flow-down is among the most serious exposures in the company. It is a
<strong>DFARS 252.204-7012(m) flow-down violation and an ESP treatment failure under 32 CFR &sect;170.19</strong>,
and its access-control consequences are already scored at 3.1.1, 3.5.3 and 3.7.5.</p>
<p>Score it zero and write it up as a contractual finding. An assessor who deducts against a requirement that does
not exist in the applicable revision has produced a number nobody can defend.</p></div>
<div class="in-practice"><div class="ip-label">The arithmetic</div>
<p>Starting score <strong>110</strong>. Total deductions <strong>51</strong>. Computed score <strong>59</strong>.
59 &divide; 110 = <strong>0.536</strong> &mdash; well short of the 0.8 POA&amp;M eligibility threshold. Meridian
cannot achieve even Conditional Level 2 status on this gap list.</p></div>
<div class="warnbox"><div class="warn-label">Two things a strong answer adds</div>
<p><strong>The score is not the only gate.</strong> PE.L2-3.10.3 is NOT MET and is one of the six requirements that
may never be placed on a POA&amp;M. CA.L2-3.12.4 is arguably NOT MET too, on the SSP&rsquo;s own &ldquo;needs
update&rdquo; status. Even above 88, those must be MET outright before any status could issue.</p>
<p><strong>59 is an optimistic ceiling, not a floor.</strong> Eight seeded findings expanded across fourteen lines
is a gap analysis of selected areas, not an assessment of 110 requirements. Media disposal, physical access at
Dayton, and the uncontrolled upload path into AWS GovCloud are three the list never reaches. Any figure between
<strong>50 and 59</strong> with the reasoning shown is correct; a bare number is not.</p></div>"""),
  dict(title="What the score commits a company to", html="""
<p>Meridian eventually submitted a score of <strong>88</strong> to SPRS. Priya Mehta prepared it from a
spreadsheet the consultant provided. She did not check the arithmetic. Marcus Ellison signed it.</p>
<p>Ellison affirmed 88 on the basis that &ldquo;Dennis and the consultant said that was the number.&rdquo; She did
not verify it and would not know how. She does not know what an Affirming Official is personally liable for.</p>
<div class="tw"><table>
<thead><tr><th>Element</th><th>What it involves</th></tr></thead>
<tbody>
<tr><td>Where it is posted</td><td>SPRS, as the assessment of record</td></tr>
<tr><td>Why it matters at award</td><td>A condition of award under DFARS 252.204-7019 and -7020; the Contracting Officer verifies it</td></tr>
<tr><td>Who affirms</td><td>A senior official of the OSC with authority to bind it &mdash; not the IT manager, not the consultant, not the assessor</td></tr>
<tr><td>What it attests</td><td>Continued compliance. A present-tense statement, not a memory of the assessment</td></tr>
<tr><td>The exposure</td><td>An affirmation that is not true is a false statement in a federal system, with False Claims Act consequences attaching personally to the official who signed</td></tr>
</tbody></table></div>
<p>Hold Ellison in mind on Friday when you write the sustainment section. Nobody at Meridian behaved
dishonestly. The number is still wrong, and she is still the person who attested to it.</p>"""),
  dict(title="The incident clock: INC-003", html="""
<div class="in-practice"><div class="ip-label">Wednesday, 09:40</div>
<p>Trevor Nakamura, reconciling VPN accounts against the HR separation list in preparation for the assessment, finds
that one of the six stale accounts &mdash; <code>jhollis</code>, belonging to a design engineer who left in November
&mdash; shows <strong>successful VPN authentications on four dates over the past six weeks</strong>, the most recent
eleven days ago. Each session lasted between twenty and ninety minutes.</p>
<p><strong>Known:</strong> the account was never disabled. It held membership in the engineering security group,
granting read and write access to the CUI tree on SYS-003 and to the Arena PLM. The VPN has no MFA. The password was
last set fourteen months ago.</p>
<p><strong>Not known:</strong> who authenticated. Whether anything was accessed, opened or copied. Whether the
sessions came from the former employee, from someone using credentials he left behind, or from an unrelated party.
The FortiGate retains authentication events; SYS-003 and SYS-004 retain 30 days and are not reviewed, so file-level
records for three of the four sessions have already rolled off.</p>
<p><strong>Nakamura&rsquo;s position:</strong> &ldquo;It is almost certainly Jared. He was finishing a handover and
he is a good guy. Nothing has been taken &mdash; we would see it.&rdquo;</p></div>
<h3>The determination</h3>
<div class="tw"><table>
<thead><tr><th>Question</th><th>Answer</th></tr></thead>
<tbody>
<tr><td><strong>Does it trigger?</strong></td><td><strong>Yes.</strong> A cyber incident includes actions
resulting in an actual or <em>potentially</em> adverse effect on an information system or the information residing in
it. Unauthorised authentication to a network holding CUI, by an account that should not exist, with write access to
the CUI store, is not merely potential &mdash; it is actual unauthorised access. The open question is only what was
done with it.</td></tr>
<tr><td><strong>Which paragraph</strong></td><td>252.204-7012(c)(1) for the rapid report; the definition of cyber
incident at (a) supplies the threshold. Media preservation under (e) attaches once reported &mdash; urgently here,
because logs are actively rolling off.</td></tr>
<tr><td><strong>When the clock starts</strong></td><td>72 hours from <em>discovery</em> &mdash; Wednesday 09:40, when
Nakamura identified the authentications. Not from the first session six weeks ago, and not from the separation date.
Document the gap: a contracting officer will ask how an account authenticated four times unnoticed, and the answer is
evidence about the monitoring capability rather than about the clock.</td></tr>
<tr><td><strong>Who decides</strong></td><td>Not Nakamura. There is an IRP naming an Incident Commander, and it is
three years stale and lists a departed employee &mdash; so in practice the CISO and the CEO, who is also the
Authorizing Official, must be involved. That the decision has nowhere to go is itself a finding under
IR.L2-3.6.1.</td></tr>
<tr><td><strong>What preservation now requires</strong></td><td>Images of affected systems and relevant monitoring
data for at least 90 days from the report. With 30-day retention and no review, <strong>the preservation obligation
is already partly impossible to satisfy</strong> for the earlier sessions. Preserving what remains is urgent, and it
is the first thing an assessor would ask whether anyone did.</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">The counter-argument, and the answer</div>
<p>Nakamura&rsquo;s position deserves to be taken seriously before it is dismantled: it is almost certainly the
former employee finishing a handover; there is no evidence of exfiltration; and reporting an incident involving a
trusted ex-colleague feels disproportionate.</p>
<p>The threshold is &ldquo;potentially adverse,&rdquo; not &ldquo;malicious,&rdquo; and reporting is not an
accusation. An authorised handover would have been performed on an authorised account. And &ldquo;almost certainly
Jared&rdquo; is an inference about identity the environment cannot support: with no MFA, the authentication proves
possession of a credential and nothing whatever about who held it.</p>
<p>His second claim &mdash; &ldquo;nothing has been taken, we would see it&rdquo; &mdash; is an appeal to the absence
of evidence. Ask whether Meridian has the capability to have observed what he says has not happened. It does not: no
file-access review, no SIEM, no correlation, and 30-day retention that has already consumed most of the record.</p>
<p><em>Could this organization know what it claims to know?</em> That is the question you will ask for the rest of
your career.</p></div>"""),
 ],
 case=dict(tag="Meridian &middot; Day 4 Afternoon &middot; Deliverable D7",
   title="Compute the score, then rule on the incident",
   html="""
<p>The <strong>SPRS Score Calculator</strong> loads the thirteen gaps as Meridian maps them. Assign a point
value to each, watch the running total, and see the eligibility threshold move against you. The tool checks each
value against the methodology and flags the two over-deductions and the one trap that catch most people.</p>
<p>Then defend three deductions in writing, at least one of which must be a deduction you believe the company has
mapped to the wrong requirement. State your mapping and why. Then say, in three or four sentences, what your score
does and does not represent &mdash; be precise about what a gap list is, and about the difference between this
figure and a certification determination.</p>
<p>Part B is INC-003, issued cold. Rule on it, name the clause paragraph, state when the clock starts and why, say
who is entitled to make the call, and say what Meridian must hold in order to file at all. Then state the
strongest argument against your decision and answer it. <strong>A decision that does not engage the other side is
an opinion.</strong></p>""",
   actions=[("Open the SPRS Calculator &rarr;","sprs-calculator.html",False),
            ("Domain Worksheet","domain-worksheet.html",True)]),
 kc=[
  dict(stem="MFA is enforced on the cloud tenant for all users, but not on the VPN (remote access) or on domain controller RDP (privileged access). What is deducted under 3.5.3?", opts=[
   ("0 &mdash; MFA is implemented",False,"Implemented somewhere is not implemented. The requirement reaches the assessment scope."),
   ("3 &mdash; partial credit applies",False,"The most common wrong answer here. Partial credit requires MFA for remote <em>and</em> privileged users. Neither is present."),
   ("5 &mdash; neither remote nor privileged users have MFA",True,"The exception is a conjunction, not a spectrum. Either one missing takes you to the full deduction."),
   ("1 &mdash; a derived requirement with limited effect",False,"3.5.3 is a 5-point requirement, and the partial-credit exception is the only variation available."),
  ]),
  dict(stem="Encryption is employed to protect CUI but is not FIPS validated. What is deducted under 3.13.11?", opts=[
   ("0",False,"Non-validated encryption does not satisfy the requirement."),
   ("3",True,"The second of the two partial-credit requirements. 5 if encryption is not employed at all. Note the interaction with POA&M rules: 3.13.11 is POA&M-eligible only where encryption is used but not FIPS validated."),
   ("5",False,"5 applies where no encryption is employed. Here it is employed."),
   ("It cannot be scored until validation is confirmed",False,"The methodology contemplates exactly this state and prices it at 3."),
  ]),
  dict(stem="Meridian has never submitted a SPRS score. Its gap list includes this as G-13, mapped to DFARS 252.204-7019. What is the deduction?", opts=[
   ("5 &mdash; it is a significant failure",False,"Significance is not the test. The methodology scores NIST SP 800-171 requirements."),
   ("1 &mdash; it is an administrative requirement",False,"Still not a NIST requirement, so no point value attaches at any level."),
   ("0 &mdash; DFARS 252.204-7019 is not a NIST SP 800-171 requirement",True,"Failing to submit a score is a contractual violation, not a scored one. Students who deduct for it have not understood what the instrument measures."),
   ("It cannot be scored; the assessment is invalid without a prior score",False,"A missing prior score does not invalidate an assessment."),
  ]),
  dict(stem="A contractor implements nothing at all. What score does the DoD Assessment Methodology produce?", opts=[
   ("0",False,"A natural guess, and the scale does not floor at zero."),
   ("−110",False,"That would be the arithmetic if every requirement were worth 1 point. They are not."),
   ("−203",True,"The weighted deductions total far more than 110. A negative score is not a computational error, and contractors do post them."),
   ("The score is undefined below zero",False,"It is well defined, and −203 is the stated floor."),
  ]),
  dict(stem="A stale VPN account belonging to a separated employee is found to have authenticated four times over six weeks; the most recent session was eleven days ago and the discovery is made Wednesday at 09:40. When does the 72-hour clock start?", opts=[
   ("At the first session six weeks ago",False,"The clause runs from discovery, not from occurrence. The six-week gap belongs in the timeline as evidence about monitoring, and it does not move the clock."),
   ("Wednesday at 09:40, on discovery",True,"72 hours from discovery. Document the six-week gap: a contracting officer will ask how an account authenticated four times unnoticed, and the answer speaks to the monitoring capability rather than to the deadline."),
   ("When forensic analysis confirms whether CUI was accessed",False,"Confirmation is not the trigger. This is the reading contractors act on, and it is wrong &mdash; here it is also impossible, since most of the file-access record has already rolled off."),
   ("It does not start &mdash; the sessions were probably the former employee",False,"The threshold is a potentially adverse effect. And with no MFA, the authentication proves possession of a credential and nothing about who held it."),
  ]),
  dict(stem="Nakamura argues no report is needed because \"nothing has been taken — we would see it.\" What is the assessor's strongest response?", opts=[
   ("He may be right, so the decision should be deferred pending investigation",False,"Deferring past 72 hours is itself the violation, and the clock does not pause for an investigation."),
   ("The organization has no capability to have observed what he says has not happened",True,"No PLM session logging, no log review, no defined retention. His position rests on an inference from absence of evidence, and absence of evidence proves nothing when nothing is looking."),
   ("His seniority does not make him a designated decision-maker",False,"True, and it is a separate point. The substantive answer is that his claim is unsupportable on the organization's own capability."),
   ("Reporting is mandatory for all lost devices regardless of circumstances",False,"Overstated. The test is whether the incident meets the clause threshold, and here it does &mdash; but not because every lost device does."),
  ]),
  dict(stem="What must Meridian hold in order to file a cyber incident report at all?", opts=[
   ("A DIBNet account and a CAGE code",False,"Necessary and not sufficient. One further item is required and Meridian has never obtained it."),
   ("A DoD-approved medium assurance certificate",True,"Without it the report cannot be filed. Meridian has never obtained one, which means it will discover this at hour 70 of a 72-hour clock."),
   ("A completed forensic report",False,"The rapid report precedes forensics. Waiting for analysis is how the clock is missed."),
   ("Written authorisation from the Contracting Officer",False,"No such authorisation is contemplated; the obligation runs to the contractor."),
  ]),
  dict(stem="Which best distinguishes the DoD Assessment score from a CMMC certification determination?", opts=[
   ("They are the same instrument, expressed differently",False,"Conflating them is the error this session exists to prevent."),
   ("The score is a weighted strategic risk instrument; the certification determination is a binary conformity determination at the objective level",True,"Different purposes, different mechanics, different consequences. A company can hold a respectable score and still fail certification &mdash; and two of the requirements that block certification are worth one point each."),
   ("The score applies to Level 1 and the determination to Level 2",False,"The DoD Assessment Methodology concerns the 110 NIST requirements, which is Level 2 territory."),
   ("The score is produced by the C3PAO and the determination by DoD",False,"Reversed and wrong in both directions. The score is typically a contractor self-assessment; the certification determination is the C3PAO's."),
  ]),
  dict(stem="A student computes Meridian's score as 59 and stops. What is missing?", opts=[
   ("Nothing &mdash; 59 is the correct figure from the gap list",False,"It is the correct arithmetic and an incomplete answer. A bare number is what gets posted to SPRS in the real world."),
   ("A statement that 59 is an optimistic ceiling, since eight seeded findings are not an assessment of 110 requirements",True,"A real assessment examines all 110 and would find more NOT MET &mdash; media disposal, Dayton physical access, and the uncontrolled AWS upload path are three the list never reaches. Also worth stating: the score is not the only gate, because a POA&M-ineligible requirement is already failing."),
   ("Conversion of the score to a percentage",False,"59 ÷ 110 = 0.536 matters for the POA&M threshold, and it is arithmetic rather than the missing insight."),
   ("A comparison to the industry average",False,"No such benchmark governs anything in the methodology."),
  ]),
  dict(stem="Marcus Ellison affirmed a score of 88 because \"Dennis and the consultant said that was the number.\" What is the assessor's finding?", opts=[
   ("No finding &mdash; the Affirming Official may rely on technical staff",False,"Reliance is not the standard. The affirmation is a present-tense attestation of continued compliance by someone with authority to bind the organization."),
   ("The affirmation is a present-tense attestation she did not verify, and the exposure attaches to her personally",True,"An affirmation that is not true is a false statement in a federal system with False Claims Act consequences for the signer. Nobody behaved dishonestly, the number is still wrong, and she is still the person who attested to it."),
   ("The consultant is liable for the incorrect figure",False,"A consultant cannot bind the OSC and does not carry the affirmation exposure."),
   ("The finding belongs against the IT Manager for supplying the number",False,"Supplying a wrong number is a contributing failure. The attestation, and its exposure, sit with the signer."),
  ]),
 ],
)

L8 = dict(
 file="lesson08.html", short="L8 — Conducting the Assessment & Reporting", num_label="Lesson 8",
 eyebrow="Day 5 &middot; Morning &middot; CAP Phases 2&ndash;3 &middot; The mock assessment",
 title="Conducting the Assessment and Reporting Findings",
 lead=("The summative session. No lecture. Eight months have passed inside the case: the last C3PAO declined the "
       "engagement and &mdash; correctly &mdash; gave Meridian no help getting ready. The company hired a "
       "consultant, worked its plan, spent about $210,000, and engaged a different firm. You are that firm. Some "
       "of what you are about to read is real. Some of it is a document produced to close a line on a plan."),
 chips=["Day 5 &mdash; AM","~3 hours","<strong>No scaffolding</strong>","9 documents &middot; 6 interviews"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Execute","Execute a Level 2 assessment against a supplied evidence package under time constraint."),
  ("Run","Run the in-brief, daily checkpoint, and out-brief structure that CAP Phases 2 and 3 require."),
  ("Conduct","Conduct interviews that elicit evidence rather than confirmation."),
  ("Write","Write an evidence request that returns what you actually need."),
  ("Render","Render final determinations and identify the findings that follow from them."),
  ("Produce","Produce a findings report that is defensible against the Assessment Guide when challenged."),
 ],
 vocab=[
  ("In-brief","The CAP-prescribed opening of Phase 2. The Lead CCA must cover a defined minimum, and minutes or a detailed summary must be kept."),
  ("Daily checkpoint","Required at the end of each assessment day: progress, challenges, and what is needed next. Not a negotiation and not a preview of the result."),
  ("Out-brief","Delivery of assessment results. Results must be compiled and quality-reviewed beforehand by a CCA not on the team who has had no contact with it during the assessment."),
  ("Re-evaluation window","Ten business days, under 32 CFR &sect;170.17, in which limited deficiencies may be re-evaluated."),
  ("Finding","What you write about a NOT MET: which objective failed, what evidence you examined, what was missing, and a severity."),
  ("Not provided","One of the three outcomes for every requested item &mdash; alongside received-and-responsive and received-and-not-responsive. The third category is a finding in its own right."),
 ],
 sections=[
  dict(title="Two rules for the session", html="""
<div class="warnbox"><div class="warn-label">Non-negotiable</div>
<p><strong>You may not tell Meridian how to fix anything.</strong> Not in the checkpoint, not in an interview,
not in the out-brief, and not when the chief executive asks you directly and reasonably. She will.</p>
<p><strong>You may not speculate about the outcome.</strong> Not &ldquo;this is looking good,&rdquo; not &ldquo;you
are close.&rdquo; The CAP prohibits it in Phase 1 and the reasoning holds throughout: an assessment result is a
determination, not a running commentary.</p></div>"""),
  dict(title="Running the in-brief", html="""
<p>The CAP sets out what the Lead CCA must address at minimum. Your in-brief is assessed on whether you covered it.</p>
<ol>
<li>Introduce the assessment team and invite the OSC to introduce its people.</li>
<li>Confirm the CMMC assessment scope.</li>
<li>Explain the Level 2 assessment procedures under 32 CFR &sect;170.17(c).</li>
<li>Review the assessment schedule.</li>
<li>Reconfirm the absence of, or disclose, any organizational or individual conflicts of interest.</li>
<li>Inform the OSC of its right to appeal and describe the C3PAO's appeals process.</li>
<li>Invite questions.</li>
</ol>
<p>Minutes or a detailed summary must be kept. Nominate someone to take them before you start.</p>
<h3>The checkpoint</h3>
<p>A daily checkpoint with the OSC point of contact is required at the end of each assessment day: progress,
challenges, and what you need next. It is not a negotiation and it is not a preview of the result.</p>
<p>The OSC will push back, and pushing back is legitimate &mdash; an organization that accepts every preliminary
finding without question is not paying attention. Your job is to distinguish <strong>new information</strong>, which
should change your call, from <strong>pressure</strong>, which should not.</p>"""),
  dict(title="The evidence package", html="""
<p>Nine documents, supplied in good faith. Read each one against the requirement it is offered for, and then read it
against the other eight.</p>
<div class="tw"><table>
<thead><tr><th>#</th><th>Document</th><th>What it says</th><th>What to notice</th></tr></thead>
<tbody>
<tr><td>1</td><td>System Security Plan v3.0, three months ago</td>
<td>Rewritten with consultant support. Boundary section now names systems SYS-001 through SYS-014 and both sites. Control implementation described for all 110 requirements.</td>
<td>It describes the environment as it was <em>designed</em>. Cross-check the boundary against the asset inventory (Doc 3) and against what interviews reveal about the AWS upload path, which still appears nowhere.</td></tr>
<tr><td>2</td><td>POA&amp;M, exported this week from the GCC High tenant</td>
<td>Now inside the boundary, version-controlled, eleven items with owners and target dates. Seven marked Complete.</td>
<td>The storage problem is genuinely fixed &mdash; say so. <strong>No closure evidence is attached to any item marked Complete</strong>, and two target dates have been revised twice without comment.</td></tr>
<tr><td>3</td><td>Asset Inventory v1.0, four months ago</td>
<td>The artifact whose absence blocked Phase 1 last time. 164 line items across both sites.</td>
<td>Compare the count against the SSP and against what you observe. The three decommissioned drives in the server room are not on it, and neither are the CNC-side systems at Acuitas &mdash; which is correct, and worth confirming they thought about it rather than missed it.</td></tr>
<tr><td>4</td><td>MFA Status Report, exported this week</td>
<td>M365 GCC High: yes. FortiGate SSL VPN: <strong>yes &mdash; added five months ago</strong>. Domain controller RDP: no. SYS-003 file server: no. AWS GovCloud: root yes, IAM users partial.</td>
<td>Honest, current, and the VPN gap is genuinely closed. Now work the requirement again: does <em>network access to privileged accounts</em> have MFA? Domain controller RDP is the answer, and it is still no.</td></tr>
<tr><td>5</td><td>Audit Log Review Records &mdash; five monthly records</td>
<td>Each one page. Reviewer named, date, sources listed, and a short note of what was examined. Retention now set to 180 days.</td>
<td>Materially better than anything the company had before. Nothing exists prior to five months ago, and the records begin one month after the consultant arrived. Ask what happens when the consultant leaves.</td></tr>
<tr><td>6</td><td>Patch Compliance Report, two weeks ago</td>
<td>All 14 Dayton and 6 Huntsville engineering workstations enrolled in a configuration management tool. 19 of 20 fully current.</td>
<td>Strong evidence. Which machine is the twentieth, why, and is there a documented exception? The report does not say, and the answer is on the shop floor.</td></tr>
<tr><td>7</td><td>Incident Response Plan v2.0, four months ago, plus a tabletop record</td>
<td>Rewritten. DFARS 72-hour reporting language now present with the DIBNet process. Contact roster refreshed. One tabletop exercise recorded, three months ago.</td>
<td>Read the tabletop scenario. It exercises ransomware on a workstation. Neither of the company&rsquo;s two actual historical incidents &mdash; nor the stale-account authentication &mdash; resembles it.</td></tr>
<tr><td>8</td><td>ClearPath Master Services Agreement, Addendum One, signed two months ago, with a Customer Responsibility Matrix</td>
<td>DFARS 252.204-7012 incorporated and flowed down. A CRM now exists, allocating responsibilities across 110 requirements.</td>
<td>Read the CRM against Doc 4. It assigns MFA enforcement for administrative access to <em>Meridian</em>, and ClearPath technicians still reach domain admin over a VPN using a shared account. The document allocates a responsibility the company has not discharged.</td></tr>
<tr><td>9</td><td>SPRS Score Worksheet &mdash; 94, submitted six weeks ago</td>
<td>Working attached. Partial credit claimed on 3.5.3. Nine requirements marked closed per POA&amp;M items. Two N/A claims.</td>
<td>Every one of those moves is arguable and several are wrong. This is the document to work last and hardest &mdash; and note who signed it.</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">The pattern to look for</div>
<p>This is a company that has genuinely improved, which makes it a harder assessment than the one you scoped on
Wednesday. Most of these documents are real work. The failures are now in the <em>joins</em>: a CRM that allocates a
duty nobody performed, a POA&amp;M whose completions are unevidenced, an SSP that describes a designed environment
rather than the operating one, and a tabletop that exercises a scenario the company has never faced while ignoring
two it has.</p>
<p>A documentation-led assessment will pass Meridian. Only reading the documents against each other, and against
what people tell you, will not.</p></div>"""),
  dict(title="Interviews that elicit rather than confirm", html="""
<p>Six people are available and you will not reach all of them. <strong>Choosing who to interview is an assessment
decision and it is assessed as one.</strong> Ask yourself who can tell you something no document can.</p>
<p>Everyone is cooperative and nobody is lying. They will answer the question you asked. Ask a question that invites
agreement and you will get agreement, and you will have learned nothing while believing you learned something.</p>
<div class="tw"><table>
<thead><tr><th>Instead of</th><th>Ask</th></tr></thead>
<tbody>
<tr><td>&ldquo;You review the audit logs monthly, correct?&rdquo;</td><td>&ldquo;Walk me through the last review you did. What did you open?&rdquo;</td></tr>
<tr><td>&ldquo;Is MFA enabled?&rdquo;</td><td>&ldquo;Take me system by system. What happens when you sign in to the PLM?&rdquo;</td></tr>
<tr><td>&ldquo;Do you have an offboarding process?&rdquo;</td><td>&ldquo;The last person who left &mdash; tell me what happened to their accounts, and how you know.&rdquo;</td></tr>
<tr><td>&ldquo;Is the MSP access controlled?&rdquo;</td><td>&ldquo;Walk me through what happens when a ClearPath technician needs to log in. Who approves it, what account do they use, and where would I see a record of it afterwards?&rdquo;</td></tr>
</tbody></table></div>
<h3>Who is in the building</h3>
<ul>
<li><strong>Diana Kowalczyk</strong>, CISO &mdash; owns the SSP, the policies and the POA&amp;M. Competent, candid,
and has been asking for budget for two years. She will tell you what is not fixed if you ask her plainly, and she is
the reason anything improved at all.</li>
<li><strong>Trevor Nakamura</strong>, IT Administrator &mdash; built and runs the environment. Cooperative and
quietly proud. Believes that having a document means the control is implemented, and will say &ldquo;it is in the
SSP&rdquo; as though that settles a question.</li>
<li><strong>Priya Mehta</strong>, Contract Manager &mdash; precise, tracks DFARS clauses on the three prime and
subcontract vehicles rigorously. Has never applied the same discipline downward to suppliers, and does not know what
a Customer Responsibility Matrix commits the company to.</li>
<li><strong>Renata Bauer</strong>, HR Director &mdash; organized about the things anyone has asked her to keep
records of. The offboarding process is email-based and she has never been told that VPN deprovisioning is missing
from it.</li>
<li><strong>Gregory Farris</strong>, FSO and Physical Security Manager &mdash; runs badge access, visitor logs and
media destruction at Dayton, and does it well. Has never visited Huntsville.</li>
<li><strong>Marcus Ellison</strong>, President and CEO, Authorizing Official &mdash; warm, direct, commercially
focused, genuinely likeable. He has spent real money on this. He will apply pressure without meaning it as pressure,
which is what makes him the hardest interview in the room.</li>
</ul>
<div class="in-practice"><div class="ip-label">The choice that separates teams</div>
<p>Six people, forty minutes, and you will not reach them all. <strong>Choosing who to interview is an assessment
decision and it is assessed as one.</strong></p>
<p>Most teams pick Nakamura and Kowalczyk, because they own the systems and the documents. The higher-yield choices
are usually <strong>Bauer</strong> &mdash; who can tell you exactly what the offboarding process does and does not
include, which is the root cause of the finding that started this whole engagement &mdash; and <strong>Farris</strong>,
who will tell you without prompting that he has never seen the Huntsville site, and that the escort policy for MSP
technicians is something he does rather than something written down.</p></div>
<div class="warnbox"><div class="warn-label">Ellison is the ethics test</div>
<p>At some point he will ask, warmly and reasonably: &ldquo;Just tell me what you need to see and we will go and do
it.&rdquo; He may ask what a passing score looks like, or whether you think the company will make it. He has spent
$210,000 and he employs 147 people, and he will mention both.</p>
<p>You must decline, and decline without lecturing her. A team that answers the question has failed the exercise
regardless of how good their determinations are &mdash; and that failure is worth more to them than the finding.</p></div>"""),
  dict(title="The overnight evidence request", html="""
<p>You have one written request and limited time. Everything you fail to ask for, you will not have.</p>
<ul>
<li><strong>Name artifacts, not topics.</strong> Day 3 applies here exactly.</li>
<li><strong>Say which objective each item serves</strong> &mdash; it forces you to check that you need it.</li>
<li><strong>Name the custodian.</strong> At Meridian this is often the same person, which is itself worth noting.</li>
<li><strong>Ask for what would disconfirm the OSC's position</strong>, not only what would confirm it.</li>
</ul>
<div class="in-practice"><div class="ip-label">Read what comes back, not what you hoped would come back</div>
<p>Some of the supplemental material will be responsive. Some will not be. Some of what you asked for will not
exist. For every item you requested, record one of three outcomes: <strong>received and responsive</strong>,
<strong>received and not responsive</strong>, or <strong>not provided</strong>.</p>
<p>A partly responsive answer is the normal case in a real assessment, and it is where assessments quietly fail. A
document arrives, it is roughly on the subject, the schedule is tight, and it gets accepted. The third category is
a finding in its own right.</p></div>"""),
  dict(title="Determinations, findings, and the out-brief", html="""
<p>A <strong>determination</strong> is MET, NOT MET, or NOT APPLICABLE at the objective level. A
<strong>finding</strong> is what you write about a NOT MET: which objective failed, what evidence you examined, and
what was missing. Severity follows from the requirement and the exposure, not from how annoyed you are about it.</p>
<p>Rule on both incidents in Meridian's history &mdash; the October 2023 spearphishing that CrowdStrike blocked,
and the February 2024 lost unencrypted USB drive &mdash; and on anything the interviews surface. <em>One of the two
triggers the DFARS 252.204-7012 obligation and one is genuinely arguable. If you rule the same way on both without
distinguishing them, read them again.</em> Note also that the company filed nothing on either, and that the
non-reporting decisions were made informally with no documented analysis against the clause.</p>
<h3>Quality assurance before the out-brief</h3>
<p>The CAP requires assessment results to be compiled and quality-reviewed before the out-brief, and requires the
quality reviewer to be a CCA who is <strong>not on the assessment team</strong> and who has had <strong>no contact
with it</strong> during the assessment.</p>
<p>Deliver the results. Do not deliver advice. Expect at least one challenge, and be ready to concede &mdash; a team
that never concedes anything has stopped assessing and started defending.</p>
<div class="tip"><div class="tip-label">What the report is really for</div>
<p>Whether a stranger could act on it. A contracting officer, an appeals panel, or the next assessment team should
be able to read it and know exactly what you looked at, what you concluded, and why &mdash; without you in the room
to explain.</p></div>"""),
 ],
 case=dict(tag="Meridian &middot; Day 5 Morning &middot; Deliverable D8",
   title="Run the assessment, write the findings",
   html="""
<p>The case workbench holds the full evidence package, the interview personas, the incident records, and the
findings workspace. Work the two-day sequence in one session:</p>
<ul>
<li><strong>In-brief</strong> &mdash; cover the CAP minimum. Nominate a minute-taker first.</li>
<li><strong>Evidence review</strong> &mdash; nine documents, logged as you go. Do not leave determinations to memory.</li>
<li><strong>Checkpoint</strong> &mdash; brief preliminary findings. Expect pushback on at least one call.</li>
<li><strong>Evidence request</strong> &mdash; one page, artifacts not topics, with the objective and custodian named.</li>
<li><strong>Interviews</strong> &mdash; choose who, and be able to say why. Open questions only.</li>
<li><strong>Determinations and incident rulings</strong> &mdash; objective level, evidence cited.</li>
<li><strong>Out-brief</strong> &mdash; results, not advice. Concede where the evidence moves you.</li>
</ul>
<p>Then write the <strong>Assessment Findings Report</strong>: scope statement, methodology including sampling
values, determinations with evidence cited, findings with severity, incident analysis with clause reasoning, and a
preliminary score with the outcome you would recommend.</p>
<p><strong>Every finding traceable to evidence you actually examined.</strong> If you did not see it, you cannot cite
it. Where evidence was requested and not provided, say so &mdash; absence of evidence is a result and belongs in the
report. And no remediation advice anywhere, including in the recommendation section.</p>""",
   actions=[("Open the case workbench &rarr;","meridian.html",False),
            ("SPRS Calculator","sprs-calculator.html",True),
            ("Domain Worksheet","domain-worksheet.html",True)]),
 kc=[
  dict(stem="A POA&M item is marked \"Complete\" with no closure evidence attached, while the MFA Status Report shows the underlying gap still open. What is the determination on the affected requirement?", opts=[
   ("MET &mdash; the POA&M records the item as closed",False,"A POA&M is the organization's record of its own intentions. Marking an item complete is a claim, not evidence."),
   ("NOT MET, and the POA&M discrepancy is itself worth recording",True,"Three documents disagree about one fact: the SSP claims implementation, the POA&M claims closure, and the status report shows the gap open. The status report is the artifact with the most direct evidentiary value, and the inconsistency belongs in the findings."),
   ("Deferred pending confirmation from the OSC",False,"There is no deferred determination, and the OSC's confirmation would be another assertion."),
   ("MET with a documented deficiency",False,"That treatment requires a temporary deficiency covered by an operational plan of action documented in the SSP. An unevidenced \"Complete\" is not that."),
  ]),
  dict(stem="Who may perform the quality assurance review of assessment results before the out-brief?", opts=[
   ("The Lead CCA who ran the assessment",False,"The reviewer must be independent of the assessment team, which the Lead CCA plainly is not."),
   ("Any CCP employed by the C3PAO",False,"The role requires a CCA, not a CCP."),
   ("A CCA not on the assessment team who has had no contact with it during the assessment",True,"Both conditions matter. Independence of composition and independence of contact are separate requirements, and the second is the one people forget."),
   ("The OSC's Affirming Official",False,"The OSC does not quality-review the assessment of itself."),
  ]),
  dict(stem="Meridian's Incident Response Plan names three response team members, two of whom left the company more than a year ago, and records no exercise. Against IR.L2-3.6.1, what follows?", opts=[
   ("MET &mdash; an operational incident-handling capability is documented",False,"Documented is not the test. The requirement is a capability, and a plan naming people who do not work there does not establish one."),
   ("NOT MET &mdash; the plan does not evidence an operational capability",True,"A plan that has never been exercised and assigns roles to departed staff is adequate as a document and insufficient as evidence of capability. The contradiction between the plan and the personnel records is the assessable content."),
   ("NOT APPLICABLE &mdash; the company has had no reportable incidents",False,"It has had two, and in any event the requirement does not turn on whether incidents have occurred."),
   ("MET, with the staffing gap recorded as an observation",False,"An observation does not repair a NOT MET, and the failure here is the absence of a capability rather than a staffing detail."),
  ]),
  dict(stem="The ClearPath addendum incorporates DFARS 252.204-7012 in full, but no Customer Responsibility Matrix accompanies it and remote access remains via a shared VPN account with no logging. What is the assessor's analysis?", opts=[
   ("Flowdown is complete; the access arrangement is a separate finding",False,"Two-thirds right, and it misses that Meridian believes signing the addendum discharged the obligation. The CRM is part of the ESP treatment, not an optional extra."),
   ("Flowdown is satisfied, but the ESP treatment is incomplete without a CRM, and shared unlogged access implicates MA.L2-3.7.5",True,"Three threads: the clause is flowed down; the ESP documentation is incomplete; and nonlocal maintenance without MFA, session control, or records is a distinct requirement failure. Mehta believes signing the addendum completed the obligation, and that belief is itself worth recording."),
   ("The addendum is void because it postdates the CUI handling",False,"Nothing makes it void. It is a late but effective flowdown."),
   ("No finding &mdash; ClearPath is out of scope as an external party",False,"An ESP handling CUI is evaluated inside the OSC's assessment. It is squarely in scope."),
  ]),
  dict(stem="For an item you requested and received something roughly on the subject but not addressing the objective, what should the evidence log record?", opts=[
   ("Received",False,"Insufficiently precise, and it is how partly responsive material quietly becomes accepted material."),
   ("Received and not responsive",True,"One of the three outcomes, alongside received-and-responsive and not-provided. This is where assessments quietly fail: a document arrives, it is roughly on the subject, the schedule is tight, and the standard lowers itself."),
   ("Not provided",False,"Something was provided, and recording otherwise misstates what happened."),
   ("Pending",False,"Pending is a status during the assessment, not an outcome in the log."),
  ]),
  dict(stem="Marcus Ellison asks the team: \"Just tell me what you need to see and we will go and do it.\" What is the correct response?", opts=[
   ("Explain what evidence would satisfy the outstanding objectives &mdash; it is a request for clarity, not advice",False,"It is the most tempting wrong answer in the exercise, because it sounds like process rather than remediation. Telling the OSC what to produce is directing its remediation."),
   ("Decline, without lecturing, and continue the assessment",True,"A team that answers has failed regardless of how good its determinations are. Declining gracefully &mdash; no speech about independence, no implied criticism &mdash; is the skill being assessed."),
   ("Decline and explain at length why the CoPC prohibits it",False,"The declining is right and the lecture is not. She is being reasonable, and a sermon damages the engagement without improving the determination."),
   ("Refer her to the C3PAO's project manager",False,"Passing the request along does not answer it and implies someone at the firm might say yes."),
  ]),
  dict(stem="Which interview question is most likely to produce evidence rather than confirmation?", opts=[
   ("\"You review the audit logs monthly, correct?\"",False,"A yes-or-no invitation to agree. He will say yes, it will be true as he understands it, and you will have learned nothing."),
   ("\"Walk me through the last review you did. What did you open?\"",True,"Open, specific, and anchored to an actual event. This is the question that reveals the \"monthly review\" is five or ten minutes on a firewall dashboard with the Windows event logs never opened."),
   ("\"Are you satisfied that logging is adequate?\"",False,"Invites an opinion about adequacy, which is the assessor's determination to make, not the interviewee's."),
   ("\"Do you have a log retention policy?\"",False,"Answerable yes or no, and it tells you nothing about what is retained or for how long."),
  ]),
  dict(stem="Why is interviewing Diana Kowalczyk at the Huntsville warehouse often the better assessment decision?", opts=[
   ("He is the most senior person available at the second site",False,"Seniority is not the criterion, and he is a warehouse supervisor."),
   ("He can tell you things no document records and nobody else thinks matter",True,"An unchanged door code given verbally to seasonal staff, no visitor log, shared warehouse logins, an unaccounted-for spare laptop in a drawer. Almost no team chooses him, which is exactly why the material is still there."),
   ("He is the custodian of the Huntsville asset inventory",False,"There is no Huntsville asset inventory, which is part of the problem."),
   ("His account will corroborate the SSP boundary statement",False,"It will contradict it, which is the point &mdash; but corroboration is not why you would choose him."),
  ]),
  dict(stem="A team's findings report cites an artifact the team requested but never received. What is wrong?", opts=[
   ("Nothing, provided the OSC confirmed the artifact exists",False,"Confirmation that something exists is not examination of it."),
   ("Every finding must be traceable to evidence actually examined; not-provided is recorded as a result, not cited as evidence",True,"If you did not see it, you cannot cite it. Absence of evidence is a legitimate result and belongs in the report as such."),
   ("The artifact should be cited with a note that it was unavailable",False,"Citing an unexamined artifact, however annotated, misrepresents the basis of the determination."),
   ("The finding should be withdrawn",False,"The finding may be perfectly sound on other evidence. What must change is the citation."),
  ]),
  dict(stem="Which section of a CAP Phase 3 findings report is most often written badly, and what does good look like?", opts=[
   ("The scope statement &mdash; it should list every asset individually",False,"Exhaustive asset listing belongs in the matrix. The scope statement names the entity, the CAGE code, the validated scope, and what falls outside."),
   ("The findings &mdash; each should name the failing objective, the evidence examined, what was missing, and a severity",True,"The common failure is a finding that states a conclusion. A reader should be able to verify or overturn each finding without redoing the assessment."),
   ("The methodology &mdash; it should describe the CAP in general terms",False,"General description is padding. Methodology should state the methods used, the sampling approach and the depth and coverage values applied, and what was examined, tested, or established by interview."),
   ("The recommendation &mdash; it should set out a remediation roadmap",False,"It should contain no remediation at all. The recommendation names which of the outcomes the CAP provides for you would recommend."),
  ]),
 ],
)

L9 = dict(
 file="lesson09.html", short="L9 — POA&M, Closeout & Credential Roadmap", num_label="Lesson 9",
 eyebrow="Day 5 &middot; Afternoon &middot; CAP Phase 4 &middot; Transfer test &middot; Closes the CCP blueprint",
 title="POA&amp;M, Closeout, the Transfer Test, and What You Do Next",
 lead=("This morning you told Meridian it does not get a certificate. Now you deal with what happens next "
       "&mdash; for the company, for the regulatory environment you will work in, and for you. Then you are handed "
       "a company you have never seen and given thirty minutes, because that is the only honest measure of "
       "whether this week gave you a method or a familiarity."),
 chips=["Day 5 &mdash; PM","~3 hours","<strong>Cold transfer test</strong>","Tool: POA&amp;M Builder"],
 obj_lead="By the end of this session you will be able to:",
 objectives=[
  ("Construct","Construct a POA&amp;M consistent with 32 CFR &sect;170.21, distinguishing what may be deferred from what may never be."),
  ("Explain","Explain Conditional versus Final Level 2 status, the 180-day closeout window, and what happens when it expires."),
  ("Describe","Describe the three-year certification period, the annual affirmation, and what the Affirming Official is exposed to."),
  ("Evaluate","Evaluate a change in CMMC policy against primary sources, separating what is stated from what is inferred and what is advocated."),
  ("Transfer","Scope a previously unseen environment under time constraint."),
  ("Plan","Produce a credential roadmap with dated milestones toward CCP and CCA."),
 ],
 vocab=[
  ("POA&amp;M","Plan of Action and Milestones. Under 32 CFR &sect;170.21, available only where the assessment score divided by the total number of requirements is at least 0.8, and never for six enumerated requirements."),
  ("The six","AC.L2-3.1.20, AC.L2-3.1.22, CA.L2-3.12.4, PE.L2-3.10.3, PE.L2-3.10.4, PE.L2-3.10.5. These must be MET. No score, however high, changes that."),
  ("Conditional CMMC Status","Status issued where a POA&amp;M is permitted and in place. Becomes Final on a successful closeout assessment within the window, or expires."),
  ("Closeout window","180 days from the Conditional CMMC Status Date, closed out by a closeout assessment. Miss it and the conditional status expires."),
  ("Closeout C3PAO","The firm that conducts the closeout assessment. Need not be the firm that ran Phases 1&ndash;3; it assumes responsibility for the Final status determination after its own conflict-of-interest review."),
  ("Annual affirmation","Submitted in SPRS each year by the Affirming Official, attesting to continued compliance. A present-tense statement, not a memory of the assessment."),
  ("Flowdown, tested","Acuitas Machining &mdash; the supplier inside Meridian's own supply chain, and the transfer test."),
 ],
 sections=[
  dict(title="What a POA&amp;M can and cannot do", html="""
<div class="warnbox"><div class="warn-label">The fact that governs this session</div>
<p>A plan of action is not a way to defer anything you like. <strong>Six requirements may never be placed on a
POA&amp;M at all</strong>, and a POA&amp;M may not be used at any level unless the assessment score is at least
<strong>0.8</strong> of the total.</p>
<p>Two of the six are worth one point each. The cheapest requirements on the sheet are absolute barriers, and no
amount of score makes them go away.</p></div>
<div class="tw"><table>
<thead><tr><th>Rule</th><th>What it means in practice</th></tr></thead>
<tbody>
<tr><td><strong>The score threshold</strong></td><td>A POA&amp;M may be used only where the assessment score divided by the total number of Level 2 requirements is at least 0.8. For 110 requirements that is <strong>88</strong>. Below that there is no plan of action available at all &mdash; the answer is no issuance.</td></tr>
<tr><td><strong>The six that may never be deferred</strong></td><td>AC.L2-3.1.20, AC.L2-3.1.22, CA.L2-3.12.4, PE.L2-3.10.3, PE.L2-3.10.4, PE.L2-3.10.5. These must be MET.</td></tr>
<tr><td><strong>The encryption exception</strong></td><td>SC.L2-3.13.11 may be placed on a POA&amp;M only where encryption is employed but is not FIPS validated. Where no encryption is employed, it may not.</td></tr>
<tr><td><strong>The window</strong></td><td>180 days from the Conditional CMMC Status Date, closed out by a closeout assessment. Miss it and the conditional status expires.</td></tr>
<tr><td><strong>Who closes it out</strong></td><td>An authorized or accredited C3PAO &mdash; and it need not be the firm that ran Phases 1 through 3. A closeout C3PAO assumes responsibility for the Final status determination and issues the Final certificate, after its own conflict-of-interest review.</td></tr>
</tbody></table></div>
<div class="tip"><div class="tip-label">Notice what the point values do not tell you</div>
<p><strong>CA.L2-3.12.4</strong> &mdash; the System Security Plan &mdash; is worth one point.
<strong>PE.L2-3.10.3</strong> &mdash; escorting visitors &mdash; is worth one point. Both are on the list that may
never be deferred.</p>
<p>A company can be one point from a perfect score and still be unable to obtain any status at all. Scoring weight
measures exploitability; POA&amp;M eligibility measures something else entirely, and conflating the two is the most
expensive mistake available in this area.</p></div>"""),
  dict(title="Meridian, as you assessed it", html="""
<p>Work Part A from your own findings, not from a supplied list. You will reach the conclusion quickly.</p>
<p>Meridian's assessed score does not approach 88. And two of the six requirements that may never be deferred
are already failing: the System Security Plan requirement, and PE.L2-3.10.3 &mdash; the Huntsville warehouse has no
visitor log, no badge access, and delivery drivers come and go.</p>
<p><strong>Meridian is not POA&amp;M-eligible. No CMMC status may issue.</strong></p>
<div class="in-practice"><div class="ip-label">Say the consequence out loud</div>
<p>A determination of no issuance is not the end of the sentence. Write two or three lines on what it means
commercially: the AMCOM recompete the company must win to survive; the clause in the contract it already holds and is
in breach of today; and the affirmation of a score of 88 that its chief executive has already signed, in a federal
system, under penalty.</p>
<p>Assessors do not decide what happens to companies. They do have to be able to say plainly what their
determination means &mdash; without softening it, and without enjoying it.</p></div>"""),
  dict(title="Building a POA&amp;M that works", html="""
<p>Building a plan is a skill you need, so Part B works a revised assessment. Nine months later Meridian engages
a closeout-capable C3PAO for a fresh Level 2 certification assessment. This time the company has
<em>implemented</em> rather than documented. Every requirement is MET except six.</p>
<div class="tw"><table>
<thead><tr><th>Requirement</th><th>Short title</th><th>Points</th><th>Deduction</th><th>Deferrable?</th></tr></thead>
<tbody>
<tr><td>AC.L2-3.1.5</td><td>Employ the principle of least privilege</td><td>3</td><td>3</td><td>Yes</td></tr>
<tr><td>AU.L2-3.3.2</td><td>Ensure actions can be traced to individual users</td><td>3</td><td>3</td><td>Yes</td></tr>
<tr><td>CM.L2-3.4.1</td><td>Establish and maintain baseline configurations and inventories</td><td>5</td><td>5</td><td>Yes</td></tr>
<tr><td>MP.L2-3.8.7</td><td>Control the use of removable media</td><td>5</td><td>5</td><td>Yes</td></tr>
<tr><td><strong>CA.L2-3.12.4</strong></td><td>Develop, document, and periodically update the SSP</td><td>1</td><td>1</td><td><strong>Never</strong></td></tr>
<tr><td><strong>PE.L2-3.10.3</strong></td><td>Escort visitors and monitor visitor activity</td><td>1</td><td>1</td><td><strong>Never</strong></td></tr>
<tr><td colspan="3"><strong>Total deductions</strong></td><td><strong>18</strong></td><td></td></tr>
<tr><td colspan="3"><strong>Assessment score</strong></td><td><strong>92</strong></td><td>92 &divide; 110 = 0.836</td></tr>
</tbody></table></div>
<div class="warnbox"><div class="warn-label">The trap, and it is worth meeting here rather than in the field</div>
<p>The score clears the threshold. 0.836 is comfortably above 0.8, and a company reading only the threshold rule
would expect a Conditional status.</p>
<p>It cannot have one. Two of the six NOT MET requirements are on the never-defer list, and they are the two cheapest
items on the sheet. Both must be MET outright before any status can issue. <strong>The score alone never answers the
question.</strong></p></div>
<p>For each deferrable item the plan needs a milestone, a target date inside the window, and an owner. A milestone
with no owner is a wish. Sequence them so dependencies are visible &mdash; baseline configurations before least
privilege, for instance, because you cannot enforce what you have not defined.</p>
<p>And no remediation design. Naming what must be remediated and by when is the plan; specifying how to remediate
it is consulting, and it is still consulting on the last afternoon.</p>"""),
  dict(title="Closeout and sustainment", html="""
<div class="tw"><table>
<thead><tr><th>Question</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>From what date does the closeout window run, and how long?</td><td>180 days from the Conditional CMMC Status Date.</td></tr>
<tr><td>What does the closeout assessment cover?</td><td>The requirements on the POA&amp;M, assessed to confirm they are now MET.</td></tr>
<tr><td>Who may conduct it?</td><td>An authorized or accredited C3PAO &mdash; and it may be a different firm from the one that ran Phases 1&ndash;3.</td></tr>
<tr><td>What must that firm do first?</td><td>Its own conflict-of-interest review. It then assumes responsibility for the Final status determination and issues the Final certificate.</td></tr>
<tr><td>What happens if the window expires?</td><td>The Conditional status expires.</td></tr>
<tr><td>How long does a Level 2 certification run?</td><td>Three years from the CMMC Status Date.</td></tr>
<tr><td>What is submitted annually, by whom, where?</td><td>An affirmation in SPRS by the Affirming Official.</td></tr>
<tr><td>What does it attest?</td><td>That the organization continues to meet the requirements. Present tense, not a memory of the assessment.</td></tr>
<tr><td>What is the Affirming Official exposed to?</td><td>False Claims Act consequences attaching personally, where the affirmation is not true.</td></tr>
</tbody></table></div>
<p>The practical answer to the sustainment problem is continuous monitoring, so that the affirmation reports
something known rather than something assumed. Marcus Ellison affirmed a score of 88 on the basis that other
people told her it was right. Hold that in mind when you write this section.</p>"""),
  dict(title="Reading a policy change against primary sources", html="""
<p>This is the Day 1 exercise returning at full strength. Then you sorted statements from a single alert into fact,
inference, and advice. Now you do it across three sources that do not agree with one another, on a subject where the
primary sources are incomplete and moving.</p>
<ul>
<li>Two professional analyses of the same recent CMMC development, from firms that reach different conclusions.</li>
<li>A government or trade-body notice on the same subject &mdash; a different kind of source with a different agenda.</li>
</ul>
<p>Mark every substantive sentence as <strong>stated</strong>, <strong>inferred</strong>, or
<strong>advocated</strong>. Then the harder question: where the two firms disagree, <em>what would settle it</em>
&mdash; and is that thing <strong>published, pending, or unknowable</strong>?</p>
<div class="in-practice"><div class="ip-label">Why this is the last analytical exercise of the workshop</div>
<p>Everything else you have learned has a shelf life. This is the skill that lets you notice when it expires. An
assessor who can say what would settle a disagreement, and whether that thing exists yet, can tell a client the
difference between a risk and a rumour.</p></div>"""),
  dict(title="The transfer test", html="""
<p>Thirty minutes. Individual. No notes, no case study, no internet. You receive a profile of a company in
Meridian's supply chain and produce a scope determination.</p>
<p>It is not graded and it does not affect completion. It exists to tell you something you cannot find out any
other way: whether this week gave you a <strong>method</strong> or a <strong>familiarity</strong>. Both feel
identical from the inside, right up until you meet a new environment.</p>
<div class="in-practice"><div class="ip-label">Acuitas Machining Inc.</div>
<p>Springfield, Ohio, about 25 miles from Meridian&rsquo;s Dayton plant. Fourteen people. Precision CNC machining
and inspection &mdash; a job shop taking overflow and short-run work. About $800K of its $3.4M revenue comes from a
single relationship: machining overflow on Meridian&rsquo;s actuator housing line for the AMCOM contract.</p>
<p>No server. No domain. No IT staff. No SSP, no asset inventory, no network diagram, no written security policy of
any kind, and no record of any security decision ever having been made.</p>
<p>The owner's position, stated plainly: <em>&ldquo;CMMC is a DoD thing &mdash; we don't have a contract with the
government, we have a contract with Meridian.&rdquo;</em></p></div>
<h3>What you must produce</h3>
<ol>
<li><strong>Level and authority</strong> (~4 min). What level applies and what makes it apply? Answer the owner's
objection directly, in no more than four sentences, and name the instrument you rely on.</li>
<li><strong>Asset categorization</strong> (~14 min). Eight assets into the five categories, one-line basis each.
Where a category is unavailable to Acuitas, say so and say why.</li>
<li><strong>The consequential unknown</strong> (~4 min). The single fact you would most want resolved before
finalizing this scope, why it matters, and what evidence would settle it.</li>
</ol>
<div class="tip"><div class="tip-label">What is being measured</div>
<p>Not recall. Whether the method you have used on one company for four days works on a company you have never
seen &mdash; which is the only thing that would make you useful to the next OSC that hires you.</p>
<p>A confident wrong categorization scores worse than a correctly hedged one. If a category is genuinely arguable,
say what makes it arguable and what would settle it. That is the assessor's answer.</p></div>"""),
  dict(title="The credential roadmap", html="""
<p>The gap between finishing a course and sitting an exam is where most people quietly stop. Close it with dates.</p>
<div class="tw"><table>
<thead><tr><th></th><th>CCP</th><th>CCA</th></tr></thead>
<tbody>
<tr><td><strong>Prerequisites</strong></td>
<td>ATP training; relevant experience; DoW Tier 3 background determination</td>
<td>Active CCP; DoD 8140.03 Work Role 612 baseline certification at Intermediate or Advanced &mdash; CISA and CISM both qualify; ATP training; Tier 3 determination</td></tr>
<tr><td><strong>Exam</strong></td><td>170 questions, six domains</td><td>150 questions, four domains</td></tr>
<tr><td><strong>Continuing education</strong></td><td>20 CPE annually; 120 over three years, at least 90 CMMC-related</td><td>As CCP</td></tr>
</tbody></table></div>
<p>Map the domain weights against this week. Day 4 fed the 35% and 40% blocks. Day 2 afternoon and Day 5 morning
fed the 25% Assessment Process blocks. Day 3 morning fed the scoping blocks. <strong>Where you found a session
hard is where your study time goes.</strong></p>
<div class="warnbox"><div class="warn-label">Still unverified</div>
<p>Exam duration and passing scores for the CCP and CCA are not stated anywhere in this workshop, because they were
not publicly stated by ISACA at the time of research. Confirm both directly with ISACA before you register, and
treat any figure you find in a third-party study guide as unverified until you have.</p></div>"""),
 ],
 case=dict(tag="Meridian &middot; Day 5 Afternoon &middot; Deliverable D9 + Transfer Test",
   title="Close it out, then prove the method transfers",
   html="""
<p><strong>The POA&amp;M Builder</strong> runs Parts A to C. Part A takes your own assessed score and findings and
walks the eligibility test &mdash; the threshold, then the never-defer list &mdash; and asks you to state the
commercial consequence in your own words. Part B loads the revised assessment at 92 and lets you build the plan
item by item; the tool refuses a deferral of CA.L2-3.12.4 or PE.L2-3.10.3 and tells you why. Part C is closeout and
sustainment.</p>
<p>Then the <strong>Acuitas transfer test</strong> opens cold, on a thirty-minute timer, with no access to the
Meridian material. Eight assets, three questions. When the timer stops, the determination key opens &mdash;
including the honest account of where the test is won or lost, which is the industrial printer controller.</p>
<p><em>Nothing anywhere in D9 tells Meridian how to remediate anything. Naming what must be done and by when is
the plan. Designing it is somebody else's job &mdash; and after this week, never yours on a company you assess.</em></p>""",
   actions=[("Open the POA&amp;M Builder &rarr;","poam-builder.html",False),
            ("Take the transfer test (30 min) &rarr;","transfer-test.html",False),
            ("Exam-day one-pager","onepager.html",True)]),
 kc=[
  dict(stem="An OSC scores 92 of 110 (0.836). Its NOT MET requirements include CA.L2-3.12.4 and PE.L2-3.10.3. What status may issue?", opts=[
   ("Conditional Level 2 &mdash; the score clears the 0.8 threshold",False,"The trap this session exists to spring. Clearing the threshold is necessary and not sufficient."),
   ("None &mdash; two NOT MET requirements may never be placed on a POA&M",True,"Both must be MET outright before any status can issue. They are the two cheapest items on the sheet, at one point each. The score alone never answers the question."),
   ("Final Level 2, since the deductions are minor",False,"Final status requires all requirements MET, and these are not."),
   ("Conditional Level 2, with the two ineligible items deferred by exception",False,"There is no exception mechanism. The list is absolute."),
  ]),
  dict(stem="Which requirement may be placed on a POA&M only in a specific circumstance?", opts=[
   ("CA.L2-3.12.4, where the SSP is in draft",False,"3.12.4 may never be placed on a POA&M in any circumstance."),
   ("SC.L2-3.13.11, where encryption is employed but is not FIPS validated",True,"Where no encryption is employed at all, it may not be deferred. Note the symmetry with the scoring exception: the same distinction drives both the 3-versus-5 deduction and POA&M eligibility."),
   ("PE.L2-3.10.4, where the facility is leased",False,"On the never-defer list, and tenancy is irrelevant."),
   ("AC.L2-3.1.20, where the external system is government-owned",False,"Also on the never-defer list."),
  ]),
  dict(stem="From what date does the 180-day closeout window run?", opts=[
   ("The date of the out-brief",False,"The out-brief is a Phase 3 event and does not start the clock."),
   ("The Conditional CMMC Status Date",True,"180 days from that date, closed out by a closeout assessment. Miss it and the conditional status expires."),
   ("The date the POA&M is submitted",False,"Submission is not the trigger."),
   ("The date the Contracting Officer accepts the score",False,"No such acceptance step exists in the closeout mechanics."),
  ]),
  dict(stem="Who may conduct the closeout assessment?", opts=[
   ("Only the C3PAO that conducted Phases 1 through 3",False,"A common assumption and the rule is explicitly the opposite."),
   ("Any authorized or accredited C3PAO, after its own conflict-of-interest review",True,"The closeout firm assumes responsibility for the Final status determination and issues the Final certificate. Its conflict review is its own, not inherited."),
   ("DIBCAC",False,"DIBCAC conducts government-led assessments, including Level 3. Closeout of a Level 2 conditional status is C3PAO work."),
   ("The OSC, by self-assessment",False,"A conditional status arising from a certification assessment cannot be closed out by self-assessment."),
  ]),
  dict(stem="Acuitas's owner says CMMC does not apply because he has no contract with the Government. What is the complete answer?", opts=[
   ("He is right for now, but Meridian may impose requirements commercially",False,"This concedes the owner's premise. The obligation is not a commercial courtesy."),
   ("Level 2 applies: he receives CTI extracted from the TDP, through a subcontract incorporating DFARS 252.204-7012, which flows down under paragraph (m)",True,"The obligation follows the information, not the tier. The clause is in his subcontract, flowdown is how it got there, Meridian was required to put it there, and whether he has read it is irrelevant to whether it binds him."),
   ("Level 1 applies, because subcontractors carry the lower tier",False,"The most serious error available on this test, and it is the owner's own error. Tier does not determine level; information does."),
   ("Level 2 applies because he handles CUI",False,"The right conclusion without the authority. Naming the flowdown mechanism is what makes it an answer."),
  ]),
  dict(stem="Acuitas's three CNC machining centres have embedded Windows controllers that retain drawing-derived files for months. How are they categorized?", opts=[
   ("Out of scope &mdash; they are machine tools",False,"The weakest answer. They have not been read as information systems, and they retain CUI for months."),
   ("A full CUI Asset, assessed against all 110 requirements",False,"Thorough, and it misses that the Specialized Asset category exists and covers Operational Technology."),
   ("Specialized Asset by type &mdash; but the treatment is conditional on documentation and risk-based policies Acuitas cannot produce, so they stay in the assessment",True,"Where the test is won or lost. The category exists and Acuitas cannot claim it: no inventory, no SSP, no network diagram, no policy of any kind. Knowing the rule and its condition is the difference between having read the scoping guide and being able to use it."),
   ("Contractor Risk Managed, since machining is incidental to the CUI",False,"That category carries the same documentation and policy condition, which also fails &mdash; and OT is the better-fitting type in any case."),
  ]),
  dict(stem="Acuitas's part-time bookkeeper works from home on her own computer with access to the full shared drive. How is she treated?", opts=[
   ("Out of scope &mdash; she handles accounting, not CUI",False,"The dismissal the test is designed to catch. Her access is to the full shared drive, which holds the pattern files."),
   ("An External Service Provider handling CUI, assessed inside the OSC assessment, with a CRM required",True,"She holds an account with access to CUI and works from her own equipment. No CRM exists. Note the second ESP alongside her: the IT contractor with tenant administrator rights, who handles Security Protection Data."),
   ("A Contractor Risk Managed Asset",False,"Categories apply to assets. An external party is analysed under the ESP rule."),
   ("An employee for scoping purposes, since she has an account",False,"Having an account does not make an external party internal. The ESP rule exists precisely for this."),
  ]),
  dict(stem="At Acuitas, what should be scoped out?", opts=[
   ("The CMM inspection station, since it only measures parts",False,"It holds inspection programs written from the Meridian drawings and generates reports referencing them. Students who scope the machine tools carefully and forget the metrology station have found the obvious OT and missed the quieter one."),
   ("The commercial customers' artwork folders",False,"Folders are not assets, and they sit on a shared drive every account can read."),
   ("Nothing &mdash; on a single flat wireless network with a shared drive every account can read, no justification of inability exists",True,"Out-of-Scope requires the contractor to be prepared to justify the asset's inability to process, store, or transmit CUI. The absence of segmentation is what makes that impossible, and saying so explicitly is the correct answer."),
   ("The production PC, since it only sends print jobs",False,"It opens pattern files. It is a CUI Asset, and the shared login with the password on the monitor is a finding rather than a scoping question."),
  ]),
  dict(stem="Two law firm analyses of the same CMMC development reach different conclusions. What is the assessor's most useful next question?", opts=[
   ("Which firm has more CMMC experience?",False,"Authority of the author is not how a disagreement about a primary source is settled."),
   ("What would settle the disagreement, and is that thing published, pending, or unknowable?",True,"The question that distinguishes a risk from a rumour. An assessor who can answer it can tell a client which of the two they are looking at."),
   ("Which conclusion is more conservative?",False,"Conservatism is a posture, not an analysis, and it can be wrong in either direction."),
   ("What does the CMMC PMO say publicly?",False,"Useful input, and it does not resolve a disagreement about what the existing instruments mean."),
  ]),
  dict(stem="What does the annual affirmation attest, and who may make it?", opts=[
   ("That the assessment was conducted correctly; the Lead CCA",False,"The affirmation is the OSC's statement about itself, not the assessor's about the assessment."),
   ("That the organization continues to meet the requirements; a senior official with authority to bind the OSC",True,"A present-tense statement, not a memory of the assessment. The practical answer is continuous monitoring, so that it reports something known rather than assumed. False Claims Act exposure attaches personally to the signer."),
   ("That no incidents occurred in the preceding year; the IT Manager",False,"Wrong on both counts. Incidents are reported under a separate clause, and the IT Manager cannot bind the organization."),
   ("That the POA&M has been closed; the closeout C3PAO",False,"Closeout is a separate mechanism with its own assessment, and the C3PAO does not affirm on the OSC's behalf."),
  ]),
 ],
)

L10 = dict(
 file="lesson10.html", short="Bonus — Teaching CMMC (Faculty PD)", num_label="Bonus",
 eyebrow="Faculty PD &middot; Not part of the 5-day sequence",
 title="Teaching CMMC &mdash; A Faculty and Facilitator Guide",
 lead=("You have worked the material. This is how to deploy it: the 8-week graded version it was derived from, "
       "the facilitation decisions that make or break each session, the answer keys and what to do with them, "
       "the instruments that must be withheld until issued, and the maintenance obligation that comes with "
       "teaching a subject in active regulatory flux."),
 chips=["Bonus","Facilitators","<strong>Instructor-facing</strong>","Maintenance guidance"],
 obj_lead="This guide is for the person delivering the workshop. By the end of it you will be able to:",
 objectives=[
  ("Choose","Choose between the 5-day workshop, the 8-week graded course, and the hybrid, on the basis of cohort and contact hours."),
  ("Facilitate","Facilitate each session's highest-risk moments, including the ones where the correct answer is uncomfortable."),
  ("Assess","Assess against the competency rubric rather than a grade, and know what Competent versus Assessor-Ready looks like."),
  ("Protect","Protect the instruments that must be issued cold, and know why each one is withheld."),
  ("Maintain","Maintain the material against a regulatory position that is actively moving."),
 ],
 vocab=[
  ("Competency rubric","Not Yet / Developing / Competent / Assessor-Ready. Competent is the completion standard; Assessor-Ready describes work that would survive professional challenge."),
  ("Cold instrument","Material that must not be released in advance: the Module 7 evidence package, the interview role cards, and the Acuitas transfer test."),
  ("Challenge round","The peer-challenge format used for scoping and domain determinations. Arbitrated against the text on screen, never by seniority."),
  ("Three-step fade","Watch a worked example, then work with support, then work unsupported. The evidence sessions are built on it."),
  ("Minimum viable cohort","Twelve students &mdash; four teams of three &mdash; for the split-case design. Below that, run a single case and extend the challenge rounds."),
 ],
 sections=[
  dict(title="Three ways to deliver this", html="""
<div class="tw"><table>
<thead><tr><th></th><th>5-day workshop</th><th>8-week course</th><th>Hybrid</th></tr></thead>
<tbody>
<tr><td><strong>Contact hours</strong></td><td>30 (10 sessions &times; ~3 hrs)</td><td>24 (16 sessions &times; 90 min)</td><td>Varies</td></tr>
<tr><td><strong>Audience</strong></td><td>Conference, corporate cohort, faculty PD, intensive bootcamp</td><td>Non-credit academic term, Canvas-delivered</td><td>Self-paced site plus facilitated checkpoints</td></tr>
<tr><td><strong>Deliverables</strong></td><td>Self-checked tool outputs, printed to PDF</td><td>Nine graded deliverables against competency rubrics</td><td>Tools for practice; two or three deliverables graded</td></tr>
<tr><td><strong>Teams</strong></td><td>Optional; tools work solo</td><td>Teams of three, formed Week 3, stable to Week 8</td><td>Teams for the mock assessment only</td></tr>
<tr><td><strong>Summative</strong></td><td>Day 5 morning mock assessment plus the transfer test</td><td>Week 7 mock assessment plus the Week 8 transfer test</td><td>As the 5-day</td></tr>
<tr><td><strong>Instructor load</strong></td><td>~12 hrs prep, 30 hrs delivery</td><td>~75&ndash;78 hrs total including feedback</td><td>Between the two</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">Pre-delivery reading, either way</div>
<p>Ten to twelve hours, and there is no shortcut: CAP v2.0, CoPC v2.0, the CMMC Assessment Guide for Level 2, and
the CMMC Assessment Scope guidance for Level 2, end to end. You will be arbitrating challenges against these
documents in front of a room, and doing it from memory is how the exercise becomes about your authority instead of
the rule.</p></div>"""),
  dict(title="The facilitation decisions that matter", html="""
<div class="tw"><table>
<thead><tr><th>Session</th><th>The moment</th><th>How to run it</th></tr></thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Students raise whatever is currently in the trade press about CMMC changing</td>
<td>Answer it on day one using the instrument test, not the news: has a class deviation, a FAR/DFARS rule change, or an amendment to Part 170 issued? If not, the framework is what the published text says. Then redirect. Do not let it recur &mdash; and note that you have just modelled the L9 skill in thirty seconds.</td></tr>
<tr><td><strong>L2</strong></td><td>The CUI audit debrief</td>
<td>Have the NARA Registry open and projected. Look items up <em>live</em> rather than reading answers off a key &mdash; modelling the lookup is most of the lesson. Item 2 is worth half the session; push students through the temptation to keep &ldquo;CTI&rdquo; because it is nearly right, let them fail to find a fitting category, and land on the contract and the contracting officer. Students uncomfortable ending on an open item are learning the correct discomfort.</td></tr>
<tr><td><strong>L3</strong></td><td>Ethics scenario adjudication</td>
<td>One of the eight scenarios is not addressed directly by the CoPC at all. Finding that out is the exercise. An honest &ldquo;the document does not cover this, so here is what governs&rdquo; is a stronger answer than a citation that does not say what the student claims.</td></tr>
<tr><td><strong>L4</strong></td><td>The conditional categories</td>
<td>Teach the test before the name. Do the two conditional categories last and slowly: read the condition aloud, then ask what Meridian would show you. <em>The silence is the lesson.</em></td></tr>
<tr><td><strong>L5</strong></td><td>Artifact 2, the Conditional Access export</td>
<td>The artifact that separates Competent from Assessor-Ready. Watch for students who accept it outright because it is real technical evidence, and students who reject it outright because Meridian fails the requirement. Both miss the point: the artifact is excellent and the requirement is still NOT MET.</td></tr>
<tr><td><strong>L6</strong></td><td>Cross-presentation</td>
<td>Require teams to lead with their <em>least</em> comfortable determination. Teams instinctively present their best work, which wastes the exercise &mdash; nobody learns from a determination everyone agrees with.</td></tr>
<tr><td><strong>L7</strong></td><td>The 3.5.3 deduction</td>
<td>Poll the room before revealing. Expect a substantial minority at 3. Work the conjunction on screen: remote <em>and</em> privileged. The spread is the lesson.</td></tr>
<tr><td><strong>L8</strong></td><td>Ellison's request</td>
<td>Play it once per team, late, when they are tired and want to be helpful. A team that answers has failed the exercise regardless of their determinations &mdash; and that failure teaches more than the finding would have.</td></tr>
<tr><td><strong>L9</strong></td><td>The transfer test debrief</td>
<td>Ten minutes, immediately, while the reasoning is live. Poll on the printer controller <em>before</em> revealing anything &mdash; students remember their own wrong answer better than your right one. Then ask who scoped something out and make them defend it. On that environment nobody should have.</td></tr>
</tbody></table></div>"""),
  dict(title="What must be withheld", html="""
<div class="warnbox"><div class="warn-label">Three cold instruments</div>
<p><strong>The Day 5 evidence package.</strong> Issued at the in-brief. A team that has read the nine documents in
advance has done a different exercise, and the time pressure that makes the mock assessment realistic disappears.</p>
<p><strong>The interview role cards.</strong> Role-players only, one card each, never shown to assessment teams.
Every card contains at least one fact that contradicts something in the evidence package, and those contradictions
are the assessable content.</p>
<p><strong>The Acuitas transfer test.</strong> Do not release the profile in advance, do not preview the company,
and do not answer questions about it once the clock starts.</p></div>
<h3>How to play the interview cards</h3>
<p>The rule that makes it work: <strong>answer the question you were asked, and nothing more.</strong> Each card has
material that is volunteered freely and material that emerges only if a student asks a question that reaches it
&mdash; a real question, not a yes-or-no invitation to agree.</p>
<p>If a student asks &ldquo;you review the logs regularly, correct?&rdquo;, say yes. That is a true answer to a bad
question, and the student learning why it was a bad question is the point of the exercise. If a team asks only
closed questions, let the interview end early and uselessly. The silence afterwards teaches more than a rescue
would.</p>
<p>Hold the contradictions. If a team leaves without finding any of them, that is the finding &mdash; and it is the
one to open the debrief with.</p>"""),
  dict(title="Assessing competency rather than grading", html="""
<p>Four levels, applied to every deliverable. <strong>Competent</strong> is the completion standard;
<strong>Assessor-Ready</strong> describes work that would survive professional challenge.</p>
<div class="tw"><table>
<thead><tr><th>Level</th><th>What it looks like across the deliverables</th></tr></thead>
<tbody>
<tr><td><strong>Not Yet</strong></td><td>Adopts the contractor's own claims wholesale. Categorizes by intuition or by what an asset is for. Determines at the requirement level. Recommends remediation.</td></tr>
<tr><td><strong>Developing</strong></td><td>Handles the obvious cases and goes quiet on the ambiguous ones. Applies one test but not both. Names a requirement but not the objective. Advice appears once, in passing.</td></tr>
<tr><td><strong>Competent</strong></td><td>Every determination evidenced and traceable. Conditional categories recognised as earned. Both adequacy and sufficiency applied. No advice anywhere; gaps named without fixes.</td></tr>
<tr><td><strong>Assessor-Ready</strong></td><td>Says what would change each answer. Catches the under-classified item and explains why that direction is more dangerous. Names a gap so precisely that the fix is obvious without ever being stated. Written so that a company that dislikes the result still recognises it as fair.</td></tr>
</tbody></table></div>
<div class="in-practice"><div class="ip-label">The single most useful marking habit</div>
<p>Look for the <em>what would change it</em> clause. A determination that cannot describe its own falsifying
evidence has not been reasoned &mdash; it has been asserted. That one test separates Competent from Developing more
reliably than any other, and it is fast to apply.</p></div>"""),
  dict(title="Maintaining this material", html="""
<div class="warnbox"><div class="warn-label">Standing obligation before every run</div>
<p>Re-verify the regulatory position <strong>within seven days of any workshop start date.</strong> This material
deliberately carries <em>no dated policy layer</em> &mdash; it teaches 32 CFR Part 170 and the DFARS clause family
as published, so that it does not go stale with the news cycle. That design decision only holds if you check the
published instruments before you teach.</p>
<p>Apply the same test the workshop teaches: has a class deviation, a FAR or DFARS rule change, or an amendment to
Part 170 issued since the last run? If not, nothing here needs changing.</p></div>
<div class="tw"><table>
<thead><tr><th>Check</th><th>Why</th><th>What to do if it has changed</th></tr></thead>
<tbody>
<tr><td>Whether any class deviation, FAR/DFARS rule change, or amendment to 32 CFR Part 170 has issued</td><td>These are the only three instruments that change what a contractor owes, and students will arrive having read something in the trade press</td><td>If one has issued, read the instrument text and revise the affected lessons. Then make it the live L9 policy-analysis subject &mdash; a real, current disagreement is the best possible version of that exercise.</td></tr>
<tr><td>32 CFR 170.14 still specifies NIST SP 800-171 Rev 2 for Level 2</td><td>A Rev 3 transition changes the requirement count, the control identifiers, and every downstream artifact</td><td>Stop and revise L2, L5, L6, and L7 together. Do not patch one lesson &mdash; the requirement count appears in several places.</td></tr>
<tr><td>NARA Registry category pages</td><td>NARA updates continuously; authorities are added and removed without announcement</td><td>Update the CUI Determination tool's key. Then use the change in class &mdash; it is a free lesson in why you look the category up rather than reciting one.</td></tr>
<tr><td>CAP, CoPC, Assessment Guide, and Scoping Guide versions</td><td>Version numbers move</td><td>Re-verify against the DoD CIO and Cyber AB document libraries before each run.</td></tr>
<tr><td>ISACA CCP and CCA exam mechanics</td><td>Duration and passing scores remain unverified</td><td>Confirm with ISACA. Do not publish figures to learners until you have; the material currently flags them as unverified in three places, deliberately.</td></tr>
</tbody></table></div>
<h3>Practical notes</h3>
<ul>
<li><strong>Minimum viable cohort</strong> is twelve &mdash; four teams of three &mdash; for the split-case design.
Below that, run a single case per session and extend the challenge rounds.</li>
<li><strong>Schedule the Day 5 sessions contiguously.</strong> The overnight evidence-request bridge only reads as
overnight if there is a break; if you must compress, run the request as a 15-minute in-session gap and say so.</li>
<li><strong>No purchased software, lab environment, or clearance is required.</strong> Every artifact is fictional
and unclassified. Every primary source is free and publicly available.</li>
<li><strong>Note on <code>dodcio.defense.gov</code>:</strong> that host blocks automated tools but opens normally in
a browser. Do not report the links as dead.</li>
<li><strong>Where a portal module disagrees with this material on who issues the CCP,</strong> this material is
right and the portal predates December 2025. Use the discrepancy in L0 &mdash; it is the cleanest available
demonstration of source authority.</li>
</ul>"""),
 ],
 case=None,
 kc=None,
)
