from django.db import models
# Create your models here.
class editorial(models.Model):
    nombre = models.CharField(max_length=100)
    
class autor(models.Model):
    nombre = models.CharField(max_length=100)
    
class tipo_de_genero(models.Model):
    tipo = models.CharField(max_length=100)

class libro(models.Model):
    nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)
    tipo = models.ForeignKey(tipo_de_genero, verbose_name="genero", on_delete=models.CASCADE)
    editorial = models.ForeignKey(editorial, on_delete=models.CASCADE)
    
class publicado_por(models.Model):
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
