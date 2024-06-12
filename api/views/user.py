from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.response import Response
from api import models, serializers


@extend_schema(tags=['User'], responses=serializers.user.UserSerializer, request=serializers.user.UserUpdateSerializer)
class UserView(views.APIView):    
    def get(self, request):
        serializer = serializers.user.UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = serializers.user.UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if serializer.validated_data.get('first_name'):
            user.first_name = serializer.validated_data.get('first_name')
        
        if serializer.validated_data.get('last_name'):
            user.last_name = serializer.validated_data.get('last_name')
            
        employee_profile = {
            "user": user
        }
        
        if serializer.validated_data.get('position'):
            employee_profile['position'] = serializer.validated_data.get('position')
            
        if serializer.validated_data.get('department'):
            employee_profile['department'] = serializer.validated_data.get('department')
            
        if serializer.validated_data.get('phone_number'):
            employee_profile['phone_number'] = serializer.validated_data.get('phone_number')
            
        if not hasattr(user, 'employee') or not user.employee:
            models.user.EmployeeProfile.objects.create(**employee_profile)
        else:
            for attr, value in employee_profile.items():
                setattr(user.employee, attr, value)

            user.employee.save()
        
        user.save()
        user_serializer = serializers.user.UserSerializer(user)
        return Response(user_serializer.data)
