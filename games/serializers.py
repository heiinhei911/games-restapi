from rest_framework import serializers

from .models import Game
from .validators import validate_title, unique_game_title

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

class GameSerializer(serializers.ModelSerializer):
    creator = UserSerializer(source="user", read_only=True)
    title = serializers.CharField(validators=[validate_title, unique_game_title])
    url = serializers.HyperlinkedIdentityField(view_name="game-detail"
    # , lookup_field="pk"
    )
    class Meta:
        model = Game
        fields = [
            "creator",
            "title",
            "genre",
            "description",
            "release_date",
            "developer",
            "publisher",
            "rating_for",
            "price",
            "url",
            "public",
        ]

