# Django Student Management Portal

This is a Django-based web application for managing student data. It includes an interactive, premium-designed UI built with Bootstrap 5 and custom CSS styling.

## Features
- **Student Roster**: Dynamically pulls student information (name, course, age, roll number) from a SQLite database.
- **Modern UI**: Uses glassmorphism and subtle CSS animations for an engaging look.
- **Django Templates**: Cleanly separates structure and styles by using Django template includes.

## Requirements
- Python 3.x
- Django 6.x

## How to Run

1. **Activate the Virtual Environment**
   ```bash
   venv\Scripts\activate
   ```

2. **Install Requirements (if needed)**
   ```bash
   pip install django
   ```

3. **Run Migrations**
   ```bash
   cd myproject
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Open your browser to `http://127.0.0.1:8000/`.
