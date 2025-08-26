
# 🏋️ Gym Knowledge Base

A **full-stack web application** that helps fitness enthusiasts learn about gym terms, track progress, and explore supplements.  
Includes **AI-powered Q&A** using Gemini API and follows **secure coding practices** with JWT authentication and CI/CD pipelines.

---

## 🚀 Features
- 📚 **Gym Dictionary** — learn fitness terms.  
- 📈 **Progress Tracking** — log workouts, weight, and progress.  
- 💊 **Supplements Guide** — natty vs enhanced info.  
- 🤖 **AI Assistant** — ask fitness questions powered by Gemini API.  
- 🔐 **Secure Auth** — JWT-based login & signup.  
- ⚡ **CI/CD** — Automated testing + deployment via GitHub Actions.  

---

## 🛠️ Tech Stack
- **Frontend**: React (TypeScript), TailwindCSS  
- **Backend**: Django REST Framework  
- **Database**: PostgreSQL  
- **AI Integration**: Gemini API (Google) → future HuggingFace/LLMs  
- **CI/CD**: GitHub Actions, Render (backend), Vercel (frontend)  
- **Security**: HTTPS, JWT Auth, OWASP best practices  

---

## ⚙️ Installation & Setup

### 1️⃣ Backend (Django)
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
