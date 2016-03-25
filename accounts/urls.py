from django.conf.urls import include, url
from accounts.views import *

urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='login'),
]