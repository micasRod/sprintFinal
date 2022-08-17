from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cuentas(request):
    return render(request, "cuentas_app/cuentas.html")