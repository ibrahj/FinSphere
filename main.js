document.addEventListener('DOMContentLoaded', () => {
  const nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 50);
    });
  }

  const toggle = document.querySelector('.nav-mobile-toggle');
  const menu   = document.querySelector('.mobile-menu');
  const close  = document.querySelector('.mobile-menu-close');
  if (toggle && menu) toggle.addEventListener('click', () => menu.classList.add('open'));
  if (close  && menu) close.addEventListener('click',  () => menu.classList.remove('open'));
  document.querySelectorAll('.mobile-menu a').forEach(l => l.addEventListener('click', () => menu && menu.classList.remove('open')));

  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  const form = document.querySelector('.inq-form');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const btn = form.querySelector('[type=submit]');
      const success = form.querySelector('.form-success');
      if (btn) btn.style.display = 'none';
      if (success) success.style.display = 'block';
    });
  }
});
