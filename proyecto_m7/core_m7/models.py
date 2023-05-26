from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


class DatosUsuarioExtra(models.Model):
   id_user = models.OneToOneField(User, on_delete=models.CASCADE)
   rut = models.TextField()
   
   class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Datos de Usuarios"
        ordering = ["-id_user"]


def __str__(self):
        return self.id_user.username
    
    