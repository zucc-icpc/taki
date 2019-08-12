from rest_framework import permissions
from user.models import Profile

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsStaffOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsCoachOrSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        profile = request.user.profile
        if profile.type == "教练" and request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner


class IsNotGuest(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        profile = request.user.profile
        return profile.type != "普通用户"
