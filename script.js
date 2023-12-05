window.addEventListener("load", function () {
  const preloader = document.querySelector(".preloader");
  const content = document.querySelector(".App");
  setTimeout(function () {
    preloader.classList.add("hide-preloader");
    content.style.display = "block"; // Show the webpage content after the preloader is hidden
  }, 0); // Replace 3000 with the number of milliseconds you want to delay before hiding the preloader
});


var typed = new Typed(".auto-type", {
  strings: ["Open Source Contributer", "Python Developer", "Web Developer"],
  typeSpeed: 40,
  backSpeed: 40,
  loop: true
})

window.addEventListener('DOMContentLoaded', function () {
  var navbar = document.querySelector('.navbar');

  window.addEventListener('scroll', function () {
    if (window.scrollY > 15) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
});