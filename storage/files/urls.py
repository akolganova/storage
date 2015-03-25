from django.conf.urls import patterns, url

urlpatterns = []

urlpatterns += patterns(
    'storage.files.views',

    url(r'^$', 'index', {'template_name': 'files/index.html'}),
    url(r'^downloads/(.*)', 'download'),
    url(r'^delete/(.*)', 'delete'),
)
