from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):

    user = models.OneToOneField(User)
    address = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=12)
    gender = models.CharField(max_length=100)
    avatar = models.ImageField()
    userType = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


