from django.conf.urls import include, url, patterns
from products.views import *

urlpatterns = [
    #products manage
    url(r'pdt/$', ProductView.as_view(), name='product'),

    #category manage
    url(r'category/$', CategoryView.as_view(), name='category'),

    #company brand series
    url(r'company/(?P<category_id>\d+)/batch_delete/$', company_batch_delete, name='company-batch-delete'),
    url(r'company/(?P<company_id>\d+)/update/$', company_update,
        name='company-update'),
    url(r'company/(?P<category_id>\d+)/(?P<company_id>\d+)/brand/create/$', brand_create, name='company-brand-create'),
    #brand series
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

    url(r'category/attributes/(?P<category_id>\d+)/$', category_attributes, name='category-attributes'),
    url(r'category/attribute/create/(?P<category_id>\d+)/$', category_attribute_create, name='category-attribute-create'),
    url(r'category/attribute/delete/(?P<attribute_id>\d+)/$', category_attribute_delete,
        name='category-attribute-delete'),
    url(r'category/attribute/default_values/(?P<attribute_id>\d+)/$',
        category_attribute_default_values,
        name='category-attribute-default-values'),

    url(r'category/attribute/values/(?P<category_id>\d+)/(?P<series_id>\d+)/$', category_attribute_values, name='category-attribute-values'),
    url(r'category/attribute/value/update/(?P<series_id>\d+)/$', category_attribute_value_update,
        name='category-attribute-value-update'),
    url(r'category/attribute/value/delete/(?P<attribute_id>\d+)/$', category_attribute_value_delete,
        name='category-attribute-value-delete'),
    url(r'category/attribute/default_value/update/(?P<attribute_id>\d+)/$',
        category_attribute_default_value_update,
        name='category-attribute-default-value-update'),
    url(r'category/attribute/default_value/delete/(?P<attribute_id>\d+)/$',
        category_attribute_default_value_delete,
        name='category-attribute-default-value-delete'),

    url(r'product/file/upload/$', upload_product_file, name='product-file-upload'),
    url(r'product/preview/upload/$', upload_product_preview,
        name='product-preview-upload'),
]