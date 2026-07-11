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

# Modify index.html navigation links for #new, #best, #about to point back to index.html if we are not on index.html
# Wait, for the generated pages, we should use index.html#new, index.html#best, etc.
# Let's extract the components.
# Find where Hero starts
hero_start = html.find('<!-- Hero Section -->')
# Find where the category sections start and end
diffuser_start = html.find('<section id="cat-diffuser" class="section">')
hair_start = html.find('<section id="cat-hair" class="section">')
living_start = html.find('<section id="cat-living" class="section">')
about_start = html.find('<!-- ABOUT Section -->')

# The common header (everything before Hero)
header_html = html[:hero_start]

# Modify header_html for subpages to link back to index.html
header_html_sub = header_html.replace('<a href="#new">NEW</a>', '<a href="index.html#new">NEW</a>')
header_html_sub = header_html_sub.replace('<a href="#best">BEST</a>', '<a href="index.html#best">BEST</a>')
header_html_sub = header_html_sub.replace('<a href="#about">ABOUT</a>', '<a href="index.html#about">ABOUT</a>')

# Extract category sections
cat_diffuser = html[diffuser_start:hair_start]
cat_hair = html[hair_start:living_start]
cat_living = html[living_start:about_start]

# Footer / Cart / Scripts
footer_html = html[about_start:]

# Generate Diffuser HTML
with open('diffuser.html', 'w', encoding='utf-8') as f:
    f.write(header_html_sub + '<main style="padding-top:80px;">' + cat_diffuser + '</main>' + footer_html)

# Generate Hair HTML
with open('hair.html', 'w', encoding='utf-8') as f:
    f.write(header_html_sub + '<main style="padding-top:80px;">' + cat_hair + '</main>' + footer_html)

# Generate Living HTML
with open('living.html', 'w', encoding='utf-8') as f:
    f.write(header_html_sub + '<main style="padding-top:80px;">' + cat_living + '</main>' + footer_html)

# Now remove category sections from index.html
new_index_html = html[:diffuser_start] + html[about_start:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)

print("Pages generated and index.html updated successfully.")
