from django.db import models


# Create your models here.


# class TicketEvent(models.Model):
#
#
# 	event = models.ForeignKey('event.Event')




class Ticket(models.Model):

    price = models.FloatField()
    type = models.CharField(max_length=100)
    seat_num = models.CharField(max_length=10)



class Buy(models.Model):

    user = models.OneToOneField('account.User')
    event = models.OneToOneField('event.Event')
    date = models.DateField()
    purches_id = models.IntegerField()
    trace_id = models.IntegerField()
    ticket = models.ManyToManyField(Ticket)
