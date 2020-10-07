from django.db import models
from login_app.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name='books_uploaded', on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name='liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)