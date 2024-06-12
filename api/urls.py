from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register('suppliers', views.inventory.SupplierViewSet, basename='suppliers')
router.register('items', views.inventory.ItemViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls)),
    # auth
    path('token/', views.auth.MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', views.auth.MyTokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', views.auth.MyTokenBlacklistView.as_view(), name='token_blacklist'),
    # user
    path('user/', views.user.UserView.as_view(), name='user'),
    # API docs
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
