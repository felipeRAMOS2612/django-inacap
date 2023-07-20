from rest_framework import serializers
from .models import *


class librosSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro
        fields = '__all__'