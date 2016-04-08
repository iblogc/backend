from django.conf.urls import include, url, patterns
from products.views import *

urlpatterns = [
    #products manage
    url(r'pdt/$', ProductView.as_view(), name='product'),

    #category manage
    url(r'category/$', CategoryView.as_view(), name='category'),

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