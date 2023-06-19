from django.shortcuts import render, redirect
from app.form import MaquinasForm
from app.models import Maquinas


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Maquinas.objects.filter(usuario__icontains=search)
    else:
        data['db'] = Maquinas.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = MaquinasForm()
    return render(request, 'form.html', data)


def create(request):
    form = MaquinasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = Maquinas.objects.get(pk=pk)
    data['form'] = MaquinasForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Maquinas.objects.get(pk=pk)
    form = MaquinasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    

def delete(request, pk):
    db = Maquinas.objects.get(pk=pk)
    db.delete()
    return redirect('home')
    