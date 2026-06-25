// Radhika Atolia — portfolio interactions

// year
document.querySelectorAll('#yr').forEach(el => el.textContent = new Date().getFullYear());

// mobile nav — full-screen overlay menu (built from existing nav links)
(function mobileMenu() {
  const header = document.querySelector('.nav');
  const toggle = document.getElementById('navToggle');
  if (!header || !toggle) return;
  const links = [...header.querySelectorAll('a:not(.nav__brand)')];
  const ov = document.createElement('div');
  ov.className = 'nav-overlay';
  ov.innerHTML = '<button class="nav-overlay__close" aria-label="Close menu">&times;</button>';
  const ul = document.createElement('ul'); ul.className = 'nav-overlay__list';
  links.forEach((a, i) => {
    const li = document.createElement('li');
    const na = a.cloneNode(true); na.style.setProperty('--i', i);
    li.appendChild(na); ul.appendChild(li);
  });
  ov.appendChild(ul); document.body.appendChild(ov);
  const open = () => { ov.classList.add('open'); document.body.style.overflow = 'hidden'; };
  const close = () => { ov.classList.remove('open'); document.body.style.overflow = ''; };
  toggle.addEventListener('click', open);
  ov.querySelector('.nav-overlay__close').addEventListener('click', close);
  ul.addEventListener('click', e => { if (e.target.tagName === 'A') close(); });
  addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
})();

// scroll reveal
const io = new IntersectionObserver((entries) => {
  entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach((el, i) => {
  el.style.transitionDelay = (i % 3) * 70 + 'ms';
  io.observe(el);
});

// contact form (demo)
const form = document.getElementById('contactForm');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    const btn = form.querySelector('button');
    const orig = btn.textContent;
    btn.textContent = 'Thanks! ✓'; btn.style.background = '#1B6B6F'; btn.style.color = '#fff';
    form.reset();
    setTimeout(() => { btn.textContent = orig; btn.style.background = ''; btn.style.color = ''; }, 2600);
  });
}

// ---------- universe marquee: auto-scroll + manual swipe ----------
(function marquee() {
  const box = document.getElementById('universeMarquee');
  const track = box && box.querySelector('.marquee__track');
  if (!box || !track) return;
  track.innerHTML += track.innerHTML;            // duplicate → seamless half-loop
  let paused = false, half = 0;
  const measure = () => { half = track.scrollWidth / 2; };
  measure(); addEventListener('resize', measure);
  // pause while the user is interacting
  ['mouseenter','touchstart','pointerdown'].forEach(e => box.addEventListener(e, () => paused = true, {passive:true}));
  ['mouseleave','touchend','pointerup'].forEach(e => box.addEventListener(e, () => paused = false, {passive:true}));
  const SPEED = 0.5;                              // px/frame
  (function tick() {
    if (!paused && half) {
      box.scrollLeft += SPEED;
      if (box.scrollLeft >= half) box.scrollLeft -= half;   // wrap seamlessly
    }
    requestAnimationFrame(tick);
  })();
})();

// ---------- 3D tilt on cards ----------
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    const dx = (e.clientX - r.left) / r.width - 0.5;
    const dy = (e.clientY - r.top) / r.height - 0.5;
    card.style.transform = `rotateX(${(-dy*7).toFixed(2)}deg) rotateY(${(dx*7).toFixed(2)}deg) translateY(-4px)`;
  });
  card.addEventListener('mouseleave', () => { card.style.transform = ''; });
});

// ---------- 3D tilt on contact panel ----------
(function contactTilt() {
  const panel = document.getElementById('contactPanel');
  if (!panel || window.matchMedia('(hover: none)').matches) return;
  panel.style.perspective = '1200px';
  panel.addEventListener('mousemove', e => {
    const r = panel.getBoundingClientRect();
    const dx = (e.clientX - r.left) / r.width - 0.5;
    const dy = (e.clientY - r.top) / r.height - 0.5;
    panel.style.transform = `rotateX(${(-dy*4).toFixed(2)}deg) rotateY(${(dx*4).toFixed(2)}deg)`;
  });
  panel.addEventListener('mouseleave', () => { panel.style.transform = ''; });
})();

// ---------- generic 3D tilt (.tilt3d) ----------
if (!window.matchMedia('(hover: none)').matches) {
  document.querySelectorAll('.tilt3d').forEach(el => {
    el.addEventListener('mousemove', e => {
      const r = el.getBoundingClientRect();
      const dx = (e.clientX - r.left) / r.width - 0.5;
      const dy = (e.clientY - r.top) / r.height - 0.5;
      el.style.transform = `rotateX(${(-dy*10).toFixed(2)}deg) rotateY(${(dx*12).toFixed(2)}deg)`;
    });
    el.addEventListener('mouseleave', () => { el.style.transform = ''; });
  });
}

// ---------- hero sticker depth-parallax ----------
(function parallax() {
  const panel = document.querySelector('.hero__panel');
  if (!panel || window.matchMedia('(hover: none)').matches) return;
  const stickers = [...panel.querySelectorAll('.sticker')];
  panel.addEventListener('mousemove', e => {
    const r = panel.getBoundingClientRect();
    const dx = (e.clientX - r.left) / r.width - 0.5;
    const dy = (e.clientY - r.top) / r.height - 0.5;
    stickers.forEach((s, i) => {
      const depth = ((i % 3) + 1) * 8;            // 8/16/24px layers
      s.querySelector('svg').style.setProperty('--px', (dx * depth).toFixed(1) + 'px');
      s.querySelector('svg').style.setProperty('--py', (dy * depth).toFixed(1) + 'px');
    });
  });
  panel.addEventListener('mouseleave', () => {
    stickers.forEach(s => { const v = s.querySelector('svg'); v.style.setProperty('--px','0px'); v.style.setProperty('--py','0px'); });
  });
})();

// ---------- cutting-mat ruler numbers ----------
(function ruler() {
  const panel = document.querySelector('.hero__panel');
  if (!panel) return;
  const CELL = 38;
  function build() {
    panel.querySelectorAll('.ruler-x,.ruler-y').forEach(n => n.remove());
    const cols = Math.floor(panel.clientWidth / CELL);
    const rows = Math.floor(panel.clientHeight / CELL);
    const rx = document.createElement('div'); rx.className = 'ruler-x';
    for (let i = 0; i <= cols; i++) { const s = document.createElement('span'); s.textContent = i; rx.appendChild(s); }
    const ry = document.createElement('div'); ry.className = 'ruler-y';
    for (let i = 0; i <= rows; i++) { const s = document.createElement('span'); s.textContent = i; ry.appendChild(s); }
    panel.append(rx, ry);
  }
  build();
  let t; addEventListener('resize', () => { clearTimeout(t); t = setTimeout(build, 200); });
})();

// ---------- custom cursor (dot + magnifying ring) ----------
(function customCursor() {
  if (window.matchMedia('(hover: none)').matches) return; // skip touch
  const dot = document.createElement('div'); dot.className = 'cursor-dot';
  const ring = document.createElement('div'); ring.className = 'cursor-ring';
  document.body.append(dot, ring);
  document.documentElement.classList.add('has-cursor');

  let mx = innerWidth / 2, my = innerHeight / 2;   // mouse
  let rx = mx, ry = my;                             // ring (lagged)
  addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%,-50%)`;
  });

  (function loop() {
    rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18;
    ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%,-50%)`;
    requestAnimationFrame(loop);
  })();

  const hot = 'a, button, summary, input, textarea, .card, .sticker, .ability, .quest';
  addEventListener('mouseover', e => { if (e.target.closest(hot)) ring.classList.add('big'); });
  addEventListener('mouseout',  e => { if (e.target.closest(hot)) ring.classList.remove('big'); });
  addEventListener('mousedown', () => ring.classList.add('down'));
  addEventListener('mouseup',   () => ring.classList.remove('down'));
})();
