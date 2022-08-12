from django.db import models

class Prestamo(models.Model):
    cuota_prestamo = models.CharField(max_length=200)
    fecha_prestamo = models.CharField(max_length=200)
    interes_prestamo = models.CharField(max_length=200)
    total_prestamo = models.CharField(max_length=200)