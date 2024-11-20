# api/urls.py
from django.urls import path
from .views import ItemListCreateAPIView  # Correct view import

urlpatterns = [
    path('items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
]
