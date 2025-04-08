# 📝 Django To-Do List API

A simple and RESTful API built with **Django** and **Django REST Framework** for managing To-Do List. This project was developed as part of a machine test for Aifer Education Pvt Ltd.


---

## 🚀 Features

- ✅ Create, view, update, and delete to-do items
- 🕒 Automatically tracks creation time
- 📦 Clean and consistent API responses
- ⚙️ Built using class-based API views (`APIView`)

---

## 📦 Requirements

- Python 3.10
- Django 4.2
- Django REST Framework

---

## 🛠️ Project Structure

<pre>todolist/
├── api/
│   └── v1/
│       └── todo_list/
│           ├── serializers.py       # Handles data serialization/deserialization
│           ├── urls.py              # API routing
│           └── views.py             # API view logic
├── media/                           # Media file storage
├── static/                          # Static files (CSS, JS, etc.)
├── todo_list/                       # Project configuration
│   ├── asgi.py
│   ├── settings.py                  # Django project settings
│   ├── urls.py                      # Root URL configuration
│   └── wsgi.py
├── todoList/                        # Main application for to-do logic
│   ├── admin.py                     # Admin panel integration
│   ├── apps.py                      # App configuration
│   ├── migrations/                  # Database migration files
│   ├── models.py                    # Database models
│   ├── tests.py                     # Unit tests
│   └── views.py                     # Web views (if any)
├── manage.py                        # Django CLI utility
├── README.md                        # Project documentation
└── requirements.txt                 # Project dependencies
</pre>



## 📖 Setup Instructions

Follow these steps to set up and run the Django To-Do List API on your local environment:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sinsiya/todo-task.git
   
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv

3. **Activate the virtual environment**:
   ```bash
   \venv\Scripts\activate
   
4. **Install Project Dependencies**:
   ```bash
   pip install -r requirements.txt
   
5. **Set Up the Database**:
   ```bash
   python manage.py migrate
   
6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   
7. **Test the API**:

   Use tools like Postman, cURL, or a browser to interact with the API.

---

## 📡 API Endpoints

| Method | Endpoint                         | Description              |
|--------|----------------------------------|--------------------------|
| GET    | `/api/v1/todo/`                  | Retrieve all to-do items |
| POST   | `/api/v1/todo/`                  | Create a new to-do item  |
| GET    | `/api/v1/todo/details/<id>/`     | Retrieve a specific item |
| PUT    | `/api/v1/todo/details/<id>/`     | Update an existing item  |
| DELETE | `/api/v1/todo/details/<id>/`     | Delete a specific item   |
---

## 🌐 API Usage Examples

### 📥 Create a New To-Do (POST)
**Endpoint:** `/api/v1/todo/`  
**Method:** `POST`  
**Request Body:**
```json
{
  "title": "Complete Machine Test",
  "description": "Build the To-Do List API for Aifer Education Pvt Ltd",
  "completed": false
}

```
**Sample Response**:
```json
{
  "statuscode": 201,
  "title": "To-Do Created",
  "data": {
    "id": 1,
    "title": "Complete Machine Test",
    "description": "Build the To-Do List API for Aifer Education Pvt Ltd",
    "completed": false,
    "created_at": "2025-04-08T10:30:00Z"
  },
  "errors": "",
  "message": "To-Do item created successfully."
}
```
### 📤 Retrieve All To-Dos (GET)
**Endpoint:** `/api/v1/todo/`

**Method:** `GET`

**Sample Response**:
```json
{
  "statuscode": 200,
  "title": "Data received",
  "data": [
    {
      "id": 1,
      "title": "Complete Machine Test",
      "description": "Build the To-Do List API for Aifer Education Pvt Ltd",
      "completed": false,
      "created_at": "2025-04-08T10:30:00Z"
    }
  ],
  "errors": "",
  "message": "To-Do items received successfully."
}

```
### 🧾 Retrieve a Single To-Do (GET)

**Endpoint:** `/api/v1/todo/details/<id>/`  
**Method:** `GET`  
**Example:** `/api/v1/todo/details/1/`

**Sample Response:**
```json
{
  "statuscode": 200,
  "title": "Item Retrieved",
  "data": {
    "id": 1,
    "title": "Complete Machine Test",
    "description": "Build the To-Do List API for Aifer Education Pvt Ltd",
    "completed": false,
    "created_at": "2025-04-08T10:30:00Z"
  },
  "errors": "",
  "message": "To-Do item fetched successfully."
}

```
### ✏️ Update a To-Do (PUT)

**Endpoint:** `/api/v1/todo/details/<id>/`  
**Method:** `PUT`  
**Example:** `/api/v1/todo/details/1/`

**Request Body:**
```json
{
  "title": "Complete Machine Test - Updated",
  "description": "Update the To-Do List API for Aifer Education Pvt Ltd",
  "completed": true
}
```
**Sample Response:**
```json
{
  "statuscode": 200,
  "title": "Item Updated",
  "data": {
    "id": 1,
    "title": "Complete Machine Test - Updated",
    "description": "Update the To-Do List API for Aifer Education Pvt Ltd",
    "completed": true,
    "created_at": "2025-04-08T10:30:00Z"
  },
  "errors": "",
  "message": "To-Do item updated successfully."
}

```
### 🗑️ Delete a To-Do (DELETE)

**Endpoint:** `/api/v1/todo/details/<id>/`  
**Method:** `DELETE`  
**Example:** `/api/v1/todo/details/1/`  

**Sample Response:**
```json
{
  "statuscode": 204,
  "title": "Deleted",
  "data": "",
  "errors": "",
  "message": "To-Do item deleted successfully."
}
```












