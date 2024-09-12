from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.object.all()
    serializer_class = RegisterSerializer