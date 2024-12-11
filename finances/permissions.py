from rest_framework import permissions


class IsBoss(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='bosses').exists()