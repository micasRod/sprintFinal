from django.db import models

# CLASE DE EMPLO / NO SIRVE
class home(models.Model):
    tiempo_permitido = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.usuario    