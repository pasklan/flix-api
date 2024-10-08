from rest_framework import permissions


class ReviewPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # Lógica da permissão
        return True
