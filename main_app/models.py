from re import S
from django.db import models

# Create your models here.

class Strategy(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
class Kit(models.Model):
    date = models.DateField()
    strategy = models.ManyToManyField(Strategy)
    
class State(models.Model):
    confirmed = models.IntegerField()
    death = models.IntegerField()
    lat = models.CharField(max_length = 10)
    long = models.CharField(max_length = 10)