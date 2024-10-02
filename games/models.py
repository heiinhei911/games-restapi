from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.
User = settings.AUTH_USER_MODEL

class GameQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(genre__icontains=query) | Q(release_date__icontains=query) | Q(developer__icontains=query) | Q(publisher__icontains=query) | Q(rating_for__icontains=query) | Q(price__icontains=query) | Q(public__icontains=query)
        qs = self.filter(lookup)
        if user is None:
            # Get all public data
            qs = qs.is_public()
        else:
            # Get all public + private data that is created by a user
            qs2 = qs.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class GameManager(models.Manager):
    def get_queryset(self):
        return GameQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return Game.get_queryset().search(query, user=user)

class Game(models.Model):
    title = models.CharField(max_length=120)
    genre = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    release_date = models.DateField(blank=True, null=True)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    rating_for = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=19.99)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    public = models.BooleanField(default=True)

    objects = GameManager()

    def __str__(self):
        return self.title