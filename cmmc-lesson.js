/* CMMC 5-Day Faculty Workshop: shared lesson behavior (self-check quiz, flashcards). Light theme only. */

  /* Marks each option with a glyph and text, not color alone. The #score span is a polite live region. */
  function clearMarks() {
    document.querySelectorAll('#quiz .opt').forEach(o => o.classList.remove('correct', 'wrong'));
    document.querySelectorAll('#quiz .opt-mark').forEach(m => m.remove());
  }
  function mark(opt, kind, text) {
    if (!opt) return;
    opt.classList.add(kind);
    const s = document.createElement('span');
    s.className = 'opt-mark ' + kind;
    s.textContent = (kind === 'correct' ? '✓ ' : '✕ ') + text;
    (opt.querySelector(':scope > span') || opt).appendChild(s);
  }

  function gradeQuiz() {
    const questions = document.querySelectorAll('#quiz .q');
    const scoreEl = document.getElementById('score');
    const answeredCount = document.querySelectorAll('#quiz .q input:checked').length;
    if (!answeredCount) {
      if (scoreEl) scoreEl.textContent = 'Choose an answer for at least one question, then select Submit.';
      return;
    }
    clearMarks();
    let score = 0;
    questions.forEach(q => {
      const answer = q.dataset.answer;
      const right = q.querySelector('input[value="' + answer + '"]');
      const rightOpt = right ? right.closest('.opt') : null;
      const checked = q.querySelector('input:checked');
      if (checked) {
        if (checked.value === answer) { mark(checked.closest('.opt'), 'correct', 'Your answer: correct'); score++; }
        else { mark(checked.closest('.opt'), 'wrong', 'Your answer: not the best choice'); mark(rightOpt, 'correct', 'Best answer'); }
      } else {
        mark(rightOpt, 'correct', 'Best answer (you skipped this one)');
      }
      const r = q.querySelector('.rationale'); if (r) r.classList.add('show');
    });
    if (scoreEl) scoreEl.innerHTML = 'Self-check: <span>' + score + ' of ' + questions.length + '</span> best answers' +
      (answeredCount < questions.length ? ' &middot; ' + (questions.length - answeredCount) + ' skipped' : '') + '. Read each explanation below.';
    const kc = document.getElementById('knowledge-check');
    if (kc) {
      const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      kc.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    }
  }

  function resetQuiz() {
    const form = document.getElementById('quiz');
    if (!form) return;
    form.reset();
    clearMarks();
    document.querySelectorAll('#quiz .rationale').forEach(r => r.classList.remove('show'));
    const scoreEl = document.getElementById('score');
    if (scoreEl) scoreEl.textContent = '';
    const first = form.querySelector('input'); if (first) first.focus();
  }

  // Flip cards (button elements => Enter/Space handled natively)
  document.querySelectorAll('.flip-card').forEach(card => {
    card.addEventListener('click', () => {
      const flipped = card.classList.toggle('flipped');
      card.setAttribute('aria-pressed', flipped ? 'true' : 'false');
    });
  });
