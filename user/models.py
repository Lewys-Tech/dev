from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)

    USER_ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('other', 'Other'),
    ]
    user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)

    password = models.CharField(max_length=128)  # Stores hashed passwords
    
    is_active = models.BooleanField(default=True)  # Required for authentication
    is_staff = models.BooleanField(default=False)  # Required for admin access
    is_superuser = models.BooleanField(default=False)  # For superuser permissions
    
    status = models.CharField(max_length=20, default='Active')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Required attributes for Django's authentication system:
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name']

    def set_password(self, raw_password):
        """Hashes and sets the user's password."""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Checks the given password against the stored hashed password."""
        return check_password(raw_password, self.password)
    
     # These properties help Django's authentication system work as expected.
    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __str__(self):
        return f"{self.first_name} {self.second_name} ({self.user_role})"




class Student(models.Model):
    # The student's primary key is also the foreign key to the user.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        primary_key=True,
        related_name='student_profile'
    )
    
    adm_no = models.CharField(max_length=50, unique=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    enrollment_year = models.PositiveIntegerField(blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128, default="defaultpassword")  # Temporary default

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Student: {self.user.first_name} {self.user.second_name} (Adm No: {self.adm_no})"


class Staff(models.Model):
    # The primary key for staff is also a foreign key to the user model.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='staff_profile'
    )
    
    staff_no = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Staff: {self.user.first_name} {self.user.second_name} (No: {self.staff_no})"
    


class OtherUser(models.Model):
    # The primary key is also a foreign key to the User model (referenced via settings.AUTH_USER_MODEL)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='other_user_profile'
    )
    user_no = models.CharField(max_length=50)  # VARCHAR NOT NULL
    residence = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"OtherUser: {self.user_no} - {self.user}"
   