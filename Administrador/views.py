from django.shortcuts import render
from suscripciones.models import Suscriptor
from django.contrib.auth.decorators import login_required


@login_required
def menu(request):
    request.session["usuario"]=request.user.username
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, 'Administrador/menu.html', context)

def reporte_suscriptores(request):
    suscriptores=Suscriptor.objects.all()
    context={'suscriptores':suscriptores}
    return render(request, 'Administrador/menu.html', context)

def home(request):
    context={}
    return render(request, 'Administrador/home.html', context)