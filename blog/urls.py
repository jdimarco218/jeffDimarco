from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^api-auth/', include('rest_framework.urls',
    #index
    url(r'^$', 'blog.views.home', name="home"),
)
