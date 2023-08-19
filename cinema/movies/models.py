from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField("name", max_length=50, default="random")
    # actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    year = models.IntegerField()
    director = models.ForeignKey("Director", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name} "


class Actor(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ManyToManyField(Movie,blank=True,related_name="actor")
    def __str__(self):
        return self.name



