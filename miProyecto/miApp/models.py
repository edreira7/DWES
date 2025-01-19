from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Organizador' , 'organizador'),
        ('Participante' , 'participante'),
    ]
role = models.CharField(max_length=20, choices=ROLE_CHOICES)
bio = models.TextField(blank=True, null=True)

def __str__(self):
    return self.username


