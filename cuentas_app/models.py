from django.db import models


class caja_ahorro(models.Model):
    numero = models.CharField(max_length=200)
    moneda = models.CharField(max_length=200)
    trans_cuentExt = models.CharField(max_length=200)
    cant_maxima = models.CharField(max_length=200)
    cbu = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)

class caja_ahorrodls(models.Model):
    numero = models.CharField(max_length=200)
    moneda = models.CharField(max_length=200)
    trans_cuentExt = models.CharField(max_length=200)
    cant_maxima = models.CharField(max_length=200)
    cbu = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)

class cuenta_corriente(models.Model):
    numero = models.CharField(max_length=200)
    moneda = models.CharField(max_length=200)
    trans_cuentExt = models.CharField(max_length=200)
    cant_maxima = models.CharField(max_length=200)
    cbu = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)    