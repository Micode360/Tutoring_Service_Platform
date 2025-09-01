from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Manager

# Create your models here.
class User(AbstractUser): # Template
    USER_ROLES = (
      ('student', 'Student'),
      ('tutor', 'Tutor'),
      ('admin', 'Admin')
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = None
    role = models.CharField(max_length=20, choices=USER_ROLES) 
    is_approved = models.BooleanField(default=False) # Made boolean field false
    phone = models.CharField(max_length=20)

    USERNAME_FIELD = 'email' # Use email as the unique identifier
    REQUIRED_FIELDS = []

    objects = Manager() 

    def __str__(self):
        return self.email