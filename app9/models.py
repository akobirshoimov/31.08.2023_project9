from django.db import models
from datetime import datetime

# Create your models here.
class Moshinalar(models.Model):
    name = models.CharField(max_length=100,default='Onix')
    colour = models.CharField(max_length=50,default=' ')
    year = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=120,default='Uzbekiston')
    location = models.CharField(max_length=110)
    
    def __str__(self) -> str:
        return self.name
