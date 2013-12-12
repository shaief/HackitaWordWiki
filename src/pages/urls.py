# pages/urls.py
from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /pages/5/
    url(r'^(?P<page_id>\d+)/$', views.detail, name='detail'),
    # ex: /pages/NAME/
    url(r'^(?P<page_word>.+)/$', views.words, name='words'),
    
)
