from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (obj.user == request.user) or bool(request.user and request.user.is_staff)



class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user
    

class PermissionByMethodMixin:
    permissions_map = {}

    def get_permissions(self):
        permission_classes = self.permissions_map.get(
            self.request.method, [IsAdminOrReadOnly]
        )
        return [permission() for permission in permission_classes]