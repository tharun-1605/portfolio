import json
import re
import urllib.parse

with open('repos.json', 'r') as f:
    repos = json.load(f)

filtered_repos = [r for r in repos if r['name'] != 'tharun-1605']

projects_html = ""

# Map specific projects to local images if they exist
local_image_map = {
    "AccidentManagement": "assets/img/projects/Accidentmanagement-project-1.jpg",
    "OrderManagementandStockDeduction": "assets/img/projects/data-project-1.jpg",
    "flutter_front_end_for_signlanguvage_conversion": "assets/img/projects/Sign-Languvage-Conversion-project-1.jpg"
}

for repo in filtered_repos:
    name = repo['name']
    desc = repo['description']
    url = repo['url']
    lang = repo['language']
    
    # Generate placeholder image with the project name if no local image matches
    if name in local_image_map:
        img_url = local_image_map[name]
    else:
        # URL encode the project name
        encoded_name = urllib.parse.quote(name)
        # Using unspash source with keyword based on language or just placehold.co
        img_url = f"https://placehold.co/800x600/e9ecef/495057?text={encoded_name}"
    
    projects_html += f'''
        <!-- Project: {name} -->
        <div class="col-lg-4 col-md-6 project-item isotope-item filter-web">
          <div class="project-content h-100">
            <img src="{img_url}" class="img-fluid" alt="{name}">
            <div class="project-info">
              <h4>{name}</h4>
              <p>{desc}</p>
              <a href="{img_url}" title="{name}" data-gallery="project-gallery-web" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
              <a href="{url}" title="More Details" class="details-link" target="_blank"><i class="bi bi-link-45deg"></i></a>
            </div>
          </div>
        </div><!-- End Project Item -->
'''

with open('/mnt/app/Tharunk/Tharun K/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace isotope-container
iso_pattern = re.compile(r'(<div class="row gy-4 isotope-container"[^>]*>).*?(</div><!-- End Project Container -->)', re.DOTALL)
content = iso_pattern.sub(rf'\1{projects_html}\2', content)

with open('/mnt/app/Tharunk/Tharun K/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated project images.")
