from db.models import Movie, Actor


def create_movie(title: str, description: str, actors_ids: list[int]) -> Movie:
    movie = Movie.objects.create(title=title, description=description)
    movie.actors.set(actors_ids)
    return movie


def get_movies(title: str = None) -> list[Movie]:
    qs = Movie.objects.all()
    if title:
        qs = qs.filter(title__icontains=title)
    return list(qs)
