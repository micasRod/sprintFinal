from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Solicitud
from .forms import SolicitudForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def prestamos(request):
    return render(request, "prestamos_app/prestamos.html")
@login_required
def solicitud(request):
    solicitud_prestamo = SolicitudForm()

    if request.method == "POST":
        solicitud_prestamo = SolicitudForm(data=request.POST)
        if solicitud_prestamo.is_valid():
            nombre = request.POST.get('nombre', '')
            dni = request.POST.get('dni', '')
            tipo = request.POST.get('tipo', '')
            cuotas = request.POST.get('cuotas', '')
            
            

            solicitud = Solicitud(nombre=nombre, dni=dni, tipo_prestamo=tipo, cuotas_devolver=cuotas)
            solicitud.save()
        #return redirect(reverse('solicitud') + "?ok")    
    return render(request, "prestamos_app/solicitud_prestamo.html", {'form' : solicitud_prestamo})