/* ── Nav: adiciona classe 'scrolled' ao rolar ──────────────────── */
const nav = document.querySelector('.nav');
window.addEventListener('scroll', () => {
  nav.style.background = window.scrollY > 40
    ? 'rgba(4,8,16,0.96)'
    : 'rgba(4,8,16,0.82)';
});

/* ── Animação de entrada via IntersectionObserver ──────────────── */
// Adiciona data-animate nos elementos que devem animar
const targets = document.querySelectorAll(
  '.skill-group, .project-card, .timeline__item, .section__header'
);

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity  = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

targets.forEach(el => {
  el.style.opacity   = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});

/* ── Highlight do link de nav conforme a seção visível ─────────── */
const sections = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav__links a[href^="#"]');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.style.color = link.getAttribute('href') === `#${entry.target.id}`
          ? 'var(--cyan)'
          : '';
      });
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => sectionObserver.observe(s));
