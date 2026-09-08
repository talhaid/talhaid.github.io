// Shared site behaviour: mobile menu.
// Kept in one external file so the pages can run under a strict
// Content-Security-Policy (script-src 'self') with no inline scripts.

document.addEventListener('DOMContentLoaded', function () {
  // Mobile slide-in menu
  const menu = document.getElementById('mobile-menu');
  const openBtn = document.getElementById('hamburger-btn');
  const closeBtn = document.getElementById('menu-close-btn');

  if (menu && openBtn && closeBtn) {
    const toggleMenu = function () {
      if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
        setTimeout(function () {
          menu.classList.remove('translate-x-full');
        }, 10);
      } else {
        menu.classList.add('translate-x-full');
        setTimeout(function () {
          menu.classList.add('hidden');
        }, 300);
      }
    };

    openBtn.addEventListener('click', toggleMenu);
    closeBtn.addEventListener('click', toggleMenu);

    // Close the menu when a link inside it is followed
    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', toggleMenu);
    });
  }
});
