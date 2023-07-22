from django.shortcuts import render
from requests import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics
from .serializer import *
from .models import *
# Create your views here.

class BodegasView(viewsets.ModelViewSet):
    serializer_class = BodegasSerializer
    queryset = bodega.objects.all()

class BodegasCreate(generics.ListCreateAPIView):
    serializer_class = BodegasSerializer
    queryset = bodega.objects.all()

@api_view(['POST'])
def mover_productos_entre_bodegas(request):
    bodega_origen_id = request.data.get('bodega_origen_id')
    bodega_destino_id = request.data.get('bodega_destino_id')
    producto_id = request.data.get('producto_id')
    cantidad_a_mover = request.data.get('cantidad')
    usuario = request.user
    # Obtener los registros de BodegaProducto correspondientes a la bodega de origen y destino
    
    try:
         bodega_origen_producto = BodegaProducto.objects.get(bodega__id=bodega_origen_id, producto__id=producto_id)
         bodega_destino_producto, created = BodegaProducto.objects.get_or_create(bodega__id=bodega_destino_id, producto__id=producto_id)
    except BodegaProducto.DoesNotExist:
         return Response({"message": "El producto no existe en la bodega de origen."}, status=400)
    except BodegaProducto.MultipleObjectsReturned:
         return Response({"message": "Hay varios productos con la misma combinación de bodega de destino y producto."}, status=400)

    if bodega_origen_producto.cantidad < cantidad_a_mover:
        return Response({"message": "No hay suficiente cantidad en la bodega de origen."}, status=400)

# Realizar el movimiento
    bodega_origen_producto = bodega_origen_productos[0]
    bodega_origen_producto.cantidad -= cantidad_a_mover
    bodega_origen_producto.save()
    
    bodega_destino_producto, created = BodegaProducto.objects.get_or_create(bodega__id=bodega_destino_id, producto__id=producto_id)
    bodega_destino_producto.cantidad += cantidad_a_mover
    bodega_destino_producto.save()
    
    # Crear el movimiento y los detalles de movimiento
    movimiento_data = {
        'bodega_origen': bodega_origen_producto.bodega,
        'bodega_destino': bodega_destino_producto.bodega,
        'usuario': usuario.id,
        'detalles': [
            {
                'bodega_producto': bodega_origen_producto.id,
                'cantidad': -cantidad_a_mover,
            },
            {
                'bodega_producto': bodega_destino_producto.id,
                'cantidad': cantidad_a_mover,
            }
        ]
    }
    
    serializer = MovimientoBodegaSerializer(data=movimiento_data)
    serializer.is_valid(raise_exception=True)
    movimiento = serializer.save()
    
    return Response(serializer.data)

class BodegaProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodegaProducto.objects.all()
    serializer_class = MovimientoBodegaSerializer
    
class regionAPI(generics.ListAPIView):
    queryset = region.objects.all()
    serializer_class = regionesSerializer