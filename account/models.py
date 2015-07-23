from django.db import models
from django.contrib import auth

# Create your models here.


class User(auth.models.User):
	
	user = models.OneToOneField(auth.models.User)
	address = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)
	avatar = models.ImageField(max_length=100)
	userType = models.CharField(max_length=100)

