from django.conf.urls import include, url, patterns
from products.views import *

urlpatterns = [
    #products manage
    url(r'pdt/$', ProductView.as_view(), name='product'),
    url(r'active/(?P<pk>\d+)/$', ProductActiveView.as_view(), name='product-active'),
    url(r'void/(?P<pk>\d+)/$', ProductVoidView.as_view(), name='product-void'),
    url(r'detail/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product-detail'),

    #category manage
    url(r'category/$', CategoryView.as_view(), name='category'),
    url(r'category/search/$', category_search, name='category-search'),
    url(r'sub_category/(?P<category_id>\d+)/$', sub_categories, name='sub-category'),
    url(r'sub_category/(?P<category_id>\d+)/delete/$', category_delete, name='sub-category-delete'),
    url(r'sub_category/batch_delete/$', category_batch_delete, name='sub-category-batch-delete'),
    url(r'sub_category/(?P<category_id>\d+)/create/$', category_create, name='sub-category-create'),
    url(r'sub_category/(?P<category_id>\d+)/update/$', category_update, name='sub-category-update'),
    url(r'sub_category/(?P<category_id>\d+)/companies/$', companies, name='sub-category-companies'),
    url(r'sub_category/(?P<category_id>\d+)/company/create/$', company_create, name='sub-category-company-create'),

    #company brand series
    url(r'company/(?P<category_id>\d+)/(?P<company_id>\d+)/delete/$', company_delete, name='company-delete'),
    url(r'company/(?P<category_id>\d+)/batch_delete/$', company_batch_delete, name='company-batch-delete'),
    url(r'company/(?P<company_id>\d+)/update/$', company_update,
        name='company-update'),
    url(r'company/(?P<category_id>\d+)/(?P<company_id>\d+)/brands/$', brands, name='company-brand'),
    url(r'company/(?P<category_id>\d+)/(?P<company_id>\d+)/brand/create/$', brand_create, name='company-brand-create'),
    #brand series
    url(r'brand/(?P<brand_id>\d+)/series/$', brand_series, name='brand-series'),
    url(r'brand/(?P<brand_id>\d+)/update/$', brand_update, name='brand-update'),
    url(r'brand/(?P<category_id>\d+)/(?P<company_id>\d+)/(?P<brand_id>\d+)/delete/$', brand_delete,
        name='brand-delete'),
    url(r'brand/(?P<category_id>\d+)/(?P<company_id>\d+)/batch_delete/$', brand_batch_delete,
        name='brand-batch-delete'),
    url(r'brand/(?P<brand_id>\d+)/series/create/$', series_create, name='brand-series-create'),

    url(r'series/(?P<series_id>\d+)/delete/$', series_delete, name='series-delete'),
    url(r'series/batch_delete/$', series_batch_delete, name='series-batch-delete'),
    url(r'series/(?P<series_id>\d+)/update/$', series_update, name='series-update'),
    # import
    url(r'import/$', import_xls, name='import'),

    url(r'export/$', export_xls, name='export'),
]