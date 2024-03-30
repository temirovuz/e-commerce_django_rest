from rest_framework import permissions


class OrderPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_seller:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if obj.seller != request.user:
            return True
        if obj.user.is_seller:
            return False
        return True


class OrderItemAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.customer:
            return True
        return False
