from rest_framework.permissions import BasePermission


class IsTutor(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT", "DELETE"] and request.user.role != "tutor":
            return False
        return True