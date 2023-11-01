from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Crearemos una clase de estudiante con los siguientes atributos:
# Nombre, Apellido, email, edad

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()

# Creamos una clase de profesor con los siguientes atributos:
# Nombre, Apellido, email, profesion

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

# Creamos una clase de curso con los siguientes atributos:
# Nombre, Comision

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

# Creamos una clase Estregable con los siguientes atributos:
# nombre, fecha de entrega, estado(entregado, no entregado)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    estado = models.BooleanField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.imagen}'