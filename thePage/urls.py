from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    (r'^$', 'thePage.views.base'),
    #(r'^note/(?P<slug>[-\w]+)/$',
     #'django.views.generic.list_detail.object_detail',
     #dict(queryset=notes, slug_field='slug')),
    #(r'^create/$','notes.views.create_note'),
    #(r'^note/(?P<slug>[-\w]+)/update/$','notes.views.update_note'),
)