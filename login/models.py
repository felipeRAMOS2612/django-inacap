from django.db import models
from bodegas.models import region
# Create your models here.


class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    
    