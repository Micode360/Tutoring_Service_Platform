from rest_framework import serializers
from .models import Tutor
from user.serializers import UserSerializer


class TutorSerializer(serializers.ModelSerializer):
    tutor = UserSerializer(read_only=True)
    class Meta:
        model = Tutor
        fields = ["id", "tutor", "bio", "profile_picture", "rating", "is_verified"]
        read_only_fields = ('tutor',)
