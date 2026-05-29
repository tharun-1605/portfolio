import re

with open('/mnt/app/Tharunk/Tharun K/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update About Section
about_regex = re.compile(r'(<section id="about" class="about section">.*?</section><!-- /About Section -->)', re.DOTALL)
new_about = '''<section id="about" class="about section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>About</h2>
        <p>Hi, I'm Tharun K, a Computer Science Engineering student passionate about full-stack web development, cloud computing, and building cross-platform mobile applications.</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4 justify-content-center">
          <div class="col-lg-4">
            <img src="assets/img/my-profile-img.jpg" class="img-fluid" alt="">
          </div>
          <div class="col-lg-8 content">
            <h2>Full-Stack Developer &amp; Tech Enthusiast.</h2>
            <p class="fst-italic py-3">
              Currently pursuing B.E. in Computer Science and Engineering at Sri Eshwar College of Engineering, with a strong foundation in modern web and cloud technologies.
            </p>
            <div class="row">
              <div class="col-lg-6">
                <ul>
                  <li><i class="bi bi-chevron-right"></i> <strong>Degree:</strong> <span>B.E (CSE)</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Phone:</strong> <span>+91 7639231084</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>City:</strong> <span>Coimbatore, Tamil Nadu, India</span></li>
                </ul>
              </div>
              <div class="col-lg-6">
                <ul>
                  <li><i class="bi bi-chevron-right"></i> <strong>Email:</strong> <span>tharun.k2023cse@sece.ac.in</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>GitHub:</strong> <span><a href="https://github.com/tharun-1605">tharun-1605</a></span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>LinkedIn:</strong> <span><a href="https://www.linkedin.com/in/tharun-k-ba7633291/">Tharun K</a></span></li>
                </ul>
              </div>
            </div>
            <p class="py-3">
              I am eager to leverage my skills in React, Node.js, Flutter, and cloud services (AWS, Google Cloud) to solve real-world problems. I have experience developing scalable full-stack applications and deploying them using Docker and Kubernetes.
            </p>
          </div>
        </div>

      </div>

    </section><!-- /About Section -->'''

content = about_regex.sub(new_about, content)

# 2. Update Skills Section
skills_regex = re.compile(r'(<section id="skills".*?</section><!-- /Skills Section -->\s*</section>)', re.DOTALL)
new_skills = '''<section id="skills" class="skills section light-background">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Technical Skills</h2>
        <p>A summary of the programming languages, technologies, and tools I have experience working with.</p>
      </div><!-- End Section Title -->

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row skills-content skills-animation">

          <div class="col-lg-6">
            <div class="skill-category mb-4">
              <h5 class="fw-bold"><i class="bi bi-code-slash text-primary me-2"></i>Languages</h5>
              <p>Python (Intermediate), C (Intermediate), C++ (Intermediate), Java</p>
            </div>

            <div class="skill-category mb-4">
              <h5 class="fw-bold"><i class="bi bi-globe text-primary me-2"></i>Web Technologies</h5>
              <p>HTML, CSS, JavaScript</p>
            </div>

            <div class="skill-category mb-4">
              <h5 class="fw-bold"><i class="bi bi-layers text-primary me-2"></i>Frameworks & Libraries</h5>
              <p>React JS, Node JS, Flutter, ExpressJS, Flask</p>
            </div>
          </div>

          <div class="col-lg-6">
            <div class="skill-category mb-4">
              <h5 class="fw-bold"><i class="bi bi-database text-primary me-2"></i>Databases</h5>
              <p>MongoDB, MySQL</p>
            </div>

            <div class="skill-category mb-4">
              <h5 class="fw-bold"><i class="bi bi-cloud text-primary me-2"></i>Cloud & DevOps</h5>
              <p>AWS Cloud, Google Cloud, Docker, Kubernetes</p>
            </div>

            <div class="skill-category mb-4">
              <h5 class="fw-bold"><i class="bi bi-gear text-primary me-2"></i>Technical Knowledge</h5>
              <p>Data Structures, OOPS, DBMS</p>
            </div>
          </div>

        </div>

      </div>

    </section><!-- /Skills Section -->'''

content = skills_regex.sub(new_skills, content)

# 3. Resume Section replacement (replacing the commented one and adding the real one)
resume_comment_regex = re.compile(r'(<!-- Resume Section\s+<section id="resume" class="resume section">.*?</section>\s+-->)', re.DOTALL)
new_resume = '''<!-- Resume Section -->
    <section id="resume" class="resume section">
      <div class="container section-title" data-aos="fade-up">
        <h2>Resume</h2>
        <p>My education, internships, certifications, and achievements.</p>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
            <h3 class="resume-title">Education</h3>
            <div class="resume-item">
              <h4>B.E (Computer Science and Engineering)</h4>
              <h5>2023 - 2027</h5>
              <p><em>Sri Eshwar College of Engineering</em></p>
              <p>CGPA: 7.56 (up to 5th sem)</p>
            </div>

            <div class="resume-item">
              <h4>Higher Secondary Certificate (HSC)</h4>
              <h5>2022 - 2023</h5>
              <p><em>L.H.S.School</em></p>
              <p>Percentage: 80.47%</p>
            </div>

            <div class="resume-item">
              <h4>Secondary School Leaving Certificate (SSLC)</h4>
              <h5>2020 - 2021</h5>
              <p><em>L.M.H.S.School</em></p>
              <p>Pass</p>
            </div>
            
            <h3 class="resume-title">Certifications</h3>
            <div class="resume-item">
              <ul>
                <li>Master in Data Structures and Algorithm Using C and C++ (Udemy) - 2025</li>
                <li>Learn Java: Beginner To Master (Udemy) - 2025</li>
                <li>AWS Academy Graduate (AWS Academy Cloud Foundations) - 2025</li>
                <li>Devops For Beginners: Docker, Kubernetes, Cloud, CI/CD & 4 Projects (Udemy) - 2025</li>
                <li>AWS CLOUD PRACTITIONER FOUNDATION (AWS) - 2025</li>
              </ul>
            </div>
            
            <h3 class="resume-title">Programming Achievements</h3>
            <div class="resume-item">
              <ul>
                <li>Won ₹10,000 cash prize at Dhanalakshmi College for an outstanding tech project.</li>
                <li>Selected among the Top 10 teams across Tamil Nadu at the Chennai Hackathon organized by the DGP Office.</li>
                <li>Selected for an internship at Veshpher Technologies, in top 3 Students among 60.</li>
                <li>LeetCode: Completed 140 Problems</li>
                <li>Codechef: Completed 100 Problems</li>
                <li>SkillRack: Completed 600+ Problems</li>
              </ul>
            </div>
          </div>

          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="200">
            <h3 class="resume-title">Internships</h3>
            <div class="resume-item">
              <h4>MERN Stack Intern - Better Tomorrow</h4>
              <h5>2025</h5>
              <p><em><a href="https://github.com/tharun-1605/car_Rental_System" target="_blank">GitHub</a> | Project Link | Certificate</em></p>
              <p>Developed a full-stack Car Rental System using the MERN stack, implementing secure user authentication, booking workflows, and database integration.</p>
              <p><strong>Tech stack:</strong> Node JS, ReactJS, MongoDB, ExpressJS</p>
            </div>

            <div class="resume-item">
              <h4>Cloud Computing AWS-vSphere Technologies</h4>
              <h5>2025</h5>
              <p>Completed intensive training on core AWS services including EC2, S3, IAM, RDS, and VPC. Containerized and deployed a full-stack project using Docker, and uploaded the image to Docker Hub (or ECR) as part of deployment workflow.</p>
            </div>

            <div class="resume-item">
              <h4>DevOps Intern – Vespher Technologies</h4>
              <h5>2025</h5>
              <p>Worked with Kubernetes to manage containerized applications, including setup, deployment, and scaling. Learned and applied the basics of CI/CD pipelines to automate build and deployment processes. Built a solid foundation in Kubernetes architecture, resource handling, and YAML configuration files.</p>
            </div>
            
            <div class="resume-download mt-5 text-center p-4 bg-light border rounded shadow-sm">
              <h4 class="mb-3">Get My Full Resume</h4>
              <a href="tharun resume.pdf" download="tharun resume.pdf" class="btn btn-primary px-4 py-2">Download Now</a>
            </div>
          </div>
        </div>
      </div>
    </section>'''

content = resume_comment_regex.sub(new_resume, content)

# 4. Remove duplicate/bottom Resume Section
bottom_resume_regex = re.compile(r'(<!-- Resume Section -->\s*<section id="resume" class="resume section">.*?</section>\s*)', re.DOTALL)
# wait, my regex above might match the newly inserted one if I don't be careful, but they are sequentially matched?
# I'll just use a direct replace for the bottom one. The bottom one has "Get My Resume"
if 'Get My Resume' in content:
    content = re.sub(r'<!-- Resume Section -->\s*<section id="resume" class="resume section">\s*<div class="container">\s*<div class="row">\s*<div class="col-lg-6 offset-lg-3" data-aos="fade-up" data-aos-delay="100">\s*<div class="resume-download".*?</section>', '<!-- Old Resume Section Removed -->', content, flags=re.DOTALL)

# 5. Projects Section
projects_regex = re.compile(r'(<!-- Project Section -->\s*<section id="projects" class="projects section light-background">.*?</section>)', re.DOTALL)
new_projects = '''<!-- Project Section -->
<section id="projects" class="projects section light-background">

  <!-- Section Title -->
  <div class="container section-title" data-aos="fade-up">
    <h2>Projects</h2>
    <p>Explore my latest projects showcasing my skills and expertise. Each project reflects my dedication to delivering high-quality solutions.</p>
  </div><!-- End Section Title -->

  <div class="container">

    <div class="isotope-layout" data-default-filter="*" data-layout="masonry" data-sort="original-order">

      <!-- Project Filters -->
      <ul class="project-filters isotope-filters" data-aos="fade-up" data-aos-delay="100">
        <li data-filter="*" class="filter-active">All Projects</li>
        <li data-filter=".filter-web">Web Applications</li>
        <li data-filter=".filter-mobile">Mobile Applications</li>
      </ul><!-- End Project Filters -->

      <div class="row gy-4 isotope-container" data-aos="fade-up" data-aos-delay="200">

        <!-- Project 1: ComplainIQ -->
        <div class="col-lg-4 col-md-6 project-item isotope-item filter-web">
          <div class="project-content h-100">
            <img src="assets/img/projects/Sign-Languvage-Conversion-project-1.jpg" class="img-fluid" alt="ComplainIQ">
            <div class="project-info">
              <h4>ComplainIQ</h4>
              <p>Full-stack web application for posting complaints with geolocation and tracking.</p>
              <a href="assets/img/projects/Sign-Languvage-Conversion-project-1.jpg" title="ComplainIQ" data-gallery="project-gallery-web" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
              <a href="https://github.com/tharun-1605/ComplainIQ" title="More Details" class="details-link" target="_blank"><i class="bi bi-link-45deg"></i></a>
            </div>
          </div>
        </div><!-- End Project Item -->

        <!-- Project 2: UniChat -->
        <div class="col-lg-4 col-md-6 project-item isotope-item filter-web">
          <div class="project-content h-100">
            <img src="assets/img/projects/data-project-1.jpg" class="img-fluid" alt="UniChat">
            <div class="project-info">
              <h4>UniChat</h4>
              <p>AI-powered chatbot system to assist college students with instant queries.</p>
              <a href="assets/img/projects/data-project-1.jpg" title="UniChat" data-gallery="project-gallery-web" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
              <a href="https://github.com/tharun-1605/AI-Chatbot-for-College" title="More Details" class="details-link" target="_blank"><i class="bi bi-link-45deg"></i></a>
            </div>
          </div>
        </div><!-- End Project Item -->

        <!-- Project 3: SmartAttend -->
        <div class="col-lg-4 col-md-6 project-item isotope-item filter-mobile">
          <div class="project-content h-100">
            <img src="assets/img/projects/Accidentmanagement-project-1.jpg" class="img-fluid" alt="SmartAttend">
            <div class="project-info">
              <h4>SmartAttend</h4>
              <p>Flutter-based mobile app for employee attendance using ML Kit and Geolocation.</p>
              <a href="assets/img/projects/Accidentmanagement-project-1.jpg" title="SmartAttend" data-gallery="project-gallery-mobile" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
              <a href="https://github.com/tharun-1605/attend_app_fluter" title="More Details" class="details-link" target="_blank"><i class="bi bi-link-45deg"></i></a>
            </div>
          </div>
        </div><!-- End Project Item -->

      </div><!-- End Project Container -->

    </div>

  </div>
</section>'''

content = projects_regex.sub(new_projects, content)

# 6. Services / Project Details Section
services_regex = re.compile(r'(<!-- Services Section -->\s*<section id="Projects" class="services section">.*?</section><!-- /Services Section -->)', re.DOTALL)
new_services = '''<!-- Services Section -->
    <section id="project-details" class="services section">

      <!-- Section Title -->
      <div class="container section-title" data-aos="fade-up">
        <h2>Project Details</h2>
        <p>Explore my latest projects showcasing my skills and expertise. Each project reflects my dedication to delivering high-quality solutions.</p>
      </div><!-- End Section Title -->

      <div class="container">

        <div class="row gy-4">

          <div class="col-lg-4 col-md-6 service-item d-flex" data-aos="fade-up" data-aos-delay="100">
            <div class="icon flex-shrink-0"><i class="bi bi-window-desktop"></i></div>
            <div>
              <h4 class="title"><a href="https://github.com/tharun-1605/ComplainIQ" class="stretched-link" target="_blank">ComplainIQ</a></h4>
              <p class="description">Built a full-stack web application for posting complaints with geolocation, tracking status updates, and receiving admin responses. Implemented interactive maps and an admin panel to manage, resolve, and reply to user issues efficiently. Dockerized the application and pushed images to Docker Hub for scalable deployment.<br><br><strong>Technologies:</strong> React, Node.js, MongoDB</p>
            </div>
          </div><!-- End Service Item -->

          <div class="col-lg-4 col-md-6 service-item d-flex" data-aos="fade-up" data-aos-delay="200">
            <div class="icon flex-shrink-0"><i class="bi bi-chat-dots"></i></div>
            <div>
              <h4 class="title"><a href="https://github.com/tharun-1605/AI-Chatbot-for-College" class="stretched-link" target="_blank">UniChat</a></h4>
              <p class="description">Developed an intelligent AI-powered chatbot system to assist college students with instant queries, replacing traditional support methods with a 24/7 automated conversational solution. Integrating web scraping to fetch and update real-time information.<br><br><strong>Technologies:</strong> React, Python, Flask</p>
            </div>
          </div><!-- End Service Item -->

          <div class="col-lg-4 col-md-6 service-item d-flex" data-aos="fade-up" data-aos-delay="300">
            <div class="icon flex-shrink-0"><i class="bi bi-phone"></i></div>
            <div>
              <h4 class="title"><a href="https://github.com/tharun-1605/attend_app_fluter" class="stretched-link" target="_blank">SmartAttend</a></h4>
              <p class="description">Developed a Flutter-based cross-platform mobile app for employee attendance using Firebase for authentication, real-time database, and cloud storage. Implemented face recognition with Google ML Kit, Geolocation verification, camera check-ins, and local notifications. Built a scalable architecture with CI/CD pipeline for automated build.<br><br><strong>Technologies:</strong> Firebase, Flutter</p>
            </div>
          </div><!-- End Service Item -->

        </div>

      </div>

    </section><!-- /Services Section -->'''

content = services_regex.sub(new_services, content)

with open('/mnt/app/Tharunk/Tharun K/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
