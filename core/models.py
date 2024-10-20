from django.db import models
from datetime import datetime, timezone
from django.utils import timezone
from django.forms import model_to_dict

# Create your models here.

from core.choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')

    def __str__(self):
        return 'Nombre: {}'.format(self.name)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']


# class Procesos(models.Model):
#     NO_INICIADO = 'NI'
#     EN_PROCESO = 'EP'
#     TERMINADO = 'TE'
#
#     ESTADO_CHOICES = [
#             (NO_INICIADO, 'No Iniciado'),
#             (EN_PROCESO, 'En proceso'),
#             (TERMINADO, 'Terminado'),
#     ]
#     name = models.CharField(max_length=150, verbose_name='Nombre del proceso')
#     fechaInicio = models.DateField(default=datetime.now, verbose_name='Fecha de Inicio')
#     fechaFin = models.DateField(default=datetime.now, verbose_name='Fecha de Fin')
#     estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, default=NO_INICIADO)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = 'proceso'
#         verbose_name_plural = 'Procesos'
#         ordering = ['id']

# class Medicion(models.Model):
#
#     date = models.DateField(default=datetime.now, verbose_name='Fecha')
#     temp = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
#     OD = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
#     PH = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
#     oz = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
#     proceso = models.ForeignKey(Procesos, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.proceso.name
#     class Meta:
#         verbose_name = 'medicion'
#         verbose_name_plural = 'Mediciones'
#         ordering = ['id']

class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Temperature: {self.temperature}, Humidity: {self.humidity}"

    def toJSON(self):
        item = model_to_dict(self)
        # Convierte datetime a un formato legible (ISO)
        item['datetime'] = self.datetime.isoformat()  # O puedes usar str(self.datetime) si prefieres
        return item
class LedControl(models.Model):
    estado = models.DecimalField(default=0, max_digits=1, decimal_places=0)

    def __str__(self):
        return f"Estado: {self.estado}"
    def toJSON(self):
        item = model_to_dict(self)
        return item
