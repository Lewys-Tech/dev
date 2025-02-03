from django.db import models

class User(models.Model):
    # Define allowed user roles for data integrity
    USER_ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('other', 'Other'),
    ]
    
    # Fields based on your SQL table definition
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)
    status = models.CharField(max_length=20, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.second_name} ({self.user_role})"
