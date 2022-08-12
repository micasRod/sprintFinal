from django.shortcuts import render, HttpResponse
from .models import Cliente

# Create your views here.
def clientes(request):
    cliente_model = Cliente.objects.all()
    return render(request, "clientes_app/clientes.html", {'cliente_model': cliente_model})

