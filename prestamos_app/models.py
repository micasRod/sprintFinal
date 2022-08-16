from django.db import models

class Prestamo(models.Model):
    tipo_prestamo = models.CharField(max_length=200)
    cuota_prestamo = models.CharField(max_length=200)
    fecha_prestamo = models.CharField(max_length=200)
    total_prestamo = models.CharField(max_length=200)
    aPagar_prestamo = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return self.tipo_prestamo