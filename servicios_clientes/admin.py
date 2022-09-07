from django.contrib import admin
from servicios_clientes.models import servicios_clientes

@admin.register(servicios_clientes)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug', 'status', 'created_on')
    #list_filter=('status')
    #search_fields=['title','content']
    #prepopulated_fields= {'slug':('title',)}
