document.addEventListener('DOMContentLoaded', () => {
    // Random Bible Verse Logic
    const verses = [
        { text: "Love never", highlight: "fails.", reference: "- 1 Corinthians 13:8 -" },
        { text: "Done in", highlight: "love.", reference: "- 1 Corinthians 16:14 -" },
        { text: "Strong and", highlight: "courageous.", reference: "- Joshua 1:9 -" },
        { text: "He first", highlight: "loved us.", reference: "- 1 John 4:19 -" },
        { text: "Faith, hope,", highlight: "and love.", reference: "- 1 Corinthians 13:13 -" }
    ];
    
    const randomVerse = verses[Math.floor(Math.random() * verses.length)];
    const heroTitle = document.getElementById('hero-title');
    const heroSubtitle = document.getElementById('hero-subtitle');
    
    if (heroTitle && heroSubtitle) {
        heroTitle.innerHTML = `
            <span class="hero-title-line">${randomVerse.text}</span>
            <span class="hero-title-line highlight-text">${randomVerse.highlight}</span>
        `;
        heroSubtitle.textContent = randomVerse.reference;
    }

    const navbar = document.getElementById('navbar');
    
    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.add('scrolled');
            navbar.classList.remove('scrolled');
            if (window.scrollY <= 50) {
                 navbar.classList.remove('scrolled');
            }
        }
    });

    // Wishlist Button Interaction
    const wishlistBtns = document.querySelectorAll('.btn-wishlist');
    wishlistBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const icon = this.querySelector('svg');
            
            // Simple toggle for demonstration
            if (this.classList.contains('active')) {
                this.classList.remove('active');
                icon.style.fill = 'none';
                icon.style.stroke = 'currentColor';
            } else {
                this.classList.add('active');
                icon.style.fill = 'var(--color-primary)';
                icon.style.stroke = 'var(--color-primary)';
                
                // Pop animation
                this.style.transform = 'scale(1.2)';
                setTimeout(() => {
                    this.style.transform = '';
                }, 200);
            }
        });
    });

    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Apply initial styles and observe product cards
    const cards = document.querySelectorAll('.product-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });
});
