from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permissions are for users in Admin(staff) group only
        return request.user.isAdmin()
        