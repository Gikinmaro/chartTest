from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
from django.conf import settings
urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^', include('thePage.urls')),
)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
