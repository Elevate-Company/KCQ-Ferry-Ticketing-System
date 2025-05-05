from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from api.models import Ticket, Trip, Passenger, Log
from api.serializers import TicketSerializer

@extend_schema(tags=["Ticket"])
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'ticket_number'

    def create(self, request, *args, **kwargs):
        try:
            # Check for both trip and trip_id in request data
            trip_id = request.data.get('trip_id') or request.data.get('trip')
            passenger_id = request.data.get('passenger_id') or request.data.get('passenger')
            
            if not trip_id:
                return Response(
                    {'error': 'trip_id field is required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not passenger_id:
                return Response(
                    {'error': 'passenger_id field is required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Convert to integers if they're strings
            trip_id = int(trip_id)
            passenger_id = int(passenger_id)

            # Verify the trip and passenger exist
            try:
                trip = Trip.objects.get(id=trip_id)
                passenger = Passenger.objects.get(id=passenger_id)
            except Trip.DoesNotExist:
                return Response(
                    {'error': f'Trip with id {trip_id} does not exist'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            except Passenger.DoesNotExist:
                return Response(
                    {'error': f'Passenger with id {passenger_id} does not exist'}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            # Create serializer with request context
            data = request.data.copy()
            if 'trip_id' in data and 'trip' not in data:
                data['trip'] = data['trip_id']
            if 'passenger_id' in data and 'passenger' not in data:
                data['passenger'] = data['passenger_id']

            serializer = self.get_serializer(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            
            # Add the authenticated user as creator
            ticket = serializer.save(created_by=request.user)
            
            # Log the ticket creation
            Log.objects.create(
                user=request.user,
                action='CREATE',
                model_name='Ticket',
                object_id=str(ticket.id),
                details=f"Ticket {ticket.ticket_number} created for {passenger.name}, trip {trip.origin} to {trip.destination}",
                ip_address=self.get_client_ip(request)
            )
            
            # Return the created ticket data
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            
        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except DjangoValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': f'An unexpected error occurred: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip