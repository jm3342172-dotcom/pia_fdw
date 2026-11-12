from django.shortcuts import render
from .models import Servicio


# Create your views here.
def inicio(request):
    servicios = Servicio.objects.all()

    return render(request, 'contenido/inicio.html', {'servicios': servicios})