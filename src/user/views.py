from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import CustomUserCreationForm


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'user/dashboard.html'


class UserListView(LoginRequiredMixin, generic.ListView):
    template_name = 'user/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'user/user_create.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('user:user-list')
