from django.shortcuts import render, redirect
from .forms import MovieForm, CategoryForm, CastForm, CountryForm
from .models import Movie
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render (request,"index.html",{
        'movies':movies
    })

@login_required
@permission_required("netflix.add.movie")
def add(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render (request, "add.html",{
        'form':form
    })

@login_required
def display(request, id):
    movie=Movie.objects.get(pk=id)
    return render(request, "display.html",{
        'movie':movie
    })

@login_required
@permission_required("netflix.change.movie")
def update(request, id):
    movie=Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return render(request, "display.html",{
            "movie":movie
        })
    return render (request, "update.html",{
        'form':form,
        'movie':movie
    })

@login_required
@permission_required("netflix.delete.movie")
def delete(request,id):
    movie=Movie.objects.get(pk=id)
    movie.delete()
    return redirect("index")

