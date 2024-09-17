from django.shortcuts import render, redirect


from .form import AutoForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import AutosCategorias, Auto

def index(request):
    return render(request, 'autos/index.html')


#------------------------------------LIST------------------------------------

def autos_list(request):
    q = request.GET.get('q')
    if q:
        query = Auto.objects.filter(modelo__icontains=q)
    else:
        query = Auto.objects.all()
    contexto = {'object_list': query}
    return render(request, 'autos/autos_list.html', contexto)

class AutoList(ListView):
    model = Auto
    template_name = 'autos/autos_list.html'


    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Auto.objects.filter(nombre__icontains=q)
        return queryset

#------------------------------------CREATE------------------------------------

def autos_create(request):
    if request.method == 'GET':
        form = AutoForm()
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autos:autos_list')

    return render(request, 'autos/autos_create.html', {'form': form})

class AutoCreate(CreateView):
    model = Auto
    form_class = AutoForm
    success_url = reverse_lazy('autos:autos_list')
    template_name = 'autos/autos_create.html'
    context_object_name = 'object'

    def form_valid(self, form):
            auto = form.save(commit=False)  # No lo guarda aún
            auto.save()  # Guarda el objeto
            print(f"Auto guardado: {auto}")
            return super().form_valid(form)


#------------------------------------DETAIL------------------------------------

def autos_detail(request, pk: int):
    query = Auto.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'autos/autos_detail.html', context)

class AutoDeatil(DetailView):
    model = Auto
    context_object_name = 'object'
    template_name = 'autos/autos_detail.html'

#------------------------------------UPDATE------------------------------------

def autos_update(request, pk: int):
    query = Auto.objects.get(id=pk)
    if request.method == 'GET':
        form = AutoForm(instance=query)
    if request.method == 'POST':
        form = AutoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('autos:autos_list')      
    return render(request, 'autos/autos_create.html', {'form':form})

class AutoUpdate(UpdateView):
    model = Auto
    form_class = AutoForm
    success_url = reverse_lazy('autos:autos_list')
    template_name = 'autos/autos_create.html'


#------------------------------------DELETE------------------------------------

def autos_delete(request, pk: int):
    query = Auto.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('autos:autos_list')      
    return render(request, 'autos/autos_confirm_delete.html', {'object':query})
    
class AutoDelete(DeleteView):
    model = Auto
    success_url = reverse_lazy('autos:autos_list')
    template_name = 'autos/autos_confirm_delete.html'
    context_object_name = 'object'


