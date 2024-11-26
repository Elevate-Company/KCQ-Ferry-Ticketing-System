from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FerryBoatViewSet, TripViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'ferry-boats', FerryBoatViewSet)
router.register(r'trips', TripViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]