from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apellido_materno = models.CharField(blank=True,null=True,max_length=50)
    edad = models.IntegerField(blank=True,null=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"