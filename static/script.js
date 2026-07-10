// ================================
// AI Nutrition Analyzer
// script.js
// ================================

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});


// ================================
// Fade In Cards
// ================================

const cards = document.querySelectorAll(".card");

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.style.opacity = 1;
            entry.target.style.transform = "translateY(0px)";
        }

    });

});

cards.forEach(card => {

    card.style.opacity = 0;
    card.style.transform = "translateY(30px)";
    card.style.transition = "0.6s";

    observer.observe(card);

});


// ================================
// Animated Numbers
// ================================

function animateValue(element) {

    let target = Number(element.innerText);

    if (isNaN(target))
        return;

    let count = 0;

    let speed = target / 40;

    const timer = setInterval(() => {

        count += speed;

        if (count >= target) {

            count = target;
            clearInterval(timer);

        }

        element.innerText = Math.round(count);

    }, 20);

}

document.querySelectorAll(".card span").forEach(span => {

    animateValue(span);

});


// ================================
// Active Navbar
// ================================

const currentPage = window.location.pathname;

document.querySelectorAll(".nav-links a").forEach(link => {

    if (link.getAttribute("href") === currentPage) {

        link.style.color = "#38bdf8";
        link.style.fontWeight = "bold";

    }

});


// ================================
// Button Click Effect
// ================================

document.querySelectorAll("button").forEach(btn => {

    btn.addEventListener("click", () => {

        btn.style.transform = "scale(0.96)";

        setTimeout(() => {

            btn.style.transform = "scale(1)";

        }, 150);

    });

});


// ================================
// Welcome Message
// ================================

console.log("🥗 AI Nutrition Analyzer Loaded Successfully!");