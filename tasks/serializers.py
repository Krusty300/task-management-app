from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User registration
    """
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        """
        Create a new user with encrypted password
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']