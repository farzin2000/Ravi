from django.db import models

# Create your models here.

class Ticket(Model.models):
	
	price = models.FloatField()

class TicketEvent(object):
	
	# event = models.ForeignKey('event.Event')

class Buy(object):
	
	# user = models.ForeignKey('account.User')
	ticket = models.ForeignKey('Ticket')
	date = models.DateField()
	number = models.IntegerField()
	cardNum = models.CharField(max_lenght=16)
		
		