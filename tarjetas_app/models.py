from django.db import models

# CLASE DE EMPLO / NO SIRVE
class Tarjeta(models.Model):
    tipo = models.CharField(max_length=200)
    limite = models.CharField(max_length=200)
    limite_extraccion = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    fecha_alta = models.CharField(max_length=200)
    cuotas_maximas = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'

    def __str__(self):
        return self.tipo    