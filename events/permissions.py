#event/permissions.py

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Sadece admin kullanıcılar POST, PUT, DELETE yapabilir.
    Diğer kullanıcılar sadece GET isteği atabilir.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_staff
