#from django.conf.urls import url

from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),

    path('listadoSQL', views.listadoSQL, name='listadoSQL'),

    path('crud', views.crud, name='crud'),
    path('suscripcionesAdd', views.suscripcionesAdd, name='suscripcionesAdd'),
    path('suscripciones_del/<str:pk>', views.suscripciones_del, name='suscripciones_del'),
    path('suscripciones_findEdit/<str:pk>', views.suscripciones_findEdit, name='suscripciones_findEdit'),
    path('suscripcionesUpdate', views.suscripcionesUpdate, name='suscripcionesUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),

    path('acerca/', views.acerca, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
    path('galeria/', views.galeria, name='galeria'),
    path('login/', views.login, name='login'),
    path('noticia1/', views.noticia1, name='noticia1'),
    path('noticia2/', views.noticia2, name='noticia2'),
    path('noticia3/', views.noticia3, name='noticia3'),
    path('pokedex/', views.pokedex, name='pokedex'),
    path('registro/', views.registro, name='registro'),
    path('base/', views.base, name='base'),

    path('agregar_noticia',views.agregar_noticia, name='agregar_noticia'),
    path('listar_noticia',views.lista_noticia, name="listar_noticia"),
    path('listar_noticia/<int:id_noticia>/', views.noticia_eliminar, name='noticia_eliminar'),
    path('editar_noticia/<int:id_noticia>/', views.editar_noticia, name='editar_noticia'),
]
