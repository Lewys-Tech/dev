# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Student, Staff, OtherUser

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'second_name', 'email', 'phone', 'user_role', 'status', 'created_at', 'updated_at', 'password', 'is_active', 'is_staff', 'is_superuser']
        read_only_fields = ('user_id', 'created_at', 'updated_at')

    def validate_user_role(self, value):
        valid_roles = [choice[0] for choice in User.USER_ROLE_CHOICES]
        if value not in valid_roles:
            raise serializers.ValidationError("Invalid user role provided.")
        return value

    

class StudentSerializer(serializers.ModelSerializer):
    # Nested representation of the related user (read-only)
    user = UserSerializer(read_only=True)
    # Write-only field for associating a user by primary key
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        write_only=True,
        queryset=User.objects.all()
    )
    
    class Meta:
        model = Student
        fields = [
            'user',        # Nested user data, read-only
            'user_id',     # For associating a user on write operations
            'adm_no',
            'branch',
            'enrollment_year',
            'level',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
        

class StaffSerializer(serializers.ModelSerializer):
    # Include nested read-only user details
    user = UserSerializer(read_only=True)
    # Write-only field to set the related user via primary key
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        write_only=True,
        queryset=User.objects.all()
    )
    
    class Meta:
        model = Staff
        fields = [
            'user',         # Nested user data (read-only)
            'user_id',      # Write-only field to assign a user
            'staff_no',
            'department',
            'start_year',
            'category',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class OtherUserSerializer(serializers.ModelSerializer):
    # Provide a nested, read-only representation of the associated user
    user = UserSerializer(read_only=True)
    # Allow the client to set the user by primary key when creating/updating an OtherUser record.
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        write_only=True,
        queryset=User.objects.all()
    )
    
    class Meta:
        model = OtherUser
        fields = ['user', 'user_id', 'user_no', 'residence', 'age', 'gender', 'phone']