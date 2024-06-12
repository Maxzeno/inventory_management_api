from rest_framework.permissions import BasePermission
from api.utils.exception import MyAPIException


class MyPerm(BasePermission):
    def check_basic_perm(self, request, view):  
        if not request.user or not request.user.is_authenticated:
            return {'detail': 'user is not authenticated', 'code': 401}
        
        return None

    def has_permission(self, request, view):
        check_basic_perm = self.check_basic_perm(request, view)
        if check_basic_perm is not None:
            raise MyAPIException(**check_basic_perm)
        return True
