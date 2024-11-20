# KCQ/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import frontend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend, name='frontend'),
    path('api/', include('api.urls')),  # Include the api app's URLs here
]
