from django.urls import path
from . import views

urlpatterns = [
      path("logIn", views.logIn, name = "logIn"),
      path("Hello", views.hello, name = "hello")]