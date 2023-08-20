from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *
# Create your views here.

def home(request):
    return render(request,"movies/index.html",
    {
       "movies":Movie.objects.all()
    })



def insert(request,movie_id):
   if request.method=="POST":
      movie=Movie.objects.get(id=movie_id)
      actor_id=int(request.POST["actor"])
      actor=Actor.objects.get(id=actor_id)
      actor.movie.add(movie)

      return HttpResponseRedirect(reverse("movie",args=(movie.id,)))

# def add(request):

#    if request.method=="POST":
#       form=Movieform(request.POST)
#       movie_name=request.POST.get("Movie")
#       director_name=request.POST.get("Director")
#       movie_year=(request.POST.get("Year"))
#       actor_name=(request.POST.get("Actor"))

#       if not movie_name or not movie_year or not director_name or not actor_name:
#          print("Missing required fields.")
#          form=Movieform()
#          return render(request,'movies/add.html',
#          {
#             "form":form
#          })       
#       actor_name,create=Actor.objects.get_or_create(name=actor_name)
#       director,created=Director.objects.get_or_create(name=director_name)
#       if form.is_valid():
#          movie=Movie(name=movie_name,director=director,year=movie_year)
#          movie.save()
#          actor=Actor(name=actor_name,movie=movie)
#          actor.save()
#          return HttpResponseRedirect(reverse("home"))
#    else:
#       form=Movieform()
#    return render(request,'movies/add.html',
#    {
#       "form":form
#    })


def add(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data["movie"]
            director_name = form.cleaned_data["director"]
            movie_year = form.cleaned_data["year"]
            actor_name = form.cleaned_data["actor"]

            actor, created = Actor.objects.get_or_create(name=actor_name)
            director, created = Director.objects.get_or_create(name=director_name)

            movie = Movie(name=movie_name, director=director, year=movie_year)
            movie.save()
            actor.movie.add(movie)

            return HttpResponseRedirect(reverse("home"))
    else:
        form = MovieForm()

    return render(request, 'movies/add.html', {"form": form})


def movie(request,movie_id):
   movie= Movie.objects.get(id=movie_id)
   actors=movie.actor.all()
   not_inc=Actor.objects.exclude(movie=movie).all()
   # directors=movie.director.all()

   return render(request,"movies/movie.html",{
      "movie":movie,
      "actors":actors,
      "title":movie.name,
      "not_inc":not_inc
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





