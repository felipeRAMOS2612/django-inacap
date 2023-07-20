from django.db import models
from productos.models import *
from login.models import Usuario
# Create your models here.
class region(models.Model):
    region = models.CharField(max_length=100)

class bodega(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(region, on_delete=models.CASCADE)
    
class bodegaProducto(models.Model):
    bodegaOrigen = models.ForeignKey(bodega, on_delete=models.CASCADE, verbose_name="Bodega de origen", related_name="bodega_origen", null=True)
    bodegaDestino = models.ForeignKey(bodega, on_delete=models.CASCADE, verbose_name="Bodega de destino", related_name="bodega_destino", null=True)
    producto = models.ForeignKey(libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)


class movimiento_por(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    bodega_origen = models.ForeignKey(
        bodega,
        verbose_name=("Bodega de origen"),
        on_delete=models.CASCADE,
        related_name="origen",  # Cambia este nombre para el acceso inverso desde la Bodega
    )
    bodega_destino = models.ForeignKey(
        bodega,
        on_delete=models.CASCADE,
        verbose_name="Bodega de destino",
        related_name="destino",  # Cambia este nombre para el acceso inverso desde la Bodega
    )
