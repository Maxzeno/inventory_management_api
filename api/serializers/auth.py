from rest_framework import serializers

from api.utils.exception import MyAPIException


class MessageSerializer(serializers.Serializer):
    detail = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=False)
    refresh_token = serializers.CharField(required=False)
    
    def validate(self, attrs):
        if not attrs.get('access_token'):
            raise MyAPIException(detail="Access token is required", code=400)
        
        if not attrs.get('refresh_token'):
            raise MyAPIException(detail="Refresh token is required", code=400)
        
        return attrs


class AccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=False)
    
    def validate(self, attrs):
        if not attrs.get('access_token'):
            raise MyAPIException(detail="Access token is required", code=400)

        return attrs

class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=False)
    
    def validate(self, attrs):
        if not attrs.get('refresh_token'):
            raise MyAPIException(detail="Refresh token is required", code=400)
        
        return attrs

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    
    def validate(self, attrs):
        if not attrs.get('email'):
            raise MyAPIException(detail="Email is required", code=400)
        
        if not attrs.get('password'):
            raise MyAPIException(detail="Password is required", code=400)
        
        return attrs
