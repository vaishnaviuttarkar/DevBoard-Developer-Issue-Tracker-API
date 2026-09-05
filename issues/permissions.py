from rest_framework.permissions import BasePermission

class IsAdminOrDeveoper(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticaed
            and request.user.role in ["ADMIN", "DEVELOPER"]
        )