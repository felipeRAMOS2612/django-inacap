from django.db import models
from productos.models import *
from login.models import Usuario
# Create your models here.
class region(models.Model):
    region = models.CharField(max_length=100)

class bodega(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(region, on_delete=models.CASCADE)
    
class BodegaProducto(models.Model):
    bodega = models.ForeignKey(bodega, on_delete=models.CASCADE)
    producto = models.ForeignKey(libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.bodega.nombre} - {self.producto.tipo} - {self.producto.editorial.nombre}'

class MovimientoBodega(models.Model):
    bodega_origen = models.ForeignKey(bodega, on_delete=models.CASCADE)
    bodega_destino = models.ForeignKey(bodega, on_delete=models.CASCADE, related_name="movimientos_destino")
    productos = models.ManyToManyField(BodegaProducto, through='DetalleMovimiento')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class DetalleMovimiento(models.Model):
    movimiento = models.ForeignKey(MovimientoBodega, on_delete=models.CASCADE)
    bodega_producto = models.ForeignKey(BodegaProducto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

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
