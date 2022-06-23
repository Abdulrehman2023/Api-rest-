from pyexpat import model
from django.db import models

# Create your models here.

class APi_default(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)

    def __str__(self):
         return self.Firstname


