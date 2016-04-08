"""gezbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("home.urls", namespace='home')),

    url(r'^accounts/', include("accounts.urls", namespace='accounts')),
    url(r'^property/?', include("property.urls", namespace='property')),
    url(r'^product/?', include("products.urls", namespace='product')),
    url(r'^system/?', include("system.urls", namespace='system')),
    url(r'^media/(?P<path>.*)$', serve,
     {'document_root': settings.MEDIA_ROOT}),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    # sdk
    url(r'^sdk/', include("sdk.urls", namespace='sdk')),
    # resource files
    # url(r'^resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.RESOURCES_FILES}),
]
