from rest_framework import serializers
from .models import CourseBooking


class CourseBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseBooking
        fields = '__all__'

