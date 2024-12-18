from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action

from api.serializers import UpdatePasswordSerializer, AccountSerializer
from authentication.models import Account
from api.persmissons import IsAdmin

@extend_schema(tags=["Account"])
class AccountViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AccountSerializer

    def list(self, request):
        """Retrieve all account details."""
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='update-password')
    def update_password(self, request):
        """Update the user's password."""
        serializer = UpdatePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_path='my-account')
    def get_my_account(self, request):
        """Retrieve account details of the authenticated user."""
        user = request.user  # The authenticated user
        serializer = AccountSerializer(user)  # Serialize the user data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    