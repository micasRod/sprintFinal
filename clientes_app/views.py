from django.shortcuts import render, HttpResponse
from .models import Clientes

# Create your views here.
def clientes(request):
    clientes_model = Clientes.objects.all()
    return render(request, "clientes_app/clientes.html", {'clientes_model': clientes_model})

