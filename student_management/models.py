from django.db import models
from user.models import User

# Create your models here.
class Student(models.Model):
    STUDENT_LEVEL = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.JSONField(default=list, blank=True)
    level = models.CharField(max_length=50, choices=STUDENT_LEVEL, blank=True)   

