from rest_framework import serializers
from api.models import FerryBoat


class FerryBoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FerryBoat
        fields = '__all__'
