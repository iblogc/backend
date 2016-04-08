from django.conf.urls import include, url
from home.views import *
from rest_framework import routers
from .attribute_views import AttributeViewSet
from .category_views import CategoryViewSet
from .product_views import ProductViewSet
from .brand_views import BrandViewSet
from .company_views import CompanyViewSet
from .series_views import SeriesViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, 'cateogry')
router.register(r'attr', AttributeViewSet, 'attr')
router.register(r'product', ProductViewSet, 'product')
router.register(r'brand', BrandViewSet, 'brand')
router.register(r'company', CompanyViewSet, 'company')
router.register(r'series', SeriesViewSet, 'series')

urlpatterns = router.urls