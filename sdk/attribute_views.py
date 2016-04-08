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

    def create(self, request):
        name = request.POST.get('name','')
        category_id = request.POST.get('category_id', 0)
        value = [v.strip() for v in request.POST.get('value','').split('\n')]
        if '' in value:
            value.remove('')
        searchable = int(request.POST.get('searchable', 1)) == 1
        attribute = ProductCategoryAttribute()
        attribute.name = name
        attribute.category = ProductCategory.objects.get(pk=category_id)
        attribute.value = json.dumps(value)
        attribute.searchable = searchable
        attribute.save()
        return Response({'success': 1},status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        ProductCategoryAttribute.objects.filter(pk=pk).update(
            active=False)
        ProductCategoryAttributeValue.objects.filter(attribute_id=pk).update(active=False)
        return Response({'success': 1},status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def default_values(self, request, pk=None):
        values = json.loads(ProductCategoryAttribute.objects.get(pk=pk).value)
        return  Response(values,status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        attribute = ProductCategoryAttribute.objects.get(pk=pk)
        index = int(request.POST.get('index', 0))
        text = request.POST.get('text').strip()
        values = json.loads(attribute.value)
        pre_text = ''
        if len(values) <= index:
            values.append(text)
        else:
            pre_text = values[index]
            values[index] = text
        attribute.value = json.dumps(values)
        attribute.save()
        attribute.values.filter(value=pre_text).update(value=text)
        return Response({'success': 1},status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def delete_default_value(self, request, pk=None):
        attribute = ProductCategoryAttribute.objects.get(pk=pk)
        index = int(request.POST.get('index', 0))
        values = json.loads(attribute.value)
        if index < len(values):
            pre_text = values[index]
            values.remove(pre_text)
            attribute.value = json.dumps(values)
            attribute.save()
            attribute.values.filter(value=pre_text).delete()
        return Response({'success': 1},status=status.HTTP_200_OK)




