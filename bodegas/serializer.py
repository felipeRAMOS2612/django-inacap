from rest_framework import serializers
from .models import *


class BodegasSerializer(serializers.ModelSerializer):
    region_nombre = serializers.CharField(source='region.region', required=False)
    class Meta:
        model = bodega
        fields = ['id','nombre', 'region', 'region_nombre']
        
class DetalleMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleMovimiento
        fields = ('bodega_producto', 'cantidad')

class MovimientoBodegaSerializer(serializers.ModelSerializer):
    detalles = DetalleMovimientoSerializer(many=True)

    class Meta:
        model = MovimientoBodega
        fields = ('bodega_origen', 'bodega_destino', 'usuario', 'fecha', 'detalles')

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        movimiento = MovimientoBodega.objects.create(**validated_data)

        for detalle_data in detalles_data:
            DetalleMovimiento.objects.create(movimiento=movimiento, **detalle_data)

        return movimiento

class regionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = '__all__'