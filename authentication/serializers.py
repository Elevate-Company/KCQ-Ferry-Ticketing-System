from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from authentication.models import Account
from api.models import FerryBoat


class AdminLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'token')

class EmployeeLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    employee_number = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Account
        fields = ('employee_number', 'password')