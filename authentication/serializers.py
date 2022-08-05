from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    """серіалізація юзера"""
    class Meta:
        model = User
        fields = '__all__'
