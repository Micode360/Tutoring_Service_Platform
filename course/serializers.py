from rest_framework import serializers
from .models import Course




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title', 'description', 'video_file']
        read_only_fields = ('tutor',) # making this readonly so clients can't spoof it



