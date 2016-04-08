from django.conf.urls import include, url
from home.views import *
from rest_framework import routers
from .attribute_views import AttributeViewSet
from .category_views import CategoryViewSet
from .product_views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, 'cateogry')
router.register(r'attr', AttributeViewSet, 'attr')
router.register(r'product', ProductViewSet, 'product')

urlpatterns = router.urls