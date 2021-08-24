from collections import namedtuple
from Proyecto_Final.Tickets.views import lista_form
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('registro', views.registro, name='registro'),
    path('lista_form', views.lista_form, name='lista_form'),
]