🧰 Django REST Framework – Product User Management API
A simple yet powerful RESTful API built with Django and Django REST Framework, supporting product and user management with full CRUD operations, authentication, pagination, and permission control.

🚀 Features
✅ CRUD for Products
🔐 User authentication using Django’s built-in auth system
🛂 Permission handling for protected routes (e.g., only owners can update/delete their data)
🔢 Pagination for scalable API responses
🧪 Data validation with Django REST Framework’s Serializers
🗂 Admin panel access for managing data easily
💾 SQLite as the development database (easily swappable with PostgreSQL/MySQL)
🧱 Technologies Used
Django
Django REST Framework
SQLite
Python
Postman (for testing API endpoints)
🧪 Installation & Local Setup
git clone https://github.com/kalyani996/DjangoRestFrameworkCRUD.git
cd projectname
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

🧪 Sample API Endpoints
| Method | Endpoint | Description | 
| GET | /api/products/ | List all products (paginated) | (owner only)
| POST | /api/products/ | Create new product | (owner only)
| GET | /api/products/:id/ | Retrieve single product | (owner only)
| PUT | /api/products/:id/ | Update product (owner only) | 
| DELETE | /api/products/:id/ | Delete product (owner only) | 

🔐 Authentication & Access Control
- User Creation:
There is no public registration or login endpoint.
All users are created directly via the Django Admin panel (/admin).
- Authentication Flow:
API access requires users to be authenticated through Django’s admin login session. Once logged in through the admin panel, users can interact with API endpoints using the Django REST Framework's built-in session authentication (via the browsable API interface).
- Permissions:
- Only authenticated users (those logged into the Django admin) can view or modify resources.
- The API is protected using DRF’s IsAuthenticated permission class.
- Fine-grained or per-object permissions (e.g., user ownership) can be implemented in future enhancements.

⚠️ Developer Note
To test the API locally, log in through the Django Admin panel (/admin) using a superuser account. All API routes will remain read-protected unless you are authenticated through the session-based admin login.


