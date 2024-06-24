from django.shortcuts import render
from suscripciones.models import Suscriptor
#from suscriptores.views import crud
# Create your views here.

def menu(request):
    context={}
    return render(request, 'Administrador/menu.html', context)

def reporte_suscriptores(request):
    suscriptores=Suscriptor.objects.all()
    context={'suscriptores':suscriptores}
    return render(request, 'Administrador/menu.html', context)