from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "login_app/home.html")

def login(request):
    return render(request, "login_app/login.html")