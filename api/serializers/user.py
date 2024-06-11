from rest_framework import serializers
from api import models
        

class EmployeeProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = models.EmployeeProfile
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):    
    employee = EmployeeProfileSerializer(many=False)
    class Meta:
        depth = 2
        model = models.User
        exclude = ('groups', 'user_permissions', 'last_login')
        extra_kwargs = {
            'email': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_active': {'read_only': True},
            'date_joined': {'read_only': True},
            'password': {'write_only': True},
        }
