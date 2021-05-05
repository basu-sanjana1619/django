from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

class logIn_validation(forms.Form):
 username = forms.CharField(widget = forms.TextInput(attrs = {'id' : 'username'}))
 pwd = forms.CharField(widget = forms.PasswordInput(attrs = {'id' : 'pwd'}))
 
 
def logIn(request):
 return render(request, "logIn_validation/logIn.html", {"form" : logIn_validation()})
 
def hello(request):
 if request.method == "POST":
  form = logIn_validation(request.POST)
  if form.is_valid():
   obj1 = form.cleaned_data["username"]
   obj2 = form.cleaned_data["pwd"]
  return render(request,"logIn_validation/hello.html",{"form1":obj1,"form2" : obj2})
