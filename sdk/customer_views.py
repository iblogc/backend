# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory, Product
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Q
from braces.views import LoginRequiredMixin
from customers.serializers import CustomerAccountSerializer, \
    PendingApproveSerializer, ApproveLogSerializer
from customers.models import CustomerAccount, PendingApprove, ApproveLog


class CustomerAccountViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerAccountSerializer
    queryset = CustomerAccount.objects.all()

    @detail_route(methods=['get', 'post'])
    def active(self, request, pk=None):
        CustomerAccount.objects.update(active=True)
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['get', 'post'])
    def void(self, request, pk=None):
        CustomerAccount.objects.update(active=False)
        return Response(status=status.HTTP_200_OK)


class PendingApproveViewSet(viewsets.ModelViewSet):
    serializer_class = PendingApproveSerializer
    queryset = PendingApprove.objects.all()

    @detail_route(methods=['post','get'])
    def action(self, request, pk=None):
        pending_approve = PendingApprove.objects.get(pk=pk)
        customer_account = pending_approve.account
        approve = int(request.GET.get('approve', 0))
        message = request.GET.get('message')
        action_type = int(request.GET.get('action_type', 0))
        action_user = request.user.admin.realname
        approve_log = ApproveLog(account=customer_account,
                                 approve_info=pending_approve,
                                 action_type=action_type, approved=approve,
                                 message=message, action_user=action_user).save()
        if approve:
            if action_type == 0:
                pending_approve.certify()
            else:
                pending_approve.approve()
        return Response(status=status.HTTP_200_OK)



class ApproveLogViewSet(viewsets.ModelViewSet):
    serializer_class = ApproveLogSerializer
    queryset = ApproveLog.objects.all()
