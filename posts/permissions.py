from rest_framework import permissions

from .exceptions import AlreadyUpvoted, DidNotUpvoted, NeedLogin
from .models import Upvote


class CanAccessPostAPI(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if view.action == "upvote":
            if request.user.is_authenticated:
                if Upvote.objects.filter(author=request.user, post=obj):
                    raise AlreadyUpvoted
                else:
                    return True
            else:
                raise NeedLogin

        if view.action == "retract_upvote":
            if request.user.is_authenticated:
                if not Upvote.objects.filter(author=request.user, post=obj):
                    raise DidNotUpvoted
                else:
                    return True
            else:
                raise NeedLogin

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated and request.user == obj.author:
            return True

        return False
