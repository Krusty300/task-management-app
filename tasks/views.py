from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a task to edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner
        return obj.user == request.user

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model with automatic filtering per user
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        """
        This ensures users only see their own tasks
        """
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        
        # Optional: Filter by status if query param is provided
        # Example: GET /api/tasks/?status=completed
        status_filter = self.request.query_params.get('status', None)
        if status_filter in ['pending', 'completed']:
            queryset = queryset.filter(status=status_filter)
            
        return queryset
    
    def perform_create(self, serializer):
        """
        Automatically assign the authenticated user to the task
        """
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        """
        Custom action to toggle task completion status
        POST /api/tasks/{id}/toggle_complete/
        """
        task = self.get_object()
        task.status = 'completed' if task.status == 'pending' else 'pending'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    """
    View for user registration
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer