from rest_framework import serializers
from .models import Course
from student_management.models import Student



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title', 'description', 'video_file']

        # tutor is filled in automatically by backend
        # keep it read-only so students/clients cannot fake it.
        # This prevents an attack called spoofing. Adding data to account that is not yours 
        # to make it look like the owner of the account added it.
        read_only_fields = ('tutor',)




class SubscribeSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()

    # Using validation to check if the student exists.
    def validate_student_id(self, value):
        if not Student.objects.filter(id=value).exists():
            raise serializers.ValidationError("Student does not exist.")
        return value