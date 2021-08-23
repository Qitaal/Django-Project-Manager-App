from django.urls import path
from .views import (
    DashboardView,
    UserListView,
    UserCreateView,
    UserDetailView,
    UserDeleteView,
)

app_name = 'user'

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='user-dashboard'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
