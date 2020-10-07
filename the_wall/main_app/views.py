from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import User
from .models import Message,Comment
from time import gmtime, strftime
from datetime import datetime


def wall(request):
    context = {
        'posts' : Message.objects.all()
    }
    return render(request, 'the_wall.html',context)

def post_message(request):
    Message.objects.create(message = request.POST['post'],user = User.objects.get(id=request.session['user_id']))
    return redirect('/wall')

def post_comment(request):
    Comment.objects.create(comment=request.POST['comment'],message=Message.objects.get(id=request.POST['current_post']), user = User.objects.get(id = request.session['user_id']))
    return redirect('/wall')

def delete_post(request,post_id):
    x = Message.objects.get(id=post_id)
    x.delete()
    return redirect('/wall')