from logging import PlaceHolder
from django import forms

class SolicitudForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    dni = forms.CharField(label='Dni', required=True)
    tipo_prestamo = forms.CharField(label='Tipo de prestamo', required = True)
    cuotas = forms.CharField(label='Cantidad de cuotas', required = True)
    
