cart_css = """

/* Add to Cart Button on Products */
.btn-add-to-cart {
    position: absolute;
    bottom: 1rem;
    right: 1rem;
    width: 45px;
    height: 45px;
    background-color: var(--color-surface);
    color: var(--color-text-dark);
    border: none;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
    z-index: 10;
    box-shadow: var(--shadow-sm);
}

.product-card:hover .btn-add-to-cart,
.bento-item:hover .btn-add-to-cart {
    opacity: 1;
    transform: translateY(0);
}

.btn-add-to-cart:hover {
    background-color: var(--color-text-dark);
    color: white;
}

.btn-add-to-cart.added {
    background-color: var(--color-primary);
    color: white;
}

/* Cart Sidebar (Offcanvas) */
.cart-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0,0,0,0.4);
    z-index: 3000;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease;
}

.cart-overlay.active {
    opacity: 1;
    visibility: visible;
}

.cart-sidebar {
    position: fixed;
    top: 0;
    right: -400px; /* Hidden initially */
    width: 100%;
    max-width: 400px;
    height: 100vh;
    background-color: var(--color-surface);
    z-index: 3100;
    box-shadow: -5px 0 15px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    transition: right 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.cart-sidebar.active {
    right: 0;
}

.cart-header {
    padding: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--color-border);
}

.cart-header h3 {
    font-family: var(--font-heading);
    font-size: 1.5rem;
}

.cart-close {
    background: none;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    color: var(--color-text-light);
    transition: color 0.3s ease;
}

.cart-close:hover {
    color: var(--color-text-dark);
}

.cart-items {
    flex: 1;
    overflow-y: auto;
    padding: 1.5rem;
}

.empty-cart-msg {
    text-align: center;
    color: var(--color-text-light);
    margin-top: 2rem;
    font-size: 1rem;
}

.cart-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--color-border);
}

.cart-item-img {
    width: 70px;
    height: 70px;
    border-radius: var(--radius-sm);
    object-fit: cover;
    background-color: var(--color-bg);
}

.cart-item-details {
    flex: 1;
}

.cart-item-title {
    font-family: var(--font-heading);
    font-size: 1rem;
    margin-bottom: 0.25rem;
}

.cart-item-price {
    font-family: var(--font-body);
    font-weight: 600;
    color: var(--color-text-light);
    font-size: 0.9rem;
}

.cart-item-remove {
    background: none;
    border: none;
    color: var(--color-text-light);
    font-size: 0.8rem;
    cursor: pointer;
    text-decoration: underline;
    margin-top: 0.5rem;
}

.cart-footer {
    padding: 1.5rem;
    border-top: 1px solid var(--color-border);
    background-color: var(--color-surface);
}

.cart-total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: var(--font-heading);
    font-size: 1.25rem;
    margin-bottom: 1rem;
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(cart_css)

print("Appended CSS to styles.css")
