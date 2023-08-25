from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import *

class MovieForm(forms.Form):
   movie = forms.CharField(label="Movie",max_length= 100)
   year=forms.IntegerField(label="Year")
   director=forms.CharField(label="Director",max_length= 100)
   actor=forms.CharField(label="Actor", widget=forms.Textarea,help_text= 'Use comma to enter multiple Actors.')

class ActorForm(forms.Form):
   actor=forms.CharField(label="Actor", widget=forms.Textarea,help_text= 'Use comma to enter multiple Actors.')