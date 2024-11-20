from django.db import models
from .choices import CATEGORIAS
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator

# Create your models here.

class clientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators= [MinLengthValidator(10)])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='nombre del cliente : ')
    apellido = models.CharField(max_length=50, blank=False)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    direccion = models.CharField(validators=[])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} '' {self.apellido}"
    
    class Meta:
        verbose_name= 'Cliente : '
        verbose_name_plural='Clientes'
        db_table= 'Clientes'


class productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, unique=True)
    nombre = models.CharField(max_length=50, blank=False, verbose_name='nombre del producto')
    marca = models.CharField(max_length=50, unique=True)
    caracteristicas_categoria = models.CharField(max_length=100, choices=CATEGORIAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='ingresa valores decimales', verbose_name='precio')
    cantidad_stock = models.IntegerField(verbose_name='cantidad en stock: ')
    fecha_ingreso = models.DateField(auto_now_add=True)
    feha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()

    def actualizar_stock (self, cantidad):
        self.cantidad_stock -= cantidad
        self.save()

    def __str__(self):
        return f"{self.nombre} '' {self.marca}"
    
    class Meta:
        verbose_name= 'Producto : '
        verbose_name_plural='Productos'
        db_table= 'Productos' 

