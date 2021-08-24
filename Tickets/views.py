#from django.http import request
from Proyecto_Final.Tickets.models import Usuarios
from django.shortcuts import render
from .forms import RegistroForm
from Tickets.models import*
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request, "Principal/inicio.html")

def registro(request):
    if request.method == 'GET':
        formulario = RegistroForm
        contexto = {
        'formulario' : formulario
        }
    else:
        formulario = RegistroForm(request.POST)
        contexto = {
        'formulario' : formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('Tickets:lista_form')
    return render(request, 'registro/registro.html', contexto)


def lista_form(request):
    usuarios = Usuarios.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, "listas/listas.html", context)