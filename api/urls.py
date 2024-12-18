from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FerryBoatViewSet, TripViewSet, TicketViewSet, AccountViewSet, PassengerViewSet

router = DefaultRouter()
router.register(r'ferry-boats', FerryBoatViewSet)
router.register(r'trips', TripViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'passengers', PassengerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]