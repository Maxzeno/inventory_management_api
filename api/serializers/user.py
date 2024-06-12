from rest_framework import serializers
from api import models 
        

class EmployeeProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = models.user.EmployeeProfile
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):    
    employee = EmployeeProfileSerializer(many=False)
    class Meta:
        depth = 2
        model = models.user.User
        exclude = ('groups', 'user_permissions', 'last_login', 'is_superuser', 'is_staff')
        extra_kwargs = {
            'email': {'read_only': True},
            'is_active': {'read_only': True},
            'date_joined': {'read_only': True},
            'password': {'write_only': True},
        }


class UserUpdateSerializer(serializers.Serializer):    
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    position = serializers.CharField(required=False)
    department = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)

    def validate(self, attrs):
        return attrs
