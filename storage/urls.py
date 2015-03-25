from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = patterns(
    '',

    # Examples:
    # url(r'^$', 'storage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/files/'), name="index"),

    (r'^accounts/', include('storage.accounts.urls')),
    url(r'^files/', include('storage.files.urls'), name='files'),
)
