from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('show_agregar', views.show_agregar),
    path('shows/<int:id>', views.shows_mostrar),
    
    path('shows/<int:id>/edit', views.shows_edit),
    path('shows/<int:id>/delete', views.shows_delete),
    
    
    path('shows/edit', views.edit),


]
