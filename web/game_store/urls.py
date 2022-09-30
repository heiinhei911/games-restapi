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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

scheme_view = get_schema_view(
    openapi.Info(
        title="Games API",
        default_version="1.0.0",
        description="API Documentation of the Games API"
    ),
    public=True,
)

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    # api
    path("api/", include([
        path("games/", include("games.urls")), # games
        path("docs/", scheme_view.with_ui("swagger", cache_timeout=0)) # swagger ui
    ])),

    # token/authentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
