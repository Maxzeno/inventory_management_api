from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from rest_framework_simplejwt.views import TokenBlacklistView
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Auth'])
class MyTokenObtainSlidingView(TokenObtainSlidingView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return super().post(request, *args, **kwargs)


@extend_schema(tags=['Auth'])
class MyTokenRefreshSlidingView(TokenRefreshSlidingView):
    pass


@extend_schema(tags=['Auth'])
class MyTokenBlacklistView(TokenBlacklistView):
    pass