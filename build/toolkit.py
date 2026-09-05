# -*- coding: utf-8 -*-
"""Shared engine for the Meridian case tools."""
import html as _h
from theme import head, nav, FOOT, THEME_JS

ENGINE_JS = """<script>
var TOOLID='%s';
function _k(){return 'cmmc-'+TOOLID;}
function save(){var d={};document.querySelectorAll('[data-f]').forEach(function(e){d[e.dataset.f]=e.value;});
 try{localStorage.setItem(_k(),JSON.stringify(d));setMsg('Saved to this browser.');}catch(e){setMsg('Could not save.');}}
function load(){try{var d=JSON.parse(localStorage.getItem(_k())||'{}');
 document.querySelectorAll('[data-f]').forEach(function(e){if(d[e.dataset.f]!==undefined)e.value=d[e.dataset.f];});}catch(e){}}
function setMsg(t){var m=document.getElementById('msg');if(m){m.textContent=t;clearTimeout(window._mt);
 window._mt=setTimeout(function(){m.textContent=filled()+' of '+total()+' items answered.';},2600);}}
function total(){return document.querySelectorAll('.item').length;}
function filled(){var n=0;document.querySelectorAll('.item').forEach(function(it){
 var ok=false;it.querySelectorAll('[data-f]').forEach(function(e){if(e.value&&e.value.trim())ok=true;});
 if(ok)n++;});return n;}
function reveal(btn){var it=btn.closest('.item'),v=it.querySelector('.verdict');
 var sel=it.querySelector('select[data-ok]');
 if(sel){var good=sel.value===sel.dataset.ok;
   v.classList.remove('good','bad');v.classList.add(good?'good':'bad');
   var h=v.querySelector('h4');if(h)h.textContent=good?'Correct \\u2014 and here is the full reasoning':'Not this one \\u2014 here is why';}
 v.classList.add('show');btn.textContent='Model answer shown';btn.disabled=true;
 var need=it.querySelector('.needchange');
 if(need&&!need.value.trim()){var w=it.querySelector('.nc-warn');if(w)w.style.display='block';}
 save();}
function revealAll(){document.querySelectorAll('.rvbtn').forEach(function(b){if(!b.disabled)reveal(b);});}
function resetAll(){if(!confirm('Clear every answer on this page?'))return;
 try{localStorage.removeItem(_k());}catch(e){}location.reload();}
function code(){var d={};document.querySelectorAll('[data-f]').forEach(function(e){d[e.dataset.f]=e.value;});
 var s=btoa(unescape(encodeURIComponent(JSON.stringify(d))));
 var t=document.getElementById('codebox');t.style.display='block';t.value=s;t.select();
 setMsg('Progress code generated \\u2014 copy and keep it.');}
function restore(){var t=document.getElementById('codebox');t.style.display='block';
 if(!t.value.trim()){setMsg('Paste a progress code into the box first.');return;}
 try{var d=JSON.parse(decodeURIComponent(escape(atob(t.value.trim()))));
  document.querySelectorAll('[data-f]').forEach(function(e){if(d[e.dataset.f]!==undefined)e.value=d[e.dataset.f];});
  save();setMsg('Restored.');}catch(e){setMsg('That code could not be read.');}}
window.addEventListener('DOMContentLoaded',function(){load();
 document.querySelectorAll('[data-f]').forEach(function(e){e.addEventListener('change',save);});
 setMsg('');});
</script>"""

def item(iid, n, title, context="", fields=None, model="", ok_label="Check my answer"):
    """One exercise item. fields: list of dicts {label,type,name,options?,ok?,ph?,cls?}"""
    fhtml = ""
    for f in (fields or []):
        fid = f"{iid}-{f['name']}"
        cls = f.get("cls", "")
        if f["type"] == "select":
            opts = "".join(f'<option value="{_h.escape(o, quote=True)}">{o}</option>'
                           for o in [""] + f["options"])
            okattr = f' data-ok="{_h.escape(f["ok"], quote=True)}"' if f.get("ok") else ""
            fhtml += (f'<div style="margin-bottom:.8rem"><label for="{fid}">{f["label"]}</label>'
                      f'<select id="{fid}" data-f="{fid}" class="{cls}"{okattr}>{opts}</select></div>')
        elif f["type"] == "text":
            fhtml += (f'<div style="margin-bottom:.8rem"><label for="{fid}">{f["label"]}</label>'
                      f'<input type="text" id="{fid}" data-f="{fid}" class="{cls}" '
                      f'placeholder="{_h.escape(f.get("ph",""), quote=True)}"></div>')
        else:
            fhtml += (f'<div style="margin-bottom:.8rem"><label for="{fid}">{f["label"]}</label>'
                      f'<textarea id="{fid}" data-f="{fid}" class="{cls}" '
                      f'placeholder="{_h.escape(f.get("ph",""), quote=True)}"></textarea></div>')
    ncwarn = ('<div class="nc-warn" style="display:none;margin-top:.6rem;font-family:Arial,sans-serif;'
              'font-size:.78rem;color:var(--bad)"><strong>Incomplete.</strong> A verdict without a '
              '&ldquo;what would change it&rdquo; clause is not finished. Fill that field before you move on.</div>'
              ) if any(f.get("cls") == "needchange" for f in (fields or [])) else ""
    return f"""<div class="item panel" id="{iid}">
  <div style="display:flex;align-items:baseline;gap:.7rem;margin-bottom:.5rem">
    <span style="font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:1.5rem;color:var(--gold)">{n}</span>
    <h2 style="margin:0">{title}</h2></div>
  {context}
  {fhtml}
  <div class="btnrow"><button class="btn rvbtn" onclick="reveal(this)">{ok_label}</button></div>
  {ncwarn}
  <div class="verdict"><h4>Model answer</h4>{model}</div>
</div>"""

def tool_page(toolid, title, eyebrow, h1, lead, chips, intro, items_html,
              back=("Back to the lesson", "index.html"), extra_js="", extra_head=""):
    chiphtml = "".join(f'<span class="meta-chip">{c}</span>' for c in chips)
    return (head(f"{title} | CMMC 5-Day Workshop", lead[:150]) + nav() + extra_head +
            f"""<header class="lhero"><div class="lhero-in">
  <div class="eyebrow">{eyebrow}</div><h1>{h1}</h1>
  <p class="lead">{lead}</p><div class="chips">{chiphtml}</div>
</div></header>
<main class="tool-main">
{intro}
{items_html}
<div class="panel" style="text-align:center">
  <div class="btnrow" style="justify-content:center">
    <button class="btn secondary" onclick="revealAll()">Reveal every model answer</button>
    <button class="btn ghost" onclick="window.print()">&#128424; Print / Save PDF</button>
    <button class="btn ghost" onclick="code()">&#128273; Progress code</button>
    <button class="btn ghost" onclick="restore()">Restore from code</button>
    <button class="btn ghost" onclick="resetAll()">Clear</button>
  </div>
  <textarea id="codebox" style="display:none;margin-top:1rem;min-height:70px"
    placeholder="Your progress code appears here. Copy it and keep it; paste it back to restore."></textarea>
</div>
<div class="pager"><a class="prev" href="{back[1]}"><span class="pager-dir">&larr; Back</span>
  <span class="pager-name">{back[0]}</span></a></div>
</main>
<div class="savebar"><span class="msg" id="msg"></span>
  <span style="font-family:Arial,sans-serif;font-size:.72rem;color:var(--text-muted)">
    Saved in this browser only &mdash; nothing is sent anywhere.</span></div>
""" + FOOT + THEME_JS + (ENGINE_JS % toolid) + extra_js + "</body></html>")
