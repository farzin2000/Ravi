from django.shortcuts import render

# Create your views here.


def eventDetailedView(requset):

    return render(requset, 'event.html', {'guest': True})


def events(requset):
    return render(requset, 'events.html', {'signed_in': True})