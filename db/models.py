from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    genres = models.ManyToManyField(Genre, related_name="actors")


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")


class MovieSession(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_sessions"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders"
    )
    movie_session = models.ForeignKey(
        MovieSession, on_delete=models.CASCADE, related_name="orders"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Ticket(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="tickets"
    )
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    
