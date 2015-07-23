from django.shortcuts import render

# Create your views here.


def eventDetailedView(requset):

	return render(requset, 'event.html', {'guest': True})