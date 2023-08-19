from django.urls import path
from . import views

urlpatterns = [

    path("",views.home,name="home"),
    path("movie/<int:movie_id>",views.movie,name="movie"),
    path("actor/<str:actor_name>",views.actor,name="actor"),
    path("director/<str:director_name>",views.director,name="director"),
    path("add",views.add,name="add")



]