from django.urls import path
from . import views

urlpatterns = [
    path("", views.GameListCreateAPIView.as_view()),
    path("search/", views.GameSearchAPIView.as_view()),
    path("my/", views.UserGameListAPIView.as_view()),
    path("<int:pk>/", views.GameDetailAPIView.as_view(), name="game-detail"),
]