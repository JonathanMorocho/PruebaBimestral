from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.

product_status = [
    (1, 'En reparacion'),
    (2, 'Servicio Externo'),
    (3, 'Daño Electronico')
]

class Usuarios(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    Estado_equipo = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)
    fecha_inicio_ticket = models.DateTimeField("fecha de Inicio", default=datetime.now())

    def _str_(self):
        return '%s %s' % (self.Nombre, self.Apellido, self.Correo, self.Estado_equipo, self.Descripcion, self.fecha_inicio_ticket)