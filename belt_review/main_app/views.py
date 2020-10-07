from django.shortcuts import render, redirect
from login_app.models import User
from .models import Book,Review,Author
from django.contrib import messages

def index(request):
    context = {
        'reviews' : Review.objects.all(),
        'books' : Book.objects.all(),
        'recent_reviews' : Review.objects.all().order_by('-created_at')[:3]
    }
    return render(request, 'books.html', context)

def new_book(request):
    context = {
        'authors' : Author.objects.all(),
    }
    return render(request, 'new_book.html', context)

def create_book(request):
    current_user = User.objects.get(id=request.session['user_id'])
    if request.POST['author_selecter']=='-1':
        new_author = Author.objects.create(name = request.POST['new_author'])
        new_book=Book.objects.create(
            title = request.POST['title'], author = new_author, uploaded_by = current_user
        )
        Review.objects.create(
            review=request.POST['review'], rating = request.POST['rating'], user = current_user, book = new_book
        )
        return redirect(f'/books/{new_book.id}')
    new_book=Book.objects.create(
        title = request.POST['title'], author = Author.objects.get(id=request.POST['author_selecter']), uploaded_by = current_user
    )
    Review.objects.create(
        review=request.POST['review'], rating = request.POST['rating'], user = current_user, book = new_book
    )
    return redirect(f'/books/{new_book.id}')

def book_info(request, book_id):
    context = {
        'reviews' : Review.objects.all(),
        'book' : Book.objects.get(id=book_id)
    }
    return render(request,'book_info.html', context)

def new_review(request, book_id):
    current_book = Book.objects.get(id=book_id)
    current_user = User.objects.get(id=request.session['user_id'])
    Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        book = current_book,
        user = current_user
    )
    return redirect(f'/books/{book_id}')

def delete_review(request, book_id, review_id):
    current_review = Review.objects.get(id=review_id)
    current_review.delete()
    return redirect(f'/books/{book_id}')

def user_page(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'user.html', context)

