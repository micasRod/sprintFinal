from django.shortcuts import render, HttpResponse

# Create your views here.
def prestamos(request):
    return render(request, "prestamos_app/prestamos.html")