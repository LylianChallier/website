document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('main > *');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1
  });

  sections.forEach(section => {
    section.classList.add('fade-out'); // cache au départ
    observer.observe(section);
  });
});

window.addEventListener('load', () => {
  const headerTitle = document.querySelector('header h1');
  headerTitle.style.transition = 'transform 0.6s ease, opacity 0.6s ease';
  headerTitle.style.transform = 'scale(1.1)';
  headerTitle.style.opacity = '1';

  setTimeout(() => {
    headerTitle.style.transform = 'scale(1)';
  }, 600);
});

window.addEventListener('DOMContentLoaded', () => {
  const badges = document.querySelectorAll('.badges img');
  badges.forEach((img, index) => {
    img.style.setProperty('--delay', `${index * 0.15}s`);
  });
});
