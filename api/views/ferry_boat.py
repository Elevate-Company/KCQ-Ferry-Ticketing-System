from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from api.models import FerryBoat
from api.serializers import FerryBoatSerializer

@extend_schema(tags=["FerryBoat"])
class FerryBoatViewSet(viewsets.ModelViewSet):
    queryset = FerryBoat.objects.all()
    serializer_class = FerryBoatSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'


