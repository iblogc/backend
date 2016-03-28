from django.conf.urls import include, url
from products.views import *

urlpatterns = [
    url(r'pdt/$', Pdt.as_view(), name='login'),
]