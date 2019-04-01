from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, profile):
        print(request.user)
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return profile.user == request.user


class CreateOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, profile):
        print(request.user)
        if request.user.is_staff:
            return True
        if request.method in ['POST']:
            return True
        return False