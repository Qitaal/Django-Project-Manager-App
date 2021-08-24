from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project


class ProjectListView(LoginRequiredMixin, generic.ListView):
    template_name = 'project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()
