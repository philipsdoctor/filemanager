from django.conf.urls import patterns, url

from fm import views

urlpatterns = patterns('',
	# ex: /fm/
    url(r'^$', views.index, name='index'),
    # ex: /fm/list/
    url(r'^list/$', views.list, name='list'),
    # ex: /fm/manage_document/
    url(r'^manage_document/$', views.manage_document, name='manage_document'),    
    # ex: /fm/5/
    url(r'^(?P<document_id>\d+)/$', views.detail, name='detail'),
    # ex: /fm/5/results/
    url(r'^(?P<document_id>\d+)/results/$', views.results, name='results'),
)