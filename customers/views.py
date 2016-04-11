from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from braces.views import LoginRequiredMixin
from .models import CustomerAccount, ApproveLog, PendingApprove
# Create your views here.
class AccountViews(LoginRequiredMixin,ListView):
    template_name = 'customers/accounts.html'
    model = CustomerAccount

class CertifyViews(LoginRequiredMixin,ListView):
    template_name = 'customers/certifies.html'
    model = PendingApprove