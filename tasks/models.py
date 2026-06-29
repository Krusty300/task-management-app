from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Task model - each task belongs to a specific user
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending'
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    due_date = models.DateTimeField(null=True, blank=True)  # NEW: Due date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest first
    
    def __str__(self):
        return self.title
    
    def mark_completed(self):
        """Helper method to mark task as completed"""
        self.status = 'completed'
        self.save()
    
    def is_overdue(self):
        """Check if task is overdue"""
        if self.due_date and self.status != 'completed':
            from django.utils import timezone
            return self.due_date < timezone.now()
        return False