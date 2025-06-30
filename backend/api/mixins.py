from rest_framework import permissions
from .permissions import IsStaffEditorPermission
from rest_framework.permissions import IsAuthenticated


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission,IsAuthenticated]


class UserQueryMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        loopup_data = {}
        loopup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**loopup_data)