from django.db import models
from django.utils import timezone
from tutor_management.models import Tutor
from student_management.models import Student

# Create your models here.
class Course(models.Model):
    # One tutor can have many courses. (This is a one to many or many to one relationship)
    tutor = models.ForeignKey(Tutor, related_name="tutors_course", on_delete=models.CASCADE)  
    
    # Other datas about the course
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Upload video for the course to the folder media/courses/ and stores the part in the database
    video_file = models.FileField(upload_to="courses/", blank=True, null=True)
    
    # Many students can join many courses. (This is many to many)
    students = models.ManyToManyField(Student, related_name="courses") 

    # Time this course was created
    created_at = models.DateTimeField(default=timezone.now) 

    # Time this course was updated
    updated_at = models.DateTimeField(auto_now=True)
    

    