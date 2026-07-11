cart_js = """

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
"""

import os
js_path = 'script.js'

with open(js_path, 'r', encoding='utf-8') as f:
    original_js = f.read()

# We insert this before the closing bracket of DOMContentLoaded if it exists.
# Let's just append it for now, but script.js has a DOMContentLoaded wrapper.
# So we inject it before the last '});'
last_brace_idx = original_js.rfind('});')
if last_brace_idx != -1:
    new_js = original_js[:last_brace_idx] + cart_js + original_js[last_brace_idx:]
else:
    new_js = original_js + cart_js

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(new_js)

print("Appended Cart JS to script.js")
