from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.models import Trip, Ticket
from api.serializers import TripSerializer

@extend_schema(tags=["Trip"])
class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'], url_path='booked-seats')
    def booked_seats(self, request, pk=None):
        """
        Get the list of booked seats for a specific trip
        """
        try:
            trip = self.get_object()
            booked_tickets = Ticket.objects.filter(
                trip=trip,
                # Only include tickets that are not cancelled
                boarding_status__in=['BOARDED', 'CHECKED_IN', 'NOT_BOARDED']
            )
            booked_seats = [ticket.seat_number for ticket in booked_tickets if ticket.seat_number]
            
            return Response({
                'trip_id': trip.id,
                'booked_seats': booked_seats,
                'total_booked': len(booked_seats)
            }, status=status.HTTP_200_OK)
        except Trip.DoesNotExist:
            return Response(
                {'error': 'Trip not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': f'Failed to fetch booked seats: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
