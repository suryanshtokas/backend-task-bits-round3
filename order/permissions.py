from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and request.user.groups.filter(name="Seller").exists()
        )
    

class IsBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and request.user.groups.filter(name="Buyer").exists()
        )