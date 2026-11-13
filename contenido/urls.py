from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('estilistas/', views.estilistas, name='estilistas'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('productos/', views.productos, name="productos")
]