/* CMMC 5-Day Faculty Workshop: "Keep the case in view" bar for the Assessment Lab tools.
   Opens the Meridian Case Workbench (meridian.html) in one reusable side window, on the tab the tool needs.
   Each tool page sets <script src="case-window.js" data-tab="contracts"></script>. Light theme only.
   Not used on transfer-test.html: the transfer test is taken cold, without the Meridian material. */
(function () {
  'use strict';
  var me = document.currentScript;
  var DEFAULT_TAB = (me && me.getAttribute('data-tab')) || 'overview';
  var TABS = [
    ['overview', 'Overview'], ['contracts', 'Contracts'], ['org', 'Organization'], ['it', 'IT Environment'],
    ['posture', 'Security Posture'], ['personnel', 'Personnel & Training'], ['physical', 'Physical Security'],
    ['incidents', 'Incidents & Risks'], ['supply', 'Supply Chain'], ['audit', 'Audit Documents']
  ];
  var WIN_NAME = 'cmmc-meridian-case';

  var css = [
    '.cw-bar{display:flex;flex-wrap:wrap;align-items:center;gap:.6rem .8rem;background:#fdf3e3;border:1px solid #e3c48f;border-left:5px solid #c8862a;border-radius:6px;padding:.75rem 1rem;margin:0 0 1.25rem;font-family:Arial,sans-serif}',
    '.cw-label{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#12233a;margin-right:.2rem}',
    '.cw-bar select{font:.9rem Arial,sans-serif;color:#10202f;background:#fff;border:1.5px solid #7186a3;border-radius:6px;padding:.4rem .5rem;min-height:38px}',
    '.cw-btn{display:inline-flex;align-items:center;gap:.35rem;min-height:38px;padding:.45rem .9rem;border-radius:6px;border:1.5px solid #9a5b0b;background:#9a5b0b;color:#fff;font:700 .82rem Arial,sans-serif;cursor:pointer;text-decoration:none}',
    '.cw-btn:hover{background:#7c4708;border-color:#7c4708}',
    '.cw-btn.ghost{background:#fff;color:#9a5b0b}',
    '.cw-btn.ghost:hover{background:#fdf3e3}',
    '.cw-bar :focus-visible{outline:3px solid #c2410c;outline-offset:2px}',
    '.cw-msg{flex-basis:100%;font-size:.85rem;color:#10202f;margin:0}',
    '.cw-msg:empty{display:none}',
    '.cw-hint{flex-basis:100%;font-size:.8rem;color:#55697e;margin:0}',
    '@media print{.cw-bar{display:none}}'
  ].join('\n');

  function el(tag, attrs, text) {
    var n = document.createElement(tag);
    for (var k in attrs) if (Object.prototype.hasOwnProperty.call(attrs, k)) n.setAttribute(k, attrs[k]);
    if (text) n.textContent = text;
    return n;
  }

  function features() {
    // Place the window on the right half of the screen where the browser allows it.
    var sw = (window.screen && window.screen.availWidth) || 1280, sh = (window.screen && window.screen.availHeight) || 900;
    var w = Math.max(560, Math.min(920, Math.round(sw / 2))), h = Math.max(600, sh - 60);
    var left = Math.max(0, sw - w), top = 0;
    return 'width=' + w + ',height=' + h + ',left=' + left + ',top=' + top + ',resizable=yes,scrollbars=yes';
  }

  function build() {
    var main = document.querySelector('main') || document.body;
    var style = el('style'); style.textContent = css; document.head.appendChild(style);

    var bar = el('div', { 'class': 'cw-bar', role: 'group', 'aria-label': 'Keep the case in view' });
    bar.appendChild(el('span', { 'class': 'cw-label' }, 'Keep the case in view'));
    var lab = el('label', { 'for': 'cw-tab', 'class': 'cw-sr' }, 'Meridian section to open');
    lab.style.cssText = 'position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap';
    bar.appendChild(lab);
    var sel = el('select', { id: 'cw-tab' });
    TABS.forEach(function (t) { var o = el('option', { value: t[0] }, t[1]); if (t[0] === DEFAULT_TAB) o.selected = true; sel.appendChild(o); });
    bar.appendChild(sel);
    var openBtn = el('button', { type: 'button', 'class': 'cw-btn' }, 'Open the Meridian case in a new window ↗');
    bar.appendChild(openBtn);
    var tabLink = el('a', { href: 'meridian.html#' + DEFAULT_TAB, target: '_blank', rel: 'noopener', 'class': 'cw-btn ghost' }, 'Open in a new tab instead');
    bar.appendChild(tabLink);
    var msg = el('p', { 'class': 'cw-msg', role: 'status' });
    bar.appendChild(msg);
    bar.appendChild(el('p', { 'class': 'cw-hint' }, 'The case opens beside this tool. Choose another section here at any time; the same window updates. Your work in this tool is not affected.'));

    sel.addEventListener('change', function () { tabLink.setAttribute('href', 'meridian.html#' + sel.value); });
    openBtn.addEventListener('click', function () {
      var url = 'meridian.html#' + sel.value;
      var w = null;
      try { w = window.open(url, WIN_NAME, features()); } catch (e) { w = null; }
      if (!w) {
        msg.textContent = 'Your browser blocked the new window. Allow pop-ups for this page, or use "Open in a new tab instead."';
        return;
      }
      msg.textContent = '';
      try { w.focus(); } catch (e) { }
    });

    main.insertBefore(bar, main.firstChild);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
