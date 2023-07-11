from rest_framework import serializers
from django.contrib.auth import get_user_model
from login.models import *


class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'cargo', 'nombre', 'apellido', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario