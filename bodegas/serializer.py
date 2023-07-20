from rest_framework import serializers
from .models import *


class BodegasSerializer(serializers.ModelSerializer):
    region_nombre = serializers.CharField(source='region.region', required=False)
    class Meta:
        model = bodega
        fields = ['id','nombre', 'region', 'region_nombre']
        
class BodegaProductoSerializer(serializers.ModelSerializer):
    bodega_origen_nombre = serializers.CharField(source='bodega_origen.nombre', required=False)
    bodega_destino_nombre = serializers.CharField(source='bodega_destino.nombre', required=False)
    producto_nombre = serializers.CharField(source='producto.nombre', required=False)
    class Meta:
        model = bodegaProducto
        fields = ['bodega_origen', 'bodega_destino', 'producto', 'cantidad', 'bodega__origen_nombre', 'bodega_destino_nombre', 'producto_nombre']

class regionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = '__all__'