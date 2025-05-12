from rest_framework import serializers
from api.models import Ticket, Trip, Passenger, Baggage
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .trip import TripSerializer
from decimal import Decimal

class TicketPassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'email', 'phone', 'total_bookings', 'created_at', 'updated_at']

class BaggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ['id', 'weight', 'free_weight_limit', 'excess_weight', 'excess_fee_per_kg', 
                  'total_fee', 'created_at', 'updated_at']
        read_only_fields = ['id', 'excess_weight', 'total_fee', 'created_at', 'updated_at']

class TicketSerializer(serializers.ModelSerializer):
    trip = TripSerializer(read_only=True)
    trip_id = serializers.PrimaryKeyRelatedField(source='trip', queryset=Trip.objects.all(), write_only=True)
    passenger = TicketPassengerSerializer(read_only=True)
    passenger_id = serializers.PrimaryKeyRelatedField(source='passenger', queryset=Passenger.objects.all(), write_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    baggage = BaggageSerializer(read_only=True)
    baggage_weight = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True, required=False)
    
    class Meta:
        model = Ticket
        fields = ['id', 'trip', 'trip_id', 'passenger', 'passenger_id', 'ticket_number', 'seat_number', 
                 'age_group', 'price', 'discount', 'baggage_ticket', 'baggage', 'baggage_weight',
                 'payment_method', 'payment_reference', 'cash_amount', 'created_by', 'issue_date', 
                 'boarding_status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'issue_date', 'created_at', 'updated_at']

    def validate(self, data):
        payment_method = data.get('payment_method')
        payment_reference = data.get('payment_reference')
        cash_amount = data.get('cash_amount')
        
        # Validate payment information
        if payment_method in ['GCASH', 'MAYA'] and not payment_reference:
            raise ValidationError("Reference number is required for online payments")
        
        if payment_method == 'CASH' and not cash_amount:
            raise ValidationError("Cash amount is required for cash payments")
            
        return data

    def create(self, validated_data):
        try:
            request = self.context.get('request')
            if not request or not request.user:
                raise ValidationError("User authentication required")

            # Extract baggage weight if provided
            baggage_weight = validated_data.pop('baggage_weight', None)
            baggage_ticket = validated_data.get('baggage_ticket', False)
            
            # Create baggage if baggage_ticket is True
            baggage = None
            if baggage_ticket and baggage_weight is not None:
                # Ensure baggage_weight is a Decimal with 2 decimal places
                try:
                    # Convert to string first to ensure proper decimal conversion
                    decimal_weight = Decimal(str(baggage_weight)).quantize(Decimal('0.01'))
                    baggage = Baggage.objects.create(
                        weight=decimal_weight
                    )
                except Exception as e:
                    raise ValidationError(f"Invalid baggage weight: {e}")
            
            validated_data['created_by'] = request.user
            ticket = super().create(validated_data)
            
            # Associate baggage with ticket
            if baggage:
                ticket.baggage = baggage
                ticket.save()
                
            return ticket

        except ObjectDoesNotExist as e:
            raise ValidationError(str(e))
        except Exception as e:
            raise ValidationError(f"Failed to create ticket: {str(e)}")
            
    def update(self, instance, validated_data):
        try:
            # Extract baggage weight if provided
            baggage_weight = validated_data.pop('baggage_weight', None)
            baggage_ticket = validated_data.get('baggage_ticket', instance.baggage_ticket)
            
            # Handle baggage update/creation
            if baggage_ticket:
                if baggage_weight is not None:
                    # Ensure baggage_weight is a Decimal with 2 decimal places
                    decimal_weight = Decimal(str(baggage_weight)).quantize(Decimal('0.01'))
                    
                    if instance.baggage:
                        # Update existing baggage
                        instance.baggage.weight = decimal_weight
                        instance.baggage.save()
                    else:
                        # Create new baggage
                        baggage = Baggage.objects.create(
                            weight=decimal_weight
                        )
                        instance.baggage = baggage
            elif not baggage_ticket and instance.baggage:
                # Remove baggage if baggage_ticket is now False
                baggage = instance.baggage
                instance.baggage = None
                baggage.delete()
                
            # Update other ticket fields
            return super().update(instance, validated_data)
            
        except Exception as e:
            raise ValidationError(f"Failed to update ticket: {str(e)}")