from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('', RedirectView.as_view(url='user/dashboard')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('project/', include('project.urls', namespace='project')),
    path('user/', include('user.urls', namespace='user')),
]
