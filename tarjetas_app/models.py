from django.db import models

class Tarjeta(models.Model):
    tipo_tarjeta = models.CharField(max_length=20,primary_key=True)
    limite = models.IntegerField()
    limite_extraccion = models.IntegerField()
    fecha_alta = models.DateField()
    cuotas_maximas = models.IntegerField()

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'

    def __str__(self):
        return self.tipo_tarjeta    