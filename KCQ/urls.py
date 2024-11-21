from django.contrib import admin
from django.urls import path, include, re_path
from .views import frontend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # API endpoints
    re_path(r'^.*$', frontend, name='frontend'),  # Catch-all for React routes
]
