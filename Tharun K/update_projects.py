import json
import re

with open('repos.json', 'r') as f:
    repos = json.load(f)

# Filter out the profile repo if it's named tharun-1605, or just keep all as requested?
# Let's keep all, except maybe 'tharun-1605' profile readme and 'portfolio' which is just the portfolio itself.
# Actually user said "add all the project", I'll add them all but skip tharun-1605 if it's just the README.
filtered_repos = [r for r in repos if r['name'] != 'tharun-1605']

projects_html = ""
details_html = ""

images = [
    "assets/img/projects/Sign-Languvage-Conversion-project-1.jpg",
    "assets/img/projects/data-project-1.jpg",
    "assets/img/projects/Accidentmanagement-project-1.jpg",
    "assets/img/projects/Bank-Management-project-1.jpg",
    "assets/img/projects/Cricket-scoreboard-project-1.jpg",
    "assets/img/projects/game-project-1.jpg"
]

for i, repo in enumerate(filtered_repos):
    name = repo['name']
    desc = repo['description']
    url = repo['url']
    lang = repo['language']
    
    # assign an image cyclically
    img = images[i % len(images)]
    
    projects_html += f'''
        <!-- Project: {name} -->
        <div class="col-lg-4 col-md-6 project-item isotope-item filter-web">
          <div class="project-content h-100">
            <img src="{img}" class="img-fluid" alt="{name}">
            <div class="project-info">
              <h4>{name}</h4>
              <p>{desc}</p>
              <a href="{img}" title="{name}" data-gallery="project-gallery-web" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
              <a href="{url}" title="More Details" class="details-link" target="_blank"><i class="bi bi-link-45deg"></i></a>
            </div>
          </div>
        </div><!-- End Project Item -->
'''

    details_html += f'''
          <!-- Detail: {name} -->
          <div class="col-lg-4 col-md-6 service-item d-flex" data-aos="fade-up" data-aos-delay="100">
            <div class="icon flex-shrink-0"><i class="bi bi-window-desktop"></i></div>
            <div>
              <h4 class="title"><a href="{url}" class="stretched-link" target="_blank">{name}</a></h4>
              <p class="description">{desc}<br><br><strong>Technologies:</strong> {lang}</p>
            </div>
          </div><!-- End Service Item -->
'''

with open('/mnt/app/Tharunk/Tharun K/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace isotope-container
iso_pattern = re.compile(r'(<div class="row gy-4 isotope-container"[^>]*>).*?(</div><!-- End Project Container -->)', re.DOTALL)
content = iso_pattern.sub(rf'\1{projects_html}\2', content)

# Replace project details row
# It's inside <section id="project-details" class="services section"> -> <div class="container"> -> <div class="row gy-4">
details_pattern = re.compile(r'(<section id="project-details"[^>]*>.*?<div class="container">\s*<div class="row gy-4">).*?(</div>\s*</div>\s*</section><!-- /Services Section -->)', re.DOTALL)
content = details_pattern.sub(rf'\1{details_html}\2', content)

with open('/mnt/app/Tharunk/Tharun K/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added", len(filtered_repos), "projects.")
