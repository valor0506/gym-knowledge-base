from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path("", views.ask_gemini, name="ask_gemini"),
    path("register/", views.register_user, name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),   # JWT login
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh JWT
    path("me/", views.current_user, name="current_user"),
]
