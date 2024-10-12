from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger Schema Ayarları
schema_view = get_schema_view(
    openapi.Info(
        title="Schedule API",
        default_version='v1',
        description="API for managing weekly schedules",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL Deseni
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('schedule_app.urls')),  # Uygulamanın URL'leri
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token Almak
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT Token Yenilemek
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  # Kök URL Swagger'a yönlendiriliyor
]
