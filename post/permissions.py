from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        if object.author == request.user:
            return True
        
