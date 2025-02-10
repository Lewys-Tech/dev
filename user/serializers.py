# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Student, Staff, OtherUser

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'second_name', 'email', 'phone', 'user_role', 'status', 'created_at', 'updated_at', 'password', 'is_active']
        read_only_fields = ('user_id', 'created_at', 'updated_at')

    def validate_user_role(self, value):
        valid_roles = [choice[0] for choice in User.USER_ROLE_CHOICES]
        if value not in valid_roles:
            raise serializers.ValidationError("Invalid user role provided.")
        return value

    

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    
    class Meta:
        model = Student
        fields = [
            'id',
            'user',
            'adm_no',
            'branch',
            'enrollment_year',
            'level',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # Get the current user from the serializer context
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["user"] = request.user
        else:
            raise serializers.ValidationError("User must be authenticated.")
        return super().create(validated_data)


class StaffSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    
    
    
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
    def create(self, validated_data):
        # Get the current user from the serializer context
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["user"] = request.user
        else:
            raise serializers.ValidationError("User must be authenticated.")
        return super().create(validated_data)


class OtherUserSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = OtherUser
        fields = ['user', 'user_id', 'user_no', 'residence', 'age', 'gender', 'phone']

    def create(self, validated_data):
        # Get the current user from the serializer context
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["user"] = request.user
        else:
            raise serializers.ValidationError("User must be authenticated.")
        return super().create(validated_data)