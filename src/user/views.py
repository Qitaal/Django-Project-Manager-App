from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'user/dashboard.html'


class UserListView(LoginRequiredMixin, generic.ListView):
    template_name = 'user/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
