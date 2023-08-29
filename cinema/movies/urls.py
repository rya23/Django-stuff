from django.urls import path
from . import views
# from .views import MovieUpdateView,MovieCreateView
urlpatterns = [

    path("",views.home,name="home"),
    path("movie/<int:movie_id>",views.movie,name="movie"),
    path("actor/<str:actor_name>",views.actor,name="actor"),
    path("director/<str:director_name>",views.director,name="director"),
    # path("movie/<int:movie_id>/insert",views.insert,name="insert"),
    path("add",views.add,name='add'),
    path('movie/<int:movie_id>/delete/', views.delete_movie, name='movie-delete'),
    path("movie/<int:movie_id>/dlete/",views.delete,name="delete")

]