from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Custom permission to only allow access to users with the 'admin' role.
    """

    def has_permission(self, request, view):
        # Check if the user has the 'admin' role
        return request.user.role == 'ADMIN'