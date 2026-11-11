from django.contrib import admin
from .models import  Servicio, Estilista, Producto, Sucursal, Cliente


# Register your models here.

admin.site.register(Servicio)
admin.site.register(Estilista)
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Cliente)