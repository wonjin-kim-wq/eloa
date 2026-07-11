document.addEventListener('DOMContentLoaded', () => {

    // Scroll Expansion Logic
    const scrollContainer = document.getElementById('scroll-hero-container');
    const media = document.getElementById('expanding-media');
    const bg = document.getElementById('scroll-hero-bg');
    const contentBottom = document.getElementById('hero-content-bottom');
    const titleLeft = document.getElementById('hero-title-left');
    const titleRight = document.getElementById('hero-title-right');

    window.addEventListener('scroll', () => {
        if (scrollContainer && media && titleLeft && titleRight) {
            // Calculate progress between 0 and 1
            const rect = scrollContainer.getBoundingClientRect();
            const startScroll = 0; // Starts at the very top
            const scrollDistance = window.innerHeight * 2; // Since container is 300vh, sticky takes 100vh, we scroll 200vh
            let progress = -rect.top / scrollDistance;
            progress = Math.min(Math.max(progress, 0), 1);

            // Expanding Media
            const isMobile = window.innerWidth < 768;
            const targetWidth = isMobile ? window.innerWidth * 0.95 : window.innerWidth * 0.95;
            const targetHeight = isMobile ? window.innerHeight * 0.8 : window.innerHeight * 0.85;
            
            const mediaWidth = 300 + progress * (targetWidth - 300);
            const mediaHeight = 400 + progress * (targetHeight - 400);
            
            media.style.width = `${mediaWidth}px`;
            media.style.height = `${mediaHeight}px`;

            // Splitting Text
            const textTranslateX = progress * (isMobile ? 180 : 150);
            titleLeft.style.transform = `translateX(-${textTranslateX}vw)`;
            titleRight.style.transform = `translateX(${textTranslateX}vw)`;

            // Fade background
            if (bg) bg.style.opacity = 1 - progress;

            // Show bottom content when fully expanded
            if (contentBottom) {
                contentBottom.style.opacity = progress > 0.8 ? (progress - 0.8) * 5 : 0;
            }
        }
    });

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

    // Search Inline Logic
    const searchBtn = document.getElementById('search-btn');
    const searchWrapper = document.getElementById('search-wrapper');
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');

    if (searchBtn && searchWrapper) {
        // Toggle search box
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            searchWrapper.classList.toggle('active');
            if (searchWrapper.classList.contains('active')) {
                setTimeout(() => searchInput.focus(), 100);
            }
        });

        // Close on click outside
        document.addEventListener('click', (e) => {
            if (!searchWrapper.contains(e.target)) {
                searchWrapper.classList.remove('active');
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && searchWrapper.classList.contains('active')) {
                searchWrapper.classList.remove('active');
                searchInput.value = '';
            }
        });

        // Search submit
        if (searchForm) {
            searchForm.addEventListener('submit', (e) => {
                e.preventDefault();
                const query = searchInput.value.trim();
                if (query) {
                    alert(`"${query}"에 대한 검색 결과 페이지로 이동합니다. (데모 기능입니다)`);
                    searchWrapper.classList.remove('active');
                    searchInput.value = '';
                }
            });
        }
    }

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


    // --- Shopping Cart Logic ---
    const cartOpenBtn = document.getElementById('cart-open-btn');
    const cartCloseBtn = document.getElementById('cart-close');
    const cartSidebar = document.getElementById('cart-sidebar');
    const cartOverlay = document.getElementById('cart-overlay');
    const cartBadge = document.getElementById('cart-badge-count');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalPrice = document.getElementById('cart-total-price');
    const addToCartBtns = document.querySelectorAll('.btn-add-to-cart');

    let cart = [];

    // Open Cart Sidebar
    function openCart() {
        cartSidebar.classList.add('active');
        cartOverlay.classList.add('active');
    }

    // Close Cart Sidebar
    function closeCart() {
        cartSidebar.classList.remove('active');
        cartOverlay.classList.remove('active');
    }

    if (cartOpenBtn) cartOpenBtn.addEventListener('click', openCart);
    if (cartCloseBtn) cartCloseBtn.addEventListener('click', closeCart);
    if (cartOverlay) cartOverlay.addEventListener('click', closeCart);

    // Render Cart
    function renderCart() {
        cartItemsContainer.innerHTML = '';
        let total = 0;

        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<div class="empty-cart-msg">장바구니가 비어 있습니다.</div>';
            cartBadge.innerText = '0';
            cartBadge.style.display = 'none';
            cartTotalPrice.innerText = '₩ 0';
            return;
        }

        cartBadge.innerText = cart.length;
        cartBadge.style.display = 'flex';

        cart.forEach((item, index) => {
            total += parseInt(item.price);

            const cartItemHTML = `
                <div class="cart-item">
                    <img src="${item.img}" alt="${item.name}" class="cart-item-img">
                    <div class="cart-item-details">
                        <h4 class="cart-item-title">${item.name}</h4>
                        <p class="cart-item-price">₩ ${parseInt(item.price).toLocaleString()}</p>
                        <button class="cart-item-remove" data-index="${index}">삭제</button>
                    </div>
                </div>
            `;
            cartItemsContainer.insertAdjacentHTML('beforeend', cartItemHTML);
        });

        cartTotalPrice.innerText = `₩ ${total.toLocaleString()}`;

        // Add event listeners to remove buttons
        document.querySelectorAll('.cart-item-remove').forEach(btn => {
            btn.addEventListener('click', function() {
                const idx = this.getAttribute('data-index');
                cart.splice(idx, 1);
                renderCart();
            });
        });
    }

    // Add to Cart Event
    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const card = this.closest('.product-card') || this.closest('.bento-item');
            if (card) {
                const name = card.getAttribute('data-name');
                const price = card.getAttribute('data-price');
                const img = card.getAttribute('data-img');

                cart.push({ name, price, img });
                
                // Button animation
                this.classList.add('added');
                setTimeout(() => {
                    this.classList.remove('added');
                }, 500);

                renderCart();
                openCart();
            }
        });
    });

    // Initialize Cart display
    renderCart();
});
