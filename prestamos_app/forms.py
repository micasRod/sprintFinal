from django import forms

class SolicitudForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    tipo_prestamo = forms.CharField(label='Tipo de prestamo', required = True)
    cuotas = forms.CharField(label='Cantidad de cuotas', required = True)
    
