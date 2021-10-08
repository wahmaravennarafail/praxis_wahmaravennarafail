from django.db import models

# Create your models here.

class project(models.Model) :
    nama = models.CharField(max_length=200)