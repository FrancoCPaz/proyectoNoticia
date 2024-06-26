#from django.conf.urls import url
from django.urls import path, include
from . import views



urlpatterns=[
    path('menu',views.menu, name='menu'),
    path('reporte_suscriptores', views.reporte_suscriptores, name='reporte_suscriptores'),
    path('home',views.home, name='home'),

    
]