import numbers
from unicodedata import numeric
from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.DateTimeField(max_length=200)


    