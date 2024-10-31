"""
URL configuration for KCQ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Import include to include API URLs
from .views import frontend  # Import the frontend view to serve the React app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend, name='frontend'),  # Serve React app at the root URL
    path('api/', include('api.urls')),  # Include URLs from the 'api' app for API endpoints
]
