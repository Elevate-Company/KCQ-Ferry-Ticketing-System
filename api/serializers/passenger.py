from rest_framework import serializers
from api.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'email', 'phone', 'total_bookings', 'boarding_status', 'created_at', 'updated_at']