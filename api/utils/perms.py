from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException


class MyAPIException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail=detail, code=code)
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code
        self.status_code = code


class MyPerm(BasePermission):
    def check_basic_perm(self, request, view):  
        if not request.user or not request.user.is_authenticated:
            return {'detail': 'user is not authenticated', 'code': 401}
        
        if not hasattr(request.user, "employee") or request.user.employee is None:
            return {'detail': 'user employee profile not set', 'code': 403}
            
        return None

    def has_permission(self, request, view):
        check_basic_perm = self.check_basic_perm(request, view)
        if check_basic_perm is not None:
            raise MyAPIException(**check_basic_perm)
        return True
