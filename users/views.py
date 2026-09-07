from rest_framework import generics
from rest_framework.response import Response

from .serializers import (
    RegisterSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
    )

from django.core.mail import send_mail
from django.conf import settings

class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data = request.data
        )

        serializer.is_valid(raise_exception=True)

        if "uid" in serializer.validated_data:
            uid = serializer.validated_data['uid']
            token = serializer.validated_data['token']

            reset_link = (
                f"http://127.0.0.1:8000/password-reset/"
                f"{uid}/{token}"
            )

            send_mail(
                subject="Password Reset",
                message=f"Reset your password using this link: \n\n {reset_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[serializer.validated_data['email']]
            )

        return Response(
            {
                "detail": "If an account with this email exists, then a password reset link has been generated"
            }
        )

class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data = request.data
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "detail": "Password has beene reset successfully."
            }
        )