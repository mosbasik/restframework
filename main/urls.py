from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', 'main.views.snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'main.views.snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
