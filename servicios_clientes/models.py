from django.db import models

# Create your models here.

class servicios_clientes(models.Model):
    title=models.CharField(max_length=225)
    content=models.TextField()
    