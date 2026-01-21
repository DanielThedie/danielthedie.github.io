document.addEventListener('DOMContentLoaded', function() {
  const burger = document.getElementById('menuBurger');
  const menu = document.getElementById('menuList');
  burger.addEventListener('click', () => {
    menu.classList.toggle('menu-open');
  });
  burger.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      menu.classList.toggle('menu-open');
    }
  });

  document.addEventListener('click', function(event) {
    if (
      menu.classList.contains('menu-open') &&
      !menu.contains(event.target) &&
      !burger.contains(event.target)
    ) {
      menu.classList.remove('menu-open');
    }
  });
});
