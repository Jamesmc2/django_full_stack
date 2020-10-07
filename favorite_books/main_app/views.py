from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import User
from time import gmtime, strftime
from datetime import datetime
from .models import Book


def books(request):
    content = {
        'books' : Book.objects.all(),
        'current_user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'books.html', content)

def add_new(request):
    new_book=Book.objects.create(title = request.POST['title'], description = request.POST['description'], uploaded_by = User.objects.get(id=request.session['user_id']))
    new_book.users_who_like.add(User.objects.get(id=request.session['user_id']))
    return redirect('/books')

def book_info(request, book_id):
    context = {
        'book' : Book.objects.get(id=book_id)
    }
    return render(request, 'book_info.html', context)