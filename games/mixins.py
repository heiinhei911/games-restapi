from games.serializers import GameSerializer
from .models import Game

class GetAllQuerySetMixin():
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class UserQuerySetMixin():
    user_field = "user"
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)