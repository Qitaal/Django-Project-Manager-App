from django.urls import path

from .views import Dashboard

app_name = 'user'

urlpatterns = [
    path('dashboard', Dashboard.as_view(), name='user-dashboard'),
]