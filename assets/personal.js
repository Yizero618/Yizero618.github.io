document.querySelectorAll('.mobile-menu nav a').forEach((link) => {
  link.addEventListener('click', () => link.closest('details').removeAttribute('open'));
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  const menu = document.querySelector('.mobile-menu[open]');
  if (menu) {
    menu.removeAttribute('open');
    menu.querySelector('summary').focus();
  }
});
document.querySelector('[data-print-resume]')?.addEventListener('click', () => window.print());
