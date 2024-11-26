from django.contrib import admin 
from django.urls import path, include

from .views import ObtainAuthTokenView, EmployeeLoginView, AdminLoginView

urlpatterns = [
    path('get-token/', ObtainAuthTokenView.as_view(), name='api_get_token'),
    path('login/', EmployeeLoginView.as_view(), name='login'),
    path('admin/login/', AdminLoginView.as_view(), name='login_admin'),
]
