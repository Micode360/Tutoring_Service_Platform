# 🎓 Tutorial Service Platform

A Django REST Framework (DRF) based API project where **tutors can upload video tutorials** and **users can subscribe** to access those videos.

---

## 🚀 Features
- 👩‍🏫 Tutors can register and upload tutorial videos.  
- 👨‍🎓 Users can sign up and subscribe to tutorials.  
- 🔐 JWT Authentication for secure login & signup.  
- 📧 OTP email system for password reset.  
- 📚 API documentation with Swagger & Redoc.  

---

## ⚙️ Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Micode360/Tutoring_Service_Platform
cd Tutoring_Service_Platform

# 2️⃣ Create & activate a virtual environment
python -m venv myenv
myenv\Scripts\activate   # On Windows
# source myenv/bin/activate   # On Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Setup environment variables in .env
# Example:
# SECRET_KEY=your_django_secret_key
# DEBUG=True
# DATABASE_URL=sqlite:///db.sqlite3
# EMAIL_HOST_USER=youremail@example.com
# EMAIL_HOST_PASSWORD=yourpassword

# 5️⃣ Run migrations
python manage.py migrate

# 6️⃣ Start the server
python manage.py runserver
