from django.db import models

# Create your models here.
class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombrecompleto = models.CharField(max_length=20)
    carrera = models.CharField(max_length=25)
