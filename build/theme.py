# -*- coding: utf-8 -*-
"""CMMC 5-Day Workshop — shared design system and page shells."""

CSS = r"""
:root{
  --navy:#12233a; --navy-mid:#0d1a2b; --navy-light:#24425f;
  --gold:#c8862a; --gold-light:#e0a244; --gold-pale:#fbf1e0;
  --cream:#f4f6f9; --text-primary:#10202f; --text-secondary:#2b4258; --text-muted:#5c7086;
  --white:#ffffff; --border:#c2ccd8; --card-bg:#ffffff; --body-bg:#eef1f5;
  --section-alt:#e3e8ee; --blue-pale:#e9eef4; --blue-pale-border:#bfcedd;
  --ok:#2f6f4f; --warn:#9a5b12; --bad:#9d3427;
}
[data-theme="dark"]{
  --cream:#071320; --text-primary:#e8eef5; --text-secondary:#a3b6c9; --text-muted:#748a9e; --card-bg:#0f2537; --body-bg:#071320; --section-alt:#0b1d2c;
  --blue-pale:#0d2436; --blue-pale-border:#1e405c; --border:#1e3a52; --gold-pale:#2b1d09; --white:#ffffff;
  --ok:#6fbf90; --warn:#e0a244; --bad:#e0796a;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;font-size:16px}
body{font-family:Georgia,'Times New Roman',serif;background:var(--body-bg);color:var(--text-primary);
  line-height:1.65;transition:background .3s,color .3s}
a{color:inherit}
/* NAV */
nav{position:sticky;top:0;z-index:100;background:var(--card-bg);border-bottom:3px solid var(--gold);
  display:flex;align-items:center;justify-content:space-between;padding:0 2rem;height:60px}
.nav-brand{display:flex;align-items:center;gap:.75rem;text-decoration:none}
.nav-seal{width:38px;height:38px;border-radius:50%;background:var(--gold);display:flex;align-items:center;
  justify-content:center;font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.62rem;
  color:#fff;letter-spacing:.02em;text-align:center;line-height:1.1;flex-shrink:0}
.nav-title{font-family:'Arial Narrow',Arial,sans-serif;font-weight:700;font-size:1rem;color:var(--text-primary);
  letter-spacing:.08em;text-transform:uppercase}
.nav-right{display:flex;align-items:center;gap:1rem}
.nav-links{display:flex;gap:1.5rem;list-style:none}
.nav-links a{color:var(--text-secondary);text-decoration:none;font-family:Arial,sans-serif;font-size:.8rem;
  letter-spacing:.06em;text-transform:uppercase;transition:color .2s}
.nav-links a:hover{color:var(--gold)}
.theme-toggle{background:transparent;border:1px solid var(--gold);color:var(--gold);padding:.3rem .75rem;
  border-radius:20px;cursor:pointer;font-size:.75rem;font-family:Arial,sans-serif;letter-spacing:.04em}
.theme-toggle:hover{background:var(--gold);color:#fff}
/* HERO */
.hero{background:var(--blue-pale);position:relative;overflow:hidden;padding:5rem 2rem 4rem;text-align:center}
.hero::before{content:'';position:absolute;inset:0;
  background:repeating-linear-gradient(-55deg,transparent,transparent 40px,rgba(18,35,58,.05) 40px,rgba(18,35,58,.05) 41px)}
.hero-eyebrow{font-family:Arial,sans-serif;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);margin-bottom:1.25rem;position:relative}
.hero h1{font-family:Georgia,serif;font-size:clamp(2.2rem,5vw,3.6rem);font-weight:700;color:var(--text-primary);
  line-height:1.15;max-width:860px;margin:0 auto 1rem;position:relative}
.hero h1 span{color:var(--gold)}
.hero-subtitle{font-family:Arial,sans-serif;font-size:1.05rem;color:var(--text-secondary);max-width:680px;
  margin:0 auto 2rem;line-height:1.7;position:relative}
.hero-cta{display:inline-flex;align-items:center;gap:.5rem;background:var(--gold);color:#fff;text-decoration:none;
  font-family:Arial,sans-serif;font-weight:700;font-size:.9rem;letter-spacing:.06em;text-transform:uppercase;
  padding:.85rem 2rem;border-radius:2px;position:relative;transition:background .2s,transform .15s}
.hero-cta:hover{background:var(--gold-light);transform:translateY(-1px)}
/* STATS */
.stats-bar{background:var(--blue-pale);border-bottom:3px solid var(--gold);padding:1rem 2rem;display:flex;
  justify-content:center;gap:0;flex-wrap:wrap}
.stat-item{display:flex;align-items:center;gap:.5rem;padding:0 2rem;border-right:2px solid rgba(200,134,42,.35)}
.stat-item:last-child{border-right:none}
.stat-num{font-family:'Arial Narrow',Arial,sans-serif;font-size:1.6rem;font-weight:900;color:var(--gold);line-height:1}
.stat-label{font-family:Arial,sans-serif;font-size:.7rem;font-weight:700;color:var(--text-secondary);
  letter-spacing:.08em;text-transform:uppercase;line-height:1.2}
/* SECTIONS */
.section{padding:4rem 2rem;max-width:1200px;margin:0 auto}
.section-alt{background:var(--section-alt)}
.section-eyebrow{font-family:Arial,sans-serif;font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);margin-bottom:.5rem}
.section-title{font-family:Georgia,serif;font-size:clamp(1.5rem,3vw,2rem);font-weight:700;
  color:var(--text-primary);margin-bottom:.5rem;line-height:1.2}
.section-desc{font-family:Arial,sans-serif;font-size:.95rem;color:var(--text-secondary);max-width:660px;
  margin-bottom:2.5rem;line-height:1.7}
.rule{width:48px;height:3px;background:var(--gold);margin:.75rem 0 1.5rem}
/* NOTICE BANNER (available; unused by default) */
.reg-banner{max-width:1200px;margin:2.5rem auto 0;padding:0 2rem}
.reg-inner{background:var(--gold-pale);border:1px solid var(--gold);border-left:5px solid var(--gold);
  border-radius:3px;padding:1.1rem 1.35rem}
.reg-tag{font-family:Arial,sans-serif;font-size:.62rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--warn);margin-bottom:.4rem}
.reg-head{font-family:Georgia,serif;font-weight:700;font-size:1rem;color:var(--text-primary);margin-bottom:.4rem}
.reg-body{font-family:Arial,sans-serif;font-size:.82rem;color:var(--text-secondary);line-height:1.65}
.reg-verify{font-family:Arial,sans-serif;font-size:.7rem;color:var(--text-muted);margin-top:.55rem;
  letter-spacing:.03em}
/* CARDS */
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:1.5rem}
.lesson-card{background:var(--card-bg);border:1px solid var(--border);border-radius:4px;padding:1.5rem;
  display:flex;flex-direction:column;gap:.75rem;transition:box-shadow .2s,transform .15s;position:relative;overflow:hidden}
.lesson-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--gold)}
.lesson-card:hover{box-shadow:0 6px 24px rgba(10,22,40,.14);transform:translateY(-2px)}
.card-header{display:flex;align-items:flex-start;justify-content:space-between;gap:1rem}
.lesson-badge{background:var(--navy);color:#fff;font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;
  font-size:.75rem;letter-spacing:.1em;padding:.25rem .6rem;border-radius:2px;white-space:nowrap;flex-shrink:0}
.domain-weight{font-family:Arial,sans-serif;font-size:.7rem;color:var(--text-muted);letter-spacing:.05em;
  text-align:right;line-height:1.3}
.domain-weight strong{display:block;font-size:1rem;color:var(--gold);font-family:'Arial Narrow',Arial,sans-serif;font-weight:900}
.card-day-tag{font-family:Arial,sans-serif;font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--text-muted);border:1px solid var(--border);border-radius:20px;padding:.15rem .6rem;width:fit-content}
.card-title{font-family:Georgia,serif;font-size:1.05rem;font-weight:700;color:var(--text-primary);line-height:1.3}
.card-desc{font-family:Arial,sans-serif;font-size:.83rem;color:var(--text-secondary);line-height:1.65;flex:1}
.card-thread{font-family:Arial,sans-serif;font-size:.72rem;color:var(--text-muted);line-height:1.5;
  border-top:1px dashed var(--border);padding-top:.6rem}
.card-thread strong{color:var(--gold);font-weight:700}
.card-footer{border-top:1px solid var(--border);padding-top:.75rem;margin-top:auto}
.launch-btn{display:inline-flex;align-items:center;gap:.4rem;background:var(--gold);color:#fff;text-decoration:none;
  font-family:Arial,sans-serif;font-weight:700;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;
  padding:.55rem 1.1rem;border-radius:2px;transition:background .2s}
.launch-btn:hover{background:var(--gold-light)}
.launch-btn .arrow{font-size:1rem;transition:transform .15s}
.launch-btn:hover .arrow{transform:translateX(3px)}
.card-special .lesson-badge{background:var(--gold);color:#fff}
.card-special::before{background:var(--navy)}
/* RESOURCES */
.resource-section-heading{display:flex;align-items:center;gap:.75rem;margin-bottom:1.25rem;padding-bottom:.75rem;
  border-bottom:2px solid var(--border)}
.resource-section-heading .rsh-icon{font-size:1.4rem;line-height:1}
.resource-section-heading h3{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:1.1rem;
  color:var(--text-primary);letter-spacing:.08em;text-transform:uppercase}
.resource-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:1.25rem;margin-bottom:3rem}
.resource-card{background:var(--card-bg);border:1px solid var(--border);border-radius:4px;padding:1.35rem 1.4rem;
  display:flex;flex-direction:column;gap:.6rem;transition:box-shadow .2s,transform .15s;position:relative;overflow:hidden}
.resource-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--gold)}
.resource-card:hover{box-shadow:0 6px 24px rgba(10,22,40,.14);transform:translateY(-2px)}
.rc-type{font-family:Arial,sans-serif;font-size:.62rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:var(--text-muted);border:1px solid var(--border);border-radius:20px;padding:.15rem .6rem;width:fit-content}
.rc-icon-title{display:flex;align-items:center;gap:.5rem}
.rc-icon{font-size:1.3rem;line-height:1;flex-shrink:0}
.rc-title{font-family:Georgia,serif;font-size:1rem;font-weight:700;color:var(--text-primary);line-height:1.25}
.rc-desc{font-family:Arial,sans-serif;font-size:.81rem;color:var(--text-secondary);line-height:1.6;flex:1}
.rc-covers{font-family:Arial,sans-serif;font-size:.72rem;color:var(--text-muted);line-height:1.5}
.rc-covers strong{color:var(--gold);font-weight:700}
.resource-card .card-footer{border-top:1px solid var(--border);padding-top:.65rem;margin-top:auto}
/* SCHEDULE */
.schedule-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:1rem;grid-auto-rows:1fr}
.day-col{background:var(--card-bg);border:1px solid var(--border);border-radius:4px;overflow:hidden;
  display:flex;flex-direction:column}
.day-header{background:var(--navy);color:#fff;font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;
  font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;padding:.65rem 1rem;text-align:center}
.day-theme{font-family:Arial,sans-serif;font-size:.65rem;color:#a3b6c9;letter-spacing:.06em;text-transform:uppercase;
  padding:.4rem 1rem;background:var(--navy-mid);text-align:center}
.day-lessons{padding:.75rem;display:flex;flex-direction:column;gap:.5rem;flex:1}
.day-lesson{display:flex;flex-direction:column;justify-content:center;gap:.15rem;padding:.6rem .7rem;
  background:var(--section-alt);border-left:3px solid var(--gold);border-radius:0 2px 2px 0;flex:1;
  text-decoration:none;cursor:pointer;transition:background .15s,border-color .15s}
.day-lesson:hover{background:var(--blue-pale);border-left-color:var(--navy-light)}
.day-lesson:hover .day-lesson-name{color:var(--gold)}
.day-lesson-num{font-family:Arial,sans-serif;font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted)}
.day-lesson-name{font-family:Georgia,serif;font-size:.86rem;font-weight:700;color:var(--text-primary);line-height:1.25}
.day-lesson-meta{font-family:Arial,sans-serif;font-size:.66rem;color:var(--text-muted)}
.day-cap{font-family:Arial,sans-serif;font-size:.64rem;color:var(--text-muted);padding:.5rem .75rem .7rem;
  border-top:1px dashed var(--border);line-height:1.45}
.day-cap strong{color:var(--gold)}
/* CAP PHASE BARS */
.bar-row{display:flex;align-items:center;gap:1rem;margin-bottom:.9rem}
.bar-label{font-family:Arial,sans-serif;font-size:.8rem;color:var(--text-secondary);width:290px;flex-shrink:0}
.bar-track{flex:1;height:22px;background:var(--section-alt);border:1px solid var(--border);border-radius:2px;overflow:hidden}
.bar-fill{height:100%;background:var(--gold);display:flex;align-items:center;justify-content:flex-end;
  padding-right:.5rem;color:#fff;font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.72rem}
/* ABOUT */
.about-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:2.5rem}
.about-body p{font-family:Arial,sans-serif;font-size:.9rem;color:var(--text-secondary);line-height:1.8;margin-bottom:1rem}
.about-body h4{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.95rem;letter-spacing:.08em;
  text-transform:uppercase;color:var(--text-primary);margin:1.5rem 0 .6rem}
.facts-box{background:var(--card-bg);border:1px solid var(--border);border-radius:4px;padding:1.5rem;height:fit-content}
.facts-box h4{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:1rem;letter-spacing:.08em;
  text-transform:uppercase;color:var(--text-primary);margin-bottom:1rem;padding-bottom:.6rem;border-bottom:2px solid var(--gold)}
.facts-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.fact .fv{font-family:'Arial Narrow',Arial,sans-serif;font-size:1.35rem;font-weight:900;color:var(--gold);line-height:1}
.fact .fl{font-family:Arial,sans-serif;font-size:.68rem;color:var(--text-muted);letter-spacing:.06em;
  text-transform:uppercase;margin-top:.2rem}
/* FOOTER */
footer{background:var(--navy);color:#a3b6c9;padding:2.5rem 2rem;text-align:center}
.foot-title{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:1rem;letter-spacing:.14em;
  text-transform:uppercase;color:#fff;margin-bottom:.9rem}
.foot-text{font-family:Arial,sans-serif;font-size:.76rem;line-height:1.75;max-width:900px;margin:0 auto}
/* ---------- LESSON PAGES ---------- */
.lwrap{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:250px 1fr;gap:2.5rem;padding:2.5rem 2rem 4rem}
.toc{position:sticky;top:80px;align-self:start;background:var(--card-bg);border:1px solid var(--border);
  border-radius:4px;padding:1.1rem 1.2rem;max-height:calc(100vh - 110px);overflow-y:auto}
.toc-title{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.78rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--text-primary);margin-bottom:.7rem;padding-bottom:.5rem;border-bottom:2px solid var(--gold)}
.toc ol{list-style:none;counter-reset:toc}
.toc li{counter-increment:toc;margin-bottom:.3rem}
.toc a{display:block;font-family:Arial,sans-serif;font-size:.76rem;color:var(--text-secondary);text-decoration:none;
  padding:.28rem .4rem;border-radius:2px;line-height:1.4;border-left:2px solid transparent}
.toc a::before{content:counter(toc) ". ";color:var(--gold);font-weight:700}
.toc a:hover{background:var(--blue-pale);color:var(--gold);border-left-color:var(--gold)}
.lhero{background:var(--blue-pale);border-bottom:3px solid var(--gold);padding:2.5rem 2rem}
.lhero-in{max-width:1200px;margin:0 auto}
.eyebrow{font-family:Arial,sans-serif;font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:.6rem}
.lhero h1{font-family:Georgia,serif;font-size:clamp(1.7rem,3.6vw,2.5rem);font-weight:700;line-height:1.2;max-width:860px}
.lead{font-family:Arial,sans-serif;font-size:.95rem;color:var(--text-secondary);line-height:1.8;max-width:800px;margin-top:.9rem}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1.2rem}
.meta-chip{font-family:Arial,sans-serif;font-size:.7rem;letter-spacing:.05em;color:var(--text-secondary);
  background:var(--card-bg);border:1px solid var(--border);border-radius:20px;padding:.25rem .8rem}
.meta-chip strong{color:var(--gold)}
h2.h{font-family:Georgia,serif;font-size:1.45rem;font-weight:700;color:var(--text-primary);line-height:1.25;margin-bottom:.2rem}
.content-section{margin-bottom:3rem;scroll-margin-top:80px}
.content-section p{font-family:Arial,sans-serif;font-size:.9rem;color:var(--text-secondary);line-height:1.85;margin-bottom:1rem}
.content-section h3{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:1rem;letter-spacing:.07em;
  text-transform:uppercase;color:var(--text-primary);margin:1.7rem 0 .7rem}
.content-section ul,.content-section ol{margin:0 0 1.1rem 1.3rem}
.content-section li{font-family:Arial,sans-serif;font-size:.88rem;color:var(--text-secondary);line-height:1.8;margin-bottom:.4rem}
.content-section strong{color:var(--text-primary)}
.cs-head{display:flex;align-items:baseline;gap:.8rem;margin-bottom:.4rem}
.cs-num{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:1.9rem;color:var(--gold);line-height:1;flex-shrink:0}
/* TABLES */
.tw{overflow-x:auto;margin:1.1rem 0 1.4rem;border:1px solid var(--border);border-radius:4px;background:var(--card-bg)}
table{border-collapse:collapse;width:100%;min-width:520px}
th{background:var(--navy);color:#fff;font-family:Arial,sans-serif;font-size:.72rem;font-weight:700;
  letter-spacing:.07em;text-transform:uppercase;text-align:left;padding:.6rem .8rem}
td{font-family:Arial,sans-serif;font-size:.82rem;color:var(--text-secondary);padding:.6rem .8rem;
  border-top:1px solid var(--border);line-height:1.6;vertical-align:top}
tbody tr:nth-child(even){background:var(--section-alt)}
td strong{color:var(--text-primary)}
/* CALLOUTS */
.tip,.in-practice,.warnbox{border-radius:3px;padding:1rem 1.2rem;margin:1.2rem 0}
.tip{background:var(--gold-pale);border:1px solid var(--gold);border-left:5px solid var(--gold)}
.tip-label{font-family:Arial,sans-serif;font-size:.62rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--warn);margin-bottom:.35rem}
.in-practice{background:var(--blue-pale);border:1px solid var(--blue-pale-border);border-left:5px solid var(--navy-light)}
.ip-label{font-family:Arial,sans-serif;font-size:.62rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--navy-light);margin-bottom:.35rem}
.warnbox{background:var(--card-bg);border:1px solid var(--bad);border-left:5px solid var(--bad)}
.warn-label{font-family:Arial,sans-serif;font-size:.62rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--bad);margin-bottom:.35rem}
.tip p,.in-practice p,.warnbox p{font-family:Arial,sans-serif;font-size:.85rem;line-height:1.75;margin:0 0 .6rem}
.tip p:last-child,.in-practice p:last-child,.warnbox p:last-child{margin-bottom:0}
/* OBJECTIVES */
.obj-list{list-style:none;margin:0!important}
.obj-list li{display:flex;gap:.8rem;align-items:flex-start;background:var(--card-bg);border:1px solid var(--border);
  border-left:3px solid var(--gold);border-radius:0 3px 3px 0;padding:.75rem .95rem;margin-bottom:.6rem}
.obj-tag{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.66rem;letter-spacing:.08em;
  text-transform:uppercase;background:var(--navy);color:#fff;border-radius:2px;padding:.18rem .5rem;flex-shrink:0;margin-top:.15rem}
/* VOCAB FLIP */
.vocab-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:.9rem;margin:1.2rem 0}
.flip-card{background:transparent;height:170px;perspective:1000px;cursor:pointer;border:none;padding:0;font:inherit;text-align:left}
.flip-inner{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.flip-card.flipped .flip-inner{transform:rotateY(180deg)}
.flip-face{position:absolute;inset:0;backface-visibility:hidden;border:1px solid var(--border);border-radius:4px;
  padding:.9rem 1rem;display:flex;flex-direction:column;justify-content:center;background:var(--card-bg);overflow:auto}
.flip-back{transform:rotateY(180deg);background:var(--navy);border-color:var(--navy)}
.vocab-term{font-family:Georgia,serif;font-size:.95rem;font-weight:700;color:var(--text-primary);line-height:1.3}
.vocab-def{font-family:Arial,sans-serif;font-size:.76rem;color:#e8eef5;line-height:1.6}
.flip-hint{font-family:Arial,sans-serif;font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--text-muted);margin-top:.6rem}
/* DIAGRAM */
.diagram{background:var(--card-bg);border:1px solid var(--border);border-radius:4px;padding:1.3rem;margin:1.3rem 0;overflow-x:auto}
.diagram figcaption{font-family:Arial,sans-serif;font-size:.74rem;color:var(--text-muted);margin-top:.8rem;line-height:1.6}
/* CASE BLOCK */
.case{background:var(--navy);border-radius:5px;padding:1.6rem 1.8rem;margin:2rem 0;border-left:6px solid var(--gold)}
.case-tag{font-family:Arial,sans-serif;font-size:.62rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);margin-bottom:.5rem}
.case h3{font-family:Georgia,serif;font-size:1.2rem;font-weight:700;color:#fff;margin-bottom:.7rem;line-height:1.3}
.case p{font-family:Arial,sans-serif;font-size:.86rem;color:#c8d6e4;line-height:1.8;margin-bottom:.9rem}
.case ul{margin:0 0 1rem 1.2rem}
.case li{font-family:Arial,sans-serif;font-size:.85rem;color:#c8d6e4;line-height:1.75;margin-bottom:.35rem}
.case strong{color:#fff}
.case-actions{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.1rem;padding-top:1.1rem;border-top:1px solid rgba(255,255,255,.18)}
.case-btn{display:inline-flex;align-items:center;gap:.4rem;background:var(--gold);color:#fff;text-decoration:none;
  font-family:Arial,sans-serif;font-weight:700;font-size:.75rem;letter-spacing:.07em;text-transform:uppercase;
  padding:.55rem 1.1rem;border-radius:2px}
.case-btn:hover{background:var(--gold-light)}
.case-btn.ghost{background:transparent;border:1px solid var(--gold);color:var(--gold)}
.case-btn.ghost:hover{background:var(--gold);color:#fff}
/* KNOWLEDGE CHECK */
.kc{background:var(--card-bg);border:1px solid var(--border);border-radius:5px;padding:1.6rem 1.8rem;margin-top:1.2rem}
.q{border-top:1px solid var(--border);padding-top:1.2rem;margin-top:1.2rem}
.q:first-of-type{border-top:none;padding-top:0;margin-top:0}
.qn{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.68rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--gold);margin-bottom:.35rem}
.q-stem{font-family:Arial,sans-serif;font-size:.9rem;color:var(--text-primary);line-height:1.75;margin-bottom:.8rem;font-weight:600}
.options{display:flex;flex-direction:column;gap:.45rem}
.opt{display:flex;gap:.7rem;align-items:flex-start;background:var(--section-alt);border:1px solid var(--border);
  border-radius:3px;padding:.6rem .8rem;cursor:pointer;font-family:Arial,sans-serif;font-size:.84rem;
  color:var(--text-secondary);line-height:1.6;text-align:left;transition:background .15s,border-color .15s;width:100%}
.opt:hover:not(:disabled){background:var(--blue-pale);border-color:var(--navy-light)}
.opt:disabled{cursor:default}
.opt-letter{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.8rem;color:var(--gold);flex-shrink:0}
.opt.correct{background:rgba(47,111,79,.14);border-color:var(--ok)}
.opt.correct .opt-letter{color:var(--ok)}
.opt.wrong{background:rgba(157,52,39,.12);border-color:var(--bad)}
.opt.wrong .opt-letter{color:var(--bad)}
.rationale{display:none;margin-top:.7rem;background:var(--blue-pale);border-left:4px solid var(--navy-light);
  border-radius:0 3px 3px 0;padding:.75rem .95rem;font-family:Arial,sans-serif;font-size:.82rem;
  color:var(--text-secondary);line-height:1.75}
.rationale.show{display:block}
.rationale strong{color:var(--text-primary)}
.kc-score{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.9rem;letter-spacing:.08em;
  text-transform:uppercase;color:var(--gold);margin-top:1.4rem;padding-top:1rem;border-top:2px solid var(--gold)}
/* PAGER */
.pager{display:flex;justify-content:space-between;gap:1rem;margin-top:2.5rem;padding-top:1.5rem;border-top:2px solid var(--border)}
.pager a{display:flex;flex-direction:column;gap:.15rem;text-decoration:none;background:var(--card-bg);
  border:1px solid var(--border);border-radius:4px;padding:.8rem 1.2rem;flex:1;max-width:47%;transition:border-color .2s}
.pager a:hover{border-color:var(--gold)}
.pager a.next{text-align:right;margin-left:auto}
.pager-dir{font-family:Arial,sans-serif;font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold)}
.pager-name{font-family:Georgia,serif;font-size:.9rem;font-weight:700;color:var(--text-primary);line-height:1.3}
/* TOOL PAGES */
.tool-main{max-width:1100px;margin:0 auto;padding:2.5rem 2rem 4rem}
.panel{background:var(--card-bg);border:1px solid var(--border);border-radius:5px;padding:1.5rem 1.7rem;margin-bottom:1.5rem}
.panel h2{font-family:Georgia,serif;font-size:1.2rem;font-weight:700;margin-bottom:.3rem}
.panel h3{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.95rem;letter-spacing:.07em;
  text-transform:uppercase;color:var(--text-primary);margin:1.4rem 0 .6rem}
.panel p{font-family:Arial,sans-serif;font-size:.86rem;color:var(--text-secondary);line-height:1.8;margin-bottom:.8rem}
.panel ul{margin:0 0 1rem 1.3rem}
.panel li{font-family:Arial,sans-serif;font-size:.85rem;color:var(--text-secondary);line-height:1.75;margin-bottom:.35rem}
label{display:block;font-family:Arial,sans-serif;font-size:.74rem;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;color:var(--text-muted);margin-bottom:.3rem}
input[type=text],textarea,select{width:100%;font-family:Arial,sans-serif;font-size:.86rem;color:var(--text-primary);
  background:var(--body-bg);border:1px solid var(--border);border-radius:3px;padding:.5rem .65rem;line-height:1.6}
textarea{min-height:74px;resize:vertical}
input:focus,textarea:focus,select:focus{outline:2px solid var(--gold);outline-offset:1px}
.btn{display:inline-flex;align-items:center;gap:.4rem;background:var(--gold);color:#fff;border:none;
  font-family:Arial,sans-serif;font-weight:700;font-size:.76rem;letter-spacing:.07em;text-transform:uppercase;
  padding:.6rem 1.15rem;border-radius:2px;cursor:pointer;text-decoration:none}
.btn:hover{background:var(--gold-light)}
.btn.secondary{background:var(--navy)}
.btn.secondary:hover{background:var(--navy-light)}
.btn.ghost{background:transparent;border:1px solid var(--gold);color:var(--gold)}
.btn.ghost:hover{background:var(--gold);color:#fff}
.btnrow{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem}
.verdict{display:none;margin-top:1rem;border-radius:3px;padding:1rem 1.2rem;font-family:Arial,sans-serif;
  font-size:.85rem;line-height:1.75;border-left:5px solid var(--navy-light);background:var(--blue-pale);
  border:1px solid var(--blue-pale-border);border-left-width:5px}
.verdict.show{display:block}
.verdict h4{font-family:'Arial Narrow',Arial,sans-serif;font-weight:900;font-size:.8rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--navy-light);margin-bottom:.4rem}
.verdict.good{background:rgba(47,111,79,.12);border-color:var(--ok)}
.verdict.good h4{color:var(--ok)}
.verdict.bad{background:rgba(157,52,39,.1);border-color:var(--bad)}
.verdict.bad h4{color:var(--bad)}
.pill{display:inline-block;font-family:Arial,sans-serif;font-size:.66rem;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;border-radius:20px;padding:.15rem .6rem;border:1px solid var(--border);color:var(--text-muted)}
.pill.ok{color:var(--ok);border-color:var(--ok)}
.pill.no{color:var(--bad);border-color:var(--bad)}
.pill.mid{color:var(--warn);border-color:var(--warn)}
.savebar{position:sticky;bottom:0;background:var(--card-bg);border-top:2px solid var(--gold);padding:.7rem 2rem;
  display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;z-index:60}
.savebar .msg{font-family:Arial,sans-serif;font-size:.76rem;color:var(--text-muted)}
@media print{
  nav,.savebar,.theme-toggle,.pager,.btnrow,.toc{display:none!important}
  body{background:#fff}
  .panel,.tw,.kc{break-inside:avoid}
}
@media (max-width:980px){
  .lwrap{grid-template-columns:1fr;padding:2rem 1.2rem 3rem}
  .toc{position:static;max-height:none}
  .schedule-grid{grid-template-columns:repeat(2,1fr)}
  .about-grid{grid-template-columns:1fr}
  .nav-links{display:none}
  .bar-label{width:150px;font-size:.72rem}
}
@media (max-width:560px){
  .schedule-grid{grid-template-columns:1fr}
  nav{padding:0 1rem}
  .section{padding:2.5rem 1.2rem}
}
"""

def head(title, desc=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{desc}">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
"""

NAVLINKS = [("index.html#lessons","Lessons"),("index.html#schedule","Schedule"),
            ("index.html#thread","Case Thread"),("index.html#resources","Tools"),
            ("index.html#about","About")]

def nav(active=""):
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAVLINKS)
    return f"""<nav>
  <a class="nav-brand" href="index.html">
    <div class="nav-seal">CMMC<br>L2</div>
    <div class="nav-title">CMMC Level&nbsp;2 &middot; 5-Day</div>
  </a>
  <div class="nav-right">
    <ul class="nav-links">{links}</ul>
    <button class="theme-toggle" onclick="tt()" id="ttb">&#9790; Dark</button>
  </div>
</nav>
"""

FOOT = """<footer>
  <div class="foot-title">CMMC Level 2 Assessor Preparation &middot; 5-Day Workshop</div>
  <p class="foot-text">
    An independent educational resource. Not affiliated with, endorsed by, or sponsored by the U.S. Department of
    War, the Department of Defense, the Cyber AB, or ISACA. CMMC&reg; is a mark of the U.S. Department of Defense;
    CCP and CCA are credentials administered by ISACA as the CMMC Assessor and Instructor Certification
    Organization. Meridian Precision Defense Systems, Inc., Acuitas Machining Inc., ClearPath IT Solutions,
    Tidewater Assurance Group, LLC, Ridgeline Compliance Group, and all personnel, CAGE codes, contract numbers,
    and incidents depicted are fictional and created for instruction. The Meridian scenario is adapted from the
    CMMC 2.0 Training Portal case study library. Nothing here is legal, compliance, or cybersecurity advice.
    Requirements are stated from primary sources &mdash; 32 CFR Part 170, 32 CFR Part 2002, the FAR, the DFARS,
    NIST SP 800-171 Rev 2 and 800-171A, the CMMC Assessment Process v2.0 and Code of Professional Conduct v2.0,
    and the NARA CUI Registry. Verify the live regulatory position before teaching or relying on this material.
  </p>
</footer>
"""

THEME_JS = """<script>
function tt(){var d=document.documentElement.getAttribute('data-theme')==='dark';
 document.documentElement.setAttribute('data-theme',d?'light':'dark');
 try{localStorage.setItem('cmmc-theme',d?'light':'dark')}catch(e){}
 document.getElementById('ttb').innerHTML=d?'\\u263E Dark':'\\u2600 Light';}
(function(){var t='light';try{t=localStorage.getItem('cmmc-theme')||'light'}catch(e){}
 document.documentElement.setAttribute('data-theme',t);
 window.addEventListener('DOMContentLoaded',function(){
   var b=document.getElementById('ttb');if(b)b.innerHTML=(t==='dark')?'\\u2600 Light':'\\u263E Dark';});})();
</script>
"""

