# 🍽️ Cafeteria API

A production-ready REST API for cafeteria management — built with Django REST Framework, JWT authentication, and SQLite. Inspired by HungerBox's B2B cafeteria digitization platform.

## 🚀 Features
- CRUD endpoints for Menu Items (name, price, category, availability)
- JWT-authenticated Order placement
- Category-based search/filter
- Admin panel at `/admin/`

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=flat&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat&logo=jsonwebtokens&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white)

## 📡 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/api/menu/` | ❌ | List all menu items |
| POST | `/api/menu/` | ❌ | Add menu item |
| PUT | `/api/menu/{id}/` | ❌ | Update item |
| DELETE | `/api/menu/{id}/` | ❌ | Delete item |
| GET | `/api/menu/?search=drinks` | ❌ | Filter by category |
| POST | `/api/orders/` | ✅ JWT | Place an order |
| GET | `/api/orders/` | ✅ JWT | List all orders |
| POST | `/api/token/` | ❌ | Get JWT token |
| POST | `/api/token/refresh/` | ❌ | Refresh token |

## ⚡ Quick Start
```bash
# Clone karo
git clone https://github.com/sandeshsingh1/cafeteria-api.git
cd cafeteria-api

# Virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Run karo
python manage.py runserver
```

## 🔐 JWT Auth Example
```bash
# Token lo
POST /api/token/
{"username": "admin", "password": "yourpassword"}

# Order place karo
POST /api/orders/
Headers: Authorization: Bearer <access_token>
Body: {"item": 1, "quantity": 2, "total_price": "100.00", "status": "pending"}
