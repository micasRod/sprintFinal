from django.shortcuts import render, HttpResponse
from .models import Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def clientes(request):
    cliente_model = Cliente.objects.all()
    return render(request, "clientes_app/clientes.html", {'cliente_model': cliente_model})

