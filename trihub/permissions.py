from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user


"""
Identifies a specific authenticated user (me), eveyone else is readonly.
"""
class SpecificUserFullAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        specific_user_id = 1
        return request.user.id == specific_user_id