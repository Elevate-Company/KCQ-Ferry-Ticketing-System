
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.utils import extend_schema

# Create your tests here.
@extend_schema(tags=["Authentication"])
class ObtainAuthTokenView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny] 