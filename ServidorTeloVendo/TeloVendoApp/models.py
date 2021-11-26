from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length= 12, unique = True)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.CharField(max_length= 30)
    edad = models.IntegerField()

class Proveedor(models.Model):
    rut =  models.CharField(max_length= 12, unique = True)
    nombre_proveedor =  models.CharField(max_length= 50)
    direccion =  models.CharField(max_length= 50)
    contacto_telefonico =  models.CharField(max_length= 30)
    email =  models.CharField(max_length= 30)
    producto =  models.CharField(max_length= 30)