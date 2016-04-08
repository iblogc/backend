from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response


class AttributeViewSet(viewsets.ViewSet):
    def list(self, request):
        cid = request.GET.get('cid', 0)
        if not cid:
            return Response(status=status.HTTP_404_NOT_FOUND)
        res = {}
        res['attr'] = []
        category = ProductCategory.objects.filter(pk=cid)
        if not category.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            category=category[0]
        for attr in ProductCategoryAttribute.objects.filter(active=1,
                                                            category=category).all():
            attr_obj = ProductCategoryAttribute.objects.get(id=int(attr.id))
            attr_dic = {}
            attr_dic['id'] = attr.id
            attr_dic['name'] = attr.name
            attr_dic["type"] = attr.type
            temp = []
            default = ""
            for value in ProductCategoryAttributeValue.objects.filter(active=1,
                                                                      attribute=attr_obj).all():
                if value.name == attr.value:
                    default = value.id
                temp.append({
                    "id": value.id,
                    "value": value.name
                })
            attr_dic['values'] = temp
            attr_dic['default'] = default
            res['attr'].append(attr_dic)
        return Response(res,
                        status=status.HTTP_200_OK)

