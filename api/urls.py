from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers
from .views import auth

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    
    path('token/', auth.MyTokenObtainSlidingView.as_view(), name='token_obtain'),
    path('token/refresh/', auth.MyTokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', auth.MyTokenBlacklistView.as_view(), name='token_blacklist'),
    
    # API docs
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
