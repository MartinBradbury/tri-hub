from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user


class IsAuthOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access for unauthenticated users
        if not request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        # For other cases, ensure the user is authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow access if the request is a safe method (read-only operations)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check if the user is the owner of the object
        return obj.owner == request.user