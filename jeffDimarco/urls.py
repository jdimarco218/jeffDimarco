from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name="home"),

    url(r'^grooveGenerator/', include('grooveGenerator.urls', namespace="grooveGenerator")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', include('posts.urls')), 
    url(r'^tags/', include('tags.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
