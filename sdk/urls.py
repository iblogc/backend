from django.conf.urls import include, url
from home.views import *
from rest_framework import routers
from .attribute_views import AttributeViewSet
from .category_views import CategoryViewSet
from .product_views import ProductViewSet
from .brand_views import BrandViewSet
from .company_views import ManufactorViewSet
from .series_views import SeriesViewSet
from .account_views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, 'cateogry')
router.register(r'attr', AttributeViewSet, 'attr')
router.register(r'product', ProductViewSet, 'product')
router.register(r'brand', BrandViewSet, 'brand')
router.register(r'manufactor', ManufactorViewSet, 'manufactor')
router.register(r'series', SeriesViewSet, 'series')
router.register(r'account', AccountViewSet, 'account')
urlpatterns = router.urls