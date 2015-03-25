from django.conf.urls import patterns, url
from storage.accounts.views import RegisterView

urlpatterns = []

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', 'logout_then_login', name='logout'),
)

urlpatterns += patterns(
    '',

    url(r'^register/$', RegisterView.as_view(template_name='accounts/register.html', success_url='/'), name='register')
)
