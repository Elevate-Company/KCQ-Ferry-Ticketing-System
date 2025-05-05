from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.utils import extend_schema

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .serializers import EmployeeLoginSerializer, AdminLoginSerializer
from .models import Account
from api.models import Log

@extend_schema(tags=["Authentication"])
class EmployeeLoginView(APIView):
    serializer_class = EmployeeLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        employee_number = request.data.get('employee_number')
        password = request.data.get('password')
        employee = None
        try:
            employee = Account.objects.get(employee_number=employee_number)
        except ObjectDoesNotExist:
            return Response({
                'error': 'Employee number does not exist'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        # Authenticate the user
        user = authenticate(username=employee.username, password=password)
        if user is not None and employee is not None:
            token, created = Token.objects.get_or_create(user=user)
            
            # Log the login activity
            Log.objects.create(
                user=user,
                action='LOGIN',
                model_name='Account',
                object_id=str(user.id),
                details=f"Employee {user.username} logged in",
                ip_address=self.get_client_ip(request)
            )
            
            return Response({
                'message': 'Login successful',
                'token': token.key,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'employee_number': employee.employee_number,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid password.'
            }, status=status.HTTP_401_UNAUTHORIZED)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

@extend_schema(tags=["Authentication"])
class AdminLoginView(APIView):
    serializer_class = AdminLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response({
                'error': 'Invalid login credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_staff:
            return Response(
                {'error': 'Access denied: Unauthorized login'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            
            # Log the login activity
            Log.objects.create(
                user=user,
                action='LOGIN',
                model_name='Account',
                object_id=str(user.id),
                details=f"Admin {user.username} logged in",
                ip_address=self.get_client_ip(request)
            )

            return Response({
                'message': 'Login successful',
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

# Original ObtainAuthToken view - for backwards compatibility
@extend_schema(tags=["Authentication"])
class ObtainAuthTokenView(ObtainAuthToken):
    pass 