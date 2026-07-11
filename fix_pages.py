import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# First, modify navigation links in the html string
html = html.replace('<a href="#cat-diffuser">Diffuser</a>', '<a href="diffuser.html">Diffuser</a>')
html = html.replace('<a href="#cat-hair">Hair Care</a>', '<a href="hair.html">Hair Care</a>')
html = html.replace('<a href="#cat-living">Living</a>', '<a href="living.html">Living</a>')

# Also update the CATEGORY Tiles links
html = html.replace('<a href="#cat-diffuser" class="category-card">', '<a href="diffuser.html" class="category-card">')
html = html.replace('<a href="#cat-hair" class="category-card">', '<a href="hair.html" class="category-card">')
html = html.replace('<a href="#cat-living" class="category-card">', '<a href="living.html" class="category-card">')

# Extract components from the original index.html (before category sections were removed in the previous script)
# Oh wait, index.html NO LONGER HAS the category sections (diffuser, hair, living)
# I need to get them from diffuser.html where they currently exist.
with open('diffuser.html', 'r', encoding='utf-8') as f:
    diffuser_html = f.read()

# Let's extract the header from index.html
hero_start = html.find('<!-- Scroll Expansion Hero -->')
header_html = html[:hero_start]
header_html_sub = header_html.replace('<a href="#new">NEW</a>', '<a href="index.html#new">NEW</a>')
header_html_sub = header_html_sub.replace('<a href="#best">BEST</a>', '<a href="index.html#best">BEST</a>')
header_html_sub = header_html_sub.replace('<a href="#about">ABOUT</a>', '<a href="index.html#about">ABOUT</a>')

# The footer starts from ABOUT section
about_start = html.find('<!-- ABOUT Section -->')
footer_html = html[about_start:]

# Now extract the category sections from diffuser_html
diffuser_start = diffuser_html.find('<section id="cat-diffuser" class="section">')
hair_start = diffuser_html.find('<section id="cat-hair" class="section">')
living_start = diffuser_html.find('<section id="cat-living" class="section">')
end_living = diffuser_html.find('</main>')

cat_diffuser = diffuser_html[diffuser_start:hair_start]
cat_hair = diffuser_html[hair_start:living_start]
cat_living = diffuser_html[living_start:end_living]

# Write diffuser.html
with open('diffuser.html', 'w', encoding='utf-8') as f:
    f.write(header_html_sub + '<main style="padding-top:80px;">' + cat_diffuser + '</main>' + footer_html)

# Write hair.html
with open('hair.html', 'w', encoding='utf-8') as f:
    f.write(header_html_sub + '<main style="padding-top:80px;">' + cat_hair + '</main>' + footer_html)

# Write living.html
with open('living.html', 'w', encoding='utf-8') as f:
    f.write(header_html_sub + '<main style="padding-top:80px;">' + cat_living + '</main>' + footer_html)

print("Fixed category pages.")
