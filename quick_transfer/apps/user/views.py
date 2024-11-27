from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import FormNewUser

from .models import User

class NewUser(CreateView):
    template_name = 'user/signup.html'
    model = User
    form_class = FormNewUser
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        ctx = super(NewUser, self).get_context_data(**kwargs)
        return ctx
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)