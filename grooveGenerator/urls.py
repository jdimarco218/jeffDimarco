from django.conf.urls import patterns, url

from grooveGenerator import views

urlpatterns = patterns('',
    url(r'^$', views.grooveGenerator, name='grooveGenerator'),
)
