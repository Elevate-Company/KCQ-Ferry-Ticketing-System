from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import FerryBoat, Trip

class FerryBoatNameSerializer(serializers.ModelSerializer):
    slug = serializers.CharField()

    class Meta:
        model = FerryBoat
        fields = ['slug']

class TripSerializer(serializers.ModelSerializer):
    ferry_boat = FerryBoatNameSerializer()
    created_by = serializers.StringRelatedField(read_only=True)  # Assuming this is set by the authenticated user
    
    class Meta:
        model = Trip
        fields = '__all__'

    def create(self, validated_data):
        ferry_boat_data = validated_data.pop('ferry_boat')
        # Check if the ferry boat exists

        if not ferry_boat_data:
            raise ValidationError({'ferry_boat': 'Need specify the ferry boat of this trip.'})

        try:
            ferry_boat = FerryBoat.objects.get(slug=ferry_boat_data['slug'])
        except FerryBoat.DoesNotExist:
            raise ValidationError({'ferry_boat': 'Ferry boat with this name does not exist.'})
        
        created_by = self.context['request'].user
        trip = Trip.objects.create(ferry_boat=ferry_boat, created_by=created_by, **validated_data)

        return trip
    
    def update(self, instance, validated_data):
        ferry_boat_data = validated_data.pop('ferry_boat', None)

        if not ferry_boat_data:
            raise ValidationError({'ferry_boat': 'Need specify the ferry boat of this trip.'})
        
        try:
            ferry_boat = FerryBoat.objects.get(slug=ferry_boat_data['slug'])
            instance.ferry_boat = ferry_boat
        except FerryBoat.DoesNotExist:
            raise ValidationError({'ferry_boat': 'Ferry boat with this slug does not exist.'})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance