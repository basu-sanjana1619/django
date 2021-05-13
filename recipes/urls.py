from django.urls import path
from . import views 

urlpatterns = [
      path("", views.index, name = "index"),
      path("chicken_soup", views.chicken_soup, name = "chicken_soup"),
      path("veg_soup", views.veg_soup, name = "veg_soup"),
      path("add", views.add, name = "add")  
     ]