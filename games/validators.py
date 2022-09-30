from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Game

def validate_title(value):
    if value.lower() in ("hello", "test", "testing","123"):
        raise serializers.ValidationError(f"{value} is not allowed!")
    return value

unique_game_title = UniqueValidator(Game.objects.all(), "This game already exists in the database!", lookup="iexact")