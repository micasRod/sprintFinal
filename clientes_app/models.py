import numbers
from tabnanny import verbose
from unicodedata import numeric
from django.db import models

class Cliente(models.Model):
    tipo = models.TextField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.DateTimeField(max_length=200)
    situacion_laboral= models.DateTimeField(max_length=200)
    categoria = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    tipo = models.TextField(max_length=200)
    cant_tarjetas = models.TextField(max_length=200)
    tipo_caja = models.TextField(max_length=200)
    cant_retiro = models.TextField(max_length=200)
    tarj_credito = models.TextField(max_length=200)
    comision = models.TextField(max_length=200)
    max_transf = models.TextField(max_length=200)
    chequera = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Tipo de categoria'

    def __str__(self):
        return self.tipo    
    