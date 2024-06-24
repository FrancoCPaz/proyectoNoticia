#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suscripciones/',include('suscripciones.urls')),
    path('Administrador/',include('Administrador.urls')),

    path("accounts/", include("django.contrib.auth.urls")),
]