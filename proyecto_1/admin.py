from django.contrib import admin
from .models import Administrador,Medico,Paciente,Imagen,Patologia,Patol_Pac
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Imagen)
admin.site.register(Patologia)
admin.site.register(Patol_Pac)
