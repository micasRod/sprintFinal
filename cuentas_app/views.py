from django.shortcuts import render, HttpResponse

# Create your views here.
def cuentas(request):
    return render(request, "cuentas_app/cuentas.html")