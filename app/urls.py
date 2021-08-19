from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('shows_crear', views.shows_crear),
    path('shows/<int:id>/edit', views.shows_edit),
    path('shows/<int:id>', views.shows_id),


]
