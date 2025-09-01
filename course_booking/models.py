from django.db import models
from tutor_management.models import Tutor
from student_management.models import Student

# Create your models here.
class CourseBooking(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Student, related_name="booked_sessions", null=True)
    expectations = models.TextField(blank=True)
