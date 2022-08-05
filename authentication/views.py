from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import generics, permissions, status


class UserSerializer(generics.ListCreateAPIView):
    """представлення юзера"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

