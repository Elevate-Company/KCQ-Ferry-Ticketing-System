from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.models import Passenger
from api.serializers import PassengerSerializer

@extend_schema(tags=["Passenger"])
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """Retrieve all passengers with total count."""
        passengers = Passenger.objects.all()
        total_passengers = passengers.count()  # Get total count of passengers

        # Serialize the passengers data
        serializer = PassengerSerializer(passengers, many=True)
        
        # Return the list of passengers and the total count
        return Response({
            'total_passengers': total_passengers,
            'passengers': serializer.data
        }, status=status.HTTP_200_OK)

    # This action will allow updating the boarding status of a passenger
    @action(detail=True, methods=['patch'], url_path='update-boarding-status')
    def update_boarding_status(self, request, pk=None):
        passenger = self.get_object()
        boarding_status = request.data.get('boarding_status')
        
        if boarding_status not in dict(Passenger.BOARDING_STATUS_CHOICES):
            return Response({"detail": "Invalid boarding status."}, status=status.HTTP_400_BAD_REQUEST)
        
        passenger.boarding_status = boarding_status
        passenger.save()

        return Response({"detail": "Boarding status updated successfully."}, status=status.HTTP_200_OK)
