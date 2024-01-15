from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        print(f"Creating user with data: {validated_data}")
        user = CustomUser.objects.create_user(**validated_data)
        print(f"Created user: {user}")
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass  


