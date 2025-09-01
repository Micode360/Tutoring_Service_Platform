from django.db import models
from user.models import User

# Create your models here.
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    subjects_taught = models.JSONField(default=list, blank=True)
    
    