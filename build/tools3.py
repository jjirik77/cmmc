# -*- coding: utf-8 -*-
"""Tool pages: Scope & Asset Matrix, Evidence Triage."""
from toolkit import tool_page, item
import tools4

CATS = ["CUI Asset","Security Protection Asset","Contractor Risk Managed Asset",
        "Specialized Asset","Out-of-Scope Asset"]

ASSETS = [
 ("SYS-001 / SYS-002 &mdash; domain controllers","MPDS-CORP-DC01 and DC02, Windows Server 2019, Dayton. Active "
  "Directory, DNS, DHCP and Group Policy for the whole environment, including Huntsville over the IPsec tunnel.",
  "Security Protection Asset",
  "They hold no CUI directly but provide authentication, group policy, and access control to the entire scope. A "
  "CUI Asset argument is acceptable only if argued from what they store rather than from importance."),
 ("SYS-003 &mdash; MPDS-FILE-SRV01","Windows Server 2022 file server, Dayton, on ENG-LAN. Identified in the case as "
  "the <strong>primary</strong> CUI store.","CUI Asset",
  "Stores CUI. The most straightforward call on the sheet, and the asset every other decision orbits."),
 ("SYS-004 &mdash; MPDS-APP-LNX01","Arena PLM on Ubuntu 22.04, Dayton, on ENG-LAN. Drawings, bills of material, and "
  "engineering change data for all three contracts.","CUI Asset",
  "Processes and stores CUI. Note that it is a Linux host in an otherwise Windows estate &mdash; worth asking "
  "whether it sits inside the patching and logging regimes that cover the Windows machines. It does not."),
 ("SYS-005 &times;14 &mdash; Dayton engineering workstations","CAD/CAM workstations, Windows 10 Enterprise 22H2. Not "
  "enrolled in any configuration management tool. Roughly four are 90+ days behind on critical Windows updates.",
  "CUI Asset",
  "They open and store CUI drawings. The patching and configuration-management failures are <em>findings</em>, not "
  "categorization questions &mdash; watch for confusing a control failure with a scoping decision."),
 ("SYS-006 &times;6 &mdash; Huntsville engineering workstations","Windows 11 Enterprise, reached over the always-on "
  "IPsec tunnel to the Dayton domain controllers. No local IT staff at the site.","CUI Asset",
  "Same reasoning as the Dayton workstations. The absence of local IT, and Meridian&rsquo;s lack of control over the "
  "building, are physical and personnel findings; neither moves the asset out of scope."),
 ("SYS-007 &mdash; Microsoft 365 GCC High tenant","Email, Teams, SharePoint, OneDrive. FedRAMP High authorised. "
  "Conditional Access only partially configured; guest access to SharePoint not fully restricted; a shared service "
  "account holds Global Admin with no individual owner assigned.","CUI Asset",
  "A CUI Asset by category <em>and</em> a CSP question by obligation &mdash; two answers, not one. The FedRAMP High "
  "authorisation satisfies the baseline; the tenant misconfigurations are separate findings against access control "
  "and configuration requirements. Teams routinely collapse the two and answer neither properly."),
 ("SYS-008 &mdash; AWS GovCloud (US-West)","Compute and S3 used for SBIR finite-element analysis. FedRAMP High. "
  "Meridian manages IAM directly; root account MFA is enabled. CUI reaches it from SYS-003 by manual upload with no "
  "automated control.","CUI Asset",
  "Stores and processes CUI. The manual upload path is the interesting part: an uncontrolled transfer between two "
  "in-scope systems is a data flow the SSP must describe, and does not."),
 ("SYS-009 &mdash; FortiGate 200F firewall","Perimeter control at Dayton. Single ISP, 1Gbps, no DMZ. Administered "
  "remotely by ClearPath IT Solutions.","Security Protection Asset",
  "Provides the perimeter boundary for the assessment scope. Note that remote administration by an external party "
  "makes ClearPath a provider handling Security Protection Data &mdash; a separate analysis in Part 3."),
 ("SYS-010 &mdash; VPN gateway","FortiGate SSL VPN module. Roughly 22 users, including ClearPath technicians. "
  "Authenticates against Active Directory with username and password only &mdash; no MFA. Six accounts belong to "
  "separated employees.","Security Protection Asset",
  "It also transmits CUI, so a CUI Asset argument is available and defensible. What is not defensible is leaving it "
  "out because it is &ldquo;part of the firewall.&rdquo;"),
 ("SYS-011 &mdash; Snort IDS/IPS sensor","Snort 3.x on Ubuntu 20.04, Dayton, on MGMT-LAN.",
  "Security Protection Asset",
  "Provides a monitoring capability to the scope. Ask what it feeds and who reads it &mdash; there is no SIEM and no "
  "review process, which is a finding against the audit requirements rather than a scoping question."),
 ("SYS-012 &mdash; Xerox AltaLink C8045","Multifunction printer on ENG-LAN, Dayton. Produces hard-copy CUI output "
  "from the PLM and the file server.","CUI Asset",
  "It processes and outputs CUI. A team may argue IoT and therefore Specialized &mdash; accept that only if they "
  "address whether the device is <em>unable to be fully secured</em>, and an enterprise MFP with a management "
  "interface generally is securable, which defeats the argument. Ask separately what it retains on internal storage."),
 ("Cisco Catalyst 2960-X &mdash; core switch","Dayton. Carries CORP-LAN, ENG-LAN and MGMT-LAN, all routing freely. "
  "No VLAN-enforced segmentation. MGMT-LAN is separated by policy only, not at the switch.",
  "Security Protection Asset",
  "It carries the whole environment and provides &mdash; or here conspicuously fails to provide &mdash; "
  "segmentation. This asset is why a compromise on CORP-LAN reaches the CUI stores on ENG-LAN, and why almost "
  "nothing at Meridian can be scoped out."),
 ("CORP-LAN workstations","Administrative and general-user machines on 10.10.1.0/24 &mdash; finance, HR, contracts, "
  "management. No CUI is stored on them by design.","CUI Asset",
  "<strong>The central contested call.</strong> Contractor Risk Managed would be the right category if the condition "
  "were met &mdash; but that treatment requires the asset to be documented in the asset inventory, the SSP, and the "
  "network diagram, and Meridian has <em>no asset inventory at all</em>. Absent that, the category is unavailable "
  "and the machines fall back to what they can do: reach SYS-003 and SYS-004 over unsegmented routing with domain "
  "credentials."),
 ("Huntsville network equipment","Cisco RV345 perimeter router and a UPS, in an <strong>unlocked utility closet "
  "accessible to building maintenance</strong>. Meridian does not control the building access system &mdash; the "
  "site is a commercial office lease.","Security Protection Asset",
  "It terminates the IPsec tunnel carrying CUI between the sites. The physical exposure is a serious PE finding and "
  "does not change the category &mdash; but it does change what evidence you would want about who can reach it."),
]

PROVIDERS = [
 ("ClearPath IT Solutions","Managed service provider. Remote administration via the SSL VPN, help desk, and "
  "firewall administration. Holds <strong>standing domain administrator rights</strong>. Month-to-month agreement, "
  "no DFARS flow-down, no cybersecurity requirements, no right-to-audit, no background-check verification.",
  "ESP (non-cloud) handling CUI",
  "<strong>The most consequential provider in the case.</strong> It handles CUI and Security Protection Data, so it "
  "sits squarely inside the ESP rule: documented in the SSP with a Customer Responsibility Matrix, evaluated inside "
  "Meridian&rsquo;s assessment, personnel expected to participate. None of that exists. Note the separate nonlocal "
  "maintenance requirement at MA.L2-3.7.5 &mdash; standing remote admin with no MFA and no session control fails it "
  "directly."),
 ("Microsoft &mdash; M365 GCC High","Email, Teams, SharePoint, OneDrive holding CUI. FedRAMP High authorised. "
  "Tenant configuration only partially complete.","CSP processing and storing CUI",
  "The FedRAMP baseline obligation under DFARS 252.204-7012(b)(2)(ii)(D) is <em>satisfied</em> &mdash; High exceeds "
  "Moderate. What remains is whether the agreement establishes the reporting, preservation and DoD access "
  "obligations, and separately whether the tenant is configured to protect the CUI in it. An authorised platform "
  "that is misconfigured is not a compliant environment."),
 ("AWS GovCloud (US-West)","Compute and S3 for SBIR analysis. FedRAMP High. Meridian manages IAM directly; root "
  "account MFA enabled.","CSP processing and storing CUI",
  "Same analysis as the M365 tenant, and better executed &mdash; root MFA is on and Meridian owns the IAM "
  "configuration. Credit teams that notice this is the one cloud service where the customer-side configuration "
  "looks defensible, and that the manual upload path into it is still an uncontrolled CUI flow."),
 ("Acuitas Machining Inc.","Sub-tier machining overflow. Receives CUI drawings via a shared SharePoint link from the "
  "GCC High tenant. <strong>No formal agreement.</strong> Never assessed.","ESP (non-cloud) handling CUI",
  "Receives CUI in order to perform work, so the flow-down obligation at DFARS 252.204-7012(m) attaches and there is "
  "no agreement carrying it. Whether Acuitas is best analysed as a subcontractor requiring flow-down, an ESP "
  "requiring a CRM, or both is genuinely arguable &mdash; say which you chose and why. You meet this company again "
  "on Friday afternoon, cold."),
 ("AeroComp Composites LLC","Composite structural parts for the UAV brackets. Receives 2D drawings by encrypted "
  "email. Flow-down referenced in the purchase order but never verified. Never assessed.",
  "ESP (non-cloud) handling CUI",
  "Receives CUI. A reference in a purchase order is a start and it is not verification &mdash; ask what evidence "
  "establishes that the clause actually reached the subcontract and was accepted. &ldquo;Partial&rdquo; flow-down is "
  "not a category the regulation recognises."),
 ("Secure Shred AL","Offsite paper shredding for the Huntsville site. Takes physical custody of hard-copy CUI. "
  "<strong>No NDA and no CUI handling agreement.</strong>","ESP (non-cloud) handling CUI",
  "The provider most often missed, because it handles paper rather than data. Taking custody of CUI in physical form "
  "is squarely within the rule. Contrast the Dayton arrangement, where shredding is in-house to DIN 66399 P-4 and is "
  "compliant &mdash; the same obligation, met at one site and not the other."),
 ("Whitmore &amp; Associates LLC","External CPA. Read-only QuickBooks access. Recorded in the case as "
  "&ldquo;not in SSP scope.&rdquo;","Neither",
  "No CUI &mdash; consistent with the Day 2 determination that payroll and ESOP records are neither CUI nor FCI. "
  "Credit answers that say <em>what was checked</em> before concluding it. Note that the company&rsquo;s own "
  "third-party register contradicts itself here, and the register is not authority."),
 ("FastenerTech Supply","Precision hardware components. No CUI access.","Neither",
  "A genuine out-of-scope supplier, included so the matrix is not simply a list of failures. Say what you checked: "
  "what the purchase orders convey, and whether any drawing or specification reaches them. Here none does."),
]

def scope_matrix():
    intro = """<div class="panel">
<h2>Before you categorize anything</h2><div class="rule"></div>
<p>Each category answers one question: <strong>what does this asset do with CUI?</strong> Fill in what an asset
<em>can reach</em> before you decide what it is.</p>
<div class="tw"><table>
<thead><tr><th>Category</th><th>The defining test</th><th>How it is assessed</th></tr></thead>
<tbody>
<tr><td><strong>CUI Asset</strong></td><td>Processes, stores, or transmits CUI</td><td>All Level 2 requirements</td></tr>
<tr><td><strong>Security Protection Asset</strong></td><td>Provides security functions or capabilities to the scope, whether or not it touches CUI</td><td>Requirements relevant to the function provided</td></tr>
<tr><td><strong>Contractor Risk Managed</strong></td><td>Can, but is not intended to, handle CUI <em>because of security policy, procedures, and practices in place</em></td><td>SSP review primarily</td></tr>
<tr><td><strong>Specialized Asset</strong></td><td>Can handle CUI but is unable to be fully secured. Closed list: IoT, IIoT, OT, GFE, Restricted Information Systems, Test Equipment</td><td>SSP review only</td></tr>
<tr><td><strong>Out-of-Scope</strong></td><td>Cannot handle CUI and provides no security protection for CUI Assets</td><td>Not assessed</td></tr>
</tbody></table></div>
<div class="verdict show"><h4>The condition that decides this matrix</h4>
<p>Two categories are <strong>conditional</strong>. Contractor Risk Managed depends on security policy, procedures,
and practices being in place. Specialized depends on documentation in the inventory, the SSP, and the network
diagram, plus demonstrable management through risk-based security policies.</p>
<p><strong>Meridian has no SSP, no network diagram, no real asset inventory, and no written security policy of
any kind.</strong> Both conditional categories are therefore closed to it, and assets fall back to what they are
capable of doing. That single fact decides most of what follows &mdash; and granting relief the organization has
not earned is the most common scoping error in the field.</p></div>
<p style="font-size:.82rem;color:var(--text-muted)"><strong>The asymmetry to remember:</strong> scoping an asset in
that did not need to be in costs the organization time. Scoping an asset out that should have been in produces an
assessment result that is wrong. When you are genuinely uncertain, the direction to err is not the comfortable
one.</p>
</div>"""
    items = ""
    for i, (name, desc, ok, model) in enumerate(ASSETS, 1):
        items += item(f"a{i}", i, name, f'<p>{desc}</p>', [
            dict(label="What can it reach?", type="text", name="reach",
                 ph="Fill this before the category — it is the column that decides."),
            dict(label="Category", type="select", name="cat", options=CATS, ok=ok),
            dict(label="Basis — reference the defining test, not what the asset is for", type="area", name="why",
                 ph='e.g. "Can reach the PLM through a browser on the same flat subnet; no policy prevents it."'),
        ], f"<p><strong>{ok}.</strong> {model}</p>")
    n = len(ASSETS)
    for j, (prov, desc, ok, model) in enumerate(PROVIDERS, 1):
        items += item(f"p{j}", n+j, f"Provider &mdash; {prov}", f'<p>{desc}</p>', [
            dict(label="Classification", type="select", name="cls",
                 options=["ESP (non-cloud) handling CUI","ESP handling Security Protection Data",
                          "CSP processing and storing CUI","Neither"], ok=ok),
            dict(label="What does that oblige — and does it exist?", type="area", name="ob",
                 ph="Name the obligation and its current state. Classification and obligation are two answers, not one."),
        ], f"<p><strong>{ok}.</strong> {model}</p>")
    n += len(PROVIDERS)
    items += item("bnd", n+1, "The assessment boundary",
      '<p>State it in prose. Name what is inside, name what is outside, and say what places each there. If nothing '
      'is outside, say that and say why &mdash; it is a legitimate answer and it needs the same defence as any '
      'other.</p>',
      [dict(label="The boundary", type="area", name="b",
            ph='Named systems. "The network" is not a boundary.')],
      """<p><strong>Everything at Dayton and Huntsville is inside the boundary except Whitmore &amp; Associates and
FastenerTech.</strong> Not because the assessor is being difficult, but because of two specific absences.</p>
<p><strong>First, no enforced segmentation.</strong> CORP-LAN, ENG-LAN and MGMT-LAN route freely through the core
switch, so every machine on CORP-LAN can reach the CUI stores on ENG-LAN. Meridian has three subnets and one
security domain.</p>
<p><strong>Second, no asset inventory.</strong> Both conditional categories require the asset to be documented in
an inventory that does not exist. That single gap closes Contractor Risk Managed and Specialized to every asset in
the environment, however well an individual asset might otherwise fit.</p>
<p>Note what makes this <em>different</em> from a company with nothing. Meridian has an SSP, ten policies, and a
network diagram. It still cannot claim the conditional treatments, because the specific artifact those treatments
depend on is the one it does not have. Saying that precisely &mdash; rather than &ldquo;they have no
documentation&rdquo; &mdash; is the difference between a Competent and an Assessor-Ready boundary statement.</p>
<p>A hostile reader who wants the boundary smaller should not be able to move any line in it.</p>""")
    items += item("flow", n+2, "Flowdown",
      '<p>Which of Meridian&rsquo;s suppliers, subcontractors, or providers must receive DFARS 252.204-7012, '
      'and on what basis? Include anyone downstream who will handle covered defense information.</p>',
      [dict(label="Parties requiring flowdown, and the basis", type="area", name="f",
            ph="Name the party, the basis, and the current state.")],
      """<p>DFARS 252.204-7012(m) requires the clause in subcontracts for operationally critical support or where
performance will involve covered defense information. Meridian has <strong>four</strong> parties in that category
and a written flow-down for none of them.</p>
<div class="tw"><table><thead><tr><th>Party</th><th>Basis</th><th>Current state</th></tr></thead><tbody>
<tr><td><strong>ClearPath IT Solutions</strong></td><td>Standing domain admin over systems holding CUI; also handles Security Protection Data</td><td>Month-to-month agreement with no DFARS flow-down, no cybersecurity requirements, no right to audit</td></tr>
<tr><td><strong>Acuitas Machining</strong></td><td>Receives CUI drawings via a SharePoint link to perform machining work</td><td><strong>No formal agreement at all</strong></td></tr>
<tr><td><strong>AeroComp Composites</strong></td><td>Receives 2D drawings by encrypted email</td><td>Referenced in the purchase order, never verified &mdash; ask what evidence shows the clause reached and was accepted</td></tr>
<tr><td><strong>Secure Shred AL</strong></td><td>Takes physical custody of hard-copy CUI at Huntsville</td><td>No NDA, no CUI handling agreement</td></tr>
</tbody></table></div>
<p><strong>FastenerTech</strong> receives no CUI and requires no flow-down &mdash; say what you checked before
concluding it.</p>
<p><strong>The observation that marks a strong answer:</strong> the obligation follows the information, not the
contract value or the tier. Secure Shred is a shredding vendor and Acuitas is an overflow machine shop; neither
looks like a defense subcontractor, and both handle CUI. Meridian&rsquo;s Contract Manager tracks DFARS clauses on
the three prime and subcontract vehicles and has not applied the same discipline downward.</p>""")
    items += item("open", n+3, "Open items",
      '<p>What you could not determine from the available material, why it matters to the scope, and what evidence '
      'would settle each. <strong>There are at least two.</strong></p>',
      [dict(label="Open items", type="area", name="o",
            ph="What you could not determine / why it affects scope / what would settle it.")],
      """<p><strong>Two that should appear in every competent matrix:</strong></p>
<ul>
<li><strong>What the Xerox AltaLink retains on internal storage, and for how long.</strong> An enterprise MFP that
spools and retains CUI print and scan jobs is an information system holding CUI, and the case does not say whether
this one does. Settled by examining the device&rsquo;s storage configuration directly &mdash; an inspection, not an
interview.</li>
<li><strong>Whether an asset inventory exists in any form.</strong> It is the condition on both conditional
categories. If nothing exists, Contractor Risk Managed and Specialized are closed to the entire environment at
once, which is what drives the boundary above. Settled by asking for the document and accepting only a document.</li>
</ul>
<p><strong>Others worth credit:</strong> what the manual upload path from SYS-003 to AWS GovCloud actually transfers
and who performs it; whether the ClearPath technicians hold individual accounts or a shared one; whether the
Huntsville workstations store CUI locally or work over the tunnel; what the M365 GCC High Conditional Access
exclusions contain; and whether Acuitas is best treated as a subcontractor, an ESP, or both.</p>
<p style="margin-top:.8rem"><em>An open item is not an admission of failure. Naming precisely what you could not
determine, why it matters, and what evidence would settle it is stronger work than a confident answer that rests on
an assumption.</em></p>""")
    return tool_page("scope-matrix","Scope &amp; Asset Matrix","Tool &middot; Deliverable D4 &middot; Lesson 4",
      "Scope &amp; Asset Applicability Matrix",
      "Every asset in the Meridian environment, categorized against the defining test and justified &mdash; "
      "then the boundary, the provider analysis, flowdown, and the open items.",
      ["14 assets","5 providers","Boundary + flowdown","Prints as D4"], intro, items,
      back=("Lesson 4 &mdash; Scoping &amp; Asset Categorization","lesson04.html"))


ARTIFACTS = [
 ("Artifact 1 &mdash; Access Control Policy (POL-001 v1.2)",
  "Supplied by Diana Kowalczyk, CISO, as a PDF. Document register shows last reviewed January 2024 &mdash; one of "
  "the four policies the company classifies as current.",
  """<pre style="font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.6;
background:var(--section-alt);border:1px solid var(--border);border-radius:3px;padding:1rem;overflow-x:auto">
MERIDIAN PRECISION DEFENSE SYSTEMS - ACCESS CONTROL POLICY
POL-001  v1.2   Last reviewed: January 2024   Approved: M. Ellison

4.1  Access to MPDS information systems shall be granted on the basis of
     least privilege and documented business need.

4.2  Accounts shall be provisioned by IT following an approved HR ticket
     and shall be disabled upon separation.

4.3  Privileged and administrative accounts shall be restricted to
     designated IT personnel and reviewed quarterly.

4.4  Remote access shall require multifactor authentication.

4.5  Third-party administrative access shall be governed by written
     agreement and subject to the same controls as employee access.</pre>""",
  "Adequate, not sufficient",
  """<p><strong>Adequate. Not sufficient.</strong> Offered against AC.L2-3.1.1, 3.1.2, 3.1.5 and IA.L2-3.5.3.</p>
  <p><strong>Adequate, and genuinely well drafted</strong> &mdash; it is current, approved by the CEO, and clauses
  4.4 and 4.5 address exactly the two things Meridian gets wrong. That is worth saying out loud.</p>
  <p><strong>Not sufficient, and the policy indicts the environment rather than defending it.</strong> Clause 4.4
  requires MFA for remote access; the SSL VPN has none. Clause 4.5 requires third-party administrative access to be
  governed by written agreement; ClearPath holds standing domain admin on a month-to-month arrangement with no
  cybersecurity terms. Clause 4.2 requires disablement on separation; six VPN accounts belong to separated
  employees. Clause 4.3 requires quarterly privileged-account review; no review record exists, and a shared service
  account holds Global Admin in the GCC High tenant with no individual owner.</p>
  <p><strong>What would change it:</strong> an account listing with privilege levels reconciled against a documented
  baseline; dated quarterly review records naming the reviewer; termination records showing account disablement
  timestamps; the executed ClearPath agreement with security terms; and MFA evidence at the network access layer.</p>
  <p><strong>The observation that marks a strong assessor:</strong> a policy this good makes the findings
  <em>worse</em>, not better. Meridian wrote down the right rule and did not follow it, which forecloses the
  &ldquo;we did not know&rdquo; reading and speaks directly to whether the control is operating.</p>"""),
 ("Artifact 2 &mdash; M365 GCC High Conditional Access export",
  "Supplied by Trevor Nakamura as a policy export from the GCC High tenant. Tenant identifier visible and matching. "
  "Exported three days before the request.",
  """<pre style="font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.6;
background:var(--section-alt);border:1px solid var(--border);border-radius:3px;padding:1rem;overflow-x:auto">
Microsoft 365 GCC High - Conditional Access policy export
Policy:        MPDS-Require-MFA-AllUsers
State:         On
Assignments
  Users:       All users (163)
  Excluded:    mpds-admin@meridianpds.onmicrosoft.com  [service account]
  Cloud apps:  All cloud apps
  Conditions:  Any location
Access controls
  Grant:       Require multifactor authentication
Modified:      7 months ago</pre>""",
  "Adequate, not sufficient",
  """<p><strong>The hardest artifact in the set, and it fails for two separate reasons.</strong> Offered against
  IA.L2-3.5.3.</p>
  <p><strong>Reason one &mdash; scope.</strong> This is a genuine policy export rather than a screenshot, it is
  current, and it covers all 163 accounts. And it covers the <em>Microsoft 365 layer only</em>. IA.L2-3.5.3 requires
  MFA for network access, and the FortiGate SSL VPN &mdash; the actual network access path, with roughly 22 users
  including the MSP &mdash; authenticates against Active Directory with username and password alone. Evidence for
  the cloud layer does not establish the objective for the network layer.</p>
  <p><strong>Reason two &mdash; the exclusion.</strong> Unlike a screenshot, an export shows exclusions, and this one
  excludes <code>mpds-admin@</code>: a shared service account holding Global Admin with no individual owner. The
  single most privileged identity in the tenant is exempted from the MFA policy. A team that reads the first four
  lines and stops will miss it, which is precisely why the export is the better artifact and precisely why you read
  all of it.</p>
  <p><strong>What would change it:</strong> MFA evidence at the VPN gateway; a sign-in test against the VPN, the
  domain controllers and the file server with a sample account; and either removal of the exclusion or a documented,
  assessed compensating control with an accountable owner for that account.</p>
  <p><strong>Hold the distinction:</strong> the artifact is excellent evidence and the requirement is NOT MET. An
  assessor who cannot praise good evidence and still find the requirement unmet will be argued out of findings.</p>"""),
 ("Artifact 3 &mdash; Email from the IT Administrator",
  "Supplied by Trevor Nakamura by email, in response to a request for audit log review records.",
  """<pre style="font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.6;
background:var(--section-alt);border:1px solid var(--border);border-radius:3px;padding:1rem;overflow-x:auto">
From:    Trevor Nakamura
To:      Assessment Team
Subject: RE: Evidence request - audit logging

Logging is on across the board - Windows event logs on the DCs and the
file server, and the PLM box writes its own logs. Retention is 30 days,
which is what the platform defaults to. I look at them when something
comes up and we have not had anything unusual. Snort would catch
anything serious anyway.

Happy to pull specific logs if you tell me what you need.

Trevor</pre>""",
  "Neither",
  """<p><strong>Neither.</strong> Offered against AU.L2-3.3.1 and 3.3.5.</p>
  <p>It is an assertion that arrived by email, which does not make it a record. An interview response is a lead to
  be corroborated, not a conclusion, and this is an interview response in written form.</p>
  <p><strong>Three moves worth naming to students explicitly.</strong> &ldquo;I look at them when something comes
  up&rdquo; is reactive review, which is not the review the requirement contemplates. &ldquo;We have not had anything
  unusual&rdquo; is an appeal to the absence of evidence &mdash; with no defined review process, no correlation and
  no SIEM, Meridian has no capability to have seen anything unusual. And &ldquo;Snort would catch anything
  serious&rdquo; substitutes a tool&rsquo;s existence for a process: nobody has said who reads its output, or when.</p>
  <p><strong>The detail a strong assessor pursues:</strong> 30 days is stated plainly and volunteered as a platform
  default rather than a decision. The requirement is retention <em>sufficient to support</em> monitoring, analysis,
  investigation and reporting &mdash; a period nobody chose cannot have been assessed against that standard. Ask
  what analysis established 30 days as sufficient. Nothing did.</p>
  <p><strong>What would change it:</strong> a documented log review procedure with a defined cadence; dated review
  records naming the reviewer and the sources reviewed; a retention determination tied to the requirement; and, for
  3.3.5, evidence that records from different sources are actually correlated.</p>
  <p><strong>Watch for:</strong> this is the artifact most likely to be accepted, because Nakamura is competent,
  cooperative and almost certainly telling the truth as he understands it. Competence and honesty are not evidence,
  and the assessments that go wrong go wrong with likeable people.</p>"""),
 ("Artifact 4 &mdash; Risk Assessment Report (POL-006)",
  "Supplied by Diana Kowalczyk. The document register records it as last performed June 2023 and flags it "
  "&ldquo;Overdue.&rdquo; Six risks are recorded.",
  """<pre style="font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.6;
background:var(--section-alt);border:1px solid var(--border);border-radius:3px;padding:1rem;overflow-x:auto">
MERIDIAN PRECISION DEFENSE SYSTEMS - RISK REGISTER (extract)
Performed: June 2023          Next review: not scheduled

ID       Risk                                  L    I    Level     Remediation            Owner
RISK-01  Unpatched ENG workstations exploited  High High Critical  Planned - no date      Nakamura
RISK-02  MSP privileged access abused          Med  High High      Not initiated          Kowalczyk
RISK-03  Stale VPN accounts used by former     Med  High High      Partial - HR notified  Nakamura
         employee or attacker
RISK-04  CUI exfiltrated via removable media   Med  Med  Medium    Policy only            Kowalczyk
RISK-05  Fire/flood in Dayton server room -    Low  High Medium    Local NAS only         Nakamura
         no offsite backup for SYS-003
RISK-06  Huntsville closet equipment accessed  Low  Med  Low-Med   Not addressed          Farris</pre>""",
  "Adequate, not sufficient",
  """<p><strong>Adequate. Not sufficient.</strong> Offered against RA.L2-3.11.1.</p>
  <p><strong>Adequate:</strong> unlike most artifacts in this case it is the right kind of document, it identifies
  real risks specific to this environment, and it assigns likelihood, impact and an owner. Meridian has genuinely
  done a risk assessment.</p>
  <p><strong>Not sufficient:</strong> the requirement is to assess risk <em>periodically</em>. This was performed
  once, 19 months ago, with no next review scheduled &mdash; so there is no periodicity to evidence. Two of the six
  risks record no remediation at all, one records &ldquo;planned&rdquo; with no date, and there is no evidence that
  any of them were tracked, escalated or closed in the intervening period.</p>
  <p><strong>The observation that separates Competent from Assessor-Ready:</strong> read the register against the
  assessment findings. RISK-01, RISK-02 and RISK-03 describe, precisely and in the company&rsquo;s own words, three
  of the failures you are about to write up as findings. Meridian identified them, rated them Critical and High,
  assigned owners, and then did nothing for 19 months. That is not an unknown risk. It is an accepted one that
  nobody was authorised to accept &mdash; and it goes directly to whether management is exercising the oversight the
  CA family requires.</p>
  <p><strong>What would change it:</strong> a defined assessment cadence with evidence of at least two cycles;
  remediation tracking showing movement on the open items; and evidence of management review and formal risk
  acceptance where remediation was deliberately deferred.</p>"""),
 ("Artifact 5 &mdash; The POA&amp;M",
  "Supplied by Diana Kowalczyk as an .xlsx attachment. Asked where the master copy lives, she states it is in her "
  "OneDrive.",
  """<pre style="font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.6;
background:var(--section-alt);border:1px solid var(--border);border-radius:3px;padding:1rem;overflow-x:auto">
MPDS_POAM_working.xlsx
Location:  Kowalczyk personal OneDrive (commercial tenant)
           NOT the M365 GCC High tenant

Item  Weakness                          Target    Status      Owner
1     VPN MFA                           TBD       Open        IT
2     Stale accounts                    TBD       In progress IT
3     Log review process                -         Open        IT
4     Workstation patching              Q3?       Open        IT
5     MSP contract / SCRM               -         Open        Contracts
6     Segmentation project              FY26      Open        IT

No version history. No AO signature. Last modified 18 months ago.</pre>""",
  "Neither",
  """<p><strong>Neither &mdash; and the artifact is itself a finding.</strong> Offered against CA.L2-3.12.2 and, as
  supporting evidence, CA.L2-3.12.4.</p>
  <p><strong>Not adequate:</strong> a plan of action must identify the weakness, the corrective action, the resources
  required, the milestones, and the completion dates. Four of six items carry no target date, none carries a named
  individual owner, none records resources, and no item has ever been closed. &ldquo;IT&rdquo; is not an owner. This
  does not match what the requirement intends.</p>
  <p><strong>Not sufficient</strong> for the obvious reason and a much worse one: <strong>it is stored outside the
  CUI boundary.</strong> The master copy lives in a personal OneDrive on a commercial tenant, not in the authorised
  GCC High environment. A document enumerating every unremediated security weakness in a defense contractor is
  precisely the kind of information an adversary would target, and it is being kept outside the accredited
  boundary.</p>
  <p><strong>Do not stop at the content.</strong> Where an artifact lives can be a more serious finding than what it
  says, and this is the clearest example in the case. It also contradicts the SSP&rsquo;s own boundary statement,
  which is a second finding.</p>
  <p><strong>What would change it:</strong> a POA&amp;M inside the GCC High boundary, under version control, with
  named individual owners, resource estimates, dated milestones, and evidence of AO review at a defined cadence.</p>
  <p><strong>Consistency check:</strong> you will need this document again on Day 5, when the eligibility rules in
  32 CFR &sect;170.21 turn on what a POA&amp;M may and may not carry. Note now that a POA&amp;M is a regulated
  instrument with a defined content standard, not a spreadsheet of intentions.</p>"""),
]

REQS15 = [
 ("AC.L2-3.1.1","Limit system access to authorized users, processes, and devices","Six VPN accounts belong to separated employees"),
 ("AC.L2-3.1.2","Limit system access to the types of transactions and functions authorized users may execute","Shared Global Admin service account in the GCC High tenant"),
 ("AC.L2-3.1.5","Employ the principle of least privilege","MSP holds standing domain admin; no privileged-account review record"),
 ("AC.L2-3.1.12","Monitor and control remote access sessions","22 VPN users including MSP technicians; no session monitoring"),
 ("IA.L2-3.5.3","Multifactor authentication for privileged accounts and network access","MFA at the M365 layer only; none on the SSL VPN"),
 ("AU.L2-3.3.1","Create and retain system audit logs sufficient to support monitoring and investigation","30-day retention taken as a platform default; no analysis behind it"),
 ("AU.L2-3.3.5","Correlate audit record review, analysis, and reporting","No SIEM; review is reactive only"),
 ("CM.L2-3.4.1","Establish and maintain baseline configurations and inventories","No asset inventory exists; ENG workstations in no configuration management tool"),
 ("CM.L2-3.4.2","Establish and enforce security configuration settings","About four of 14 workstations 90+ days behind on critical updates"),
 ("IR.L2-3.6.1","Establish an operational incident-handling capability","IRP dated 2022; contact list names a departed employee"),
 ("IR.L2-3.6.3","Test the organizational incident response capability","No tabletop or exercise since the plan was written"),
 ("MA.L2-3.7.5","MFA for nonlocal maintenance sessions; terminate them on completion","MSP remote admin with no MFA and no session control"),
 ("MP.L2-3.8.3","Sanitize or destroy media containing CUI before disposal or reuse","Three decommissioned drives in a cardboard box in the server room since 2022"),
 ("RA.L2-3.11.1","Periodically assess risk to operations, assets, and individuals","One assessment 19 months ago; no next review scheduled"),
 ("SC.L2-3.13.1","Monitor, control, and protect communications at external and key internal boundaries","CORP-LAN, ENG-LAN and MGMT-LAN route freely through the core switch"),
]

def evidence_triage():
    reqs = "".join(f'<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in REQS15)
    intro = f"""<div class="panel">
<h2>The two tests</h2><div class="rule"></div>
<div class="tw"><table>
<thead><tr><th></th><th>Adequacy</th><th>Sufficiency</th></tr></thead>
<tbody>
<tr><td><strong>The question</strong></td><td>Does this evidence exist, and does it match what the requirement intends?</td><td>Does it show the control is implemented, consistently followed, and operating?</td></tr>
<tr><td><strong>What to ask next</strong></td><td>&ldquo;What is this a document about?&rdquo;</td><td>&ldquo;How would I know this is still true, and true everywhere?&rdquo;</td></tr>
</tbody></table></div>
<p><strong>Adequate</strong> evidence shows the thing exists and matches what the requirement intends.
<strong>Sufficient</strong> evidence shows it is implemented, consistently followed, and operating. A policy
requiring MFA is adequate. A configuration export plus a sample of enrolled accounts is sufficient. Someone telling
you it is enforced is neither.</p>
<div class="verdict show"><h4>Every verdict needs a fourth field</h4>
<p>Most assessors reach similar verdicts on these five artifacts. What separates them is
<strong>what would change it</strong>. An assessor who can say &ldquo;this is adequate but not sufficient, and here
is precisely what would make it sufficient&rdquo; has given an organization something it can act on without ever
telling it what to do. This tool will not let you skip that field.</p></div>
</div>
<div class="panel"><h2>Part B reference &mdash; the fifteen requirements</h2><div class="rule"></div>
<p>The request list at the end of this tool covers these. The descriptors are pointers so you know which
requirement is meant &mdash; they are <em>not</em> the authoritative text and they are not the assessment
objectives. Work from the CMMC Assessment Guide for Level 2; decomposing the requirement into its objectives is the
skill being assessed.</p>
<div class="tw"><table><thead><tr><th style="width:130px">Requirement</th><th>In one line</th><th>Meridian gap it touches</th></tr></thead>
<tbody>{reqs}</tbody></table></div></div>"""
    items = ""
    for i, (name, prov, body, ok, model) in enumerate(ARTIFACTS, 1):
        ctx = (f'<p style="font-size:.82rem;color:var(--text-muted)"><em>{prov}</em></p>{body}')
        items += item(f"ev{i}", i, name, ctx, [
            dict(label="Which assessment objective is it offered against?", type="text", name="obj",
                 ph="Name a specific objective. If you cannot, the artifact is not evidence yet."),
            dict(label="Verdict", type="select", name="v",
                 options=["Adequate and sufficient","Adequate, not sufficient","Sufficient, not adequate","Neither"],
                 ok=ok),
            dict(label="Reasoning — three sentences maximum", type="area", name="r"),
            dict(label="What would change the verdict?", type="area", name="chg", cls="needchange",
                 ph="Be specific. This is the field that separates a Competent verdict from an Assessor-Ready one."),
        ], model)
    items += item("reqlist", 6, "Part B &mdash; the evidence request list",
      '<p>Build request lines for the fifteen requirements above. Each line names four things: the '
      '<strong>artifact</strong> (specific enough to be retrieved), the <strong>method</strong> (examine, interview, '
      'or test), the <strong>objective</strong> it serves, and the <strong>custodian</strong>.</p>'
      '<p style="font-size:.82rem;color:var(--text-muted)">A line that names a topic rather than an artifact is not '
      'a request. &ldquo;Access control documentation&rdquo; produces a pile of documents and a week of delay; '
      '&ldquo;the current Conditional Access policy export from the Microsoft 365 tenant, including '
      'exclusions&rdquo; does not.</p>',
      [dict(label="Your request list — one line per row: artifact | method | objective | custodian",
            type="area", name="list",
            ph="1. The current Conditional Access policy export from the M365 tenant, including exclusions | Examine | IA.L2-3.5.3[a] | T. Nakamura\n2. ...")],
      """<p><strong>What good looks like &mdash; a sample of strong lines:</strong></p>
<ul>
<li>FortiGate SSL VPN authentication configuration export showing the authentication method for the remote-access
portal &middot; Examine &middot; IA.L2-3.5.3 &middot; T. Nakamura &mdash; <em>and</em> a live sign-in test to the VPN,
a domain controller over RDP, and SYS-003 &middot; Test &middot; same objective &middot; T. Nakamura.</li>
<li>Active Directory account listing with group memberships, last-logon dates and enabled/disabled state, exported
during the assessment &middot; Examine &middot; AC.L2-3.1.1, 3.1.5 &middot; T. Nakamura.</li>
<li>Separation records for the six accounts identified as belonging to former employees, with the corresponding
disablement timestamps &middot; Examine &middot; AC.L2-3.1.1 &middot; R. Bauer and T. Nakamura &mdash; note the two
custodians; that split is itself informative about why the gap exists.</li>
<li>The executed ClearPath IT Solutions services agreement including any security addendum, plus the Customer
Responsibility Matrix &middot; Examine &middot; MA.L2-3.7.5 and the ESP obligation &middot; P. Mehta.</li>
<li>Log retention configuration for the domain controllers, SYS-003 and SYS-004, showing the configured period; and
any documented analysis establishing that period as sufficient &middot; Examine &middot; AU.L2-3.3.1 &middot;
T. Nakamura.</li>
<li>Patch status report for all 14 Dayton and 6 Huntsville engineering workstations as at the assessment date
&middot; Examine &middot; CM.L2-3.4.2 &middot; T. Nakamura.</li>
<li>Disposition records for the three decommissioned drives held in the Dayton server room, and the destruction
certificates for media disposed of since 2022 &middot; Examine &middot; MP.L2-3.8.3 &middot; G. Farris.</li>
<li>Any record of an incident response exercise since 2022, and the current IR contact roster reconciled against
active personnel &middot; Examine &middot; IR.L2-3.6.1, 3.6.3 &middot; D. Kowalczyk.</li>
</ul>
<p><strong>Three checks before you submit:</strong> every line names an artifact somebody could go and fetch, not a
subject somebody could write an essay about. Every verdict names the objective. And nothing anywhere in the document
tells Meridian what to do about any of it.</p>
<p><strong>The habit that matters most:</strong> ask for what would <em>disconfirm</em> the company&rsquo;s position,
not only what would confirm it. Meridian has an SSP, ten policies and a CISO &mdash; a documentation-led assessment
here will pass a company that is not compliant.</p>""")
    return tool_page("evidence-triage","Evidence Adequacy Triage","Tool &middot; Deliverable D5 &middot; Lesson 5",
      "Evidence Triage &mdash; Adequate, Sufficient, Both, or Neither",
      "Five artifacts exactly as Meridian supplied them. Name the objective, render the verdict, and say what "
      "would change it &mdash; then build a request list an OSC could satisfy without asking a question.",
      ["5 artifacts","15 requirements","Request list","Prints as D5"], intro, items,
      back=("Lesson 5 &mdash; Evidence: Adequacy &amp; Sufficiency","lesson05.html"))

def build_all():
    return [("scope-matrix.html", scope_matrix()),
            ("evidence-triage.html", evidence_triage())] + tools4.build_all()
