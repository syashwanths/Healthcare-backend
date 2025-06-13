# 🏥 Healthcare Backend API (Django + DRF + PostgreSQL)

This is a backend system for a healthcare application built using Django, Django REST Framework, and PostgreSQL. It includes user authentication (JWT), and APIs for managing patients, doctors, and mappings between them.

## 🚀 Features

- JWT-based Authentication
- Patient Management (CRUD)
- Doctor Management (CRUD)
- Patient-Doctor Mapping
- PostgreSQL Integration
- Token-based API Security
- Modular Django App Structure

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt

---

## ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/syashwanths/Healthcare-backend.git
cd Healthcare-backend

```
## 2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows
```

## 3. Configure Database Settings in settings.py
```
Instead of using .env, the database settings are directly configured in settings.py. Make sure the following part matches your PostgreSQL setup:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Make sure your PostgreSQL server is running.

```
## 4. Install Dependencies
```

```
## 5. Apply Migrations 
```
python manage.py makemigrations
python manage.py migrate

```
### 6. Run Development Server
```
python manage.py runserver
Open http://127.0.0.1:8000

```
# 🔐 Authentication (JWT)

### Register
```
POST /api/auth/register/
Body:
{
  "username": "john",
  "email": "john@example.com",
  "password": "your_password"
}

```
### Login (Get JWT Token)
```
POST /api/auth/login/
Body:
{
  "username": "john",
  "password": "your_password"
}

```
You will receive:
```
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}

```
## 🔄 Sample Data Usage (Postman or curl)
``` ```
Set your Bearer token in headers:
```
Authorization: Bearer your_access_token

```
Add Doctor
```
POST /api/doctors/
{
  "name": "Dr. Smith",
  "specialty": "Cardiology",
  "contact": "dr.smith@example.com"
}

```
Add Patient
```
POST /api/patients/
{
  "name": "Alice",
  "age": 30,
  "gender": "Female",
  "medical_history": "Asthma"
}

```
Assign Doctor to Patient
```
POST /api/mappings/
{
  "patient": 1,
  "doctor": 1
}

```
# 📁 API Endpoints Summary

## Auth
```
- POST /api/auth/register/ – Register user

- POST /api/auth/login/ – Login and get JWT

- POST /api/auth/refresh/ – Refresh token

```
## Doctors
```

- GET /api/doctors/ – List doctors

- POST /api/doctors/ – Add doctor

- GET /api/doctors/<id>/ – Doctor details

- PUT /api/doctors/<id>/ – Update doctor

- DELETE /api/doctors/<id>/ – Delete doctor

```
## Patients
```

- GET /api/patients/ – List your patients

- POST /api/patients/ – Add patient

- GET /api/patients/<id>/ – Patient details

- PUT /api/patients/<id>/ – Update patient

- DELETE /api/patients/<id>/ – Delete patient

```
## Mappings
```

- POST /api/mappings/ – Assign doctor to patient

- GET /api/mappings/ – All mappings

- GET /api/mappings/<patient_id>/ – Patient's doctors

- DELETE /api/mappings/<id>/ – Remove mapping

```
# 🧪 Testing
```
Use Postman to test all authenticated routes with your Bearer Token.

You can also access Django Admin: http://127.0.0.1:8000/admin

```
# 📌 Notes
```
Make sure PostgreSQL server is running on your system.

You can use tools like pgAdmin or psql CLI to inspect your database.

Protect your .env and don't upload it to GitHub.

```
# 👨‍💻 Author
```
Yashwanth S

GitHub: @syashwanths
