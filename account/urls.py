from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import eventDetailedView, eventsType, create_event,edit_event,delete_events,addType,delType,showsubs,delSubType,edit_subtype
from Ravi import views
from account.views import allUsers, delUsers,eventsall,types

urlpatterns = patterns('',

    url(r'^events/([a-zA-Z0-9]+)/', eventsType),
    url(r'^settings/', views.adminSetting),
    url(r'^users/all', allUsers),
    url(r'^users/(?P<userid>[0-9]+)$/', delUsers),
    url(r'^$', views.modir),
    url(r'^add-event/([a-zA-Z0-9]+)', create_event),
    url(r'^edit-events/all/', eventsall),
    url(r'^types/all/', types),
    url(r'^addTypes/', addType),
    url(r'^deleteTypes/([a-zA-Z0-9]+)', delType),
    url(r'^SubTypes/([a-zA-Z0-9]+)', showsubs),
    url(r'^deleteSubTypes/([a-zA-Z0-9]+)', delSubType),
    url(r'^edit/([a-zA-Z0-9]+)',edit_subtype),


)



