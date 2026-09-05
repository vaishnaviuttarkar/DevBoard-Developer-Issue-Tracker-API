from rest_framework import generics
from .serializers import RegisterSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer