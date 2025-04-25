document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            navbar.style.background = "rgba(0, 0, 0, 0.9)";
            navbar.style.transition = "all 0.3s ease-in-out";
        } else {
            navbar.style.background = "rgba(0, 0, 0, 0.6)";
        }
    });

    AOS.init({
        duration: 1200,
        easing: "ease-in-out",
        once: true,
    });
});
