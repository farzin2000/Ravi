from django.conf.urls import patterns, include, url
from django.contrib import admin
from event.views import eventDetailedView
from Ravi import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Ravi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),	
    url(r'^$', views.startPage),
    url(r'^main/', views.mainPage),
    url(r'^event/', eventDetailedView),
    url(r'^buy/', views.buy),
    url(r'^user/', views.user),
    url(r'^admin/', views.modir),

    


    

)

