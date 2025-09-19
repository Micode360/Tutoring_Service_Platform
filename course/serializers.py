from rest_framework import serializers
from .models import Course
from student_management.models import Student
from tutor_management.serializers import TutorSerializer



class CourseSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id','title', 'description', 'video_file', 'tutor']

        # tutor is filled in automatically by backend
        # keep it read-only so students/clients cannot fake it.
        # This prevents an attack called spoofing. Adding data to account that is not yours 
        # to make it look like the owner of the account added it.
        read_only_fields = ('tutor',)
