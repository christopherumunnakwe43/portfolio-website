document.addEventListener("DOMContentLoaded", () => {
  // Typing effect for your name
  const nameElement = document.getElementById("typing-name");
  const nameText = "Christopher Umunnakwe";
  nameElement.textContent = "";
  
  let i = 0;
  function typeWriter() {
    if (i < nameText.length) {
      nameElement.textContent += nameText.charAt(i);
      i++;
      setTimeout(typeWriter, 100);
    }
  }
  typeWriter();

  // Fade in paragraphs with delay
  const fadeTexts = document.querySelectorAll(".fade-text");
  fadeTexts.forEach((el, index) => {
    el.style.animationDelay = `${1 + index * 0.3}s`;
  });

  // Smooth scroll for internal links
  document.querySelectorAll('.smooth-link').forEach(link => {
    link.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
});
