from django.db import models
from login_app.models import User

class BookManager(models.Manager):
    def basic_validator_book(self,postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = 'You must have a title for the book.'
        if len(postData['author']) == 0:
            errors['author'] = 'You must have an author for the book.'
        if len(postData['review']<10):
            errors['review'] = 'Review must be at least 10 characters'

class Author(models.Model):
    name = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name = 'uploaded_books', on_delete = models.CASCADE)
    author = models.ForeignKey(Author, related_name = 'books', on_delete = models.CASCADE)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name = 'reviews', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = 'reviews', on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)




