from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (DeleteView)
# Create your views here.

def home(request):
    return render(request,"movies/home.html",
    {
       "movies":Movie.objects.all()
    })



# def insert(request,movie_id):
#    if request.method=="POST":
#       movie_form = ActorForm(request.POST)
#       if form.is_valid():
#          actor_names = form.cleaned_data["actor"].split(',')
#          for actor_name in actor_names:
#                actor_name = actor_name.strip()
#                actor, created = Actor.objects.get_or_create(name=actor_name)
#                movie.actor.add(actor)
#    # return HttpResponseRedirect(reverse("movie",args=(movie.id,)))
#          return HttpResponseRedirect(reverse("movie"))

#    else:
#         movie_form = ActorForm()

#    return render(request, 'movies/movie.html', {"movie_form": movie_form})

@login_required
def add(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data["movie"]
            director_name = form.cleaned_data["director"]
            movie_year = form.cleaned_data["year"]
            actor_names = form.cleaned_data["actor"].split(',')
            user = request.user
            director, created = Director.objects.get_or_create(name=director_name)
            movie = Movie(name=movie_name, director=director, year=movie_year,user=user)
            movie.save()

            for actor_name in actor_names:
                actor_name = actor_name.strip()
                actor, created = Actor.objects.get_or_create(name=actor_name)
                movie.actor.add(actor)

            return HttpResponseRedirect(reverse("home"))
    else:
        form = MovieForm()

    return render(request, 'movies/add.html', {"form": form})


def movie(request,movie_id):
   movie= Movie.objects.get(id=movie_id)
   actors=movie.actor.all()
   not_inc=Actor.objects.exclude(movie=movie).all()
   # directors=movie.director.all()
   if request.method=="POST":
      movie_form = ActorForm(request.POST)
      if movie_form.is_valid():
         actor_names = movie_form.cleaned_data["actor"].split(',')
         for actor_name in actor_names:
               actor_name = actor_name.strip()
               actor, created = Actor.objects.get_or_create(name=actor_name)
               movie.actor.add(actor)
   # return HttpResponseRedirect(reverse("movie",args=(movie.id,)))
         return HttpResponseRedirect(reverse("movie"))
   else:
      movie_form = ActorForm()

   return render(request, 'movies/movie.html', 
   {"movie_form": movie_form,
      "movie":movie,
      "actors":actors,
      "title":movie.name,
      "not_inc":not_inc
   
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


def register(request):
   return render(request,"movies/register.html")   

