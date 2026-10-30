/* Dolan & Co: theme toggle, mobile menu, badge eyes, copy email, contact form, blog filters. */
(function () {
  'use strict';

  var root = document.documentElement;
  function safeGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function safeSet(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* storage blocked */ } }

  /* External links open in a new tab */
  document.querySelectorAll('a[href^="http"]').forEach(function (a) {
    if (a.hostname && a.hostname !== location.hostname) {
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
    }
  });

  /* Theme toggle */
  var themeBtn = document.querySelector('[data-theme-toggle]');
  function currentTheme() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  function syncThemeBtn() {
    if (!themeBtn) return;
    var dark = currentTheme() === 'dark';
    themeBtn.setAttribute('aria-pressed', dark ? 'true' : 'false');
    themeBtn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    var meta = document.querySelectorAll('meta[name="theme-color"]');
    if (meta.length) { /* keep the media-specific tags, the browser picks one */ }
  }
  if (themeBtn) {
    syncThemeBtn();
    themeBtn.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      safeSet('dolan-theme', next);
      syncThemeBtn();
    });
  }

  /* Mobile menu */
  var menu = document.getElementById('menu');
  var openBtn = document.querySelector('[data-menu-open]');
  var closeBtn = document.querySelector('[data-menu-close]');
  if (menu && openBtn && closeBtn) {
    var lastFocus = null;
    function openMenu() {
      lastFocus = document.activeElement;
      menu.hidden = false;
      document.body.style.overflow = 'hidden';
      openBtn.setAttribute('aria-expanded', 'true');
      closeBtn.focus();
    }
    function closeMenu() {
      menu.hidden = true;
      document.body.style.overflow = '';
      openBtn.setAttribute('aria-expanded', 'false');
      if (lastFocus) lastFocus.focus();
    }
    openBtn.addEventListener('click', openMenu);
    closeBtn.addEventListener('click', closeMenu);
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) closeMenu(); });
    window.addEventListener('resize', function () { if (window.innerWidth > 960 && !menu.hidden) closeMenu(); });
  }

  /* Badge eyes follow the pointer */
  var eyes = document.querySelector('.eyes');
  if (eyes && !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) {
    var pupils = eyes.querySelectorAll('b');
    document.addEventListener('pointermove', function (e) {
      pupils.forEach(function (p) {
        var r = p.parentElement.getBoundingClientRect();
        var cx = r.left + r.width / 2, cy = r.top + r.height / 2;
        var dx = e.clientX - cx, dy = e.clientY - cy;
        var d = Math.hypot(dx, dy) || 1;
        var m = Math.min(4, d / 20);
        p.style.transform = 'translate(' + (dx / d * m).toFixed(2) + 'px,' + (dy / d * m * 1.2).toFixed(2) + 'px)';
      });
    }, { passive: true });
  }

  /* Copy email */
  var copyBtn = document.querySelector('[data-copy-email]');
  if (copyBtn) {
    var status = document.querySelector('[data-copy-status]');
    var email = copyBtn.getAttribute('data-copy-email');
    var original = copyBtn.textContent;
    function say(msg) {
      copyBtn.textContent = msg;
      if (status) status.textContent = msg;
      setTimeout(function () { copyBtn.textContent = original; if (status) status.textContent = ''; }, 2200);
    }
    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = email; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      say(ok ? 'Copied' : 'Press Ctrl C');
    }
    copyBtn.addEventListener('click', function () {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(function () { say('Copied'); }, fallback);
      } else { fallback(); }
    });
  }

  /* Contact form */
  var form = document.querySelector('[data-contact-form]');
  if (form) {
    var ok = document.querySelector('[data-form-ok]');
    var fail = document.querySelector('[data-form-fail]');
    var submit = form.querySelector('button[type="submit"]');
    var submitText = submit ? submit.querySelector('[data-label]') : null;
    var idle = submitText ? submitText.textContent : '';

    function setError(input, msg) {
      var holder = input.closest('.field');
      var err = holder.querySelector('.field__error');
      if (msg) {
        if (!err) {
          err = document.createElement('span');
          err.className = 'field__error label';
          err.id = input.id + '-error';
          holder.appendChild(err);
        }
        err.textContent = msg;
        input.setAttribute('aria-invalid', 'true');
        input.setAttribute('aria-describedby', err.id);
      } else {
        if (err) err.remove();
        input.removeAttribute('aria-invalid');
        input.removeAttribute('aria-describedby');
      }
    }
    function validate() {
      var bad = null;
      form.querySelectorAll('.field__control').forEach(function (input) {
        var msg = '';
        var v = input.value.trim();
        if (input.required && !v) msg = 'I need this one.';
        else if (input.type === 'email' && v && v.indexOf('@') < 0) msg = 'That email address is missing an @.';
        setError(input, msg);
        if (msg && !bad) bad = input;
      });
      return bad;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (ok) ok.hidden = true;
      if (fail) fail.hidden = true;
      var bad = validate();
      if (bad) { bad.focus(); return; }
      if (submit) submit.disabled = true;
      if (submitText) submitText.textContent = 'One moment.';
      var url = form.getAttribute('action').replace('formsubmit.co/', 'formsubmit.co/ajax/');
      fetch(url, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) })
        .then(function (r) { if (!r.ok) throw new Error('bad'); return r.json(); })
        .then(function () {
          form.reset();
          if (ok) { ok.hidden = false; ok.focus(); }
        })
        .catch(function () {
          if (fail) { fail.hidden = false; fail.focus(); }
        })
        .then(function () {
          if (submit) submit.disabled = false;
          if (submitText) submitText.textContent = idle;
        });
    });
  }

  /* Blog archive: build filters from the posts that exist */
  var list = document.querySelector('[data-posts]');
  if (list) {
    var posts = Array.prototype.slice.call(list.querySelectorAll('[data-category]'));
    var filters = document.querySelector('[data-filters]');
    var empty = document.querySelector('[data-empty]');
    function count(cat) {
      return posts.filter(function (p) { return cat === 'all' || p.getAttribute('data-category') === cat; }).length;
    }
    function apply(cat) {
      posts.forEach(function (p) { p.hidden = !(cat === 'all' || p.getAttribute('data-category') === cat); });
      if (filters) filters.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', b.getAttribute('data-filter') === cat ? 'true' : 'false');
      });
    }
    if (posts.length) {
      if (empty) empty.hidden = true;
      if (filters) {
        var cats = [];
        posts.forEach(function (p) { var c = p.getAttribute('data-category'); if (c && cats.indexOf(c) < 0) cats.push(c); });
        filters.innerHTML = '';
        ['all'].concat(cats).forEach(function (c) {
          var b = document.createElement('button');
          b.type = 'button';
          b.setAttribute('data-filter', c);
          b.setAttribute('aria-pressed', c === 'all' ? 'true' : 'false');
          b.innerHTML = (c === 'all' ? 'explore all' : c) + '<sup>' + count(c) + '</sup>';
          b.addEventListener('click', function () { apply(c); });
          filters.appendChild(b);
        });
      }
    }
  }
})();
