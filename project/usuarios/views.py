from django.shortcuts import render, redirect


from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import UsuarioForm
from .models import Usuario

def index(request):
    return render(request, 'usuarios/index.html')

#------------------------------------LIST------------------------------------

def usuario_list(request):
    q = request.GET.get('q')
    if q:
        query = Usuario.objects.filter(nombre__icontains=q)
    else: 
        query = Usuario.objects.all()
    contexto = {'object_list': query}
    return render(request, 'usuarios/usuario_list.html', contexto)

class UsuarioList(ListView):
    model = Usuario

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Usuario.objects.filter(nombre__icontains=q)
        return queryset

#------------------------------------CREATE------------------------------------

def usuario_create(request):
    if request.method == 'GET':
        form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:usuario_list')

    return render(request, 'usuarios/usuario_create.html', {'form': form})

class UsuarioCreate(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:usuario_list')
    template_name = 'usuarios/usuario_create.html'
    context_object_name = 'object'

    def form_valid(self, form):
    # Esto guarda el nuevo objeto en la base de datos
        auto = form.save(commit=False)
        auto.save()
        return super().form_valid(form)


#------------------------------------DETAIL------------------------------------

def usuario_detail(request, pk: int):
    query = Usuario.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'usuarios/usuario_detail.html', context)

class UsuarioDeatil(DetailView):
    model = Usuario
    context_object_name = 'object'

#------------------------------------UPDATE------------------------------------

def usuario_update(request, pk: int):
    query = Usuario.objects.get(id=pk)
    if request.method == 'GET':
        form = UsuarioForm(instance=query)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('usuarios:usuario_list')
    return render(request, 'usuarios/usuario_create.html', {'form':form})

class UsuarioUpdate(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('autos:autos_list')
    template_name = 'usuarios/usuario_create.html'


#------------------------------------DELETE------------------------------------

def usuario_delete(request, pk: int):
    query = Usuario.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('usuarios:usuario_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'object':query})

class UsuarioDelete(DeleteView):
    model = Usuario
    success_url = reverse_lazy('autos:autos_list')
