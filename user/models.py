from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, second_name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, first name, second name, and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            second_name=second_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, second_name, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, first name, second name, and password.
        """
        
        extra_fields.setdefault('is_active', True)

        

        return self.create_user(email, first_name, second_name, password, **extra_fields)

    def get_by_natural_key(self, email):
        """
        Allows authentication using the natural key (email).
        """
        return self.get(email=email)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)

    USER_ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('other', 'Other'),
    ]
    user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)

    status = models.CharField(max_length=20, default='Active')

    # Required for Django's admin and authentication:
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # Set email as the unique identifier for authentication.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name']

    def __str__(self):
        return f"{self.first_name} {self.second_name} ({self.user_role})"



class Student(models.Model):
    # The student's primary key is also the foreign key to the user.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
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
        related_name='other_user_profile'
    )
    user_no = models.CharField(max_length=50)  # VARCHAR NOT NULL
    residence = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"OtherUser: {self.user_no} - {self.user}"
   