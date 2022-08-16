"""itbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from clientes_app import views as  clientes_views
from cuentas_app import views as cuentas_views
from home_app import views as home_views
from login_app import views as login_views
from prestamos_app import views as prestamos_views
from tarjetas_app import views as tarjetas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_views.login, name="login"),
    path('home/',home_views.home, name="home"),
    path('clientes/',clientes_views.clientes, name="clientes"),
    path('cuentas/',cuentas_views.cuentas, name="cuentas"),
    path('tarjetas/',tarjetas_views.tarjetas, name="tarjetas"),
    path('prestamos/',prestamos_views.prestamos, name="prestamos"),
    path('solicitud/',prestamos_views.solicitud, name="solicitud"),

]
