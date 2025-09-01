from django.db import models
from tutor_management.models import Tutor
from student_management.models import Student

# Create your models here.
class Course(models.Model):
    tutor = models.ForeignKey(Tutor, related_name="tutors_course", on_delete=models.CASCADE) # One to many relationship
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to="courses/", blank=True, null=True)
    students = models.ManyToManyField(Student, related_name="courses") # Many to many relationships
    

    