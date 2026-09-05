# -*- coding: utf-8 -*-
"""Tool pages 1-5: Clause Trace, CUI Determination, Ethics Gate, Scope Matrix, Evidence Triage."""
from toolkit import tool_page, item
import tools2

# ---------------------------------------------------------------- 1. CLAUSE TRACE
CHAIN = [
 ("EO 13556 (2010)","Creates the government-wide CUI Program; names NARA as Executive Agent."),
 ("32 CFR Part 2002 (2016)","Implements the CUI Program: designation, marking, safeguarding, dissemination, decontrol."),
 ("NIST SP 800-171 Rev 2 (2020)","110 security requirements for protecting CUI on nonfederal systems. Binding on no one by itself."),
 ("DFARS 252.204-7012 (2017)","Makes 800-171 contractual for DoD contractors; adds 72-hour incident reporting."),
 ("DFARS 252.204-7019 / -7020","Require a current DoD Assessment score in SPRS as a condition of award."),
 ("32 CFR Part 170 (eff. Dec 2024)","Establishes the CMMC Program: levels, assessment types, scoping, affirmation, ecosystem."),
 ("48 CFR acquisition rule (eff. Nov 2025)","Amends the DFARS so contracting officers may insert the CMMC clause."),
 ("DFARS 252.204-7021","The clause. Makes a CMMC level and status a condition of award and continued performance."),
 ("Flowdown","The prime passes the requirement to subcontractors handling covered defense information."),
]

def clause_trace():
    chain = "".join(
        f'<tr><td style="width:38px"><strong>{i}</strong></td><td><strong>{a}</strong></td><td>{b}</td></tr>'
        for i, (a, b) in enumerate(CHAIN, 1))
    intro = f"""<div class="panel">
<h2>The solicitation</h2><div class="rule"></div>
<p><strong>W58RGZ-26-R-0301</strong> &mdash; Army AMCOM, Clothing &amp; Textiles. Flame-Resistant Combat
Uniform Coat, Improved Pattern. IDIQ, firm fixed price, $12.4M over five years, total small business set-aside.
Meridian Precision Defense Systems is the incumbent; the expiring contract is $11.4M of its $17.9M annual DoD revenue.</p>
<h3>Section C &mdash; Statement of Work (extract)</h3>
<ul>
<li><strong>C.3.2</strong> On award the Government furnishes the complete Technical Data Package: engineering
drawings, pattern grading specifications, seam and stitch construction standards, flame-resistance test protocols,
approved materials list. Portions bear <strong>Distribution Statement D</strong> and are subject to the export
control provisions cited in Section I.</li>
<li><strong>C.3.3</strong> The contractor maintains and transmits monthly production status reports, first-article
test results, lot traceability records, and deviation requests, referencing drawing numbers and revision levels
from the TDP.</li>
<li><strong>C.4.1</strong> Any subcontractor that will receive, store, process, or transmit any portion of the TDP
shall be identified to the Contracting Officer, and the safeguarding and certification requirements of Section I
shall be included in that subcontract.</li>
</ul>
<h3>Section I &mdash; Contract clauses (partial)</h3>
<p>FAR 52.204-21 &middot; DFARS 252.204-7008 &middot; DFARS 252.204-7012 &middot; DFARS 252.204-7019 &middot;
DFARS 252.204-7020 &middot; <strong>DFARS 252.204-7021 &mdash; Required CMMC Status: ______ (see Section L.5)</strong>
&middot; DFARS 252.225-7048 &middot; DFARS 252.247-7023</p>
<h3>Section L.5 &mdash; Cybersecurity representations</h3>
<p>Offerors shall, at proposal submission, have a current assessment of record posted in SPRS covering all
information systems that will process, store, or transmit information furnished under C.3.2. The Contracting
Officer will verify status in SPRS prior to award. <em>The CMMC status required by DFARS 252.204-7021 shall be that
which corresponds to the categories of information identified in Section C, determined in accordance with 32 CFR
Part 170.</em></p>
<div class="verdict show"><h4>Note what the solicitation does not do</h4>
<p>It never states a level in plain language. The fill-in is blank and Section L points you back to Section C. The
level is a function of the information, and the information is described in the Statement of Work &mdash; so you
read Section C before Section I.</p></div>
</div>
<div class="panel"><h2>The chain, for reference</h2><div class="rule"></div>
<div class="tw"><table><thead><tr><th>#</th><th>Link</th><th>What it does</th></tr></thead>
<tbody>{chain}</tbody></table></div>
<p style="font-size:.82rem;color:var(--text-muted)">Links 1&ndash;5 were in force years before CMMC existed. That
is why a change to the CMMC programme at links 6&ndash;8 does not touch the obligation to protect CUI, which lives
at link 4.</p></div>"""

    items = item("q1", 1, "What authority makes CMMC applicable to this solicitation?",
      '<p>Trace it. Name the instruments in order and say what each contributes. Primary sources only &mdash; cite '
      'to part, section, or clause. A law firm alert may have oriented you; it does not appear in your answer.</p>',
      [dict(label="Your trace",type="area",name="a",
            ph="Start where the obligation originates and end at the clause in this solicitation.")],
      """<p><strong>The operative chain for this solicitation:</strong></p>
<ul>
<li><strong>32 CFR Part 170</strong> establishes the CMMC Program and, at &sect;170.14, the level structure. This is
the instrument Section L.5 expressly points to.</li>
<li><strong>The 48 CFR acquisition rule</strong> (eff. 10 Nov 2025) amended the DFARS so the Contracting Officer may
insert the CMMC clause &mdash; which is why 252.204-7021 appears in Section I at all.</li>
<li><strong>DFARS 252.204-7021</strong> is the clause that makes a CMMC status a condition of award and of continued
performance.</li>
<li>Underneath it, and independent of it: <strong>DFARS 252.204-7012</strong> imposes adequate security via
<strong>NIST SP 800-171 Rev 2</strong> and the 72-hour report; <strong>DFARS 252.204-7019/-7020</strong> require the
SPRS assessment of record that Section L.5 says will be verified; and <strong>FAR 52.204-21</strong> applies to FCI.</li>
<li>Further back: <strong>NIST SP 800-171 Rev 2</strong> specifies the requirements but binds no one on its own;
<strong>32 CFR Part 2002</strong> implements the CUI Program; <strong>EO 13556</strong> created it.</li>
</ul>
<p><strong>Assessor-Ready adds:</strong> where the chain differs for a subcontractor. C.4.1 and DFARS
252.204-7012(m) put the obligation on any subcontractor receiving the TDP &mdash; the obligation follows the
information, not the tier.</p>""")

    items += item("q2", 2, "What CMMC level, and what evidence must exist at award?",
      '<p>Reason from Section C, not from the clause list.</p>',
      [dict(label="Level", type="select", name="lvl",
            options=["Level 1","Level 2","Level 3","Cannot be determined from the excerpt"], ok="Level 2"),
       dict(label="Why &mdash; and what evidence must exist at the time of award?", type="area", name="b",
            ph="Name the information type, the category it falls in, and what Section L.5 requires to be in place.")],
      """<p><strong>Level 2.</strong> C.3.2 describes engineering drawings, pattern grading specifications,
construction standards, and test protocols, with portions bearing Distribution Statement D and subject to export
control. That is technical information with military application subject to controls on access, use, reproduction,
modification, release, or dissemination &mdash; <strong>Controlled Technical Information</strong>, a CUI category in
the NARA Registry's Defense index. CUI drives Level 2 under 32 CFR 170.14.</p>
<p>C.3.3 matters independently: production reports, first-article results, and lot traceability records referencing
TDP drawing numbers are information the contractor <em>generates</em> during performance, and DFARS 252.204-7012's
definition of covered defense information captures exactly that.</p>
<p><strong>Evidence at award:</strong> Section L.5 requires a <em>current assessment of record posted in SPRS</em>
covering all systems that will process, store, or transmit the C.3.2 information, verified by the Contracting
Officer before award. An offeror without one is ineligible. Meridian has never calculated or submitted a
score.</p>""")

    items += item("q3", 3, "Which obligations would survive if the CMMC clause were struck tomorrow?",
      '<p>Ellison will ask what the company is actually exposed to, and whether any of this can wait. Answer in '
      'terms he can act on.</p>',
      [dict(label="Your answer to the executive", type="area", name="c",
            ph="Separate what CMMC adds from what already binds this company, and say what that means today.")],
      """<p><strong>What CMMC adds</strong> is the verification regime: a stated level and status as a condition of
award under DFARS 252.204-7021, assessed under 32 CFR Part 170.</p>
<p><strong>What binds the company independently of it:</strong> DFARS 252.204-7012 &mdash; adequate security via all
110 NIST SP 800-171 Rev 2 requirements, the 72-hour DIBNet report, malicious-software submission, 90-day media
preservation, DoD access on request, the cloud-provider conditions, and flowdown at (m). DFARS 252.204-7019 and
-7020 and the SPRS assessment of record. FAR 52.204-21 wherever FCI is handled. None of that arrives with CMMC and
none of it leaves with it.</p>
<p><strong>What that means for Meridian today:</strong> all three contracts carry 252.204-7012. The company has an
unenforced MFA gap on the VPN, six active accounts belonging to separated employees, no reviewed audit logs, and two
security events that were never assessed against the clause's reporting threshold and never reported. That is not a
future exposure contingent on an assessment &mdash; it is present non-conformity with a clause the company signed.</p>
<div class="tw"><table><thead><tr><th>The distinction to hold</th></tr></thead><tbody>
<tr><td>CMMC changes <em>how conformity is demonstrated</em>. It does not change what must be true. An assessor who
cannot state that cleanly will be talked into treating programme changes as relief from the underlying
obligation.</td></tr></tbody></table></div>""")
    return tool_page("clause-trace","Clause Trace","Tool &middot; Deliverable D1 &middot; Lesson 1",
      "Clause Trace &mdash; From Executive Order to Contract",
      "Build the chain that binds Meridian to solicitation W58RGZ-26-R-0301, then answer the three questions "
      "the Regulatory Trace Memo asks. Primary sources only, cited to part, section, or clause.",
      ["3 questions","Primary sources only","Prints as D1"], intro, items,
      back=("Lesson 1 &mdash; Compliance Landscape","lesson01.html"))

# ---------------------------------------------------------------- 2. CUI DETERMINATION
CUI_ITEMS = [
 ("Actuator housing technical data packages",
  "Engineering drawings, dimensional tolerances, material specifications and qualification test protocols furnished "
  "by AMCOM after award under W58RGZ-23-C-0174. Portions bear Distribution Statement D and are ITAR-controlled. "
  "Held on SYS-003 and in the Arena PLM.",
  'CUI &mdash; &ldquo;ITAR Data&rdquo;', "CUI",
  "Invented category name",
  """<p><strong>CUI &mdash; and the company is right about that.</strong> Controlled Technical Information &middot;
  <strong>CTI</strong> &middot; Specified &middot; banner <strong>CUI//SP-CTI</strong>. The Registry cites 48 CFR
  252.204-7012; distribution statements under DoDI 5230.24; &ldquo;technical data&rdquo; as defined at DFARS
  252.227-7013.</p>
  <p><strong>The error is the citation, not the determination.</strong> &ldquo;ITAR Data&rdquo; is not a Registry
  category name. ITAR is a <em>control regime</em> under 22 CFR Parts 120&ndash;130 that may apply to the same
  information; it is not the CUI category, and the two answer different questions. This is the most common
  real-world pattern in aerospace and ordnance work: people know the material is controlled, and reach for the
  regime they hear about most rather than the Registry.</p>
  <p>Ask what a document containing this data must be marked, and who applies the marking if AMCOM failed to.</p>"""),
 ("UAV airframe bracket design files",
  "FEA reports and engineering drawings to MIL-DTL-31000C, produced <em>by Meridian</em> under the Raytheon "
  "subcontract RTX-SUB-2024-4489 and delivered to the prime. Held in the PLM and the GCC High tenant.",
  'CUI &mdash; &ldquo;CTI&rdquo;', "CUI", "Correct",
  """<p><strong>CUI, and correct.</strong> Controlled Technical Information &middot; CTI &middot; Specified.</p>
  <p><strong>Note what makes it correct, because it is the part contractors get wrong.</strong> Meridian
  <em>generated</em> this material itself &mdash; it was not furnished by the Government. It is still CUI, because
  the definition at 32 CFR 2002.4 reaches information an entity creates for or on behalf of the Government, and
  because DFARS 252.204-7012 defines covered defense information to include information the contractor collects,
  develops, receives, transmits, uses or stores in support of contract performance.</p>
  <p>Mark this one right and say why. An inventory in which every correct call is an accident is not an inventory
  you can rely on for the rest.</p>"""),
 ("Personnel security submissions",
  "SF-86 data and DISS records for staff requiring a determination, collected on behalf of the Government. Held by "
  "Gregory Farris, FSO, in a restricted SharePoint library in the GCC High tenant.",
  'CUI &mdash; &ldquo;Privacy&mdash;Personnel&rdquo;', "CUI",
  "Label is not a Registry name; substance correct",
  """<p><strong>CUI, and the company is right in substance.</strong> Privacy index: <strong>Personnel Records
  &middot; PERS</strong>, and/or <strong>General Privacy &middot; PRVCY</strong>. This material is collected and
  held <em>for the Government</em> under a personnel security process, which is what puts it inside the CUI
  definition.</p>
  <p><strong>Pair this deliberately with item 5.</strong> Both concern employees; one is CUI and one is not. The
  distinction is not sensitivity &mdash; it is who the information was created for. SF-86 and DISS material is
  collected on the Government's behalf; a W-4 and an ESOP participant statement are not.</p>"""),
 ("SBIR final technical report and composite actuator research data",
  "Research output under NAVAIR SBIR Phase II N68335-22-C-0552, now in its final reports phase. The contract "
  "identifies CUI//SP-EXPT. Analysis data is held in AWS GovCloud; the draft report is on SYS-003.",
  '&ldquo;Proprietary R&amp;D &mdash; company confidential&rdquo;', "CUI",
  "Treated as company property when the contract says otherwise",
  """<p><strong>CUI.</strong> <strong>Export Controlled &middot; EXPT</strong>, and the contract itself identifies
  <strong>CUI//SP-EXPT</strong>. Read the category page for whether the authority relied on makes it Specified or
  Basic &mdash; that is the point of the item.</p>
  <p><strong>The error is a category error, not a citation error.</strong> Meridian has classified work it performed
  as its own commercial property. But the CUI definition expressly reaches information an entity creates or
  possesses <em>for or on behalf of</em> the Government, and this was performed under a $1.85M federal contract that
  names the category.</p>
  <p><strong>SBIR data rights are real, and they are a different question.</strong> A contractor may hold data
  rights in technical data and that information may still be CUI. Rights govern what the Government may do with it;
  CUI status governs how it must be protected. Conflating the two is the specific error here, and it is extremely
  common in research-performing contractors.</p>
  <p>An assessor who says &ldquo;this is CUI//SP-EXPT under the contract, and your data rights position is
  unaffected by that&rdquo; has made the determination and defused the argument in one sentence.</p>"""),
 ("Payroll, ESOP participant records, and commercial supplier invoices",
  "Payroll and benefits for all 147 employees, ESOP participant statements, and invoices from commercial "
  "raw-material suppliers. Collected and generated by Meridian as an employer and as a business, at its own "
  "expense. Payroll and accounting in QuickBooks, read-only access held by an external CPA.",
  'Inconsistent &mdash; two company records disagree', "Neither CUI nor FCI",
  "Internal contradiction",
  """<p><strong>Neither CUI nor FCI.</strong> Fails 32 CFR 2002.4 &mdash; created and held by Meridian as an employer
  and a business, at its own expense, for its own purposes. Fails FCI at FAR 52.204-21(a) &mdash; not provided by or
  generated for the Government under any of the three contracts.</p>
  <p><strong>Resolve the contradiction; do not average it.</strong> The company's data classification page says this
  material is sensitive business data outside the CUI definition &mdash; that page is right. Its third-party register
  records Whitmore &amp; Associates as handling &ldquo;employee PII / CUI-Privacy,&rdquo; while stating elsewhere that
  the firm is &ldquo;not in SSP scope&rdquo; &mdash; those entries are wrong and mutually inconsistent.</p>
  <p>Neither page is <em>authority</em>; the Registry and the definition are. Expect resistance on this item: it is
  personal, it is regulated, and it is obviously sensitive. All true, none of it relevant. Ask what law requires an
  <em>agency</em> to control it.</p>"""),
 ("Cost and pricing data under the Raytheon subcontract",
  "Indirect cost pools, negotiated labour rates, cost proposals and the supporting build-ups behind them, submitted "
  "to the prime under the CPFF subcontract and flowed to AFLCMC. Held on SYS-003 and in email.",
  'FCI', "Arguably CUI — at minimum not settled",
  "Classified too low",
  """<p><strong>Arguably CUI, and at minimum not settled.</strong> <strong>General Procurement and Acquisition
  &middot; PROCURE &middot; Specified &middot; CUI//SP-PROCURE</strong> covers cost or pricing data, contract
  information, indirect costs and direct labour rates on its face. Authorities: 48 CFR 3.104-4; 41 U.S.C. 2105;
  48 CFR 3.104-8; 48 CFR 52.215-1(e). Pre-award proposal evaluation material held by the Government would instead be
  <strong>Source Selection &middot; SSEL</strong>.</p>
  <p><strong>This is the item classified too low, and it is the direction that costs money.</strong> Everything else
  in this inventory is either correct or over-reaching; this reverses it. A cost-plus subcontract generates far more
  cost and pricing material than a firm fixed price one, which is why the exposure sits here rather than on the
  larger Army contract.</p>
  <p>If the company is wrong, material on SYS-003 and in email has been handled at the FCI standard when it should
  have been handled at the CUI standard &mdash; which changes the boundary and possibly the level analysis.</p>
  <p>The argument is not airtight, and saying so is the stronger answer. What would settle it: the subcontract
  terms, any markings Raytheon applied, and ultimately the contracting officer.</p>"""),
]

def cui_determination():
    intro = """<div class="panel">
<h2>How to work this</h2><div class="rule"></div>
<p>Six information types, with Meridian's own classification reproduced verbatim. Treat each as a claim under
test, not as a starting point you inherit.</p>
<p>For every item you determine is <strong>CUI</strong>: the exact Registry category name, the marking, Basic or
Specified, and the authority the Registry cites. For every item you determine is <strong>FCI or neither</strong>:
the element of the definition it fails, and which definition you applied.</p>
<p>Then say what kind of error the company made where it is wrong &mdash; a category that does not exist, a category
that exists but does not fit, an internal contradiction, or an item classified too low.</p>
<div class="verdict show"><h4>Before you start</h4>
<p><strong>Some of the company's calls are right.</strong> You are not looking for an organization that got
everything wrong. You are looking for the specific places where a plausible-sounding label does not survive contact
with the authority &mdash; and for the one place where the company has under-classified, which is the direction
that costs it money.</p>
<p>One item will not resolve cleanly from the Registry. That is a real outcome. Say so, say what you checked, and
say what would settle it.</p></div>
<h3>Two definitions, for reference</h3>
<p><strong>FCI &mdash; FAR 52.204-21(a).</strong> Information, not intended for public release, provided by or
generated for the Government under a contract to develop or deliver a product or service. Excludes public
information and simple transactional information such as that necessary to process payments.</p>
<p><strong>CUI &mdash; 32 CFR 2002.4.</strong> Information the Government creates or possesses, or that an entity
creates or possesses for or on behalf of the Government, that a law, regulation, or government-wide policy requires
or permits an agency to handle with safeguarding or dissemination controls. Excludes classified information and
information a company develops purely at its own expense for its own purposes.</p>
</div>"""
    items = ""
    for i, (name, desc, claim, correct, errkind, model) in enumerate(CUI_ITEMS, 1):
        ctx = (f'<p>{desc}</p><div class="in-practice"><div class="ip-label">The company&rsquo;s classification</div>'
               f'<p style="margin:0"><strong>{claim}</strong></p></div>')
        items += item(f"c{i}", i, name, ctx, [
            dict(label="Your determination", type="select", name="det",
                 options=["CUI","FCI","Neither CUI nor FCI",
                          "Open item — cannot be settled from the Registry",
                          "Arguably CUI — at minimum not settled"], ok=correct),
            dict(label="Category / marking / Basic or Specified / authority — or the definition element it fails",
                 type="area", name="cite",
                 ph="Exact Registry category name, marking, Basic or Specified, and the authority cited."),
            dict(label="Is the company right? If not, what kind of error is it?", type="area", name="err",
                 ph="A category that does not exist, one that exists but does not fit, an internal contradiction, or classified too low."),
        ], model + f'<p style="margin-top:.7rem"><strong>Error type:</strong> {errkind}.</p>')
    items += item("c7", 7, "The determination that follows: level, boundary, and what you tell Priya Mehta",
      '<p>Three contracts are in play and all three carry DFARS 252.204-7012. State the level obligation and where '
      'the CUI boundary falls &mdash; naming systems, because &ldquo;the network&rdquo; is not a boundary.</p>',
      [dict(label="Level obligation and authority", type="area", name="lvl",
            ph="All three contracts. Name the authority for each."),
       dict(label="Inside the boundary / outside the boundary", type="area", name="bnd",
            ph="Named systems, with what places each there.")],
      """<p><strong>Level.</strong> CMMC Level 2 under DFARS 252.204-7021 for the Army prime contract, which carries
the clause expressly along with -7019 and -7020. The Raytheon subcontract and the NAVAIR SBIR both carry
252.204-7012 and both involve CUI, so the safeguarding obligation attaches across all three regardless of which one
carries the CMMC clause. FAR 52.204-21 continues to apply wherever FCI is handled and is <em>subsumed, not
replaced</em>.</p>
<p>Authority chain: 32 CFR 170.14 for the level structure; DFARS 252.204-7012 for the safeguarding obligation
already in force on all three; DFARS 252.204-7019/-7020 for the SPRS assessment of record.</p>
<p><strong>Inside:</strong> SYS-001 and SYS-002 (domain controllers), SYS-003 (file server, primary CUI store),
SYS-004 (PLM), SYS-005 &times;14 and SYS-006 &times;6 (engineering workstations), SYS-007 (GCC High tenant),
SYS-008 (AWS GovCloud), SYS-009/010 (firewall and VPN), SYS-011 (IDS), SYS-012 (MFP), the core switch, the CORP-LAN
workstations, and the Huntsville network equipment. The absence of VLAN enforcement between CORP-LAN and ENG-LAN
pulls in everything that can reach the CUI stores.</p>
<p><strong>Outside:</strong> Whitmore &amp; Associates as a service, and FastenerTech. Little else with
confidence.</p>
<p><strong>What separates Competent from Assessor-Ready:</strong> saying that the boundary is wide because of two
specific absences &mdash; no enforced segmentation and no asset inventory &mdash; rather than because the company is
generally disorganised. Meridian has an SSP, ten policies and an accurate network diagram. Naming exactly which
missing artifact closes the conditional categories is the difference.</p>
<p>And saying what would change each answer: what the subcontract terms would have to say for item 6 to resolve;
what Microsoft would have to commit to beyond the FedRAMP authorisation; and what evidence would move the Huntsville
workstations across the line.</p>
<p><strong>Third parties:</strong> ClearPath requires flow-down under 252.204-7012(m) and ESP treatment; Acuitas,
AeroComp and Secure Shred all receive or take custody of CUI and none has an adequate agreement; the GCC High and
GovCloud tenants are CSP questions under (b)(2)(ii)(D). The full ESP analysis belongs to Day 3 &mdash; naming the
deferral is a strength, not a gap.</p>""")
    return tool_page("cui-determination","CUI Determination","Tool &middot; Deliverable D2 &middot; Lesson 2",
      "CUI Determination &mdash; Auditing Meridian&rsquo;s Inventory",
      "Six information types, six company classifications, and your determination on each. Cited to the NARA CUI "
      "Registry, or to the element of the definition the item fails.",
      ["6 items + boundary","NARA Registry","Prints as D2"], intro, items,
      back=("Lesson 2 &mdash; FCI, CUI &amp; the Regulatory Stack","lesson02.html"))

def build_all():
    out = [("clause-trace.html", clause_trace()),
           ("cui-determination.html", cui_determination())]
    out += tools2.build_all()
    return out
