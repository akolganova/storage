from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns(
    '',

    url(r'^$', RedirectView.as_view(url='/files/'), name="index"),

    (r'^accounts/', include('storage.accounts.urls')),
    url(r'^files/', include('storage.files.urls'), name='files'),
)
