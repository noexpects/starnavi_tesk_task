from rest_framework import permissions


class CanAccessUserAPI(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == "create" and request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user or request.user.is_anonymous:
            return True

        if request.user and request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated and request.user == obj:
            return True

        return False
