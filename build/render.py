# -*- coding: utf-8 -*-
"""Renderers: lesson pages, index, manuscript dump."""
import html as _h
from theme import head, nav, FOOT, THEME_JS

def _chips(ch):
    return "".join(f'<span class="meta-chip">{c}</span>' for c in ch)

def _objectives(objs):
    li = "".join(
        f'<li><span class="obj-tag">{b}</span><span>{t}</span></li>' for b, t in objs)
    return f'<ul class="obj-list">{li}</ul>'

def _vocab(v):
    cards = ""
    for term, dfn in v:
        cards += (f'<button class="flip-card" onclick="this.classList.toggle(\'flipped\')" '
                  f'aria-label="Definition of {_h.escape(term)}">'
                  f'<div class="flip-inner">'
                  f'<div class="flip-face flip-front"><div class="vocab-term">{term}</div>'
                  f'<div class="flip-hint">Click to reveal</div></div>'
                  f'<div class="flip-face flip-back"><div class="vocab-def">{dfn}</div></div>'
                  f'</div></button>')
    return f'<div class="vocab-grid">{cards}</div>'

def _case(c):
    acts = ""
    for label, href, ghost in c.get("actions", []):
        cls = "case-btn ghost" if ghost else "case-btn"
        acts += f'<a class="{cls}" href="{href}">{label}</a>'
    acts = f'<div class="case-actions">{acts}</div>' if acts else ""
    return (f'<div class="case"><div class="case-tag">{c["tag"]}</div>'
            f'<h3>{c["title"]}</h3>{c["html"]}{acts}</div>')

def _kc(kc, lid):
    out = ['<div class="kc">']
    for i, q in enumerate(kc, 1):
        out.append(f'<div class="q"><div class="qn">Question {i} of {len(kc)}</div>'
                   f'<div class="q-stem">{q["stem"]}</div><div class="options">')
        for j, (txt, ok, rat) in enumerate(q["opts"]):
            L = "ABCDEFGH"[j]
            out.append(f'<button class="opt" data-q="{i}" data-ok="{1 if ok else 0}" '
                       f'data-rat="{_h.escape(rat, quote=True)}" onclick="pick(this)">'
                       f'<span class="opt-letter">{L}</span><span>{txt}</span></button>')
        out.append('</div><div class="rationale"></div></div>')
    out.append(f'<div class="kc-score" id="kcs">Answered 0 of {len(kc)}</div></div>')
    return "".join(out)

KC_JS = """<script>
var _tot=%d,_done={},_right=0;
function pick(b){var q=b.dataset.q;if(_done[q])return;_done[q]=1;
 var box=b.closest('.q'),opts=box.querySelectorAll('.opt'),rat=box.querySelector('.rationale');
 opts.forEach(function(o){o.disabled=true;if(o.dataset.ok==='1')o.classList.add('correct');});
 if(b.dataset.ok==='1'){_right++;}else{b.classList.add('wrong');}
 var correct=box.querySelector('.opt[data-ok="1"] span:last-child').textContent;
 rat.innerHTML='<strong>'+(b.dataset.ok==='1'?'Correct.':'Not this one.')+'</strong> '+b.dataset.rat+
   (b.dataset.ok==='1'?'':' <br><br><strong>The answer is:</strong> '+correct+' \\u2014 '+
    box.querySelector('.opt[data-ok="1"]').dataset.rat);
 rat.classList.add('show');
 var n=Object.keys(_done).length;
 document.getElementById('kcs').textContent='Answered '+n+' of '+_tot+' \\u2014 '+_right+' correct'+
   (n===_tot?(_right===_tot?' \\u2014 clean sweep.':' \\u2014 review the rationales above.'):'');}
</script>"""

def lesson_page(L, allL):
    idx = allL.index(L)
    prev = allL[idx-1] if idx > 0 else None
    nxt = allL[idx+1] if idx < len(allL)-1 else None
    toc = ['<li><a href="#objectives">Learning objectives</a></li>',
           '<li><a href="#vocab">Key terminology</a></li>']
    body = []
    # objectives + vocab
    body.append('<section class="content-section" id="objectives">'
                '<div class="cs-head"><span class="cs-num">A</span><h2 class="h">Learning objectives</h2></div>'
                '<div class="rule"></div>'
                f'<p>{L["obj_lead"]}</p>{_objectives(L["objectives"])}</section>')
    body.append('<section class="content-section" id="vocab">'
                '<div class="cs-head"><span class="cs-num">B</span><h2 class="h">Key terminology</h2></div>'
                '<div class="rule"></div>'
                '<p>Click a card to reveal the definition. These are the terms the CCP and CCA exams use '
                'precisely, and the terms practitioners most often use loosely.</p>'
                f'{_vocab(L["vocab"])}</section>')
    for i, s in enumerate(L["sections"], 1):
        sid = f"s{i}"
        toc.append(f'<li><a href="#{sid}">{s["title"]}</a></li>')
        body.append(f'<section class="content-section" id="{sid}">'
                    f'<div class="cs-head"><span class="cs-num">{i}</span>'
                    f'<h2 class="h">{s["title"]}</h2></div><div class="rule"></div>{s["html"]}</section>')
    if L.get("case"):
        toc.append('<li><a href="#thread">Meridian &mdash; your turn</a></li>')
        body.append(f'<section class="content-section" id="thread">'
                    f'<div class="cs-head"><span class="cs-num">&#9670;</span>'
                    f'<h2 class="h">Meridian &mdash; your turn</h2></div><div class="rule"></div>'
                    f'{_case(L["case"])}</section>')
    if L.get("kc"):
        toc.append('<li><a href="#check">Knowledge check</a></li>')
        body.append(f'<section class="content-section" id="check">'
                    f'<div class="cs-head"><span class="cs-num">&#10003;</span>'
                    f'<h2 class="h">Knowledge check</h2></div><div class="rule"></div>'
                    f'<p>{L.get("kc_lead","Scenario-based questions in the style of the CCP and CCA exams. "
                    "Pick an answer to see why it is right or wrong &mdash; the rationale matters more than the score.")}</p>'
                    f'{_kc(L["kc"], L["file"])}</section>')
    pager = '<div class="pager">'
    if prev:
        pager += (f'<a class="prev" href="{prev["file"]}"><span class="pager-dir">&larr; Previous</span>'
                  f'<span class="pager-name">{prev["short"]}</span></a>')
    if nxt:
        pager += (f'<a class="next" href="{nxt["file"]}"><span class="pager-dir">Next &rarr;</span>'
                  f'<span class="pager-name">{nxt["short"]}</span></a>')
    pager += '</div>'
    kcjs = KC_JS % len(L.get("kc", [])) if L.get("kc") else ""
    return (head(f'{L["short"]} | CMMC Level 2 5-Day Workshop', L["lead"][:150]) + nav() +
            f'<header class="lhero"><div class="lhero-in">'
            f'<div class="eyebrow">{L["eyebrow"]}</div><h1>{L["title"]}</h1>'
            f'<p class="lead">{L["lead"]}</p><div class="chips">{_chips(L["chips"])}</div>'
            f'</div></header>'
            f'<div class="lwrap"><aside class="toc"><div class="toc-title">On this page</div>'
            f'<ol>{"".join(toc)}</ol></aside><main>' + "".join(body) + pager +
            '</main></div>' + FOOT + THEME_JS + kcjs + '</body></html>')

def manuscript(allL):
    out = ["# Stage 3 — Content Manuscript",
           "## CMMC Level 2 Assessor Preparation — 5-Day Workshop",
           "",
           "Generated from `build/content_*.py`, which is the authoritative source for every word a learner "
           "reads. Edit the content modules and rebuild; do not edit this file.",
           "",
           "**Register.** Peer-to-peer with working professionals. Direct, unhedged, no motivational filler. "
           "Second person for instructions and judgment work; third person for the regulation. Requirements are "
           "stated as the primary source states them, with the citation attached. Where the material is "
           "genuinely unsettled, it says so rather than manufacturing certainty.", ""]
    for L in allL:
        out += [f"---", f"# {L['num_label']} — {L['title']}", f"*{L['eyebrow']}*", "", L["lead"], "",
                "## Learning objectives", L["obj_lead"], ""]
        for b, t in L["objectives"]:
            out.append(f"- **[{b}]** {t}")
        out += ["", "## Key terminology", ""]
        for t, d in L["vocab"]:
            out.append(f"- **{t}** — {_strip(d)}")
        out.append("")
        for i, s in enumerate(L["sections"], 1):
            out += [f"## {i}. {s['title']}", "", _strip(s["html"]), ""]
        if L.get("case"):
            out += [f"## ThreadBridge — {L['case']['title']}", "", _strip(L["case"]["html"]), ""]
        if L.get("kc"):
            out += ["## Knowledge check", ""]
            for i, q in enumerate(L["kc"], 1):
                out.append(f"**Q{i}.** {_strip(q['stem'])}")
                for j, (txt, ok, rat) in enumerate(q["opts"]):
                    mark = " **(correct)**" if ok else ""
                    out.append(f"  - {'ABCDEFGH'[j]}. {_strip(txt)}{mark}")
                    out.append(f"    - *Feedback:* {_strip(rat)}")
                out.append("")
    return "\n".join(out)

import re
def _strip(s):
    s = re.sub(r"<(script|style)[\s\S]*?</\1>", "", s)
    s = re.sub(r"</(p|li|tr|h3|h4|div)>", "\n", s)
    s = re.sub(r"<li>", "- ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = _h.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()
