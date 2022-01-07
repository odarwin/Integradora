from django.shortcuts import render
from .models import Administrador,Medico,Paciente,Imagen,Paciente,Patol_Pac

def index(request):

    # Genera contadores de algunos de los objetos principales
    #num_books=Book.objects.all().count()
    #num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index/index.html',
        context={'num_books':0},
    )

def login (request):

    return render(
request,
'login/login.html',
context={'resultado':1}
    )