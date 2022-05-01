from django.shortcuts import render, redirect
from .models import Plato
from .forms import platoForm
# Create your views here.

def inicio(request):
    platos = Plato.objects.all()
    print(platos)
    return render(request, 'listar.html', {'platos': platos})

def editar(request,id):
    plato = Plato.objects.get(id=id)
    form = platoForm(instance=plato)
    if request.POST:
        form = platoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    return render(request, 'editar.html', {'form': form})

def crear(request):
    form = platoForm(request.POST or None)
    if request.POST:
        form = platoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    return render(request, 'crear.html', {'form': form})

def eliminar(request, id):
    plato = Plato.objects.get(id=id)
    plato.delete()
    return redirect("inicio")