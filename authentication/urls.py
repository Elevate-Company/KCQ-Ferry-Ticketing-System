from django.contrib import admin 
from django.urls import path, include

from .views import ObtainAuthTokenView

urlpatterns = [
    path('get-token/', ObtainAuthTokenView.as_view(), name='api_get_token'),
]
