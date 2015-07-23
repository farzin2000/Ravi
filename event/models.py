from django.db import models

# Create your models here.

class Music(models.Model):
	
	style = models.CharField(max_length=10)
	desc = models.CharField(max_length=1000)


class Cinema(models.Model):
	
	director = models.CharField(max_length=10)
	genre = models.CharField(max_length=10)
	producer = models.CharField(max_length=10)


# class Sport(object):
	

# class IndividualSport(object):
	

# class Theater(models.Model):
	
		

class Place(models.Model):
	
	addr = models.CharField(max_length=100)
	capacity = models.IntegerField()
	placeType = models.CharField(max_length=10)

		

class Event(models.Model):
	
	name = models.CharField(max_length=100)
	duration = models.FloatField()
	date = models.DateField()
	deadline = models.DateField()
	picture = models.ImageField()
	place_id = models.ForeignKey('Place')

		
		