from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.conf import settings

from core.views import HomePageView

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^home/$', HomePageView.as_view(), name='home'),
    ]

