from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.contrib import messages

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def shows_new(request):
    context = {
        'show': 'Show create'
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

        errors = Show.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else: 
            show = Show.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                desc = request.POST['desc'],
            )
            messages.success(request, "Show de TV agregado correctamente")
            #return redirect("/shows/" + str(show.id))
            return redirect(f"/shows/{show.id}")

def shows_edit(request, id):
    if request.method == 'GET':
        show_by_id = Show.objects.get(id=id)
        print("Mostardo Show antes de editar: ", show_by_id)
        context = {
            'show': show_by_id,
        }
        return render(request, 'shows_edit.html', context)

def edit(request):
    if request.method == 'POST':
        print("---POST ----", request.POST)
        id_show = request.POST['id_show']
        show = Show.objects.get(id=id_show)
        errors = Show.objects.edit_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id_show}/edit')
        else:
            print("---Else de actualizacion---", request.POST)
            ed_title = request.POST['ed_title']
            ed_network = request.POST['ed_network']
            ed_desc = request.POST['ed_desc']
            show.title = ed_title
            show.network = ed_network
            show.desc = ed_desc
            show.save()
            return redirect(f'/shows/{id_show}')


def shows_delete(request, id):
    show_by_id = Show.objects.get(id=id)
    print("Borrando: ", show_by_id)
    show_by_id.delete()
    return redirect('/shows')
