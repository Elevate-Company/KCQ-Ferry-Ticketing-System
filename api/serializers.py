from rest_framework import serializers
from .models import FerryBoat, Trip, Passenger, Ticket

class FerryBoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FerryBoat
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    ferry_boat = FerryBoatSerializer()
    created_by = serializers.StringRelatedField()
    
    class Meta:
        model = Trip
        fields = '__all__'
        
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
