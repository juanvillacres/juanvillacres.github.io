'use strict';
(() => {
  const root = document.documentElement;
  const theme = document.getElementById('theme-toggle');
  const media = matchMedia('(prefers-color-scheme: dark)');
  const effectiveTheme = () => root.dataset.theme || (media.matches ? 'dark' : 'light');
  if (theme) {
    const update = () => { const label = `Switch to ${effectiveTheme() === 'dark' ? 'light' : 'dark'} mode`; theme.setAttribute('aria-label', label); theme.title = label; };
    theme.hidden = false; update();
    theme.addEventListener('click', () => { const next = effectiveTheme() === 'dark' ? 'light' : 'dark'; root.dataset.theme = next; try { localStorage.setItem('jv-theme', next); } catch (_) {} update(); });
    if (media.addEventListener) media.addEventListener('change', update);
  }
  const nav = document.getElementById('site-nav'), menu = document.getElementById('menu-toggle');
  if (nav && menu) {
    menu.hidden = false;
    const setOpen = open => { nav.classList.toggle('open', open); menu.setAttribute('aria-expanded', String(open)); menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation'); };
    menu.addEventListener('click', () => setOpen(menu.getAttribute('aria-expanded') !== 'true'));
    nav.addEventListener('click', e => { if (e.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { setOpen(false); menu.focus(); } });
    matchMedia('(min-width: 1000px)').addEventListener('change', () => setOpen(false));
  }
  const filters = document.getElementById('publication-filters');
  if (filters) {
    const search = document.getElementById('pub-search'), year = document.getElementById('pub-year'), type = document.getElementById('pub-type'), topic = document.getElementById('pub-topic');
    const items = [...document.querySelectorAll('#publication-list .publication')];
    const count = document.getElementById('publication-count'), empty = document.getElementById('pub-empty');
    const normalize = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    const apply = () => { const q = normalize(search.value.trim()); let shown = 0; items.forEach(item => { const visible = (!q || normalize(item.textContent).includes(q)) && (!year.value || item.dataset.year === year.value) && (!type.value || item.dataset.type === type.value) && (!topic.value || item.dataset.topic === topic.value); item.hidden = !visible; if (visible) shown++; }); document.querySelectorAll('.publication-group').forEach(group => { group.hidden = !group.querySelector('.publication:not([hidden])'); }); count.textContent = `${shown} of ${items.length} publications`; empty.hidden = shown !== 0; };
    const requested = new URLSearchParams(location.search).get('topic');
    if (requested && [...topic.options].some(o => o.value === requested)) topic.value = requested;
    filters.hidden = false; search.addEventListener('input', apply); [year,type,topic].forEach(el => el.addEventListener('change', apply));
    document.getElementById('pub-reset').addEventListener('click', () => { [search,year,type,topic].forEach(el => el.value = ''); apply(); }); apply();
  }
  if (navigator.clipboard && window.isSecureContext) {
    document.querySelectorAll('.copy-citation').forEach(button => { button.hidden = false; button.addEventListener('click', async () => { const status = document.getElementById('copy-status'); try { await navigator.clipboard.writeText(button.dataset.citation); button.textContent = 'Copied'; if (status) status.textContent = 'Citation copied.'; setTimeout(() => button.textContent = 'Copy citation', 1500); } catch (_) { if (status) status.textContent = 'Copy failed. Select the citation text manually.'; button.textContent = 'Copy failed'; setTimeout(() => button.textContent = 'Copy citation', 1500); } }); });
  }
})();
