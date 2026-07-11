import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Cart Button in Header
html = html.replace('<button aria-label="Cart" class="icon-btn">', '<button aria-label="Cart" class="icon-btn" id="cart-open-btn">')
html = html.replace('<span class="cart-badge">2</span>', '<span class="cart-badge" id="cart-badge-count">0</span>')

# 2. Add add-to-cart icon SVG
cart_svg = '<button class="btn-add-to-cart" aria-label="Add to cart"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg></button>'

# 3. New NEW section
new_section = f'''
    <!-- NEW Section -->
    <section id="new" class="section new-section">
        <div class="section-header">
            <h2 class="section-title">Just Arrived</h2>
            <p class="section-desc">가장 먼저 만나는 ELOA의 새로운 감각</p>
        </div>
        <div class="product-grid new-grid">
            <article class="product-card" data-name="시그니처 퍼퓸 룸스프레이" data-price="24000" data-img="./assets/cat_diffuser_1.png">
                <div class="product-image-wrapper bg-yellow">
                    <img src="./assets/cat_diffuser_1.png" alt="룸스프레이" class="product-img" />
                    <span class="badge badge-new">NEW</span>
                    {cart_svg}
                </div>
                <div class="product-info">
                    <h3 class="product-name">시그니처 퍼퓸 룸스프레이</h3>
                    <p class="product-price">₩ 24,000</p>
                </div>
            </article>
            <article class="product-card" data-name="오가닉 바디워시" data-price="21000" data-img="./assets/cat_hair_1.png">
                <div class="product-image-wrapper bg-pink">
                    <img src="./assets/cat_hair_1.png" alt="바디워시" class="product-img" />
                    {cart_svg}
                </div>
                <div class="product-info">
                    <h3 class="product-name">오가닉 바디워시</h3>
                    <p class="product-price">₩ 21,000</p>
                </div>
            </article>
            <article class="product-card" data-name="프리미엄 린넨 샤쉐" data-price="12000" data-img="./assets/cat_living_2.png">
                <div class="product-image-wrapper bg-blue">
                    <img src="./assets/cat_living_2.png" alt="샤쉐" class="product-img" />
                    {cart_svg}
                </div>
                <div class="product-info">
                    <h3 class="product-name">프리미엄 린넨 샤쉐</h3>
                    <p class="product-price">₩ 12,000</p>
                </div>
            </article>
        </div>
    </section>
'''

# 4. New BEST section
best_section = f'''
    <!-- BEST Section -->
    <section id="best" class="section best-section">
        <div class="section-header">
            <h2 class="section-title">Our Signature</h2>
            <p class="section-desc">가장 많은 사랑을 받은 ELOA의 베스트셀러를 만나보세요.</p>
        </div>
        <div class="bento-grid">
            <article class="bento-item bento-large product-card" data-name="엘로아 선셋 디퓨저" data-price="32000" data-img="./assets/diffuser.png">
                <div class="ranking-badge badge-gold">1</div>
                <div class="product-image-wrapper bg-yellow">
                    <img src="./assets/diffuser.png" alt="엘로아 선셋 디퓨저" class="product-img" />
                    {cart_svg}
                </div>
                <div class="bento-info">
                    <h3 class="product-name">엘로아 선셋 디퓨저</h3>
                    <p class="product-price">₩ 32,000</p>
                </div>
            </article>
            <article class="bento-item bento-small product-card" data-name="보태니컬 실크 샴푸" data-price="28000" data-img="./assets/shampoo.png">
                <div class="ranking-badge badge-silver">2</div>
                <div class="product-image-wrapper bg-pink">
                    <img src="./assets/shampoo.png" alt="보태니컬 실크 샴푸" class="product-img" />
                    {cart_svg}
                </div>
                <div class="bento-info-side">
                    <div>
                        <h3 class="product-name">보태니컬 실크 샴푸</h3>
                        <p class="product-price">₩ 28,000</p>
                    </div>
                </div>
            </article>
            <article class="bento-item bento-small product-card" data-name="프리미엄 에코 제습제" data-price="15000" data-img="./assets/dehumidifier.png">
                <div class="ranking-badge badge-bronze">3</div>
                <div class="product-image-wrapper bg-blue">
                    <img src="./assets/dehumidifier.png" alt="프리미엄 에코 제습제" class="product-img" />
                    {cart_svg}
                </div>
                <div class="bento-info-side">
                    <div>
                        <h3 class="product-name">프리미엄 에코 제습제</h3>
                        <p class="product-price">₩ 15,000</p>
                    </div>
                </div>
            </article>
        </div>
    </section>
'''

category_tiles = '''
    <!-- CATEGORY Section -->
    <section id="category" class="section category-section">
        <div class="section-header">
            <h2 class="section-title">Shop by Category</h2>
        </div>
        <div class="category-grid">
            <a href="#cat-diffuser" class="category-card">
                <div class="category-bg bg-blue"></div>
                <div class="category-content">
                    <h3 class="category-title">Diffuser</h3>
                    <span class="category-link">자세히 보기 &rarr;</span>
                </div>
            </a>
            <a href="#cat-hair" class="category-card">
                <div class="category-bg bg-pink"></div>
                <div class="category-content">
                    <h3 class="category-title">Hair Care</h3>
                    <span class="category-link">자세히 보기 &rarr;</span>
                </div>
            </a>
            <a href="#cat-living" class="category-card">
                <div class="category-bg bg-yellow"></div>
                <div class="category-content">
                    <h3 class="category-title">Living</h3>
                    <span class="category-link">자세히 보기 &rarr;</span>
                </div>
            </a>
        </div>
    </section>
'''

cat_diffuser = f'''
    <section id="cat-diffuser" class="section">
        <div class="section-header">
            <h2 class="section-title">Diffuser</h2>
            <p class="section-desc">공간을 채우는 은은한 향기</p>
        </div>
        <div class="product-grid">
            <article class="product-card" data-name="미드나잇 우드 디퓨저" data-price="35000" data-img="./assets/cat_diffuser_1.png">
                <div class="product-image-wrapper bg-yellow">
                    <img src="./assets/cat_diffuser_1.png" alt="미드나잇 우드 디퓨저" class="product-img" />
                    {cart_svg}
                </div>
                <div class="product-info"><h3 class="product-name">미드나잇 우드 디퓨저</h3><p class="product-price">₩ 35,000</p></div>
            </article>
            <article class="product-card" data-name="프레시 코튼 룸스프레이" data-price="22000" data-img="./assets/cat_diffuser_2.png">
                <div class="product-image-wrapper bg-pink">
                    <img src="./assets/cat_diffuser_2.png" alt="프레시 코튼 룸스프레이" class="product-img" />
                    {cart_svg}
                </div>
                <div class="product-info"><h3 class="product-name">프레시 코튼 룸스프레이</h3><p class="product-price">₩ 22,000</p></div>
            </article>
            <article class="product-card" data-name="베르가못 오일 세트" data-price="42000" data-img="./assets/cat_diffuser_3.png">
                <div class="product-image-wrapper bg-blue">
                    <img src="./assets/cat_diffuser_3.png" alt="베르가못 오일 세트" class="product-img" />
                    {cart_svg}
                </div>
                <div class="product-info"><h3 class="product-name">베르가못 오일 세트</h3><p class="product-price">₩ 42,000</p></div>
            </article>
            <article class="product-card" data-name="시그니처 글래스 디퓨저" data-price="38000" data-img="./assets/cat_diffuser_4.png">
                <div class="product-image-wrapper bg-yellow">
                    <img src="./assets/cat_diffuser_4.png" alt="시그니처 글래스 디퓨저" class="product-img" />
                    {cart_svg}
                </div>
                <div class="product-info"><h3 class="product-name">시그니처 글래스 디퓨저</h3><p class="product-price">₩ 38,000</p></div>
            </article>
        </div>
    </section>
'''

cat_hair = f'''
    <section id="cat-hair" class="section">
        <div class="section-header">
            <h2 class="section-title">Hair Care</h2>
            <p class="section-desc">자연 유래 성분으로 완성하는 부드러움</p>
        </div>
        <div class="product-grid">
            <article class="product-card" data-name="오가닉 로즈마리 샴푸" data-price="26000" data-img="./assets/cat_hair_1.png">
                <div class="product-image-wrapper bg-pink"><img src="./assets/cat_hair_1.png" alt="오가닉 로즈마리 샴푸" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">오가닉 로즈마리 샴푸</h3><p class="product-price">₩ 26,000</p></div>
            </article>
            <article class="product-card" data-name="너리싱 헤어 에센스" data-price="31000" data-img="./assets/cat_hair_2.png">
                <div class="product-image-wrapper bg-blue"><img src="./assets/cat_hair_2.png" alt="너리싱 헤어 에센스" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">너리싱 헤어 에센스</h3><p class="product-price">₩ 31,000</p></div>
            </article>
            <article class="product-card" data-name="보태니컬 트리트먼트" data-price="28000" data-img="./assets/cat_hair_3.png">
                <div class="product-image-wrapper bg-yellow"><img src="./assets/cat_hair_3.png" alt="보태니컬 트리트먼트" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">보태니컬 트리트먼트</h3><p class="product-price">₩ 28,000</p></div>
            </article>
            <article class="product-card" data-name="스칼프 케어 토닉" data-price="34000" data-img="./assets/cat_hair_4.png">
                <div class="product-image-wrapper bg-pink"><img src="./assets/cat_hair_4.png" alt="스칼프 케어 토닉" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">스칼프 케어 토닉</h3><p class="product-price">₩ 34,000</p></div>
            </article>
        </div>
    </section>
'''

cat_living = f'''
    <section id="cat-living" class="section">
        <div class="section-header">
            <h2 class="section-title">Living</h2>
            <p class="section-desc">일상의 감도를 높이는 오브제</p>
        </div>
        <div class="product-grid">
            <article class="product-card" data-name="내추럴 소이 캔들" data-price="25000" data-img="./assets/cat_living_1.png">
                <div class="product-image-wrapper bg-blue"><img src="./assets/cat_living_1.png" alt="내추럴 소이 캔들" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">내추럴 소이 캔들</h3><p class="product-price">₩ 25,000</p></div>
            </article>
            <article class="product-card" data-name="프리미엄 린넨 샤쉐" data-price="12000" data-img="./assets/cat_living_2.png">
                <div class="product-image-wrapper bg-yellow"><img src="./assets/cat_living_2.png" alt="프리미엄 린넨 샤쉐" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">프리미엄 린넨 샤쉐</h3><p class="product-price">₩ 12,000</p></div>
            </article>
            <article class="product-card" data-name="편백나무 룸 스프레이" data-price="23000" data-img="./assets/cat_living_3.png">
                <div class="product-image-wrapper bg-pink"><img src="./assets/cat_living_3.png" alt="편백나무 룸 스프레이" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">편백나무 룸 스프레이</h3><p class="product-price">₩ 23,000</p></div>
            </article>
            <article class="product-card" data-name="퓨어 에코 제습제" data-price="15000" data-img="./assets/cat_living_4.png">
                <div class="product-image-wrapper bg-blue"><img src="./assets/cat_living_4.png" alt="퓨어 에코 제습제" class="product-img" />{cart_svg}</div>
                <div class="product-info"><h3 class="product-name">퓨어 에코 제습제</h3><p class="product-price">₩ 15,000</p></div>
            </article>
        </div>
    </section>
'''

about_section = '''
    <!-- ABOUT Section -->
    <section id="about" class="section about-section">
        <div class="about-container">
            <h2 class="about-title">Add a Splash of Color to Your Life.</h2>
            <p class="about-desc">
                ELOA는 당신의 일상에 다채로운 색을 입히는 라이프스타일 브랜드입니다.<br>
                평범한 순간들이 모여 특별한 하루가 될 수 있도록, 가장 감각적인 제품을 제안합니다.
            </p>
        </div>
    </section>
'''

cart_html = '''
    <!-- Cart Sidebar -->
    <div class="cart-overlay" id="cart-overlay"></div>
    <div class="cart-sidebar" id="cart-sidebar">
        <div class="cart-header">
            <h3>Your Cart</h3>
            <button class="cart-close" id="cart-close">&times;</button>
        </div>
        <div class="cart-items" id="cart-items">
            <!-- Items injected via JS -->
            <div class="empty-cart-msg">장바구니가 비어 있습니다.</div>
        </div>
        <div class="cart-footer">
            <div class="cart-total">
                <span>Total</span>
                <span id="cart-total-price">₩ 0</span>
            </div>
            <button class="btn-primary" style="width: 100%; margin-top: 1rem;">Checkout</button>
        </div>
    </div>
'''

# Find where NEW section starts
start_idx = html.find('<!-- NEW Section -->')
# Find where scripts start
end_idx = html.find('<!-- Scripts -->')

new_html = html[:start_idx] + new_section + best_section + category_tiles + cat_diffuser + cat_hair + cat_living + about_section + cart_html + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html")
