from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Food


# Create your views here.
class Enter_recipe(forms.Form):
 name = forms.CharField()
 recipe= forms.CharField(widget=forms.Textarea(attrs={"rows":30, "cols":100}))
 

def index(request):
 return render(request, "recipes/index.html",{"form" : Enter_recipe()})

def chicken_soup(request):
 return render(request, "recipes/chicken_soup.html")
 
def veg_soup(request):
 return render(request, "recipes/vegetable_soup.html")
 
def add(request):
 if request.method == "POST":
  record = Enter_recipe(request.POST)
  if record.is_valid():
   record1 = record.cleaned_data["name"]
   record2 = record.cleaned_data["recipe"]
   r = Food(name = record1, recipe = record2)
   r.save()
   return render(request, "recipes/success.html")
  else:
   return render(request, "recipes/error.html")