from django.conf.urls import patterns, url

from grooveGenerator import views
from grooveGenerator.views import ColorList

urlpatterns = patterns('',
    #url(r'^$', views.grooveGenerator, name='grooveGenerator'),
    url(r'^$', ColorList.as_view(), name="grooveGenerator"),
    url(r"^like_color_(?P<color_id>\d+)/$", "grooveGenerator.views.toggle_color_like", name="toggle_color_like"),
)
