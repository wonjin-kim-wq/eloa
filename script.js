document.addEventListener('DOMContentLoaded', () => {
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
