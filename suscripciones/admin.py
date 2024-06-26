from django.contrib import admin
from .models import Genero, Suscriptor, Noticia

# Register your models here.


admin.site.register(Genero)
admin.site.register(Suscriptor)
admin.site.register(Noticia)