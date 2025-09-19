from rest_framework import serializers
from .models import Student
from user.serializers import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id","user", "profile_picture","interests", "level"]
        read_only_fields = ("user",)
