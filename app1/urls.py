from django.conf.urls import patterns, include, url
from app1.views import App1Home, Validate
urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', App1Home.as_view(), name='app1home'),
    url(r'^validate/$', Validate.as_view(), name='validate_member'),

)