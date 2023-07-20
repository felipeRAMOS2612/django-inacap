from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *
# Create your views here.

class BodegasView(viewsets.ModelViewSet):
    serializer_class = BodegasSerializer
    queryset = bodega.objects.all()

    
from rest_framework import generics

class BodegasCreate(generics.ListCreateAPIView):
    serializer_class = BodegasSerializer
    queryset = bodega.objects.all()

class BodegaProductoListCreateView(generics.ListCreateAPIView):
    queryset = bodegaProducto.objects.all()
    serializer_class = BodegaProductoSerializer

class BodegaProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = bodegaProducto.objects.all()
    serializer_class = BodegaProductoSerializer
    
class regionAPI(generics.ListAPIView):
    queryset = region.objects.all()
    serializer_class = regionesSerializer