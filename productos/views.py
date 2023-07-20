from django.shortcuts import render
from rest_framework import viewsets
from .serializer import librosSerializer
from .models import *
# Create your views here.

class LibrosView(viewsets.ModelViewSet):
    serializer_class = librosSerializer
    queryset = libro.objects.all()