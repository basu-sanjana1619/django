from django.urls import path
from . import views

urlpatterns = [
      path("", views.logIn, name = "logIn"),
      path("hello", views.hello, name = "hello")
      ]