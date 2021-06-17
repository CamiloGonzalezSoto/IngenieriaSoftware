from django.db import models

# Create your models here.

class registro_usuario(models.Model):

    nombreCompleto = models.CharField(max_length=100, verbose_name='Nombre completo')
    correoElectronico = models.CharField(max_length=100 , verbose_name='Correo Electronico')
    contrasenia = models.CharField(max_length=100 , verbose_name='contraseña')
    confirmarcontrasenia = models.CharField(max_length=100 , verbose_name='Confirmar contraseña')   

    def __str__(self):
        return self.nombreCompleto