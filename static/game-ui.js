document.addEventListener("DOMContentLoaded", () => {

    // Initialize 3D Coverflow Carousel for Projects
    if (typeof Swiper !== 'undefined') {
        const swiper = new Swiper('.mySwiper', {
            effect: 'coverflow',
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            coverflowEffect: {
                rotate: 15,
                stretch: 0,
                depth: 300,
                modifier: 1,
                slideShadows: false, // Turn off default shadows to let our glassmorphism shine
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            initialSlide: 0,
            keyboard: {
                enabled: true,
            },
        });
    }

    // Initialize Typewriter for About Me section using IntersectionObserver
    const aboutSection = document.getElementById('about');
    const typewriterContainer = document.getElementById('typewriter-container');

    if (aboutSection && typewriterContainer && typeof Typewriter !== 'undefined') {
        // Save the original text and clear the container
        const textToType = typewriterContainer.textContent.trim().replace(/\s+/g, ' ');
        typewriterContainer.innerHTML = '';

        let typewriterInitialized = false;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !typewriterInitialized) {
                    typewriterInitialized = true;

                    const typewriter = new Typewriter(typewriterContainer, {
                        delay: 30, // typing speed
                        cursor: '█'
                    });

                    typewriter.typeString(textToType)
                        .start();
                }
            });
        }, { threshold: 0.4 });

        observer.observe(aboutSection);
    }
});
