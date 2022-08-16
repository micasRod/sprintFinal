from tabnanny import verbose
from django.db import models


class Caja(models.Model):
    tipo = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    moneda = models.CharField(max_length=200)
    trans_cuentExt = models.CharField(max_length=200)
    cant_maxima = models.CharField(max_length=200)
    cbu = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Caja de ahorro'
        verbose_name_plural = 'Cajas de ahorro'

    def __str__(self):
        return self.numero


class cuenta_corriente(models.Model):
    numero = models.CharField(max_length=200)
    moneda = models.CharField(max_length=200)
    trans_cuentExt = models.CharField(max_length=200)
    cant_maxima = models.CharField(max_length=200)
    cbu = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)    

    class Meta:
        verbose_name = "Cuenta Corriente"
        verbose_name_plural = "Cuentas Corriente"

    def __str__(self):
        return self.numero   