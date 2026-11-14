from django.db import models

# Create your models here.


# service model

class Servicio(models.Model):  
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

# permitira que  django muestre el nombre del servicio en lugar de "Servicio object (1)" en el panel de administración.

    def __str__(self):
        return self.nombre


# estilista model

class Estilista(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    disponible = models.BooleanField(default=True)
    foto = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre



# producto model

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# sucursal model

class Sucursal(models.Model):

    TIPOS_SUCURSAL = [
        ('principal', 'Principal'),
        ('secundaria', 'Secundaria'),
        ('franquicia', 'Franquicia')
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_SUCURSAL)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    horario = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):  
        return self.nombre



# cliente model

class Cliente(models.Model):

        TIPOS_CLIENTE = [
            ('regular', 'Regular'),
            ('vip', 'VIP'),
            ('nuevo', 'Nuevo')
        ]
        nombre = models.CharField(max_length=100)
        apellidos = models.CharField(max_length=150)
        telefono = models.CharField(max_length=15)
        correo = models.EmailField()
        fecha_registro = models.DateField(auto_now_add=True)
        tipo = models.CharField(max_length=15, choices=TIPOS_CLIENTE, default='regular')

        def __str__(self):
            return f"{self.nombre} {self.apellidos}"