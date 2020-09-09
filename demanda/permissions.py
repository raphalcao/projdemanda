from rest_framework import permissions
from .models import User


class ValidaSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            if request.user.is_superuser:
                return User.is_admin
