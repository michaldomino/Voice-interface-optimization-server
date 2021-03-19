from rest_framework import permissions


class IsVerified(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.verified