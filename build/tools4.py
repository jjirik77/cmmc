# -*- coding: utf-8 -*-
"""Tool pages: Domain Worksheet, SPRS Calculator, POA&M Builder, Transfer Test, One-Pager."""
from toolkit import tool_page, item, ENGINE_JS
from theme import head, nav, FOOT, THEME_JS

DET = ["MET","NOT MET","NOT APPLICABLE"]

# ---------------------------------------------------------------- DOMAIN WORKSHEET
DOMAIN_ITEMS = [
 ("AC.L2-3.1.1","Limit system access to authorized users, processes acting on behalf of authorized users, and devices",
  ["Authorized users are identified","Processes acting on behalf of authorized users are identified",
   "Devices authorized to connect are identified","System access is limited to authorized users",
   "System access is limited to processes acting on behalf of authorized users",
   "System access is limited to authorized devices"],
  "Six VPN accounts belong to employees who separated between three and fourteen months ago; HR notifies IT by "
  "email with no checklist and VPN deprovisioning is not on it. A shared service account holds Global Admin in the "
  "GCC High tenant with no individual owner. ClearPath technicians reach domain admin over the VPN. No asset "
  "inventory exists, so no register of authorized devices exists either.","NOT MET",
  "No objective survives. Authorized users are not identified in any maintained artifact; devices authorized to "
  "connect are not identified at all, because there is no inventory; and access is demonstrably not limited to "
  "authorized users, which the six live accounts prove. A finding here names all six objectives, not "
  "&ldquo;access control is weak.&rdquo;"),
 ("AC.L2-3.1.5","Employ the principle of least privilege, including for specific security functions and privileged accounts",
  ["Privileged accounts are identified","Access to privileged accounts is authorized per least privilege",
   "Security functions are identified","Access to security functions is authorized per least privilege"],
  "ClearPath holds standing domain administrator rights under a month-to-month agreement with no cybersecurity "
  "terms and no background-check verification. Policy POL-001 &sect;4.3 requires quarterly review of privileged "
  "accounts; no review record exists. The shared <code>mpds-admin@</code> account holds Global Admin with no "
  "individual owner.","NOT MET",
  "Privileged accounts are not identified in any maintained register; access to them is not authorized against a "
  "least-privilege standard; security functions are not documented; and a standing external domain admin defeats "
  "the principle outright. Note this is a <strong>3-point</strong> requirement, not 5 &mdash; a frequent scoring "
  "error. Note also that the policy requires exactly the review that is missing, which strengthens the finding "
  "rather than mitigating it."),
 ("IA.L2-3.5.3","Use multifactor authentication for local and network access to privileged accounts and for network access to non-privileged accounts",
  ["Privileged accounts are identified",
   "MFA is implemented for local access to privileged accounts",
   "MFA is implemented for network access to privileged accounts",
   "Non-privileged accounts are identified",
   "MFA is implemented for network access to non-privileged accounts"],
  "Conditional Access enforces MFA across the GCC High tenant for all 163 accounts, all cloud apps, any location "
  "&mdash; with the shared <code>mpds-admin@</code> Global Admin service account excluded. The FortiGate SSL VPN, "
  "which is the network access path for roughly 22 users including ClearPath, authenticates against Active "
  "Directory with username and password alone. AWS GovCloud root has MFA enabled.","NOT MET",
  "The tenant evidence is excellent and covers one layer. Network access to privileged accounts fails at the VPN; "
  "network access to non-privileged accounts fails at the VPN; and the two &ldquo;accounts are identified&rdquo; "
  "objectives fail because no privileged-account register is maintained. The Conditional Access exclusion is a "
  "separate and serious observation: the most privileged identity in the tenant is exempt from the policy that "
  "covers everyone else."),
 ("AU.L2-3.3.1","Create and retain system audit logs and records sufficient to enable monitoring, analysis, investigation, and reporting",
  ["Audit logs needed to enable monitoring, analysis, investigation, and reporting of unlawful or unauthorized system activity are specified",
   "The content of audit records needed to support monitoring, analysis, investigation, and reporting is defined",
   "Audit records are created (generated)",
   "Audit records, once created, contain the defined content",
   "Retention requirements for audit records are defined",
   "Audit records are retained as defined"],
  "SYS-003 and SYS-004 generate logs. Retention is 30 days, which Nakamura describes in interview as the platform "
  "default rather than a decision. No formal review process exists and no SIEM is deployed. Snort runs on MGMT-LAN; "
  "nobody is identified as reading its output.","NOT MET",
  "Audit records are created, so that objective may be satisfied. The logs needed have never been "
  "<em>specified</em>; the content of audit records has never been <em>defined</em>, so the objective requiring "
  "records to contain the defined content cannot be reached at all; and a retention period inherited as a default "
  "has not been <em>determined</em> against the standard the requirement sets, which is sufficiency to support "
  "investigation. One objective possibly MET does not carry the requirement."),
 ("CA.L2-3.12.4","Develop, document, and periodically update a system security plan that describes system boundaries, environments of operation, security requirement implementation, and relationships with other systems",
  ["A system security plan is developed",
   "The system boundary is described and documented",
   "The system environment of operation is described and documented",
   "Security requirements identified and approved by the designated authority as non-applicable are identified",
   "The method of security requirement implementation is described and documented",
   "The relationship with or connection to other systems is described and documented",
   "The frequency to update the system security plan is defined",
   "The system security plan is updated with the defined frequency"],
  "SSP POL-008 version 2.1, dated October 2023. Meridian&rsquo;s own document register marks it <strong>&ldquo;needs "
  "update.&rdquo;</strong> The company has a network diagram. The SSP does not describe the ClearPath relationship, "
  "the Acuitas or AeroComp data flows, or the manual upload path from SYS-003 into AWS GovCloud. No update frequency "
  "is stated anywhere in it.","NOT MET",
  "<strong>This is the requirement where having documents makes the assessment harder, not easier.</strong> A plan "
  "exists and a boundary is described, so two objectives may be satisfied &mdash; and Meridian will argue from "
  "there. But relationships with other systems are not described: three CUI-handling external parties and an "
  "inter-cloud data flow are absent. No update frequency is defined, so the last two objectives cannot be reached, "
  "and the company&rsquo;s own register concedes the plan is out of date.<br><br><strong>Consequence:</strong> "
  "CA.L2-3.12.4 is worth <em>one point</em> and is one of the six that may never be placed on a POA&amp;M. A NOT MET "
  "here blocks any CMMC status regardless of score."),
 ("IR.L2-3.6.1","Establish an operational incident-handling capability that includes preparation, detection, analysis, containment, recovery, and user response activities",
  ["An operational incident-handling capability is established","Preparation is addressed","Detection is addressed",
   "Analysis is addressed","Containment is addressed","Recovery is addressed","User response activities are addressed"],
  "Incident Response Plan POL-002 v1.0, dated March 2022, marked &ldquo;stale &mdash; 3+ yrs&rdquo; in the "
  "company&rsquo;s own register. Never exercised. The contact roster names a project manager who left in early 2024. "
  "The plan contains no DFARS 72-hour reporting language. Two security events in Oct 2023 and Feb 2024 were handled "
  "by chat and email; neither was assessed against the clause; zero reports have been filed in 24 months.","NOT MET",
  "A documented plan is not an operational capability. The plan has never been tested, names a responder who does "
  "not work here, and omits the reporting obligation entirely &mdash; so user response activities and analysis are "
  "not addressed in any operative sense. The two unassessed events are the proof: when the capability was needed "
  "twice, it did not function."),
 ("MA.L2-3.7.5","Require multifactor authentication to establish nonlocal maintenance sessions via external network connections, and terminate such connections when nonlocal maintenance is complete",
  ["MFA is required to establish nonlocal maintenance sessions via external network connections",
   "Nonlocal maintenance sessions are terminated when maintenance is complete"],
  "ClearPath performs remote administration over the FortiGate SSL VPN, which has no MFA. The engagement is "
  "month-to-month with no security terms. There is no session recording and no access logging configured for the "
  "MSP&rsquo;s access.","NOT MET",
  "Both objectives fail, and cleanly. MFA is not required to establish the session &mdash; that is the same VPN gap "
  "as IA.L2-3.5.3, appearing here in its maintenance aspect. And with no session logging there is no evidence "
  "whatever that sessions terminate on completion; standing access is by design the opposite of a session that "
  "ends. Note this requirement is where the MSP relationship becomes a technical finding rather than a contractual "
  "one."),
 ("PE.L2-3.10.1","Limit physical access to organizational systems, equipment, and the respective operating environments to authorized individuals",
  ["Authorized individuals allowed physical access are identified",
   "Physical access to systems is limited to authorized individuals",
   "Physical access to equipment is limited to authorized individuals",
   "Physical access to operating environments is limited to authorized individuals"],
  "Dayton: HID card readers, Server Room 104 on card plus PIN restricted to three named people, MSP escorted under "
  "an <em>informal, undocumented</em> escort policy. The engineering area has no separate access control &mdash; any "
  "corporate badge holder can reach the CAD/CAM workstations. Huntsville: commercial office lease, Meridian does not "
  "control the building access system, and the network switch and UPS sit in an unlocked utility closet accessible "
  "to building maintenance.","NOT MET",
  "Dayton is largely creditable and Huntsville is not, and the requirement applies across the assessment scope. "
  "Authorized individuals for the Huntsville equipment are not identified and cannot be &mdash; Meridian does not "
  "control who holds building access. Physical access to equipment carrying CUI between the sites is not limited to "
  "authorized individuals by any mechanism the company operates.<br><br>Watch for teams that assess only the "
  "headquarters. A single site meeting a requirement does not carry an environment that spans two."),
]

MAPPINGS = [
 ("GAP-04 &mdash; &ldquo;No asset inventory; unpatched engineering workstations&rdquo;, which the company maps to "
  "3.4.2, described in its own documentation as &ldquo;establish and maintain a component inventory&rdquo;",
  "CM.L2-3.4.1 for the inventory; CM.L2-3.4.2 for the patching",
  "The company&rsquo;s <em>description</em> of 3.4.2 is wrong. In Rev 2, <strong>3.4.1</strong> is the requirement "
  "that covers baseline configurations <em>and inventories</em>; <strong>3.4.2</strong> is establishing and "
  "enforcing security configuration settings. The gap as written is really two gaps against two requirements.<br><br>"
  "This dispute does not move the score &mdash; both are 5-point requirements &mdash; which is exactly why it is "
  "worth catching. It changes <em>what evidence closes it</em>: an inventory closes 3.4.1 and does nothing for "
  "3.4.2, and a patch report closes neither on its own."),
 ("GAP-05 &mdash; &ldquo;No formal POA&amp;M; informal spreadsheet, not AO-approved&rdquo;, which the company maps "
  "to 3.12.4","CA.L2-3.12.2",
  "3.12.4 is the <strong>System Security Plan</strong> requirement. A deficient plan of action is "
  "<strong>CA.L2-3.12.2</strong>, which concerns developing and implementing plans of action to correct "
  "deficiencies.<br><br><strong>The consequence is not academic.</strong> CA.L2-3.12.4 is one of the six "
  "requirements that may never be placed on a POA&amp;M; 3.12.2 is not. Which requirement this gap belongs to helps "
  "decide whether Meridian is blocked from any CMMC status outright.<br><br>Note the second-order point: Meridian&rsquo;s "
  "SSP is version 2.1 from October 2023 and its own register marks it &ldquo;needs update.&rdquo; So 3.12.4 is "
  "arguably NOT MET <em>on its own merits</em> &mdash; the requirement includes periodic update &mdash; and the "
  "block may hold either way. An assessor who reaches that conclusion by two independent routes has done the work."),
 ("GAP-08 &mdash; &ldquo;No segmentation between CORP-LAN and ENG-LAN&rdquo;, which the company maps to 3.13.3",
  "SC.L2-3.13.1",
  "3.13.3 is <em>separate user functionality from system management functionality</em> &mdash; which is arguably "
  "engaged by the policy-only MGMT-LAN separation, but is not what the finding describes. What is described is a "
  "failure to monitor, control and protect communications at a key internal boundary: <strong>SC.L2-3.13.1</strong>, "
  "worth 5 points rather than 1. The correction raises deductions by 4."),
]

def domain_worksheet():
    intro = """<div class="panel">
<h2>Three determinations</h2><div class="rule"></div>
<div class="tw"><table>
<thead><tr><th>Determination</th><th>What it means</th><th>What it requires of you</th></tr></thead>
<tbody>
<tr><td><strong>MET</strong></td><td>All applicable objectives satisfied by final-form evidence. An enduring exception with documented mitigation, or a temporary deficiency covered by an operational plan of action, can still be MET.</td><td>Cite evidence for each objective.</td></tr>
<tr><td><strong>NOT MET</strong></td><td>One or more objectives is not satisfied.</td><td>Name the objective and what is missing.</td></tr>
<tr><td><strong>NOT APPLICABLE</strong></td><td>The requirement does not apply to the scope.</td><td>Justify it. N/A scores as MET, so it will be challenged.</td></tr>
</tbody></table></div>
<div class="verdict show"><h4>Work at the objective level</h4>
<p>A worksheet that determines at the requirement level has not done the work. Every objective is listed for you
below. Read each one, decide whether the evidence reaches it, and let the requirement determination follow.</p>
<p><strong>There is no partial credit.</strong> One objective unmet makes the whole requirement NOT MET.</p></div>
<div class="tip"><div class="tip-label">On the objective text below</div>
<p>The assessment objectives listed for each requirement are the decompositions in
<strong>NIST SP 800-171A</strong>, reproduced here so you can work without switching documents.
<strong>They are a study aid, not the authority.</strong> In a real assessment you work from the CMMC Assessment
Guide for Level 2 and NIST SP 800-171A directly, and you verify the objective text and count against the current
published version before you rely on it.</p></div>
<p style="font-size:.82rem;color:var(--text-muted)"><strong>Citation standard:</strong> &ldquo;Interview with T. Nakamura,
14 March, on privileged account inventory; access control matrix v1.2 &sect;3&rdquo; is a citation.
&ldquo;Discussion&rdquo; is not. And no remediation anywhere &mdash; state what is missing, not what to do about
it.</p></div>"""
    items = ""
    for i, (rid, text, objs, ev, ok, model) in enumerate(DOMAIN_ITEMS, 1):
        objhtml = "".join(f"<li>{o}</li>" for o in objs)
        ctx = (f'<p style="font-family:Arial,sans-serif;font-size:.88rem;color:var(--text-secondary);'
               f'line-height:1.8"><strong>{rid}</strong> &mdash; {text}</p>'
               f'<h3>Assessment objectives</h3><ol>{objhtml}</ol>'
               f'<div class="in-practice"><div class="ip-label">Evidence available</div><p style="margin:0">{ev}</p></div>')
        items += item(f"d{i}", i, rid, ctx, [
            dict(label="Requirement determination", type="select", name="det", options=DET, ok=ok),
            dict(label="Which objectives fail, and what is missing?", type="area", name="obj",
                 ph="Name each failing objective. A NOT MET with no named objective cannot be defended or remediated."),
            dict(label="Evidence relied on — named", type="area", name="ev",
                 ph="Artifact, section, date; or interview, person, date, subject."),
        ], f"<p><strong>{ok}.</strong> {model}</p>")
    n = len(DOMAIN_ITEMS)
    for j, (gap, ok, model) in enumerate(MAPPINGS, 1):
        items += item(f"m{j}", n+j, f"Mapping dispute &mdash; {gap.split(',')[0]}",
          f'<p>{gap}</p><p>Do you accept the company&rsquo;s mapping? If not, give yours.</p>', [
            dict(label="The requirement you would map it to", type="select", name="map",
                 options=["Accept the company's mapping",
                          "CM.L2-3.4.1 for the inventory; CM.L2-3.4.2 for the patching",
                          "CM.L2-3.4.1 only",
                          "CA.L2-3.12.2",
                          "CA.L2-3.12.4",
                          "SC.L2-3.13.1",
                          "SC.L2-3.13.5",
                          "No Rev 2 requirement — this is a Rev 3 practice"], ok=ok),
            dict(label="Why — and what it does to the score", type="area", name="why"),
          ], f"<p><strong>{ok}.</strong> {model}</p>")
    items += item("consist", n+3, "Consistency check",
      '<p>Your determinations must be consistent with the scope you drew in Lesson 4 and the evidence you triaged '
      'in Lesson 5. Where a determination here would change a call you made earlier, say so.</p>',
      [dict(label="Any determination here that changes an earlier call?", type="area", name="c",
            ph="Name the earlier call, the change, and why.")],
      """<p>Two places where the Day 5 evidence package should move an earlier call:</p>
<ul>
<li><strong>The SSP now exists</strong>, so the Lesson 4 statement that both conditional asset categories are closed
to Meridian needs re-testing &mdash; and it survives, because the SSP's boundary section names no systems and
there is still no network diagram and no written policy. Say that explicitly rather than leaving the earlier
reasoning to stand unexamined.</li>
<li><strong>MFA was added to the SSL VPN four months ago.</strong> That does not change the IA.L2-3.5.3
determination, because domain controller RDP is still single-factor &mdash; but it does change the
<em>scoring</em> analysis you will do next, and a worksheet that ignores it will produce the wrong deduction.</li>
</ul>
<p>Noting where a determination here would change a call made earlier is an Assessor-Ready behaviour. It is also how
you avoid a findings report that contradicts its own scope statement.</p>""")
    return tool_page("domain-worksheet","Domain Determination Worksheet","Tool &middot; Deliverable D6 &middot; Lesson 6",
      "Domain Determination Worksheet",
      "Eight requirements across six families, decomposed into their assessment objectives with the Meridian "
      "evidence attached. Determine each objective, cite the evidence, and argue the two disputed mappings.",
      ["8 requirements","Objective level","2 mapping disputes","Prints as D6"], intro, items,
      back=("Lesson 6 &mdash; Assessing the Fourteen Domains","lesson06.html"))

# ---------------------------------------------------------------- SPRS CALCULATOR
GAPS = [
 ("GAP-01","MFA enforced at the M365 GCC High layer only; the FortiGate SSL VPN authenticates against AD with "
  "username and password alone","3.5.3",5,
  "<strong>The trap.</strong> Partial credit at 3 requires MFA for remote <em>and</em> privileged users. The VPN is "
  "the remote access path and has none; the MSP reaches domain admin across it. Neither condition is met, so the "
  "exception does not apply. A substantial minority deduct 3 here."),
 ("GAP-02a","Six VPN accounts belong to separated employees; no automated deprovisioning between HR and AD","3.1.1",5,
  "Basic requirement, 5 points."),
 ("GAP-02b","Shared Global Admin service account in the GCC High tenant with no individual owner","3.1.2",5,
  "Basic requirement, 5 points."),
 ("GAP-03a","Logs generated on SYS-003 and SYS-004 but no formal review process; 30-day retention taken as a "
  "platform default","3.3.1",5,"Basic requirement, 5 points."),
 ("GAP-03b","No correlation across sources; no SIEM deployed","3.3.2",3,
  "3 points, not 5. Assuming every AU requirement is worth 5 over-deducts here."),
 ("GAP-04","No asset inventory exists; 14 engineering workstations in no configuration management tool, about four "
  "90+ days behind on critical updates","3.4.2",5,
  "5 points <em>as the company maps it</em>. See the mapping dispute &mdash; the company labels 3.4.2 as "
  "&ldquo;component inventory,&rdquo; which is not what Rev 2 says."),
 ("GAP-05","No formal POA&amp;M; informal spreadsheet in a personal OneDrive outside the CUI boundary, not "
  "AO-reviewed in 18+ months","3.12.4",1,
  "1 point <em>as the company maps it</em>. See the mapping dispute &mdash; a POA&amp;M deficiency is not the SSP "
  "requirement, and which one you choose decides whether the company is blocked outright."),
 ("GAP-06","No supply chain risk management programme; MSP and three CUI-handling suppliers unassessed, with no "
  "flow-down","3.17.1 / 3.17.2",0,
  "<strong>Zero &mdash; and this is the most instructive line on the sheet.</strong> Practices 3.17.1 and 3.17.2 "
  "belong to the SR family in NIST SP 800-171 <em>Rev 3</em>. CMMC Level 2 is anchored to <strong>Rev 2</strong>, "
  "which has fourteen families and no SR family at all. There is nothing here to deduct under this instrument. That "
  "does not make the gap harmless: it is a DFARS 252.204-7012(m) flow-down violation and an ESP treatment failure "
  "under 32 CFR &sect;170.19, and its access-control consequences are already scored at 3.1.1, 3.5.3 and 3.7.5. "
  "Score it as zero and write it up as a contractual finding."),
 ("GAP-07a","IRP dated 2022, never exercised; contact roster names an employee who left in early 2024","3.6.1",5,
  "Basic requirement, 5 points."),
 ("GAP-07b","Two security events handled informally; neither assessed against the reporting threshold; zero reports "
  "filed in 24 months","3.6.2",5,"Basic requirement, 5 points."),
 ("GAP-08","CORP-LAN, ENG-LAN and MGMT-LAN route freely through the core switch; a CORP-LAN compromise reaches the "
  "CUI file stores directly","3.13.3",1,
  "1 point <em>as the company maps it</em>. See the mapping dispute &mdash; 3.13.1 would be 5."),
 ("GAP-09","Security awareness training at 89% completion overall and 71% at Huntsville; no role-based track for "
  "privileged users or MSP technicians","3.2.2",5,"Basic requirement, 5 points."),
 ("GAP-10","MSP holds standing remote administrative access with no MFA, no session recording and no access "
  "logging","3.7.5",5,"Derived requirement, 5 points."),
 ("GAP-11","Huntsville network equipment in an unlocked utility closet accessible to building maintenance; Meridian "
  "does not control the building access system","3.10.3",1,
  "1 point &mdash; <strong>and POA&amp;M-ineligible under &sect;170.21.</strong>"),
]

SPRS_JS = """<script>
function recalc(){var t=0,done=0;
 document.querySelectorAll('.ded').forEach(function(s){
  if(s.value!==''){done++;t+=parseInt(s.value,10);}});
 var score=110-t, ratio=(score/110);
 document.getElementById('sp-ded').textContent=t;
 document.getElementById('sp-score').textContent=score;
 document.getElementById('sp-ratio').textContent=ratio.toFixed(2);
 var el=document.getElementById('sp-elig');
 if(done<%d){el.textContent='—';el.className='pill';}
 else if(ratio>=0.8){el.textContent='Above 0.8 threshold';el.className='pill ok';}
 else {el.textContent='Below 0.8 — no POA&M available';el.className='pill no';}
 var bar=document.getElementById('sp-bar');
 var pct=Math.max(0,Math.min(100,(score/110)*100));
 bar.style.width=pct+'%%';
 bar.style.background = ratio>=0.8 ? 'var(--ok)' : 'var(--gold)';
 bar.textContent = score;
 document.getElementById('sp-prog').textContent=done+' of %d scored';}
window.addEventListener('DOMContentLoaded',function(){
 document.querySelectorAll('.ded').forEach(function(s){s.addEventListener('change',recalc);});
 setTimeout(recalc,80);});
</script>"""

def sprs_calculator():
    rows = ""
    for gid, desc, req, val, note in GAPS:
        opts = "".join(f'<option value="{v}">{v}</option>' for v in [0,1,3,5])
        rows += (f'<tr><td><strong>{gid}</strong></td><td>{desc}</td><td><code>{req}</code></td>'
                 f'<td style="width:110px"><select class="ded" data-f="ded-{gid}" data-ok="{val}">'
                 f'<option value="">&mdash;</option>{opts}</select></td></tr>')
    keyrows = "".join(
        f'<tr><td><strong>{g}</strong></td><td><code>{r}</code></td><td><strong>{v}</strong></td><td>{n}</td></tr>'
        for g, d, r, v, n in GAPS)
    intro = f"""<div class="panel">
<h2>The weighting</h2><div class="rule"></div>
<div class="tw"><table><thead><tr><th>Value</th><th>What it covers</th></tr></thead><tbody>
<tr><td><strong>5</strong></td><td>Absence renders other controls ineffective or permits significant exploitation or exfiltration</td></tr>
<tr><td><strong>3</strong></td><td>A specific and confined security effect</td></tr>
<tr><td><strong>1</strong></td><td>Remaining derived requirements, limited or indirect effect</td></tr>
</tbody></table></div>
<div class="verdict show"><h4>Two partial-credit exceptions, and only two</h4>
<p><strong>3.5.3 &mdash; MFA.</strong> Deduct 3 where MFA is implemented for remote <em>and</em> privileged users but
not the general user. Deduct 5 where MFA is not implemented for any users.</p>
<p><strong>3.13.11 &mdash; FIPS-validated encryption.</strong> Deduct 3 where encryption is employed but not FIPS
validated. Deduct 5 where encryption is not employed.</p>
<p>Every other requirement is all or nothing. Awarding partial credit elsewhere because an organization has
&ldquo;mostly&rdquo; done something is the most common scoring error there is.</p></div>
<p style="font-size:.82rem;color:var(--text-muted)">Maximum 110. Floor <strong>&minus;203</strong> &mdash; the
weighted deductions total far more than 110, so a negative score is not a computational error and contractors do
post them. Look each value up in the methodology; do not work from memory.</p>
</div>
<div class="panel"><h2>Meridian gap list, as the company maps it</h2><div class="rule"></div>
<p>Assign a deduction to each. The running total updates as you go. <strong>Three of these mappings are worth
arguing with, and one requirement does not exist in Rev 2 at all</strong> &mdash; score them as the company maps
them first, then take up the disputes below.</p>
<div class="tw"><table><thead><tr><th style="width:70px">Gap</th><th>Description</th><th style="width:130px">Mapped to</th><th>Deduct</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<div style="margin-top:1.4rem;padding-top:1.2rem;border-top:2px solid var(--gold)">
  <div style="display:flex;flex-wrap:wrap;gap:1.6rem;align-items:flex-end;margin-bottom:1rem">
    <div><div style="font-family:Arial,sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted)">Deductions</div>
      <div style="font-family:'Arial Narrow',Arial,sans-serif;font-size:2rem;font-weight:900;color:var(--gold)" id="sp-ded">0</div></div>
    <div><div style="font-family:Arial,sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted)">Score</div>
      <div style="font-family:'Arial Narrow',Arial,sans-serif;font-size:2rem;font-weight:900;color:var(--gold)" id="sp-score">110</div></div>
    <div><div style="font-family:Arial,sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted)">Score &divide; 110</div>
      <div style="font-family:'Arial Narrow',Arial,sans-serif;font-size:2rem;font-weight:900;color:var(--gold)" id="sp-ratio">1.00</div></div>
    <div><div style="font-family:Arial,sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted)">POA&amp;M eligibility</div>
      <div style="margin-top:.35rem"><span class="pill" id="sp-elig">&mdash;</span></div></div>
    <div style="margin-left:auto;font-family:Arial,sans-serif;font-size:.74rem;color:var(--text-muted)" id="sp-prog"></div>
  </div>
  <div class="bar-track" style="height:28px"><div class="bar-fill" id="sp-bar" style="width:100%">110</div></div>
</div>
</div>"""
    items = item("k1", 1, "Check your arithmetic",
      '<p>Reveal the scoring key once you have assigned every value.</p>', [],
      f"""<div class="tw"><table><thead><tr><th>Gap</th><th>Requirement</th><th>Deduct</th><th>Note</th></tr></thead>
<tbody>{keyrows}</tbody></table></div>
<p style="margin-top:1rem"><strong>Starting score 110. Total deductions 51. Computed score 59.
59 &divide; 110 = 0.536</strong> &mdash; well short of the 0.8 threshold. Meridian cannot achieve even Conditional
Level 2 status on this gap list.</p>
<div class="tip"><div class="tip-label">On the point values</div>
<p>Every value above comes from the NIST SP 800-171 DoD Assessment Methodology, Section 5 and Annex A. Look them up
yourself rather than working from this table or from memory &mdash; the discipline is the skill, and the methodology
is the authority.</p></div>""", ok_label="Show the scoring key")

    items += item("k2", 2, "Defend three deductions",
      '<p>At least one must be a deduction where you believe the company has mapped the gap to the wrong '
      'requirement. State the mapping you would use and why.</p>',
      [dict(label="Deduction 1", type="area", name="d1"),
       dict(label="Deduction 2", type="area", name="d2"),
       dict(label="Deduction 3 — the mapping dispute", type="area", name="d3",
            ph="Name the gap, the company's mapping, your mapping, and the effect on the score.")],
      """<p><strong>The two mappings worth disputing, and what each does to the total:</strong></p>
<div class="tw"><table><thead><tr><th>Correction</th><th>Effect on the score</th></tr></thead><tbody>
<tr><td>GAP-04 split into 3.4.1 (inventory) and 3.4.2 (configuration settings)</td><td>Deductions rise to 56; score falls to <strong>54</strong></td></tr>
<tr><td>GAP-08 to 3.13.1 (5 points instead of 1)</td><td>Deductions rise to 55; score falls to <strong>55</strong></td></tr>
<tr><td>Both corrections together</td><td>Deductions 60; score <strong>50</strong></td></tr>
<tr><td>GAP-05 to 3.12.2 instead of 3.12.4</td><td>Changes the eligibility analysis rather than the arithmetic &mdash; see below</td></tr>
</tbody></table></div>
<p>Any figure in the range <strong>50 to 59</strong>, with the reasoning shown, is a correct answer. A bare number
with no working is not.</p>
<div class="warnbox"><div class="warn-label">The most consequential correction barely moves the score</div>
<p>Re-mapping the POA&amp;M deficiency from 3.12.4 to 3.12.2 changes almost nothing arithmetically. It changes
whether one of the six never-defer requirements is failing &mdash; which decides whether any CMMC status can issue
at all, at any score.</p>
<p>Scoring weight measures exploitability. POA&amp;M eligibility measures something else entirely. A student who
notices that the most important correction on the sheet is nearly invisible in the total has understood the
difference between the two instruments.</p></div>
<p><strong>Also worth defending:</strong> G-01 at 5 rather than 3 (the conjunction, not a spectrum); G-03b at 3
rather than 5 (not all AU requirements are 5); G-06b at 1 rather than 5 (not in either enumerated list); and G-13 at
0 (not a NIST requirement at all).</p>""")

    items += item("k3", 3, "What your score does and does not represent",
      '<p>Three or four sentences. Be precise about what a gap list is, and about the difference between this figure '
      'and a CMMC certification determination.</p>',
      [dict(label="Your statement", type="area", name="s")],
      """<p><strong>Three things a strong answer says:</strong></p>
<ul>
<li><strong>59 is an optimistic ceiling, not a floor.</strong> Eight seeded findings expanded across fourteen lines
is a gap analysis of selected areas, not an assessment of 110 requirements. A real assessment examines all of them
and would find more NOT MET &mdash; media disposal, physical access at Dayton, and the uncontrolled data flow into
AWS GovCloud are three this list never reaches. The true score is <em>at most</em> 59.</li>
<li><strong>The score is not the only gate.</strong> At least one and arguably two of the six requirements that may
never be placed on a POA&amp;M are failing &mdash; PE.L2-3.10.3, and CA.L2-3.12.4 if the SSP&rsquo;s own
&ldquo;needs update&rdquo; status is taken at face value. Even above 88, those must be MET outright before any status
could issue.</li>
<li><strong>This is a different instrument from a certification determination.</strong> The DoD Assessment
Methodology is a weighted strategic risk score. A CMMC determination is binary at the objective level with no
partial credit. Conflating them is the error the session exists to prevent.</li>
</ul>""")

    items += item("inc", 4, "INC-003 &mdash; the incident decision",
      """<div class="in-practice"><div class="ip-label">Wednesday, 09:40</div>
<p>Trevor Nakamura, reconciling VPN accounts against the HR separation list in preparation for the assessment,
finds that one of the six stale accounts &mdash; <code>jhollis</code>, belonging to a design engineer who left in
November &mdash; shows <strong>successful VPN authentications on four dates over the past six weeks</strong>, the
most recent eleven days ago. Each session lasted between twenty and ninety minutes.</p>
<p><strong>What is known:</strong> the account was never disabled. It held membership in the engineering security
group, which grants read and write access to the CUI tree on SYS-003 and to the Arena PLM. The VPN has no MFA. The
account's password was last set fourteen months ago and has not changed.</p>
<p><strong>What is not known:</strong> who authenticated. Whether anything was accessed, opened, or copied. Whether
the sessions originated from the former employee, from someone using credentials he left behind, or from an
unrelated party. The FortiGate retains authentication events; SYS-003 and SYS-004 retain 30 days of logs and are
not reviewed, so file-level access records for three of the four sessions have already rolled off.</p>
<p><strong>Nakamura's position:</strong> &ldquo;It is almost certainly Jared. He was finishing a handover and he is
a good guy. Nothing has been taken &mdash; we would see it.&rdquo;</p></div>""",
      [dict(label="Does this trigger the 72-hour reporting obligation?", type="select", name="t",
            options=["Yes — report","No — does not meet the threshold",
                     "Not yet — report only if compromise is confirmed"], ok="Yes — report"),
       dict(label="Clause paragraph, clock start, and who is entitled to decide", type="area", name="cl"),
       dict(label="The strongest argument against your decision — and your answer to it", type="area", name="ca")],
      """<div class="tw"><table><tbody>
<tr><td style="width:190px"><strong>Does it trigger?</strong></td><td><strong>Yes.</strong> A cyber incident
includes actions resulting in an actual or <em>potentially</em> adverse effect on an information system or the
information residing in it. Unauthorised authentication to a network holding CUI, by an account that should not
exist, with write access to the CUI store, is not a potential compromise &mdash; it is an actual unauthorised
access. The only open question is what was done with it.</td></tr>
<tr><td><strong>Which paragraph</strong></td><td>252.204-7012(c)(1) for the rapid report; the definition of cyber
incident at (a) supplies the threshold. Media preservation under (e) attaches once reported &mdash; which matters
urgently here, because logs are actively rolling off.</td></tr>
<tr><td><strong>Clock start</strong></td><td>72 hours from <em>discovery</em> &mdash; Wednesday 09:40, when
Nakamura identified the authentications. Not from the first session six weeks ago, and not from the separation date.
Document the six-week gap: a contracting officer will ask how an account authenticated four times without anyone
noticing, and the answer is evidence about the monitoring capability rather than about the clock.</td></tr>
<tr><td><strong>Who decides</strong></td><td>Not Nakamura. Meridian has an IRP naming an Incident Commander, and
that plan is three years stale and lists a departed employee &mdash; so in practice the CISO and the CEO, who is
also the Authorizing Official, must be involved. That the decision has nowhere to go is itself a finding under
IR.L2-3.6.1.</td></tr>
<tr><td><strong>What preservation requires now</strong></td><td>Images of affected systems and relevant monitoring
data for at least 90 days from the report. With 30-day retention and no review, <strong>the preservation obligation
is already partly impossible to satisfy</strong> for the earlier sessions. Preserving what remains is urgent and is
the first thing an assessor would ask whether anyone did.</td></tr>
</tbody></table></div>
<p style="margin-top:1rem"><strong>The counter-argument:</strong> it is almost certainly the former employee
finishing a handover; no evidence of exfiltration; reporting an incident involving a trusted ex-colleague is
disproportionate.</p>
<p><strong>The answer:</strong> the threshold is &ldquo;potentially adverse,&rdquo; not &ldquo;malicious,&rdquo; and
reporting is not an accusation. An authorised handover would have been performed on an authorised account.
&ldquo;Almost certainly Jared&rdquo; is an inference about identity that the environment cannot support: with no
MFA, the account proves possession of a credential and nothing whatever about who held it.</p>
<p>And Nakamura&rsquo;s second claim &mdash; &ldquo;nothing has been taken, we would see it&rdquo; &mdash; is an
appeal to the absence of evidence. Ask whether Meridian has the capability to have observed what he says has not
happened. It does not: no file-access review, no SIEM, no correlation, and 30-day retention that has already
consumed most of the record.</p>
<p><em>Could this organization know what it claims to know?</em> That is the question you will ask for the rest of
your career.</p>""")
    return tool_page("sprs-calculator","SPRS Score Calculator","Tool &middot; Deliverable D7 &middot; Lesson 7",
      "SPRS Score Calculator and the Incident Clock",
      "Fourteen gap lines, a live running total, and the POA&amp;M eligibility threshold moving against you &mdash; then "
      "an account that should not exist authenticating four times, and a decision about whether a 72-hour clock\n      has started.",
      ["110 to &minus;203","2 partial-credit exceptions","0.8 threshold","Prints as D7"], intro, items,
      back=("Lesson 7 &mdash; Scoring, SPRS &amp; the Incident Clock","lesson07.html"),
      extra_js=SPRS_JS % (len(GAPS), len(GAPS)))

def build_all():
    import tools5
    return [("domain-worksheet.html", domain_worksheet()),
            ("sprs-calculator.html", sprs_calculator())] + tools5.build_all()
