from django.db import models

# Create your models here.
class curso(models.Model):
    
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()


class ALumnos(models.Model):
    nombre_alumno = models.CharField(max_length=20)
    apellido_alumno = models.CharField(max_length=20)
    edad_alumno = models.IntegerField()

class Profesores(models.Model):
    nombre_prof = models.CharField(max_length=20)
    apellido_prof = models.CharField(max_length=29)
    curso_prfo = models.CharField(max_length=30)