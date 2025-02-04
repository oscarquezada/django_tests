from django.db import models
from django.utils import timezone

# ============================
# MODELOS PARA TESTCASE
# ============================

# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)

    def aumentar_stock(self, cantidad):
        self.stock += cantidad
        self.save()

# Modelo Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

# Modelo Pedido
class Pedido(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(default=timezone.now)

# ============================
# MODELOS PARA TRANSACTIONTESTCASE
# ============================

# Modelo Usuario (con restricción de unicidad en email)
class Usuario(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

# Modelo Reserva
class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    confirmada = models.BooleanField(default=False)

    def confirmar(self):
        self.confirmada = True
        self.save()

# Modelo Categoria (con restricción de unicidad en nombre)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
