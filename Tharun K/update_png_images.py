import json
import re

with open('repos.json', 'r') as f:
    repos = json.load(f)

filtered_repos = [r for r in repos if r['name'] != 'tharun-1605']

# Define the thematic PNG images
img_map = {
    "web_development": "assets/img/projects/web_development.png",
    "mobile_app": "assets/img/projects/mobile_app.png",
    "ai_machine_learning": "assets/img/projects/ai_machine_learning.png",
    "business_finance": "assets/img/projects/business_finance.png",
    "cloud_devops": "assets/img/projects/cloud_devops.png",
    "pet_care": "assets/img/projects/pet_care.png",
    "car_rental": "assets/img/projects/car_rental.png",
    "hotel_booking": "assets/img/projects/hotel_booking.png"
}

project_image_mapping = {
    "ComplainIQ": "web_development",
    "Tool_managemnt": "business_finance",
    "Varsheedha-st-project": "web_development",
    "clam-path1": "web_development",
    "Varshedha": "web_development",
    "portfolio": "web_development",
    "project": "web_development",
    "Software-testing-projetc": "web_development",
    "Second-Round-project": "web_development",
    "attend_app_fluter": "mobile_app",
    "personal_chat_new": "mobile_app",
    "personal_chat": "mobile_app",
    "Student-Mental-Health": "mobile_app",
    "flutter_front_end_for_signlanguvage_conversion": "mobile_app",
    "mlmodel": "ai_machine_learning",
    "AI-Chatbot-for-College": "ai_machine_learning",
    "ML_project": "ai_machine_learning",
    "invocegenrator-main-feroTech": "business_finance",
    "cloudhackthonproject1-crm": "business_finance",
    "OrderManagementandStockDeduction": "business_finance",
    "Expence-Tracker": "business_finance",
    "Back_end_expensesTracker": "business_finance",
    "campus-placement-devops": "cloud_devops",
    "Deployment-main": "cloud_devops",
    "Smart-Pet-Website": "pet_care",
    "Smart-Pet-Website-main": "pet_care",
    "car_Rental_System": "car_rental",
    "Backend_car": "car_rental",
    "AccidentManagement": "car_rental",
    "Hotelbooking-System": "hotel_booking",
    "hotel": "hotel_booking",
    "public_toilet-sug": "hotel_booking"
}

projects_html = ""

for repo in filtered_repos:
    name = repo['name']
    desc = repo['description']
    url = repo['url']
    
    category = project_image_mapping.get(name, "web_development")
    img_url = img_map[category]
    
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

iso_pattern = re.compile(r'(<div class="row gy-4 isotope-container"[^>]*>).*?(</div><!-- End Project Container -->)', re.DOTALL)
content = iso_pattern.sub(rf'\1{projects_html}\2', content)

with open('/mnt/app/Tharunk/Tharun K/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated with thematic PNGs.")
