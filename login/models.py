from django.db import models
from bodegas.models import region
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
    
class cargo(models.Model):
    cargo = models.CharField(max_length=100)


class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=True, default = None)
    cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=255, default=None, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def get_username(self):
        return self.username
    