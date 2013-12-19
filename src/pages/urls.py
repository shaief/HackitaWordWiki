# pages/urls.py
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /pages/5/
    #url(r'^add-word/$', login_required(view.PostPageView.as_view()), name='page_create'),
        # ex: /pages/NAME/
    url(r'^(?P<page_id>\d+)/$', views.pageid, name='detail'),

    url(r'^post-page/$',
        login_required(views.PostPageView.as_view()),
        name='post_page'),                   
     
    
    # ex: /pages/1/edit/
    url(r'^(?P<pk>\d+)[^\/]*\/delete/$',
        login_required(views.DeletePageView.as_view()), name='page_delete'),
    
    url(r'^(?P<pk>\d+)[^\/]*\/edit/$',
        login_required(views.EditPageView.as_view()), name='page_edit'),
    
    # ex: /pages/NAME/
    url(r'^(?P<page_word>[^/]+)$', views.words, name='words'),
    #url(r'^(?P<word_edit>[a-z]+)/edit/$', views.edit, name='word_edit'),
    url(r'^(?P<word>[^/]+)/edit/$',
        login_required(views.EditPageView.as_view()), name='page_edit'),
    
    #ex: /pages/NAME/edit/
    
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name="login"),

    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('home')}, name="logout"),



)
