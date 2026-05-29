import json

descriptions = {
    "ComplainIQ": "Built a full-stack web application for posting complaints with geolocation, tracking status updates, and receiving admin responses. Implemented interactive maps and an admin panel to manage, resolve, and reply to user issues efficiently.",
    "Tool_managemnt": "A robust management system developed for tracking tools, maintenance schedules, and monitoring inventory levels effectively.",
    "attend_app_fluter": "Developed a Flutter-based cross-platform mobile app for employee attendance using Firebase for authentication, real-time database, and cloud storage. Implemented face recognition with Google ML Kit.",
    "mlmodel": "Python-based Machine Learning models focusing on predictive analytics, data preprocessing, and algorithm optimization.",
    "personal_chat_new": "A secure, real-time personal chat application built with Dart and Flutter featuring instant messaging and modern UI.",
    "personal_chat": "A real-time chat application designed for private messaging and seamless user communication.",
    "AI-Chatbot-for-College": "Developed an intelligent AI-powered chatbot system to assist college students with instant queries, replacing traditional support methods with a 24/7 automated conversational solution.",
    "invocegenrator-main-feroTech": "An advanced, dynamic invoice generator built with TypeScript for automated billing, PDF exports, and data management.",
    "cloudhackthonproject1-crm": "A Customer Relationship Management (CRM) application developed during a cloud hackathon to streamline client interactions.",
    "Varsheedha-st-project": "A JavaScript-focused web project exploring interactive UI elements and responsive frontend design.",
    "Software-testing-projetc": "A comprehensive software testing suite showcasing unit testing, integration testing, and modern QA methodologies.",
    "clam-path1": "A dynamic JavaScript-based web application exploring data visualization or pathfinding algorithms.",
    "Smart-Pet-Website": "An interactive website platform designed for managing pet care, feeding schedules, and health records.",
    "Smart-Pet-Website-main": "The main frontend interface repository for the comprehensive Smart Pet Care management portal.",
    "campus-placement-devops": "DevOps pipelines and infrastructure-as-code configurations built for a campus placement tracking system.",
    "Varshedha": "Web development application focusing on modern UI/UX design principles and interactive components.",
    "public_toilet-sug": "A responsive TypeScript application aimed at helping users locate and rate public restrooms in real-time.",
    "ML_project": "A comprehensive machine learning project showcasing data analysis, feature engineering, model training, and evaluation.",
    "Second-Round-project": "An interactive JavaScript application developed as part of a competitive hackathon or technical interview challenge.",
    "Student-Mental-Health": "A Flutter application dedicated to student well-being, providing resources, daily tracking, and mental health support.",
    "Deployment-main": "A collection of scripts and configuration files crafted for automated application deployment and CI/CD pipelines.",
    "flutter_front_end_for_signlanguvage_conversion": "A Flutter-based frontend interface designed to facilitate the conversion of sign language gestures into text and speech.",
    "car_Rental_System": "Developed a full-stack Car Rental System implementing secure user authentication, booking workflows, and database integration.",
    "portfolio": "My personal portfolio website showcasing my technical skills, past projects, resume, and contact information.",
    "project": "A general-purpose full-stack application highlighting software architecture, database management, and API design.",
    "Hotelbooking-System": "A comprehensive Hotel Booking System featuring real-time room availability, reservations, and payment gateway integration.",
    "hotel": "A dynamic hotel management web interface tailored for staff administration and daily operational tasks.",
    "Backend_car": "The backend API services and database architecture powering the full-stack car rental system.",
    "Expence-Tracker": "A user-friendly JavaScript application for tracking daily expenses, categorizing spending, and managing budgets.",
    "Back_end_expensesTracker": "Robust backend API services and database models for the comprehensive expense tracker application.",
    "OrderManagementandStockDeduction": "Designed and developed an Order and Stock Management System to streamline inventory tracking, order processing, and stock updates in real-time.",
    "AccidentManagement": "Designed an Accident Management System to streamline the reporting, tracking, and analysis of road accidents using Java and MySQL."
}

with open('repos.json', 'r') as f:
    repos = json.load(f)

for repo in repos:
    name = repo['name']
    if name in descriptions:
        repo['description'] = descriptions[name]
    else:
        # Fallback if I missed any
        if not repo['description'] or repo['description'] == "No description provided." or repo['description'] == "None":
            repo['description'] = f"A {repo['language']} project focused on solving specific problems through code. Explore the repository for detailed implementation."

with open('repos.json', 'w') as f:
    json.dump(repos, f, indent=2)

print("Updated descriptions in repos.json.")
