# -*- coding: utf-8 -*-
"""Tool pages 3-5: Ethics Gate, Scope Matrix, Evidence Triage."""
from toolkit import tool_page, item
import tools3

DISPO = ["Disclose only","Disclose and mitigate","Avoid — remove the individual",
         "Avoid — the C3PAO must decline the engagement","No conflict"]

# ---------------------------------------------------------------- 3. ETHICS GATE
CONFLICTS = [
 ("Marcus Reyes &mdash; CCA",
  "Employed by Meridian as an IT specialist 2019&ndash;2022, where he built the Active Directory group "
  "structure and the file server permission model <em>still in use, including on the /CUI tree</em>. Left on good "
  "terms; no services since. Participated in Tidewater&rsquo;s gap assessment ten months ago.",
  "Avoid — remove the individual",
  """<p><strong>Two separate problems, and neither is cured by disclosure.</strong></p>
  <p>First, he would be assessing his own work. The permission model on the /CUI tree is his, and it is squarely
  within scope. That is an impartiality failure under CoPC &sect;2.2 with no mitigation short of removal.</p>
  <p>Second, he participated in the gap assessment that produced Appendix C, a Recommended Remediation Sequence.
  That is advisory activity to prepare the organization, and it engages the three-year bar at 32 CFR
  &sect;170.8(b)(17)(ii)(G) / CoPC &sect;2.2(d) &mdash; which covers <em>any type</em> of CMMC assessment.</p>
  <p><strong>Who decides:</strong> the C3PAO. Not Reyes, and not the OSC.</p>"""),
 ("Priya Raghunathan &mdash; CCP",
  "Two years alongside Meridian&rsquo;s IT Manager, Trevor Nakamura, on the board of their local professional "
  "association chapter; they see each other monthly and occasionally dine with the wider board. No financial or "
  "family relationship. Participated in the gap assessment ten months ago.",
  "Avoid — remove the individual",
  """<p>The chapter-board relationship alone would be a <strong>disclose-and-mitigate</strong> question: an ongoing
  personal relationship with a key interviewee could reasonably appear to compromise impartiality, and mitigation by
  reassignment is available. Overcorrecting &mdash; treating every professional acquaintance as disqualifying &mdash;
  is its own error.</p>
  <p>But she also participated in the gap assessment, which engages the three-year bar independently. Removal
  follows from the second fact, not the first.</p>
  <p><strong>Watch the trap:</strong> teams that spot the chapter board and stop have found the softer of the two
  conflicts and missed the one that actually decides it.</p>"""),
 ("Thomas Blalock &mdash; CCA",
  "No relationship with Meridian. Holds approximately $30,000 of common stock in Cardinal Industrial Group, a "
  "publicly traded company. Cardinal is the parent of <strong>ClearPath IT Solutions</strong>, the vendor that maintains "
  "Meridian&rsquo;s PLM and holds standing remote access to it. Disclosed the holding to Tidewater on joining.",
  "Disclose and mitigate",
  """<p>A general disclosure on joining is <em>not</em> disclosure of a conflict in this engagement. The holding
  becomes a live conflict the moment ClearPath appears in an assessment scope &mdash; and ClearPath is an ESP that
  will be evaluated inside this assessment, with its own findings.</p>
  <p>The obligation is to disclose in writing as soon as the conflict is known or reasonably should be known.
  Disposition is the C3PAO&rsquo;s: mitigation by removing him from the ESP portion is arguable, and removal from
  the team is cleaner. What is not available is Blalock deciding it is immaterial because the interest is in the
  parent rather than the subsidiary.</p>"""),
 ("Tidewater Assurance Group &mdash; the firm",
  "Conducted a non-certification gap assessment for Meridian ten months ago. Three days on site. The 26-page "
  "deliverable included <strong>Appendix C &mdash; Recommended Remediation Sequence</strong>, a prioritized plan "
  "with suggested tooling for five of the thirteen gaps and estimated timelines and costs. Meridian built its "
  "POA&amp;M directly from Section 4 and has worked partway through Appendix C.",
  "Avoid — the C3PAO must decline the engagement",
  """<p><strong>This is the conflict the packet does not label, and it is the one that decides the engagement.</strong></p>
  <p>The three-year bar binds <em>the C3PAO as an organization</em>, not only individual assessors. Tidewater
  consulted to prepare Meridian for a CMMC assessment within three years: a recommended remediation sequence
  with suggested tooling and cost estimates is advisory activity by any reading, and the company&rsquo;s own POA&amp;M
  is built from it.</p>
  <p>Substituting personnel does not cure a firm-level bar. Where a conflict cannot be sufficiently mitigated, the
  C3PAO does not proceed. <strong>Tidewater must decline.</strong></p>
  <p>A D3 that quietly ignores this in order to have something to plan has failed the exercise regardless of how
  good the rest of the plan is.</p>"""),
 ("The engagement letter",
  "<strong>Outcome provision:</strong> &ldquo;In the event a Certificate of CMMC Status is not issued, thirty "
  "percent (30%) of the fee shall be credited against a subsequent assessment conducted by Tidewater within twelve "
  "months.&rdquo;<br><strong>Support provision:</strong> &ldquo;Tidewater will make its assessors available to "
  "answer implementation questions arising from the assessment for a period of 60 days following the out-brief.&rdquo;",
  "Avoid — the C3PAO must decline the engagement",
  """<p><strong>Both terms are prohibited, for different reasons.</strong></p>
  <p>The <strong>outcome provision</strong> creates a financial interest contingent on the certificate issuing: the
  firm keeps the full fee only if it does. The contract may not include guarantees, promises of outcome, or any
  incentive or bonus contingent on a certificate being issued. Reading it as ordinary commercial risk-sharing is
  exactly how such a term survives review.</p>
  <p>The <strong>support provision</strong> is post-assessment consulting sold inside an assessment engagement.
  &ldquo;Answering implementation questions&rdquo; is advising on remediation, and it also creates an interest in a
  continuing relationship with the assessed party.</p>
  <p>Either term must be struck before execution. Neither is a commercial detail; both are findings about the
  C3PAO.</p>"""),
 ("Ellison&rsquo;s request",
  "&ldquo;Can you help us get the SSP written first, so we are not wasting your time?&rdquo; She has also asked "
  "twice whether fieldwork can be compressed.",
  "Avoid — the C3PAO must decline the engagement",
  """<p>The request is reasonable-sounding, made in good faith, by a company that genuinely needs the help. The
  answer is still no, and being able to say why <em>without being prompted and without lecturing her</em> is what
  Lesson 3 has been building toward.</p>
  <p>Writing the SSP is preparing the organization for the assessment. Doing it would place Tidewater squarely
  inside the three-year bar for any future certification assessment of Meridian, and it would mean the firm
  later assesses a document it authored.</p>
  <p>Note the second half too: an adverse readiness determination is a <em>legitimate</em> Phase 1 outcome, and
  under no circumstances does the C3PAO, the team, or anyone affiliated with it then help the OSC get ready. The
  consulting bar arrives at the moment it is hardest to honour.</p>
  <p>On the schedule pressure: compressing fieldwork is a scoping and sufficiency question, not a courtesy. If the
  compressed schedule would not support accurate determinations, it is refused on that ground.</p>"""),
]

SCENARIOS = [
 ("The former employer","You are a CCA. Four years ago you spent three years as a systems administrator at the "
  "company your C3PAO has just been engaged to assess. You built the file-share permission structure, and it is "
  "still in place. You left on good terms and have never provided CMMC consulting to anyone.",
  "You would be assessing your own work. The three-year bar is not engaged &mdash; you never consulted for a CMMC "
  "assessment &mdash; but impartiality under CoPC &sect;2.2 plainly is, and the structure is still in scope. "
  "Disclose; the available mitigation is removal from the team, and the C3PAO decides."),
 ("The spouse","Your spouse is a program manager at the OSC. They work on client delivery, have no IT or security "
  "responsibilities, and no involvement in the CMMC effort. You have not mentioned the relationship to anyone at "
  "your C3PAO, on the basis that it has nothing to do with the systems being assessed.",
  "The failure here is the non-disclosure, not the relationship. A family relationship with an employee of the OSC "
  "is a textbook impartiality threat and the CoPC&rsquo;s own worked examples mitigate it by removing the assessor "
  "from the team. Deciding for yourself that it is immaterial is precisely what you may not do."),
 ("The templates","Your C3PAO has a sister company operating as an RPO. Eighteen months ago that RPO sold the OSC a "
  "package of CMMC policy templates and a gap-analysis workbook. No person advised the OSC directly; it bought the "
  "materials and implemented them itself. The OSC now wants your C3PAO to conduct its Level 2 certification "
  "assessment.",
  "Supplying templates, workbooks, or tools that guide implementation is advisory activity. The bar reaches "
  "organizations, and a sister company inside the same group does not create distance. Whether a human gave advice "
  "is not the test. Expect this to be argued; the argument does not survive the text."),
 ("The drafted finding","To save time on a long evidence review, a team member pastes several paragraphs of the "
  "OSC&rsquo;s system security plan and a screenshot of its access-control configuration into a public web-based AI "
  "assistant, and asks it to draft finding language. They read the output, edit it, and enter it as their "
  "determination.",
  "Two breaches, not one. <strong>Confidentiality</strong> &mdash; engagement-confidential material describing how "
  "to attack the OSC left the boundary. <strong>Proper Use of Technology and AI</strong> &mdash; a tool produced "
  "reasoning that is the credentialed assessor&rsquo;s to produce. <strong>Information Integrity</strong> is "
  "arguably a third. Editing the output cures neither of the first two. Report to the C3PAO."),
 ("The portfolio","On the last day of on-site work the OSC&rsquo;s chief executive presents each team member with a "
  "leather portfolio embossed with the company logo, worth roughly $150. She is warm and slightly awkward about it "
  "and says explicitly that it carries no expectation, whatever the outcome. The determination has not been issued.",
  "Timing and value both matter, and the determination is still open. Accepting a gift of this value from the "
  "assessed party before determinations are issued creates an appearance problem that no amount of stated "
  "disinterest removes. Decline graciously, and disclose that it was offered."),
 ("The marginal control","One security requirement is genuinely borderline &mdash; the evidence is thin and a "
  "reasonable assessor could go either way. The OSC&rsquo;s point of contact mentions in passing that a $4M award "
  "depends on the certificate and source selection closes in three weeks. Separately, your project manager mentions "
  "the engagement is over budget and asks whether the remaining items can be closed out quickly.",
  "Neither piece of information bears on the evidence. Both are pressure &mdash; one commercial to the OSC, one "
  "commercial to your own firm, and the second is the more dangerous because it comes from inside. Decide the "
  "requirement on the objectives, document the thinness of the evidence, and disclose the budget pressure if it is "
  "affecting the assessment. Note that the CoPC&rsquo;s impartiality principle names commercial pressure explicitly."),
 ("The referral","At the out-brief the OSC asks who could help remediate the gaps you identified. A team member "
  "names a specific remediation firm, adding that they are excellent and he knows the principal well. Two months "
  "later that firm pays him a referral fee. He does not mention it to the C3PAO.",
  "Three failures compounding. Naming a remediation firm at an out-brief is advice. Naming one he has a "
  "relationship with is a conflict. Accepting an undisclosed fee arising from an assessment he conducted is a "
  "Professionalism and Impartiality breach that would end a career. The correct answer to the question asked is "
  "that the assessment team cannot make referrals."),
 ("The chapter board","You and the OSC&rsquo;s IT Director have both served on the board of your local professional "
  "association chapter for two years. You see each other at monthly meetings and occasionally have dinner with the "
  "wider board afterwards. There is no financial relationship, no family connection, and you have never advised "
  "the company.",
  "This is the scenario the CoPC does not address directly, and finding that out is part of the exercise. Say so "
  "plainly and reason from the principles: the test in &sect;2.2 is whether something could compromise the "
  "determination <em>or reasonably appear to</em>. An ongoing social relationship with a key interviewee reaches "
  "that. Disclose; the C3PAO decides whether reassignment suffices. An honest &ldquo;the document does not cover "
  "this, so here is what governs&rdquo; is stronger than a citation that does not say what you claim it says."),
]

def ethics_gate():
    intro = """<div class="panel">
<h2>The engagement</h2><div class="rule"></div>
<div class="tw"><table><tbody>
<tr><td style="width:190px"><strong>C3PAO</strong></td><td>Tidewater Assurance Group, LLC &mdash; Norfolk, Virginia. Accredited, listed in the Marketplace, in good standing.</td></tr>
<tr><td><strong>OSC</strong></td><td>Meridian Precision Defense Systems, Inc. &mdash; Dayton, Ohio. CAGE 7RK42.</td></tr>
<tr><td><strong>Request</strong></td><td>Marcus Ellison, CEO, contacted Tidewater directly requesting a Level 2 certification assessment.</td></tr>
<tr><td><strong>Why now</strong></td><td>The Army prime contract comes up for renewal in 18 months and the recompete requires a current assessment of record. No SPRS score has ever been submitted.</td></tr>
<tr><td><strong>Timing</strong></td><td>Fieldwork within 120 days. Ellison has asked twice whether it can be sooner.</td></tr>
<tr><td><strong>Prior engagement</strong></td><td>Tidewater conducted a non-certification gap assessment ten months ago.</td></tr>
<tr><td><strong>Contract</strong></td><td>Draft engagement letter circulated, not yet executed.</td></tr>
</tbody></table></div>
<h3>What the organization has produced</h3>
<p><strong>No System Security Plan &mdash; none has ever been written.</strong> No CMMC Assessment Scope statement.
No asset categorization. No access control matrix. No Customer Responsibility Matrix (neither the IT Manager nor the
Contracts Manager was familiar with the term). A thirteen-item POA&amp;M built from Tidewater&rsquo;s own report,
several items without milestone dates. An asset inventory with FCI and CUI columns completed by the IT Manager from
memory. One vulnerability scan approximately 14 months ago, summary only, remediation untracked. Audit logs enabled
and reviewed only when a problem arises. Two incidents handled by informal email, neither assessed against DFARS
252.204-7012, neither reported.</p>
<div class="verdict show"><h4>Two questions, in order</h4>
<p><strong>First:</strong> may this engagement proceed at all? Work every conflict individually. Name the principle
and the specific practice, decide disclose / mitigate / avoid, and say who decides. Some conflicts are in the team
biographies. At least one is not.</p>
<p><strong>Then:</strong> on the stated assumption that a conflict-free team and organization have been substituted,
build the plan. A plan that quietly ignores a disqualifying conflict in order to have something to plan is the exact
failure this exercise exists to prevent.</p></div>
</div>"""
    items = ""
    for i, (who, facts, ok, model) in enumerate(CONFLICTS, 1):
        ctx = f'<p>{facts}</p>'
        items += item(f"e{i}", i, who, ctx, [
            dict(label="Disposition", type="select", name="d", options=DISPO, ok=ok),
            dict(label="Principle and practice relied on", type="text", name="p",
                 ph="e.g. CoPC §2.2(d); 32 CFR §170.8(b)(17)(ii)(G)"),
            dict(label="Who decides, and why", type="area", name="w",
                 ph="Name the deciding party and the basis."),
        ], model)
    n = len(CONFLICTS)
    items += item("egate", n+1, "The gate: may this engagement proceed?",
      '<p>Having worked every conflict, answer the question Phase 1 exists to answer.</p>',
      [dict(label="May Tidewater conduct this assessment?", type="select", name="g",
            options=["Yes, with the conflicted individuals removed",
                     "Yes, with all conflicts disclosed and mitigated",
                     "No — the C3PAO must decline",
                     "Yes, subject to the OSC's written consent"],
            ok="No — the C3PAO must decline"),
       dict(label="State the basis, and what would have to change", type="area", name="b",
            ph="Cite the instrument. Then say what a different firm would need in order to take this engagement.")],
      """<p><strong>No. Tidewater must decline.</strong></p>
<p>The firm-level three-year bar is dispositive on its own: Tidewater consulted to prepare Meridian for a CMMC
assessment within three years, through a gap assessment whose Appendix C was a recommended remediation sequence with
suggested tooling, and from which the company built its POA&amp;M. Substituting personnel cannot cure a bar that
binds the organization.</p>
<p>Two prohibited contract terms would independently require renegotiation before execution, and three individual
conflicts would require dispositions. But none of that is reached, because the engagement fails at the firm level.</p>
<p><strong>What would have to change:</strong> a different, unconflicted C3PAO &mdash; which is exactly what happens
in the case. Eight months later Meridian engages Ridgeline Compliance Group, and that is the assessment you run
on Day 5.</p>""")

    items += item("ephase1", n+2, "Phase 1: is Meridian ready to be assessed?",
      '<p>Assume the conflict problem solved. Phase 1 asks one question &mdash; not whether the company will pass, '
      'but whether the evaluative work of Phase 2 can sensibly begin.</p>',
      [dict(label="Readiness determination", type="select", name="r",
            options=["Ready — proceed to Phase 2",
                     "Ready, subject to the scope being validated",
                     "Not ready — adverse readiness determination",
                     "Defer the determination pending more information"],
            ok="Not ready — adverse readiness determination"),
       dict(label="Readiness risks you would raise with the Affirming Official", type="area", name="rr",
            ph="Name risks without naming fixes. Naming a risk is assessment; naming its fix is consulting.")],
      """<p><strong>Not ready.</strong> An adverse readiness determination is a legitimate Phase 1 outcome and the
paperwork is still completed.</p>
<p>Phase 1 requires the C3PAO to review the SSP for completeness, accuracy, and consistency. <strong>There is
nothing to review.</strong> No SSP has ever been written. No scope statement, no asset categorization, no network
diagram, no access control matrix &mdash; the artifacts Phase 1 reviews do not exist. The ESP question cannot be
addressed because no Customer Responsibility Matrix exists and ClearPath has not been told an assessment is planned.
Evidence availability cannot be confirmed because the IT Manager is the sole source of most of the environment's
documentation, and is himself the subject of several gaps.</p>
<p><strong>Risks stated correctly, without fixes:</strong></p>
<ul>
<li>No System Security Plan exists; the artifact the CAP requires Phase 1 to review is absent.</li>
<li>No documented assessment boundary; scope cannot be validated under 32 CFR &sect;170.19(c), and scope
disagreements must be resolved before Phase 2 may begin.</li>
<li>ClearPath has standing remote access to a CUI-bearing system, has not been informed of the assessment, and its
MSA contains no obligation to support one.</li>
<li>The environment's documentation is held in one person's memory; that person is the subject of several
identified gaps.</li>
<li>The POA&amp;M derives from a report authored by the prospective assessor.</li>
</ul>
<p><strong>What none of these say:</strong> what Meridian should do about any of it. Including in response to
Ellison's SSP request.</p>""")

    scen = '<div class="panel"><h2>The eight CoPC scenarios</h2><div class="rule"></div>' \
      '<p>Worked in session and adjudicated against the text. For each: name the principle and the specific ' \
      'practice, decide disclose / mitigate / avoid, and say who decides. <strong>One of the eight is not ' \
      'addressed directly by the Code at all</strong> &mdash; finding that out is part of the exercise.</p>'
    for i, (t, f, a) in enumerate(SCENARIOS, 1):
        scen += ('<div style="border-top:1px solid var(--border);padding-top:1rem;margin-top:1rem">'
                 '<h3>Scenario ' + str(i) + ' &mdash; ' + t + '</h3><p>' + f + '</p>'
                 '<details style="margin-top:.5rem"><summary style="cursor:pointer;font-family:Arial,sans-serif;'
                 'font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--gold)">'
                 'Show the adjudication</summary>'
                 '<div class="verdict show" style="margin-top:.7rem"><h4>Adjudication</h4><p>' + a + '</p></div>'
                 '</details></div>')
    scen += '</div>'
    items += scen
    return tool_page("ethics-gate","Engagement &amp; Ethics Gate","Tool &middot; Deliverable D3 &middot; Lesson 3",
      "Engagement &amp; Ethics Gate &mdash; May This Assessment Proceed?",
      "Every conflict in the Meridian engagement packet, dispositioned individually and cited to the Code of "
      "Professional Conduct &mdash; then the CAP Phase 1 readiness call.",
      ["6 conflicts + 2 gates","8 CoPC scenarios","CAP Phase 1","Prints as D3"], intro, items,
      back=("Lesson 3 &mdash; Ethics, Independence &amp; Planning","lesson03.html"),
      extra_head="")

def build_all():
    return [("ethics-gate.html", ethics_gate())] + tools3.build_all()
