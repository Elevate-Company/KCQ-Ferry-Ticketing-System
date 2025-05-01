from rest_framework import serializers
from api.models import Ticket, Trip, Passenger
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .trip import TripSerializer

class TicketPassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'email', 'phone', 'total_bookings', 'boarding_status', 'created_at', 'updated_at', 'is_delete']

class TicketSerializer(serializers.ModelSerializer):
    trip = TripSerializer(read_only=True)
    trip_id = serializers.PrimaryKeyRelatedField(source='trip', queryset=Trip.objects.all(), write_only=True)
    passenger = TicketPassengerSerializer(read_only=True)
    passenger_id = serializers.PrimaryKeyRelatedField(source='passenger', queryset=Passenger.objects.all(), write_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Ticket
        fields = ['id', 'trip', 'trip_id', 'passenger', 'passenger_id', 'ticket_number', 'seat_number', 
                 'age_group', 'price', 'discount', 'baggage_ticket', 
                 'created_by', 'issue_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'issue_date', 'created_at', 'updated_at']

    def create(self, validated_data):
        try:
            request = self.context.get('request')
            if not request or not request.user:
                raise ValidationError("User authentication required")

            validated_data['created_by'] = request.user
            return super().create(validated_data)

        except ObjectDoesNotExist as e:
            raise ValidationError(str(e))
        except Exception as e:
            raise ValidationError(f"Failed to create ticket: {str(e)}")