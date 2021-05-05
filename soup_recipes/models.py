from django.db import models

# Create your models here.
class logIn(models.Model):
 username = models.CharField(max_length = 64, primary_key = True)
 password = models.CharField(max_length = 64)
