import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the old cart array initialization with localStorage logic
# And update the renderCart and AddToCart functions

new_cart_js = """
    // --- Shopping Cart Logic (Local Storage) ---
    const cartOpenBtn = document.getElementById('cart-open-btn');
    const cartCloseBtn = document.getElementById('cart-close');
    const cartSidebar = document.getElementById('cart-sidebar');
    const cartOverlay = document.getElementById('cart-overlay');
    const cartBadge = document.getElementById('cart-badge-count');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalPrice = document.getElementById('cart-total-price');
    const addToCartBtns = document.querySelectorAll('.btn-add-to-cart');

    // Initialize cart from LocalStorage
    let cart = JSON.parse(localStorage.getItem('eloa_cart')) || [];

    // Save cart to LocalStorage
    function saveCart() {
        localStorage.setItem('eloa_cart', JSON.stringify(cart));
    }

    // Open Cart Sidebar
    function openCart() {
        if(cartSidebar && cartOverlay) {
            cartSidebar.classList.add('active');
            cartOverlay.classList.add('active');
        }
    }

    // Close Cart Sidebar
    function closeCart() {
        if(cartSidebar && cartOverlay) {
            cartSidebar.classList.remove('active');
            cartOverlay.classList.remove('active');
        }
    }

    if (cartOpenBtn) cartOpenBtn.addEventListener('click', openCart);
    if (cartCloseBtn) cartCloseBtn.addEventListener('click', closeCart);
    if (cartOverlay) cartOverlay.addEventListener('click', closeCart);

    // Render Cart
    function renderCart() {
        if(!cartItemsContainer) return;

        cartItemsContainer.innerHTML = '';
        let total = 0;

        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<div class="empty-cart-msg">장바구니가 비어 있습니다.</div>';
            if(cartBadge) {
                cartBadge.innerText = '0';
                cartBadge.style.display = 'none';
            }
            if(cartTotalPrice) cartTotalPrice.innerText = '₩ 0';
            return;
        }

        if(cartBadge) {
            cartBadge.innerText = cart.length;
            cartBadge.style.display = 'flex';
        }

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

        if(cartTotalPrice) cartTotalPrice.innerText = `₩ ${total.toLocaleString()}`;

        // Add event listeners to remove buttons
        document.querySelectorAll('.cart-item-remove').forEach(btn => {
            btn.addEventListener('click', function() {
                const idx = this.getAttribute('data-index');
                cart.splice(idx, 1);
                saveCart();
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
                saveCart();
                
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
"""

# Find the start of the cart logic
start_idx = js.find('// --- Shopping Cart Logic ---')
if start_idx != -1:
    new_js = js[:start_idx] + new_cart_js
    # Ensure it's before the final '});' if it existed after it.
    if new_js.count('});') < js.count('});'):
        new_js += '\n});\n'
else:
    new_js = js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

print("Updated script.js with localStorage logic.")
