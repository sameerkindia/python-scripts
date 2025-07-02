// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Add scroll effect to navbar
window.addEventListener("scroll", () => {
  const nav = document.querySelector("nav");
  if (window.scrollY > 100) {
    nav.style.background = "rgba(15, 20, 25, 0.95)";
  } else {
    nav.style.background = "rgba(15, 20, 25, 0.9)";
  }
});

// Form submission
// document
//   .querySelector(".contact-form")
//   .addEventListener("submit", function (e) {
//     e.preventDefault();
//     alert("Thank you for your message! I will get back to you soon.");
//     this.reset();
//   });

// Skill items animation on hover
document.querySelectorAll(".skill-item").forEach((item) => {
  item.addEventListener("mouseenter", function () {
    this.style.transform = "translateY(-10px) rotateY(5deg)";
  });

  item.addEventListener("mouseleave", function () {
    this.style.transform = "translateY(0) rotateY(0)";
  });
});

// Parallax effect for floating cards
window.addEventListener("scroll", () => {
  const scrolled = window.pageYOffset;
  const parallax = document.querySelectorAll(".floating-card");

  parallax.forEach((element) => {
    const speed = 0.5;
    element.style.transform = `translateY(${scrolled * speed}px)`;
  });
});
