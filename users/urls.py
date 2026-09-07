from django.urls import path
from .views import (
    RegisterUser,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("register/",RegisterUser.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("refresh/",TokenRefreshView.as_view()),
    path(
        "password-reset/",
        PasswordResetRequestView.as_view()
    ),

    path(
        "password-reset-confirm/",
        PasswordResetConfirmView.as_view()
    ),
]