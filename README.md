# 🪪 ID Card Generator – Django & MySQL

A **web-based ID Card Management System** built using **Django** and **MySQL**.  
This application allows admins to manage **employees, departments, admins**, and **generate ID cards** from a centralized dashboard.

---

## 🚀 Features

### 🔐 Authentication & Admin Management
- Admin login & logout
- Add new admin users
- Secure dashboard access

### 👨‍💼 Employee Management
- Add employee with:
  - Unique Employee ID
  - Full name
  - Email (used as username)
  - Phone number (with country code)
  - Department
  - Profile photo
- Update employee details
- Delete employees
- View employee list

### 🏢 Department Management
- Add department
- Edit department
- Delete department
- Search departments
- Department count
- **Delete protection**: Departments cannot be deleted if employees are assigned

### 🪪 ID Card Generator
- Generate ID cards using employee data
- ID card includes:
  - Profile photo
  - Employee name
  - Employee ID
  - Department name
  - Contact details

### 📊 Dashboard
- Central dashboard connecting all modules
- Displays:
  - Total employees
  - Total departments
  - Total admins
- Quick navigation buttons

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Database:** MySQL
- **Frontend:** HTML, CSS (Django Templates)
- **Authentication:** Django Auth System
- **Media Handling:** Django Media Files

---

## 📂 Project Structure
```bash
idcard/
│── idcard/ # Project settings
│── idcardapp/ # Main application
│ ├── models.py # Employee & Department models
│ ├── views.py # Views & logic
│ ├── urls.py # App URLs
│ ├── forms.py # Django forms
│── templates/ # HTML templates
│── media/ # Uploaded profile photos
│── static/ # CSS / JS files
│── manage.py
```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/siddh-exe/idcard.git
cd idcard
```
---
## Install Dependencies
```bash
pip install django mysqlclient pillow
```
## Configure MySQL Database
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'idcard_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
## Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
## Create Admin User
```bash
python manage.py createsuperuser
```
## Run Server
```bash
python manage.py runserver
```
Open browser 👉 http://127.0.0.1:8000/
---

## 🔑 Key Django Concepts Used

Custom relationships using related_name

Department delete protection

Django authentication system

Media file upload handling

Django messages framework

Login-required views
---

## 📌 Future Enhancements

Download ID card as PDF

Role-based permissions (Super Admin / Sub Admin)

Search & filter employees

Responsive UI design
---

## 👨‍💻 Author

Siddhesh
Python & Django Developer
---

## 📜 License

This project is developed for learning and educational purposes.
