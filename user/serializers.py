# users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Expose all fields. You can also list fields explicitly if preferred.
        fields = '__all__'
        read_only_fields = ('user_id', 'created_at', 'updated_at')
    
    # Optional: Validate that a user_role is provided and valid.
    def validate_user_role(self, value):
        valid_roles = [choice[0] for choice in User.USER_ROLE_CHOICES]
        if value not in valid_roles:
            raise serializers.ValidationError("Invalid user role provided.")
        return value
