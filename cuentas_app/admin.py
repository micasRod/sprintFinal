from django.contrib import admin
from .models import Caja as tipo_caja
from .models import cuenta_corriente as cuenta_corriente
# Register your models here.
admin.site.register(tipo_caja)
admin.site.register(cuenta_corriente)