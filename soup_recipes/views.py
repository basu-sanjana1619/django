from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

class logIn_validation(forms.Form):
 username = forms.CharField(label = "Username")
 pwd = forms.CharField(label = "Password")
 
 
def logIn(request):
 return render(request, "soup_recipes/index.html", {"form" : logIn_validation()})
 
def hello(request):
 if request.method == "POST":
  form = logIn_validation(request.POST)
  if form.is_valid():
   obj1 = form.cleaned_data["username"]
   obj2 = form.cleaned_data["pwd"]
  return render(request,"soup_recipes/hello.html",{"form1":obj1,"form2" : obj2})
