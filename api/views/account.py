from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema,  OpenApiParameter, OpenApiResponse
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser

from api.serializers import UpdatePasswordSerializer, AccountSerializer
from authentication.models import Account
from api.persmissons import IsAdmin
from api.models import Log

@extend_schema(tags=["Account"])
class AccountViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer

    @extend_schema(
        responses={200: AccountSerializer},
        request=AccountSerializer,
    )
    def list(self, request):
        """Retrieve all account details."""
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
    responses={200: OpenApiResponse(description="Password updated successfully.")},
    request=UpdatePasswordSerializer
    )
    @action(detail=False, methods=['post'], url_path='update-password')
    def update_password(self, request):
        """Update the user's password."""
        # Pass the request to the serializer context
        serializer = UpdatePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            
            # Log the password update
            Log.objects.create(
                user=request.user,
                action='UPDATE',
                model_name='Account',
                object_id=str(user.id),
                details=f"Password updated for {user.username}",
                ip_address=self.get_client_ip(request)
            )
            
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses={200: AccountSerializer},
        request=None  # No request body for this action
    )
    @action(detail=False, methods=['get'], url_path='my-account')
    def get_my_account(self, request):
        """Retrieve account details of the authenticated user."""
        user = request.user  # The authenticated user
        serializer = AccountSerializer(user)  # Serialize the user data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        responses={200: AccountSerializer},
        request=AccountSerializer,
    )
    @action(detail=False, methods=['put', 'patch'], url_path='update-profile')
    def update_profile(self, request):
        """Update account profile information."""
        user = request.user
        serializer = AccountSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            # Log the profile update
            Log.objects.create(
                user=request.user,
                action='UPDATE',
                model_name='Account',
                object_id=str(user.id),
                details=f"Profile updated for {user.username}",
                ip_address=self.get_client_ip(request)
            )
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses={200: AccountSerializer},
    )
    @action(detail=False, methods=['post'], url_path='upload-profile-image', parser_classes=[MultiPartParser, FormParser])
    def upload_profile_image(self, request):
        """Upload a profile image for the authenticated user."""
        user = request.user
        
        if 'profile_image' not in request.FILES:
            return Response({"error": "No profile image provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        user.profile_image = request.FILES['profile_image']
        user.save()
        
        # Log the profile image upload
        Log.objects.create(
            user=request.user,
            action='UPDATE',
            model_name='Account',
            object_id=str(user.id),
            details=f"Profile image uploaded for {user.username}",
            ip_address=self.get_client_ip(request)
        )
        
        serializer = AccountSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    