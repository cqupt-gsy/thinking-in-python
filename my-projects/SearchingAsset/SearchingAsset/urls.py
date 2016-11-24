from django.conf.urls import patterns, include, url
from django.contrib import admin


from MySearching import views
from MySearching import solid_views
from MySearching import thing_views
from MySearching import medical_views
from MySearching import others_views




urlpatterns = patterns('',
    # Examples:

    # url(r'^$', 'SearchingAsset.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.indexPage),
    url(r'^thing/$', views.thingPage),
    url(r'^medical/$', views.medicalPage),
    url(r'^others/$', views.othersPage),
    url(r'^solidsearch/$', solid_views.solidSearchResults),
    url(r'^thingsearch/$', thing_views.thingSearchResults),
    url(r'^medicalsearch/$', medical_views.medicalSearchResults),
    url(r'^otherssearch/$', others_views.othersSearchResults),
    url(r'^admin/', include(admin.site.urls)),
)
