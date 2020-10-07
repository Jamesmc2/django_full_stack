from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages

def index(request):
    return redirect('/shows')

def newShow(request):
    return render(request,'new_show.html')

def createShow(request):
    errors = Show.objects.basic_validator_create(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f'/shows/{new_show.id}')

def aboutShow(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id),
    }
    return render(request,'about_show.html', context)

def listShows(request):
    context = {
        'shows' : Show.objects.all(),
    }
    return render(request,'shows_list.html',context)

def editShow(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id),
    }
    return render(request,'edit_show.html',context)

def updateShow(request, show_id):
    errors = Show.objects.basic_validator_edit(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')

    show=Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{show_id}')

def destroyShow(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')


