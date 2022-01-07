from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    idAdministrador=models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    cedula=models.CharField(max_length=10)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    clave=models.CharField(max_length=100)
class Medico (models.Model):
    idMedico=models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    cedula=models.CharField(max_length=10,unique=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    clave=models.CharField(max_length=100,unique=True)
    idAdministrador=models.ForeignKey(Administrador, related_name='%(class)s_administrador',on_delete=models.CASCADE,)

class Paciente (models.Model):
    idPaciente=models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    cedula=models.CharField(max_length=10,unique=True)
    idMedico=models.ForeignKey(Medico, related_name='%(class)s_medico',on_delete=models.CASCADE,) #nuevo
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    sexo=models.CharField(max_length=1) #F y M
    telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=50)

class Imagen (models.Model):
    idImagen=models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    idPaciente=models.ForeignKey(Paciente, related_name='%(class)s_paciente',on_delete=models.CASCADE,) #nuevo
    rutaImagen=models.CharField(max_length=200)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    descripcion=models.TextField(max_length=4000)
    Estado=models.CharField(max_length=3) #INA ACT
    idAdministrador=models.ForeignKey(Administrador, related_name='%(class)s_administrador',on_delete=models.CASCADE,)



class Patologia(models.Model):
    idPatologia=models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    descripcion=models.TextField(max_length=4000)

class Patol_Pac(models.Model):
    idPatol_Pac=models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    idPaciente=models.ForeignKey(Paciente, related_name='%(class)s_paciente',on_delete=models.CASCADE,)
    idPatologia=models.ForeignKey(Patologia, related_name='%(class)s_patologia',on_delete=models.CASCADE,)

