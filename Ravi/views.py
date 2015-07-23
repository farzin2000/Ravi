from django.shortcuts import render, render_to_response
from django.template import Context, Template
from django.http import HttpResponse
import datetime

def mainPage(requset):
	# now = datetime.datetime.now()
	# t = Template("<html><body>It is now {{ current_date }}.</body></html>")
	# html = t.render(Context({'current_date': now}))
	# return HttpResponse(html)
	return render(requset, 'main.html', {'guest': True})


def startPage(requset):

	return render(requset, 'start.html', {'sigend_in': True})

def buy(requset):
	
	return render(requset, 'buy.html', {'sigend_in': True})


def user(requset):
	return render(requset, 'userProfile.html', {'sigend_in': True})

def modir(requset):
	return render(requset, 'admin.html')