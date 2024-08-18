from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("contato/", views.contato, name="contato"),
    path("ajuda/", views.ajuda, name="ajuda"),
    path("perfil/<str:usuario>", views.perfil, name='perfil'),
    path("diasemana/<str:dia>", views.diasemana, name='diasemana'),
]