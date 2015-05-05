from art_gallery import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^artists$', views.artists, name='artists'),
    url(r'^artwork$', views.artwork, name='artwork'),
    url(r'^belongs_to$', views.belongs_to, name='belongs_to'),
    url(r'^customer$', views.customer, name='customer'),
    url(r'^groups$', views.groups, name='groups'),
    url(r'^likes_artist$', views.likes_artist, name='likes_artist'),
    url(r'^likes_group$', views.likes_group, name='likes_group')
)