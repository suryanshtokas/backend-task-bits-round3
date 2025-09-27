from rest_framework import permissions


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to see if he's logged in
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # always allow read permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # allow write permissions if user is the seller
        return obj.seller == request.user