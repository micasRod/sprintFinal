import numbers
from tabnanny import verbose
from unicodedata import numeric
from django.db import models

"""class Categoria(models.Model):
    categoria_tipo = models.CharField(max_length=10,primary_key=True)
    cant_tarjetas = models.IntegerField()
    cant_cajas = models.IntegerField()
    compra_venta_dolares = models.BooleanField(default=False)
    retiro_max = models.IntegerField()
    tarj_cred = models.BooleanField(default=False)
    chequera = models.BooleanField(default=False)
    comision = models.IntegerField()
    trans_recib_max = models.IntegerField()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria_tipo   """ 



class Cliente(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_DNI = models.CharField(max_length=10,null=True)
    customer_name = models.CharField(max_length=50,null=True)
    customer_surname = models.CharField(max_length=50,null=True)
    branch_id = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.customer_name





