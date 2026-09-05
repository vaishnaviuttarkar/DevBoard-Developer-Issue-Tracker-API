from django.urls import path
from .views import RegisterUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("register/",RegisterUser.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("refresh/",TokenRefreshView.as_view()),
]