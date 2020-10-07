from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.new_book),
    path('create_book/', views.create_book),
    path('<int:book_id>/', views.book_info),
    path('<int:book_id>/new_review/', views.new_review,),
    path('<int:book_id>/<int:review_id>/delete/', views.delete_review),
    path('users/<int:user_id>/', views.user_page)
]