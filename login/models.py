from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
    
class cargo(models.Model):
    cargo = models.CharField(max_length=100)
    def __str__(self):
        return self.cargo


class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=True, default = None)
    cargo = models.ForeignKey(cargo, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    password = models.CharField(max_length=255, default=None, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def get_username(self):
        return self.username
    