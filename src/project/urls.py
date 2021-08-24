from django.urls import path
from .views import (
    ProjectListView,
)

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
]
