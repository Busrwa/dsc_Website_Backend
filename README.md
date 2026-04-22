# 🎓 DSC HKU Website – Backend

Django REST Framework API powering the official website of the 
Developer Student Clubs chapter at Hasan Kalyoncu University.
Deployed on Render with PostgreSQL. Live at: https://dschku.com

## ⚙️ Tech Stack
- Django + Django REST Framework
- PostgreSQL (Django ORM)
- Cloudinary (image storage & transformation)
- DRF Token Authentication
- Render deployment

## 💡 Features
- Public read-only endpoints (events, blog posts, sponsors)
- Admin write endpoints with token authentication
- Cloudinary integration via custom DRF serializer
- CORS restricted to production frontend domain
- Rich text (Quill.js HTML) stored with server-side sanitization

## 📡 API Endpoints
| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/api/events/` | GET | None | List all events |
| `/api/posts/` | GET | None | List blog posts |
| `/api/sponsors/` | GET | None | List sponsors |
| `/api/events/` | POST | Token | Create event |
| `/api/posts/{id}/` | PATCH | Token | Update post |

## 🔗 Related
- Frontend: [DSC HKU React App](https://github.com/Busrwa/dsc_Website_Frontend)
- Live Site: https://dschku.com

## 🚀 Getting Started
```bash
git clone https://github.com/Busrwa/dsc_Website_Backend.git
cd dsc_Website_Backend
pip install -r requirements.txt
# Add .env with: DATABASE_URL, CLOUDINARY_URL, SECRET_KEY
python manage.py migrate
python manage.py runserver
```
