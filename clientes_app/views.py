from django.shortcuts import render, HttpResponse

# Create your views here.
def clientes(request):
    return render(request, "clientes_app/clientes.html")