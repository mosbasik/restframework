from django.conf.urls import url

urlpatterns = [
    url(r'^snippets/$', 'main.views.snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'main.views.snippet_detail'),
]
