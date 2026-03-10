from db.models import Movie


def get_movies() -> list[Movie]:
    return list(Movie.objects.all())
