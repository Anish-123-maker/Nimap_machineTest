# Nimap_machineTest

# Project: Client-User-Project API

This project is a Django REST Framework-based API for managing clients, users, and projects. It provides endpoints to create, update, and retrieve information about clients, users, and projects.

---

## Features
- Register and manage clients.
- Add and manage users.
- Create and assign projects to clients and users.
- Retrieve projects assigned to a user.

---

## Prerequisites

- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+
- MySQL database

---

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/project-api.git
   cd project-api
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database:**
   - Update the `DATABASES` section in `settings.py` with your MySQL credentials.
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

7. **Test the API:**
   Use Postman, cURL, or any HTTP client to interact with the API.

---

## How to Run Machine
1. Start your machine and ensure Python and MySQL are properly installed.
2. Activate the virtual environment using:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```

---

## How to Run DB Design
1. Log in to your MySQL server.
2. Create a new database:
   ```sql
   CREATE DATABASE project_api;
   ```
3. Update `settings.py` with the database credentials.
4. Apply migrations to create tables in the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## How to Run the Code
1. Clone the repository and set up the virtual environment.
2. Configure the database and apply migrations.
3. Start the server using:
   ```bash
   python manage.py runserver
   ```
4. Use Postman, cURL, or any HTTP client to test the API endpoints.

---

## API Endpoints

### **Client Management**
1. **Register a Client**
   - **Endpoint:** `POST /api/register-client/`
   - **Payload:**
     ```json
     {
         "client_name": "Client A",
         "created_by": "Admin"
     }
     ```

2. **Fetch All Clients**
   - **Endpoint:** `GET /api/fetch-clients/`

3. **Edit a Client**
   - **Endpoint:** `PUT /api/edit-client/<client_id>/`
   - **Payload:**
     ```json
     {
         "client_name": "Updated Client Name"
     }
     ```

4. **Delete a Client**
   - **Endpoint:** `DELETE /api/delete-client/<client_id>/`

### **User Management**
1. **Add a User**
   - **Endpoint:** `POST /api/add-user/`
   - **Payload:**
     ```json
     {
         "user_name": "John Doe",
         "user_email": "john.doe@example.com",
         "user_password": "securepassword"
     }
     ```

2. **Update a User**
   - **Endpoint:** `PUT /api/update-user/<user_id>/`
   - **Payload:**
     ```json
     {
         "user_name": "Updated User Name"
     }
     ```

3. **Fetch All Users**
   - **Endpoint:** `GET /api/fetch-users/`

### **Project Management**
1. **Add a Project**
   - **Endpoint:** `POST /api/add-project/`
   - **Payload:**
     ```json
     {
         "project_name": "Project A",
         "project_description": "Sample project description",
         "client": 1,
         "users": [1, 2],
         "created_by": "Admin"
     }
     ```

2. **Retrieve User's Projects**
   - **Endpoint:** `GET /api/user-projects/<user_id>/`

---

## Development Notes
- Use `PrimaryKeyRelatedField` for foreign key relationships to pass IDs.
- The `to_representation` method in serializers ensures nested data is included in responses.


