from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FerryBoatViewSet, TripViewSet, TicketViewSet, AccountViewSet, PassengerViewSet, LogViewSet

router = DefaultRouter()
router.register(r'ferry-boats', FerryBoatViewSet)
router.register(r'trips', TripViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'passengers', PassengerViewSet)
router.register(r'logs', LogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]