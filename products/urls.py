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
    url(r'sub_category/(?P<pk>\d+)/$', SubCategoryView.as_view(), name='sub-category'),
    url(r'sub_category/(?P<pk>\d+)/delete/$', SubCategoryDeleteView.as_view(), name='sub-category-delete'),
    url(r'sub_category/(?P<pk>\d+)/create/$', SubCategoryCreateView.as_view(), name='sub-category-create'),
    url(r'sub_category/(?P<pk>\d+)/update/$', SubCategoryUpdateView.as_view(), name='sub-category-update'),
    url(r'sub_category/(?P<pk>\d+)/companies/$', SubCategoryCompaniesView.as_view(), name='sub-category-companies'),
    url(r'sub_category/(?P<pk>\d+)/company/create/$', SubCategoryCompanyCreateView.as_view(), name='sub-category-company-create'),

    #company brand series
    url(r'company/(?P<category_id>\d+)/(?P<company_id>\d+)/delete/$', SubCategoryCompanyDeleteView.as_view(), name='company-delete'),
    url(r'company/(?P<pk>\d+)/update/$', CompanyUpdateView.as_view(),
        name='company-update'),
    url(r'company/(?P<category_id>\d+)/(?P<company_id>\d+)/brands/$', CompanyBrandView.as_view(), name='company-brand'),
    url(r'company/(?P<category_id>\d+)/(?P<company_id>\d+)/brand/create/$', CompanyBrandCreateView.as_view(), name='company-brand-create'),
    #brand series
    url(r'brand/(?P<pk>\d+)/series/$', BrandSeriesView.as_view(), name='brand-series'),
    url(r'brand/(?P<pk>\d+)/update/$', CompanyBrandUpdateView.as_view(), name='brand-update'),
    url(r'brand/(?P<category_id>\d+)/(?P<company_id>\d+)/(?P<brand_id>\d+)/delete/$', CompanyBrandDeleteView.as_view(),
        name='brand-delete'),
    url(r'brand/(?P<pk>\d+)/series/create/$', BrandSeriesCreateView.as_view(), name='brand-series-create'),

    url(r'series/(?P<pk>\d+)/delete/$', SeriesDeleteView.as_view(), name='series-delete'),
    url(r'series/(?P<pk>\d+)/update/$', SeriesUpdateView.as_view(), name='series-update'),
]