from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.response import Response
from api import serializers
from api import models
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


@extend_schema(tags=['Auth'], responses=serializers.auth.TokenSerializer, request=serializers.auth.LoginSerializer, auth=None)
class MyTokenObtainPairView(views.APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.auth.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(models.user.User, email=serializer.validated_data.get('email'))

        if not user.check_password(serializer.validated_data.get('password')):
            return Response({'detail': 'Invalid credentials'}, status=400)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh)
        }, status=200)


@extend_schema(tags=['Auth'], responses=serializers.auth.AccessTokenSerializer, request=serializers.auth.RefreshTokenSerializer, auth=None)
class MyTokenRefreshView(views.APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.auth.RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        refresh_token = serializer.validated_data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'access_token': access_token}, status=status.HTTP_200_OK)


@extend_schema(tags=['Auth'], responses=serializers.auth.MessageSerializer, request=serializers.auth.RefreshTokenSerializer, auth=None)
class MyTokenBlacklistView(views.APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.auth.RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        refresh_token = serializer.validated_data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Token blacklisted successfully'}, status=status.HTTP_200_OK)
    