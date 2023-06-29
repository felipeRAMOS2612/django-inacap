from django.db import models

# Create your models here.
class region(models.Model):
    region = models.CharField(max_length=100)

class bodega(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)