from rest_framework import permissions
from codebase.models import Codebase


class IsCodebaseOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        print('obj.codebase.owner', obj.codebase.owner)
        print('request.user.id', request.user)
        return obj.codebase.owner == request.user
