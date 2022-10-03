from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .mixins import GetAllQuerySetMixin, UserQuerySetMixin
from .permissions import IsAdminGroupPermission
from .models import Game

# Create your views here.
class GameListCreateAPIView(GetAllQuerySetMixin, generics.ListCreateAPIView):
    """
    View all public (+private, if authenticated) games or (if authenticated) Create a new game
    """
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            return qs.filter(public=True)
        return qs

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class GameDetailAPIView(GetAllQuerySetMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    View, Update, or Delete an existing game (only staffed users inside the "admin" group are allowed to perform these actions)
    """
    # lookup_field = "pk"
    permission_classes = [IsAdminUser, IsAdminGroupPermission]

class UserGameListAPIView(GetAllQuerySetMixin, UserQuerySetMixin, generics.ListAPIView):
    """
    View all games created by a user
    """
    permission_classes = [IsAuthenticated]

class GameSearchAPIView(GetAllQuerySetMixin, generics.ListAPIView):
    """
    Search all public (+private, if authenticated) games by querying '/serach/?q={query}'. The query searches all the fields that are assoicated with a game (e.g., title, description, release_date)
    """
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        results = Game.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
