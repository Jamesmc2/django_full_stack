from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('add_new', views.add_new),
    path('<int:book_id>', views.book_info)
]