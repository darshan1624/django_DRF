from django.db import models

# Create your models here

class Student(models.Model):
    name = models.CharField(max_length=800)
    roll = models.IntegerField(max_length=800)
    city = models.CharField(max_length=800)
