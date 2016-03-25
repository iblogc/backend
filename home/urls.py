from django.conf.urls import include, url
from home.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
]