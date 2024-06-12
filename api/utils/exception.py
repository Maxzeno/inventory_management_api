from rest_framework.exceptions import APIException


class MyAPIException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail=detail, code=code)
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code
        self.status_code = code