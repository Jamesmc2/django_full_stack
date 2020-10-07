from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.listShows),
    path('shows/new', views.newShow),
    path('shows/create', views.createShow),
    path('shows/<int:show_id>', views.aboutShow),
    path('shows/<int:show_id>/edit', views.editShow),
    path('shows/<int:show_id>/update', views.updateShow),
    path('shows/<int:show_id>/destroy', views.destroyShow),

]