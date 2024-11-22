from django.contrib import admin 
from django.urls import path, include

from authentication.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('api/token/', ObtainAuthToken.as_view(), name='api_get_token'),
]
