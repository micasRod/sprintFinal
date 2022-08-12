from django.contrib import admin
from .models import caja_ahorro as caja_ahorro
from .models import caja_ahorrodls as caja_ahorrodls
from .models import cuenta_corriente as cuenta_corriente
# Register your models here.
admin.site.register(caja_ahorro)
admin.site.register(caja_ahorrodls)
admin.site.register(cuenta_corriente)