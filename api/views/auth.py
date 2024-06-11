from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.response import Response
from api import serializers
from rest_framework.permissions import IsAuthenticated


@extend_schema(tags=['Auth'])
class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return super().post(request, *args, **kwargs)


@extend_schema(tags=['Auth'])
class MyTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=['Auth'], responses=serializers.user.UserSerializer)
class UserView(views.APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = serializers.user.UserSerializer(request.user)
        data = serializer.data
        data['token'] = request.META.get('HTTP_AUTHORIZATION', '').split()[-1]
        return Response(data)


@extend_schema(tags=['Auth'])
class MyTokenBlacklistView(TokenBlacklistView):
    pass