from django.conf.urls import patterns, url, include

from grooveGenerator import views
from grooveGenerator.views import ColorList
from grooveGenerator import *

urlpatterns = patterns('',
    #url(r'^$', views.grooveGenerator, name='grooveGenerator'),
    url(r'^$', ColorList.as_view(), name="grooveGenerator"),
    url(r"^like_color_(?P<color_id>\d+)/$", "grooveGenerator.views.toggle_color_like", name="toggle_color_like"),
    url(r'^ajax1_json$', 'grooveGenerator.views.ajax1'),
    #url(r"^search/$", "grooveGenerator.views.submit_color_search_from_ajax", name="color_list"),

    # adding to attempt ajax
    #url(r'^ajax/', post),
    #url(r'^$', PostExample.as_view(), name='test-start'), 
)
