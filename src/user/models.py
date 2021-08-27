from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE = (
        ('Admin', 'Admin'),
        ('HR', 'HR'),
        ('PM', 'PM'),
        ('Developer', 'Developer'),
    )
    
    role = models.CharField(choices=USER_ROLE, max_length=50)