from django.conf.urls import include, url
from customers.views import AccountViews, CertifyViews, ApproveViews, LogViews

urlpatterns = [
    url(r'accounts/$', AccountViews.as_view(), name='accounts'),
    url(r'certifies/$', CertifyViews.as_view(), name='certifies'),
    url(r'approves/$', ApproveViews.as_view(), name='approves'),
    url(r'logs/$', LogViews.as_view(), name='logs'),
]