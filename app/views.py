from django.shortcuts import render, redirect
from .models import *
# Import Datetime class
from datetime import datetime

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def shows_new(request):
    context = {
        'saludo': 'Show create'
    }
    return render(request, 'shows_create.html', context)

def shows_mostrar(request, id):
    show_by_id = Show.objects.get(id=id)
    print("Mostrando: ", show_by_id)
    context = {
        'show' : show_by_id,
    }
    return render(request, 'shows_mostrar.html', context)


def show_agregar(request):
    if request.method =='POST':
        print("---POST ----", request.POST)
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc'],
        )
    return redirect("/shows/" + str(show.id))


def shows_edit(request, id):
    if request.method == 'GET':
        show_by_id = Show.objects.get(id=id)
        print("Mostardo Show antes de editar: ", show_by_id)
        context = {
            'show': show_by_id,
        }
        return render(request, 'shows_edit.html', context)

def edit(request):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        id_show = request.POST['id_show']
        show = Show.objects.get(id=id_show)
        print("Vamos a actualizar")
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.desc = request.POST['desc']
        show.save()
        return redirect(f'/shows/{id_show}')


def shows_delete(request, id):
    show_by_id = Show.objects.get(id=id)
    print("Borrando: ", show_by_id)
    show_by_id.delete()
    return redirect('/shows')
