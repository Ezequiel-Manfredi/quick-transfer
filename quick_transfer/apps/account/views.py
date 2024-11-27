from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView

from .models import Account

class Details(LoginRequiredMixin,TemplateView):
  template_name = 'account/home.html'
  user = None
  
  def dispatch(self, request, *args, **kwargs):
    self.user = request.user
    return super().dispatch(request, *args, **kwargs)
  
  def get_context_data(self, **kwargs):
      ctx = super(Details, self).get_context_data(**kwargs)
      ctx['account'] = self.user.account
      return ctx

class Load(LoginRequiredMixin,TemplateView):
  template_name = 'account/load.html'
  user = None
  
  def dispatch(self, request, *args, **kwargs):
    self.user = request.user
    return super().dispatch(request, *args, **kwargs)
  
  def get_context_data(self, **kwargs):
      ctx = super(Load, self).get_context_data(**kwargs)
      ctx['account'] = self.user.account
      return ctx
  
  def post(self, request, *args, **kwargs):
    amount = int(request.POST['amount'])
    account = self.user.account
    account.balance = account.balance + amount
    account.save()
    return redirect('account:home')
  
class Search(LoginRequiredMixin,TemplateView):
  model = Account
  user = None
  
  def dispatch(self, request, *args, **kwargs):
    self.user = request.user
    return super().dispatch(request, *args, **kwargs)
  
  def get_context_data(self, **kwargs):
      ctx = super(Load, self).get_context_data(**kwargs)
      ctx['account'] = self.user.account
      return ctx
  
  def get(self, request, *args, **kwargs):
    
    return redirect('account:home')