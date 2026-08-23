const root = document.documentElement;
const languageButtons = Array.from(document.querySelectorAll('[data-set-lang]'));
const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const pageMeta = {
  zh: {
    title: '王亦琳 | AI 产品、研究与设计',
    description: '王亦琳的个人作品集：AI 产品、行业研究、数据分析与环境设计。',
    socialDescription: '把复杂用户场景转化为可验证、可交付的产品。',
    htmlLang: 'zh-CN'
  },
  en: {
    title: 'Yilin Wang | AI Product, Research & Design',
    description: 'Yilin Wang works across AI product, strategy research, data analysis, and environmental design.',
    socialDescription: 'Turning complex user contexts into testable, deliverable products.',
    htmlLang: 'en'
  }
};

function setMeta(selector, value) {
  document.querySelector(selector)?.setAttribute('content', value);
}

function setLanguage(language, persist = true) {
  const next = language === 'en' ? 'en' : 'zh';
  const meta = pageMeta[next];
  root.dataset.lang = next;
  root.lang = meta.htmlLang;
  document.title = meta.title;
  setMeta('meta[name="description"]', meta.description);
  setMeta('meta[property="og:title"]', meta.title);
  setMeta('meta[property="og:description"]', meta.socialDescription);
  setMeta('meta[name="twitter:title"]', meta.title);
  setMeta('meta[name="twitter:description"]', meta.socialDescription);
  languageButtons.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.setLang === next)));
  if (persist) {
    try { localStorage.setItem('yilin-site-language', next); } catch (_) { /* storage can be unavailable */ }
  }
}

languageButtons.forEach((button) => button.addEventListener('click', () => setLanguage(button.dataset.setLang)));
try {
  const savedLanguage = localStorage.getItem('yilin-site-language');
  if (savedLanguage) setLanguage(savedLanguage, false);
} catch (_) { /* keep the default language */ }

function closeNavigation() {
  nav?.classList.remove('is-open');
  navToggle?.setAttribute('aria-expanded', 'false');
}

navToggle?.addEventListener('click', () => {
  const open = nav?.classList.toggle('is-open');
  navToggle.setAttribute('aria-expanded', String(Boolean(open)));
});
nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeNavigation));
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeNavigation();
});

const revealItems = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && !reducedMotion) {
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -6% 0px' });
  revealItems.forEach((item) => revealObserver.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add('is-visible'));
}

const progressBar = document.querySelector('.reading-progress span');
let progressFrame;
function updateProgress() {
  progressFrame = undefined;
  const available = document.documentElement.scrollHeight - window.innerHeight;
  const progress = available > 0 ? Math.min(1, Math.max(0, window.scrollY / available)) : 0;
  if (progressBar) progressBar.style.transform = `scaleX(${progress})`;
}
window.addEventListener('scroll', () => {
  if (!progressFrame) progressFrame = requestAnimationFrame(updateProgress);
}, { passive: true });
updateProgress();

const sectionLinks = Array.from(nav?.querySelectorAll('a[href^="#"]') || []);
const sections = sectionLinks.map((link) => document.querySelector(link.getAttribute('href'))).filter(Boolean);
if ('IntersectionObserver' in window && sections.length) {
  const sectionObserver = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    sectionLinks.forEach((link) => link.setAttribute('aria-current', String(link.getAttribute('href') === `#${visible.target.id}`)));
  }, { rootMargin: '-22% 0px -64% 0px', threshold: [0, .1, .3] });
  sections.forEach((section) => sectionObserver.observe(section));
}

const filterButtons = Array.from(document.querySelectorAll('[data-case-filter]'));
const caseStudies = Array.from(document.querySelectorAll('[data-case-category]'));
filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.caseFilter;
    filterButtons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    caseStudies.forEach((study) => {
      const matches = filter === 'all' || study.dataset.caseCategory === filter;
      study.hidden = !matches;
      if (matches && !reducedMotion) {
        study.classList.remove('is-filtering');
        requestAnimationFrame(() => study.classList.add('is-filtering'));
        window.setTimeout(() => study.classList.remove('is-filtering'), 380);
      }
    });
  });
});

if (!reducedMotion && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
  document.querySelectorAll('.tilt-card').forEach((card) => {
    card.addEventListener('pointermove', (event) => {
      const bounds = card.getBoundingClientRect();
      const x = (event.clientX - bounds.left) / bounds.width - .5;
      const y = (event.clientY - bounds.top) / bounds.height - .5;
      card.style.setProperty('--ry', `${(x * 4).toFixed(2)}deg`);
      card.style.setProperty('--rx', `${(-y * 4).toFixed(2)}deg`);
    });
    card.addEventListener('pointerleave', () => {
      card.style.setProperty('--ry', '0deg');
      card.style.setProperty('--rx', '0deg');
    });
  });
}

const year = document.getElementById('year');
if (year) year.textContent = String(new Date().getFullYear());
