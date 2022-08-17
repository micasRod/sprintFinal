from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def login(request):
    return render(request, "registration/login.html")