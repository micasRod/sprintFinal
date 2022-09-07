from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Solicitud
from .forms import SolicitudForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Prestamo
from .serialIzers import PrestamoSerializer
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

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

class PrestamoPost(APIView):
    def post(self, request, format=None):
        serializer = PrestamoSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrestamoDelete(APIView):
    def delete(self,request, pk):
        
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if prestamo:
            serializer = PrestamoSerializer(prestamo)
            prestamo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)