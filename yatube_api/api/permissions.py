from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    public_read_actions = ['retrieve', 'list']

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if getattr(view, 'action', None) in self.public_read_actions:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
