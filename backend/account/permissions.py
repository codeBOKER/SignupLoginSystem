from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Admin users have all permissions
        if request.user.is_staff:
            return True
        
        # Object owner has permission
        return obj == request.user