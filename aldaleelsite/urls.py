from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'aldaleel.views.home', name='home'),
    url(r'^companies$', 'aldaleel.views.companies', name='companies'),
    url(r'^company-details$', 'aldaleel.views.company_details', name='company-details'),
    url(r'^about', 'aldaleel.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
