from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(max_length=50, verbose_name="Email")
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-nombre"]
        
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    direccion = models.CharField(max_length=50, verbose_name="Direccion")
    telefono = models.IntegerField(verbose_name="Telefono")
    creditos = models.IntegerField(verbose_name="Creditos")
    email = models.EmailField(max_length=50, verbose_name="Email")
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-direccion"]
        
    def __str__(self):
        return self.direccion
    
class Estado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["-nombre"]
        
    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    total = models.IntegerField(verbose_name="Total")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="Estado")
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-fecha"]
        
    def __str__(self):
        return self.fecha
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    precio = models.IntegerField(verbose_name="Precio")
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-nombre"]
        
    def __str__(self):
        return self.nombre
    
    
    
class Detalle(models.Model):
    cantidad = models.IntegerField(verbose_name="Cantidad")
    total_detalle = models.IntegerField(verbose_name="Total")
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name="Pedido")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    
    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        ordering = ["-cantidad"]
    
    def __str__(self):
        return self.cantidad
    
    
    
    

    