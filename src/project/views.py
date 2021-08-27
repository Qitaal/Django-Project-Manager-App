from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project, Task


class ProjectListView(LoginRequiredMixin, generic.ListView):
    template_name = 'project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.all()
