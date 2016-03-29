from django.conf.urls import include, url
from products.views import *

urlpatterns = [
    url(r'pdt/$', Pdt.as_view(), name='login'),
    url(r'active/(?P<pk>\d+)/$', ProductActiveView.as_view(), name='active'),
    url(r'void/(?P<pk>\d+)/$', ProductVoidView.as_view(), name='void'),
    url(r'detail/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
]