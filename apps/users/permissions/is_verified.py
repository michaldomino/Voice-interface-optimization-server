from rest_framework import permissions


class IsVerified(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_verified') and request.user.is_verified