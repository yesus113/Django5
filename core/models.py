from django.db import models
from datetime import datetime
# Create your models here.

class Type  (models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    def __str__(self):
        return self.name

class Categoria (models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['id']

class EmpleadosModel(models.Model):
    categoria = models.ManyToManyField(Categoria, verbose_name="Categoria")
    type = models.ForeignKey(Type, verbose_name="Tipo", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    #genero = models.CharField(max_length=50, verbose_name="Genero")
    dni = models.CharField(max_length=10, verbose_name="DNI", unique=True)
    data_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    data_create = models.DateTimeField(auto_now=True) #El primer, con los demas no
    data_update = models.DateTimeField(auto_now_add=True) #Con todos
    age = models.PositiveIntegerField(default=0.0, verbose_name="Edad") #Solo toma numeros positivos
    salary = models.DecimalField (default=0.00, max_digits=9, decimal_places=2, verbose_name="Salario")
    state = models.BooleanField (default=True, verbose_name="Estado")
    avatar = models.ImageField(upload_to="avatar/%Y%m%d", null=True, blank=True)
    cvitae = models.FileField(upload_to="cvitae/%Y%m%d", null=True, blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "empleados"
        ordering = ['id']