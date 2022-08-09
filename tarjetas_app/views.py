from django.shortcuts import render, HttpResponse

# Create your views here.
def tarjetas(request):
    return render(request, "tarjetas_app/tarjetas.html")