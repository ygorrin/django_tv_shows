from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'saludo': 'shows'
    }
    return render(request, 'shows.html', context)

def shows_new(request):

    context = {
        'saludo': 'Show create'
    }
    return render(request, 'shows_create.html', context)

def shows_crear(request):
    if request.method =='POST':
        print("---POST ----", request.POST)
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc'],
        )
    return redirect('/shows')
    

def shows_edit(request, id):
    context = {
        'saludo': 'Show update'
    }
    return render(request, 'shows_update.html', context)

def shows_id(request,id):
    context = {
        'saludo': 'Show by id'
    }
    return render(request, 'shows_id.html', context)