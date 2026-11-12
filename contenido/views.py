from django.shortcuts import render
from .models import Servicio


# Create your views here.
def inicio(request):
    servicios = Servicio.objects.filter(disponible=True)[:4]  # Obtener los primeros 4 servicios disponibles

    return render(request, 'contenido/inicio.html', {'servicios': servicios})

def servicios(request):
    servicios = Servicio.objects.filter(disponible=True)  # Obtener todos los servicios disponibles

    return render(request, 'contenido/servicios.html', {'servicios': servicios})
