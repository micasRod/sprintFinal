from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, "home_app/homebanking.html")

def inicio(request):
    return render(request, "home_app/inicio.html")    

def dolar(request):
    return render(request, 'home_app/dolar.html')    
