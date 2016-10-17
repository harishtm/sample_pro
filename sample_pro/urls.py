from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^app1/', include('app1.urls')),
    url(r'^app2/', include('app2.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
