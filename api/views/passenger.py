from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.models import Passenger, Ticket, Log
from api.serializers import PassengerSerializer, TicketSerializer

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

    def destroy(self, request, pk=None):
        """
        Log delete attempt for passenger instead of actually deleting.
        Only admin can permanently delete passengers.
        """
        try:
            passenger = self.get_object()
            
            # Create log entry for the deletion attempt
            Log.objects.create(
                user=request.user,
                action='DELETE',
                model_name='Passenger',
                object_id=str(passenger.id),
                details=f"Delete attempted for passenger: {passenger.name}",
                ip_address=self.get_client_ip(request)
            )
            
            # Return success message but don't actually delete
            return Response(
                {"detail": "Delete request has been logged. Administrator will review the request."},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"detail": f"Failed to process delete request: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def get_client_ip(self, request):
        """Get client IP address from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    # This action will allow updating the boarding status of a passenger
    @action(detail=True, methods=['patch'], url_path='update-boarding-status')
    def update_boarding_status(self, request, pk=None):
        passenger = self.get_object()
        boarding_status = request.data.get('boarding_status')
        
        if boarding_status not in dict(Passenger.BOARDING_STATUS_CHOICES):
            return Response({"detail": "Invalid boarding status."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Don't allow changing from BOARDED to NOT_BOARDED
        if passenger.boarding_status == 'BOARDED' and boarding_status == 'NOT_BOARDED':
            return Response({"detail": "Cannot change from BOARDED to NOT_BOARDED."}, status=status.HTTP_400_BAD_REQUEST)
            
        passenger.boarding_status = boarding_status
        passenger.save()

        return Response({"detail": "Boarding status updated successfully."}, status=status.HTTP_200_OK)
        
    # This action will allow updating the boarding status of a specific ticket
    @action(detail=True, methods=['patch'], url_path='update-ticket-boarding-status')
    def update_ticket_boarding_status(self, request, pk=None):
        passenger = self.get_object()
        boarding_status = request.data.get('boarding_status')
        ticket_number = request.data.get('ticket_number')
        
        if not ticket_number:
            return Response({"detail": "Ticket number is required."}, status=status.HTTP_400_BAD_REQUEST)
            
        if boarding_status not in dict(Passenger.BOARDING_STATUS_CHOICES):
            return Response({"detail": "Invalid boarding status."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Find the specific ticket
            ticket = Ticket.objects.get(ticket_number=ticket_number, passenger=passenger)
            
            # Check rules for status updates
            # Only allow changing from NOT_BOARDED to CANCELLED, or NOT_BOARDED to BOARDED
            if passenger.boarding_status == 'BOARDED' and boarding_status != 'BOARDED':
                return Response({"detail": "Cannot change status once BOARDED."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Update the passenger's boarding status and save
            passenger.boarding_status = boarding_status
            passenger.save()
            
            return Response({"detail": "Boarding status updated successfully for ticket."}, status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response({"detail": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
            
    # Add an endpoint to get tickets for a passenger
    @action(detail=True, methods=['get'], url_path='tickets')
    def get_tickets(self, request, pk=None):
        """Get all tickets for a specific passenger."""
        passenger = self.get_object()
        tickets = Ticket.objects.filter(passenger=passenger)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
