(() => {
  'use strict';
  const key = 'cst-handbook-018-read';
  let read = [];
  try { const stored = JSON.parse(localStorage.getItem(key) || '[]'); if (Array.isArray(stored)) read = stored.filter(v => typeof v === 'string'); } catch (_) {}
  const lessonLinks = Array.from(document.querySelectorAll('[data-lesson]'));
  const validLessons = new Set(lessonLinks.map(el => el.dataset.lesson));
  read = Array.from(new Set(read)).filter(id => validLessons.has(id));
  function updateProgress() {
    const count = document.getElementById('progress-count');
    if (count) count.textContent = read.length + ' of 17';
    const progress = document.getElementById('progress');
    if (progress) progress.value = read.length;
    lessonLinks.forEach(el => { el.querySelector('.lesson-check').textContent = read.includes(el.dataset.lesson) ? '✓' : ''; });
    document.querySelectorAll('[data-complete]').forEach(button => {
      const done = read.includes(button.dataset.complete);
      button.setAttribute('aria-pressed', String(done));
      button.textContent = done ? 'Read · mark as unread' : 'Mark lesson as read';
    });
  }
  function saveProgress() { try { localStorage.setItem(key, JSON.stringify(read)); } catch (_) {} updateProgress(); }
  document.querySelectorAll('[data-complete]').forEach(button => button.addEventListener('click', () => {
    const id = button.dataset.complete;
    read = read.includes(id) ? read.filter(x => x !== id) : read.concat(id);
    saveProgress();
  }));
  document.getElementById('reset-progress')?.addEventListener('click', () => {
    if (window.confirm('Clear the lessons marked read in this browser?')) { read = []; saveProgress(); }
  });
  updateProgress();

  const menu = document.querySelector('.menu-button');
  const sidebar = document.getElementById('sidebar');
  function closeMenu() { sidebar.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); }
  menu.addEventListener('click', () => {
    const open = sidebar.classList.toggle('open');
    menu.setAttribute('aria-expanded', String(open));
    if (open) document.getElementById('search').focus();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && sidebar.classList.contains('open')) { closeMenu(); menu.focus(); }
  });
  document.addEventListener('click', event => {
    if (sidebar.classList.contains('open') && !sidebar.contains(event.target) && !menu.contains(event.target)) closeMenu();
  });
  window.matchMedia('(min-width:901px)').addEventListener('change', event => { if (event.matches) closeMenu(); });

  const search = document.getElementById('search');
  const results = document.getElementById('search-results');
  const status = document.getElementById('search-status');
  let searchIndex;
  let searchPromise;
  let request = 0;
  async function searchLessons() {
    const query = search.value.trim().toLowerCase();
    const current = ++request;
    results.replaceChildren();
    results.hidden = !query;
    if (!query) { status.textContent = ''; return; }
    try {
      if (!searchPromise) searchPromise = fetch('search-index.json').then(response => {
        if (!response.ok) throw new Error('Search index unavailable');
        return response.json();
      }).catch(error => { searchPromise = null; throw error; });
      searchIndex = await searchPromise;
      if (current !== request) return;
      const terms = query.split(/\s+/).filter(Boolean);
      const matches = searchIndex.filter(item => terms.every(term => (item.title + ' ' + item.text).toLowerCase().includes(term)))
        .sort((a, b) => Number(b.title.toLowerCase().includes(query)) - Number(a.title.toLowerCase().includes(query))).slice(0, 8);
      status.textContent = matches.length + ' matching lessons';
      if (!matches.length) {
        const empty = document.createElement('p'); empty.className = 'search-empty';
        empty.textContent = 'No matching lesson. Try “LED”, “notes”, “pairing” or “print”.'; results.append(empty);
      }
      matches.forEach(item => {
        const link = document.createElement('a'); link.className = 'search-result'; link.href = item.url;
        const title = document.createElement('strong'); title.textContent = item.number + ' · ' + item.title;
        const excerpt = document.createElement('small'); excerpt.textContent = item.summary;
        link.append(title, excerpt); results.append(link);
      });
    } catch (_) {
      if (current !== request) return;
      const note = document.createElement('p'); note.className = 'search-empty';
      note.textContent = 'Search is unavailable. Use the lesson list or your browser’s Find command.'; results.append(note);
      status.textContent = note.textContent;
    }
  }
  search.addEventListener('input', searchLessons);

  const dialog = document.getElementById('image-dialog');
  let imageOpener;
  document.querySelectorAll('.zoom-image').forEach(link => link.addEventListener('click', event => {
    if (typeof dialog.showModal !== 'function') return;
    event.preventDefault();
    imageOpener = link;
    const source = link.querySelector('img');
    const target = dialog.querySelector('img');
    target.src = source.src; target.alt = source.alt;
    dialog.querySelector('p').textContent = source.alt;
    dialog.showModal();
  }));
  dialog.querySelector('.close-dialog').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => { imageOpener?.focus(); });
  document.getElementById('print-guide')?.addEventListener('click', () => window.print());

  const quiz = document.getElementById('knowledge-quiz');
  quiz?.addEventListener('submit', event => {
    event.preventDefault();
    const answers = new FormData(quiz);
    const expected = {q1: 'continue', q2: 'host', q3: 'seen'};
    const score = Object.entries(expected).filter(([id, value]) => answers.get(id) === value).length;
    document.getElementById('quiz-result').textContent = score + ' of 3 correct. ' + (score === 3 ?
      'Well understood. Now practise the workflow on the simulator with your trainer.' :
      'Remember: Blank only hides output; control returns to the host; Seen needs the recipient’s tap. Review your answers and try again.');
  });
})();
