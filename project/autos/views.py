from django.shortcuts import render

from .models import AutosCategorias

def index(request):
    return render(request, 'autos/index.html')

def autoscategorias_list(request):
    query = AutosCategorias.objects.all()
    contexto = {'object_list': query}
    return render(request, 'autos/autoscategorias_list.html', contexto)

