from django.shortcuts import render, redirect

from .forms import UsuarioForm
from .models import Usuario

def index(request):
    return render(request, 'usuarios/index.html')

def usuario_list(request):
    query = Usuario.objects.all()
    contexto = {'object_list': query}
    return render(request, 'usuarios/usuario_list.html', contexto)

def usuario_create(request):
    if request.method == 'GET':
        form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:usuario_list')

    return render(request, 'usuarios/usuario_create.html', {'form': form})


