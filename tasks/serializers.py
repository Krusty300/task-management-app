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
    is_overdue = serializers.SerializerMethodField()  # NEW: Computed field
    
    class Meta:
        model = Task
        fields = [
            'id', 'user', 'title', 'description', 'status', 
            'priority', 'due_date', 'is_overdue',  # Added due_date and priority
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'is_overdue']
    
    def get_is_overdue(self, obj):
        """Check if task is overdue"""
        return obj.is_overdue()