# wordwiki/urls.py
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from pages import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wordwiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^pages/', include('pages.urls', namespace="pages")),
)
