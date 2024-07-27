# Job Aplication Agent

## Prerequisites
* Python 3.7+
* MongoDB instance (local or cloud-based)

## Instalation
1. Clone the repository:
```
git clone https://github.com/almazagit1002/job_aplication_agent.git
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate virtual environment:
* On macOS and Linux:
```
source venv/bin/activate  
```
* # On Windows:
 ```
venv\Scripts\activate
```

4. Install `pip` (if not already installed)
 * Check if pip is installed:
  ```
  pip --version
  ```
If `pip` is not installed, follow these steps to install it:
* Using `curl`:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
* Using `wget`:
```
wget https://bootstrap.pypa.io/get-pip.py
```

Install:
```
python get-pip.py
```

5. Install Project Dependencies:
```
pip install -r requirements.txt

```

6. Running the Application
```
uvicorn main:app --reload --host localhost --port 8888
```
* Access the interactive API documentation:
Open your browser and go to
```
 http://localhost:8888/api/v1/users/docs 
```
or
```
http://localhost:8888/api/v1/users/redoc
```

## Project Structure

```
job_application_agent/
├── main.py
├──db
|  ├── models/
│       ├── base.py
│       ├── user.py
│       ├── contact_info.py
│       ├── education.py
│       ├── experience.py
│       ├── skills.py
│       └── projects.py
|  ├── db_set_up.py
|
├── api/
│   ├── utils
│       └── users.py
│   └── users.py

```

## Usage
Go to `\job_aplication_agent\research\06_test_api.ipynb` and do shit enter in the firts cell

or use followng data as example: 

```
 {
    "email": "johnaaaaadoe@example.com",
    "role": "user",  # Role can be 'admin' or 'user'
    "is_active": True,
    "certifications": [
        {
            "start_year": "2018",
            "end_year": "2019",
            "certificates": [
                {"certificate": "Certified Kubernetes Administrator"},
                {"certificate": "AWS Certified Solutions Architect"}
            ]
        },
        {
            "start_year": "2020",
            "end_year": "2021",
            "certificates": [
                {"certificate": "Certified Data Scientist"}
            ]
        }
    ],
    "contact_info": {
        "name": "Alejandro Maza Villalpando",
        "phon_ext": "123",
        "phone": "+4591197494",
        "linkedin": "https://www.linkedin.com/in/ale-mazavillalpando/",
        "github": "https://github.com/almazagit1002",
        "website": "https://www.example.com"
    },
    "education": [
        {
            "start_year": "2021",
            "end_year": "2023",
            "degree": "Masters in Computational Physics",
            "institution": "Copenhagen University",
            "subjects": [
                {"subject": "Applied Statistics"},
                {"subject": "High-performance parallel computing"},
                {"subject": "Inverse problems"},
                {"subject": "Advanced Applied Statistics"}
            ],
            "thesis": "Machine Learning Methods for Predicting Stellar Parameters in Realistic Molecular Cloud Environments"
        },
        {
            "start_year": "2015",
            "end_year": "2019",
            "degree": "Bachelors in Physics",
            "institution": "University of the West of Scotland",
            "subjects": [
                {"subject": "Complex analysis"},
                {"subject": "Statistical mechanics"},
                {"subject": "Partial differential equations"}
            ]
        }
    ],
    "experience": [
        {
           "start_date": "2019-06",
            "end_date": "2021-08",
            "company": "Tech Solutions Inc.",
            "job_type": "Full time",
            "responsabilities": "Developed and maintained software solutions, led a team of developers, and collaborated with cross-functional teams."
        },
        {
            "start_date": "2022-01",
            "end_date": None,
            "company": "Innovative Software Co.",
            "job_type": "Part Time",
            "responsabilities": "Worked on machine learning projects, developed data pipelines, and provided technical support to clients."
        }
    ],
    "projects": [
        {
            "start_year": "2021",
            "end_year": "2022",
            "project_name": "Machine Learning Model for Predictive Analytics",
            "project_description": "Developed a machine learning model to predict sales trends.",
            "project_link": "https://github.com/almazagit1002/predictive-analytics"
        },
        {
            "start_year": "2020",
            "end_year": "2021",
            "project_name": "E-commerce Web Application",
            "project_description": "Created a full-stack web application for an e-commerce platform.",
            "project_link": "https://github.com/almazagit1002/ecommerce-web-app"
        }
    ],
    "soft_skills": [
        {"skill": "Leadership"},
        {"skill": "Communication"},
        {"skill": "Problem-solving"}
    ],
    "technical_skills": [
        {
            "tech_skill": "Python",
            "experinece_time": 5,
            "use_case": "Developed backend services and machine learning models."
        },
        {
            "tech_skill":  "AWS",
            "experinece_time": 3,
            "use_case": "Deployed scalable applications and managed cloud infrastructure."
        }
    ],
    "about_me": "Passionate about technology and education. Always eager to learn new skills and contribute to innovative projects."
}
```


## Ignore this 

install miktex https://miktex.org/
install pearl https://strawberryperl.com/