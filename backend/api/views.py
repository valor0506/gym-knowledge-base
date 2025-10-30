import os
import requests
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Load .env
load_dotenv("C:/Users/suvan/gym-knowledge-base/backend/.env")

# Make sure your .env file has:
# GEMINI_API_KEY=AIzaSy........
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("DEBUG GEMINI KEY:", GEMINI_API_KEY)  # should not be None


# ---------------------------
# Gemini AI endpoint
# ---------------------------
@api_view(["POST"])
def ask_gemini(request):
    user_query = request.data.get("query", "")

    if not user_query:
        return Response({"error": "No query provided"}, status=400)

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }

    payload = {
        "contents": [
            {"parts": [{"text": user_query}]}
        ]
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        data = r.json()
        print("DEBUG RESPONSE:", data)

        reply = data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        reply = f"Sorry, something went wrong. Details: {str(e)}"

    return Response({"reply": reply})


# ---------------------------
# User Registration
# ---------------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    try:
        if not data.get("username") or not data.get("password"):
            return Response({"error": "Username and password required"}, status=400)

        if User.objects.filter(username=data["username"]).exists():
            return Response({"error": "Username already exists"}, status=400)

        user = User.objects.create(
            username=data["username"],
            email=data.get("email", ""),
            password=make_password(data["password"]),
        )
        return Response({"success": True, "message": "User registered"})
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=500)


# ---------------------------
# Get Current User
# ---------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
    })
