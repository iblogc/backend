from django.conf.urls import include, url
from home.views import *
from rest_framework import routers
from .views import CategoryViewSet, AttributeViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, 'cateogry')
router.register(r'attr', AttributeViewSet, 'attr')

urlpatterns = router.urls