from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.hashers import make_password

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
    
    def validate_password(self, value: str) -> str:
        return make_password(value)