document.addEventListener("DOMContentLoaded", () => {


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
