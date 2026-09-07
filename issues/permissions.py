from rest_framework.permissions import BasePermission

class IssuePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Everyone can see and create issues
        if view.action in ["list","retrieve","create"]:
            return True

        # Only ADMIN and DEVELOPERS can use put and patch method in issues
        if view.action in ["update","partial_update"]:
            return request.user.role in ["ADMIN","DEVELOPER"]

        # Only ADMIN can delete issues
        if view.action == "destroy":
            return request.user.role == "ADMIN"

        return False