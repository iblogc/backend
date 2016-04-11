from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from braces.views import LoginRequiredMixin
from .models import CustomerAccount, ApproveLog, PendingApprove, ApproveLog
# Create your views here.
class AccountViews(LoginRequiredMixin,ListView):
    template_name = 'customers/_accounts.html'
    model = CustomerAccount

class CertifyViews(LoginRequiredMixin,ListView):
    template_name = 'customers/_certifies.html'
    model = PendingApprove

class ApproveViews(LoginRequiredMixin,ListView):
    template_name = 'customers/_approves.html'
    model = PendingApprove

class LogViews(LoginRequiredMixin,ListView):
    template_name = 'customers/_logs.html'
    model = ApproveLog