"""game_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .settings import DEBUG
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator

class HttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http"] if DEBUG else ["https"]
        return schema

scheme_view = get_schema_view(
    openapi.Info(
        title="Games API",
        default_version="1.0.0",
        description="API Documentation of the Games API"
    ),
    public=True,
    generator_class=HttpsSchemaGenerator
)

urlpatterns = [
    # index
    path("", scheme_view.with_ui("swagger", cache_timeout=0)), # swagger ui

    # admin panel
    path('admin/', admin.site.urls),

    # api/games
    path("api/games/", include("games.urls")),

    # token/authentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
