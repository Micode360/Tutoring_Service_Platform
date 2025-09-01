from django.db import models
from tutor_management.models import Tutor

# Create your models here.
class Course(models.Model):
    tutor = models.ForeignKey(Tutor, related_name="tutors_course", on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to="media/courses/", blank=True, null=True)
    