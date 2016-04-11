from django.conf.urls import include, url
from customers.views import AccountViews

urlpatterns = [
    url(r'accounts/$', AccountViews.as_view(), name='accounts'),
]