from django.shortcuts import render

from .models import Usuario

def index(request):
    return render(request, 'usuarios/index.html')

def usuario_list(request):
    query = Usuario.objects.all()
    contexto = {'object_list': query}
    return render(request, 'usuarios/usuario_list.html', contexto)


