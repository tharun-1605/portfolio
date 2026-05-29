import re

# 1. Update HTML Fonts
with open('/mnt/app/Tharunk/Tharun K/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace fonts
old_fonts_regex = re.compile(r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=Roboto[^>]+>\s*<link[^>]+display=swap"\s*rel="stylesheet">', re.DOTALL)

# Let's just use a more robust regex or replace string
font_str = '''<link
    href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
    rel="stylesheet">'''

new_font_str = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'

if font_str in html_content:
    html_content = html_content.replace(font_str, new_font_str)
else:
    # try regex fallback
    html_content = re.sub(r'<link[^>]+family=Roboto[^>]+>', new_font_str, html_content)


# Enhance specific sections in HTML to support glassmorphism
# We will wrap or add classes to cards
html_content = html_content.replace('class="resume-item"', 'class="resume-item glass-card"')
html_content = html_content.replace('class="service-item d-flex"', 'class="service-item d-flex glass-card"')
html_content = html_content.replace('class="project-content h-100"', 'class="project-content h-100 glass-card"')
html_content = html_content.replace('class="skill-category mb-4"', 'class="skill-category mb-4 glass-card p-4 rounded-4"')
html_content = html_content.replace('class="info-item d-flex"', 'class="info-item d-flex glass-card"')

with open('/mnt/app/Tharunk/Tharun K/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)


# 2. Update CSS Variables and Add Animations
with open('/mnt/app/Tharunk/Tharun K/assets/css/main.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace fonts
css_content = re.sub(r'--default-font: "Roboto"[^;]+;', '--default-font: "Inter", system-ui, -apple-system, sans-serif;', css_content)
css_content = re.sub(r'--heading-font: "Raleway"[^;]+;', '--heading-font: "Outfit", sans-serif;', css_content)
css_content = re.sub(r'--nav-font: "Poppins"[^;]+;', '--nav-font: "Inter", sans-serif;', css_content)

# Replace global colors
old_global = r'''/\* Global Colors.*?{.*?--background-color: #ffffff;.*?--default-color: #272829;.*?--heading-color: #050d18;.*?--accent-color: #149ddd;.*?--surface-color: #ffffff;.*?--contrast-color: #ffffff;.*?}'''
new_global = '''/* Global Colors */
:root { 
  --background-color: #0a0f16;
  --default-color: #a1aab5;
  --heading-color: #ffffff;
  --accent-color: #00e5ff;
  --surface-color: rgba(255, 255, 255, 0.03);
  --contrast-color: #000000;
  
  --glass-border: rgba(255, 255, 255, 0.08);
  --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
  --spring-easing: cubic-bezier(0.175, 0.885, 0.32, 1.275);
}'''
css_content = re.sub(r'/\* Global Colors.*?}', new_global, css_content, flags=re.DOTALL)


# Light/Dark backgrounds
old_bgs = r'''\.light-background\s*\{.*?\}.*?\.dark-background\s*\{.*?\}'''
new_bgs = '''.light-background {
  --background-color: #0f1620;
  --surface-color: rgba(255, 255, 255, 0.04);
}

.dark-background {
  --background-color: #06090e;
  --default-color: #a1aab5;
  --heading-color: #ffffff;
  --surface-color: rgba(255, 255, 255, 0.02);
  --contrast-color: #ffffff;
}'''
css_content = re.sub(old_bgs, new_bgs, css_content, flags=re.DOTALL)


# Header Glassmorphism
header_regex = r'(\.header\s*\{[^}]*?background-color: var\(--background-color\);)'
css_content = re.sub(header_regex, r'\1\n  background: rgba(10, 15, 22, 0.7);\n  backdrop-filter: blur(20px);\n  -webkit-backdrop-filter: blur(20px);\n  border-right: 1px solid var(--glass-border);', css_content)


# Append Glassmorphic Classes and Animations to end of CSS
glass_css = '''

/* =======================================================
   GLASSMORPHISM & ANIMATIONS OVERHAUL
   ======================================================== */

.glass-card {
  background: var(--surface-color);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border);
  box-shadow: var(--glass-shadow);
  border-radius: 16px;
  transition: all 0.4s var(--spring-easing);
  overflow: hidden;
}

.glass-card:hover {
  transform: translateY(-8px) scale(1.02);
  border-color: rgba(0, 229, 255, 0.4);
  box-shadow: 0 15px 40px 0 rgba(0, 229, 255, 0.15);
  background: rgba(255, 255, 255, 0.05);
}

/* Enhancing existing components */
.resume .resume-item {
  padding: 20px 20px 20px 20px !important;
  margin-bottom: 20px;
  border-left: none !important;
  position: relative;
}

.resume .resume-item::before {
  display: none !important; /* Remove old circles */
}

/* Project Cards Update */
.project-content {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
}

.project-content img {
  transition: all 0.5s ease;
}

.project-content:hover img {
  transform: scale(1.1);
  filter: brightness(0.8);
}

.project-info {
  background: rgba(10, 15, 22, 0.85) !important;
  backdrop-filter: blur(10px);
  border-top: 1px solid var(--glass-border);
}

/* Service Item Update */
.services .service-item {
  padding: 30px !important;
}

.services .service-item .icon {
  background: rgba(0, 229, 255, 0.1);
  border-radius: 50%;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-color);
  transition: all 0.3s ease;
}

.services .service-item:hover .icon {
  background: var(--accent-color);
  color: #000;
  transform: rotate(10deg) scale(1.1);
}

/* Buttons and Links */
a {
  transition: all 0.3s ease;
}

.btn-primary, .resume-download a {
  background: var(--accent-color) !important;
  color: #000 !important;
  font-weight: 600;
  border-radius: 30px !important;
  border: none !important;
  box-shadow: 0 4px 15px rgba(0, 229, 255, 0.3);
  transition: all 0.3s var(--spring-easing) !important;
}

.btn-primary:hover, .resume-download a:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 25px rgba(0, 229, 255, 0.5);
  background: #ffffff !important;
  color: var(--accent-color) !important;
}

/* Typed Text Glow */
.typed {
  color: var(--accent-color);
  text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
}

/* Skills Category specific */
.skill-category {
  margin-bottom: 30px !important;
}
.skill-category h5 {
  color: var(--heading-color);
  font-size: 1.1rem;
}

/* Hero Background Enhancement */
.hero:before {
  background: linear-gradient(135deg, rgba(10,15,22,0.9) 0%, rgba(10,15,22,0.6) 100%) !important;
}

'''
css_content += glass_css

with open('/mnt/app/Tharunk/Tharun K/assets/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated UI structure and CSS!")
