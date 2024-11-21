from django.http import JsonResponse
from django.urls import path
from .views import LoginView  # Your LoginView

def api_root(request):
    return JsonResponse({
        "endpoints": {
            "login": "/api/login/",
            "token_obtain": "/api/token/",
            "token_refresh": "/api/token/refresh/"
        }
    })

urlpatterns = [
    path('', api_root, name='api_root'),  # Default response for /api/
    path('login/', LoginView.as_view(), name='login'),  # Login endpoint
]
