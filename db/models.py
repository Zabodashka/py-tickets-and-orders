from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Genre(models.Model):
    name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    name: str = models.CharField(max_length=255)
    age: int = models.PositiveIntegerField(default=0)
    genres: models.ManyToManyField = models.ManyToManyField(
        Genre, related_name="actors"
    )

    def __str__(self) -> str:
        return self.name
