const root = document.documentElement;
const languageButtons = Array.from(document.querySelectorAll('[data-set-lang]'));
const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');

const pageMeta = {
  zh: {
    title: '王亦琳 | AI 产品、研究与设计',
    description: '王亦琳的个人主页：AI 产品、行业研究、数据分析与环境设计作品集。',
    htmlLang: 'zh-CN'
  },
  en: {
    title: 'Yilin Wang | AI Product, Research & Design',
    description: 'Yilin Wang works across AI product, strategy, data analysis, and environmental design.',
    htmlLang: 'en'
  }
};

function setLanguage(language, persist = true) {
  const next = language === 'en' ? 'en' : 'zh';
  const meta = pageMeta[next];
  root.dataset.lang = next;
  root.lang = meta.htmlLang;
  document.title = meta.title;
  document.querySelector('meta[name="description"]')?.setAttribute('content', meta.description);
  languageButtons.forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.setLang === next));
  });
  if (persist) localStorage.setItem('yilin-site-language', next);
}

languageButtons.forEach((button) => {
  button.addEventListener('click', () => setLanguage(button.dataset.setLang));
});

const savedLanguage = localStorage.getItem('yilin-site-language');
if (savedLanguage) setLanguage(savedLanguage, false);

navToggle?.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  navToggle.setAttribute('aria-expanded', String(open));
});

nav?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    nav.classList.remove('is-open');
    navToggle?.setAttribute('aria-expanded', 'false');
  });
});

const revealItems = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add('is-visible'));
}

document.getElementById('year').textContent = String(new Date().getFullYear());
