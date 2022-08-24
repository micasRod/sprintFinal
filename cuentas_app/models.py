from tabnanny import verbose
from django.db import models as models
from clientes_app.models import Cliente as Cliente_cuenta

class Cuenta(models.Model):
    account_id = models.IntegerField(null=False, primary_key=True)
    customer_id = models.ForeignKey(Cliente_cuenta, null=True, blank=True, on_delete=models.CASCADE)
    balance = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'



