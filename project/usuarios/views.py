from django.shortcuts import render

from .models import Usuario

def usuario_list(request):
    usuarios = Usuario.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'usuarios/usuario_list.html', contexto)


