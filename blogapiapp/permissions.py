from rest_framework import permissions

#Check User Permission
class BlogUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id

#Check Post Permission
class BlogPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.post_id.id==request.user.id