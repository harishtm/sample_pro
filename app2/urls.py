from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from app2.views import App2Home
urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', App2Home.as_view(), name='app2home'),

)