from rest_framework import serializers
from api.models import FerryBoat, Passenger, Ticket
from .trip import TripSerializer

from rest_framework import serializers

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    trip = TripSerializer()
    passenger = PassengerSerializer()
    created_by = serializers.StringRelatedField()
    
    class Meta:
        model = Ticket
        fields = '__all__'