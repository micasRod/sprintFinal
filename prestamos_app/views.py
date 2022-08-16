from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SolicitudForm
from django.urls import reverse

# Create your views here.
def prestamos(request):
    return render(request, "prestamos_app/prestamos.html")

def solicitud(request):
    solicitud_prestamo = SolicitudForm()

    if request.method == "POST":
        solicitud_prestamo = SolicitudForm(data=request.POST)
        if solicitud_prestamo.is_valid():
            nombre = request.POST.get('nombre', '')
            print(nombre)
        #return redirect(reverse('solicitud') + "?ok")    
    return render(request, "prestamos_app/solicitud_prestamo.html", {'form' : solicitud_prestamo})