from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'role', 'is_approved', 'confirm_password']

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "the password does not match."})
        
        validate_password(attrs["password"]) # Checks if the password is strong
        return attrs
    

    def create(self, validated_data):
        user = User(
            first_name = validated_data.get("first_name"),
            last_name = validated_data.get("last_name"),
            email = validated_data.get("email"),
            role = validated_data.get("role")
        )
        user.set_password(validated_data.get("password"))
        user.save()
        return user
