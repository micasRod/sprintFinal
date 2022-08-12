from django.db import models

# CLASE DE EMPLO / NO SIRVE
class home(models.Model):
    tiempo_permitido = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    created = models.CharField(max_length=200)
    updated = models.CharField(max_length=200)