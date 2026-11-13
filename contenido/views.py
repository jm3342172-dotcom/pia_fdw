from django.shortcuts import render
from .models import Servicio, Estilista , Producto


# Página de inicio
def inicio(request):
    servicios = Servicio.objects.filter(disponible=True)[:4]

    return render(request, 'contenido/inicio.html', {
        'servicios': servicios
    })


# Página de servicios
def servicios(request):
    servicios = Servicio.objects.filter(disponible=True)

    return render(request, 'contenido/servicios.html', {
        'servicios': servicios
    })


# Página de estilistas
def estilistas(request):
    estilistas = Estilista.objects.all()

    return render(request, 'contenido/estilistas.html', {
        'estilistas': estilistas
    })

    
def sucursales(request):
    return render(request, 'contenido/sucursales.html')

# Página de productos
def productos(request):
    productos = Producto.objects.all()

    return render(request, 'contenido/productos.html', {
        'productos': productos
    })