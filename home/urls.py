from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("contato/", views.contato, name="contato"),
    path("desafio/", views.desafio, name="desafio"),
    path("perfil/<str:usuario>", views.perfil, name='perfil'),
    path("diasemana/<str:dia>", views.diasemana, name='diasemana'),
    path("lista/", views.lista, name='lista'),
    path("formularioproduto/", views.formularioproduto, name='formularioproduto')
]