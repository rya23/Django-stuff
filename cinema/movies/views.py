from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request,"movies/index.html",
    {
       "movies":Movie.objects.all()
    })

def movie(request,movie_id):
   movie= Movie.objects.get(id=movie_id)
   actors=movie.actor.all()
   # directors=movie.director.all()
   return render(request,"movies/movie.html",{
      "movie":movie,
      "actors":actors,
      "title":movie.name
      # "directors":directors
   })
def actor(request,actor_name):
   actor=Actor.objects.get(name=actor_name)
   movies=actor.movie.all()
   return render(request,"movies/actor.html",
   {
      "actor":actor,
      "movies":movies,
      "title":actor.name
   })

def director(request,director_name):
   director=Director.objects.get(name=director_name)
   movie=Movie.objects.all()
   return render(request,"movies/director.html",
   {
        "director":director,
        "movie":movie,
        "title":director.name
   })

def add(request):
   return render(request,"movies/add.html")
