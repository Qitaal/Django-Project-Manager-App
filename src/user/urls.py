from django.urls import path
from .views import DashboardView

app_name = 'user'

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='user-dashboard'),
]
