from django.conf.urls import include, url
from products.views import *

urlpatterns = [
    #products manage
    url(r'pdt/$', ProductView.as_view(), name='product'),
    url(r'active/(?P<pk>\d+)/$', ProductActiveView.as_view(), name='product-active'),
    url(r'void/(?P<pk>\d+)/$', ProductVoidView.as_view(), name='product-void'),
    url(r'detail/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product-detail'),

    #category manage
    url(r'category/$', CategoryView.as_view(), name='category'),
]