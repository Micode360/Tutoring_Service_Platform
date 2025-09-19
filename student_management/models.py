from django.db import models
from user.models import User
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    STUDENT_LEVEL = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.JSONField(default=list, blank=True)
    profile_picture = models.ImageField(upload_to="students/", null=True, blank=True)
    level = models.CharField(max_length=50, choices=STUDENT_LEVEL, default="beginner") 
    created_at = models.DateTimeField(default=timezone.now)  

