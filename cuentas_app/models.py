from tabnanny import verbose
from django.db import models as models

class Cuenta(models.Model):
    tipo = models.CharField(max_length=10, primary_key=True)
    moneda = models.CharField(max_length=10)
    trans_cuentExt = models.BooleanField(default=False)
    cbu = models.IntegerField()
    alias = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Caja de ahorro'
        verbose_name_plural = 'Cajas de ahorro'

    def __str__(self):
        return self.numero


