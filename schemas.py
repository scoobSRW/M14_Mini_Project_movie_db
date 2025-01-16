import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Movie as MovieModel, Genre as GenreModel, db
from sqlalchemy.orm import Session

# Object Types
class Genre(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

# Queries
class Query(graphene.ObjectType):
    movies = graphene.List(Movie)
    genres = graphene.List(Genre)
    get_movies_by_genre = graphene.List(Movie, genre_id=graphene.Int(required=True))
    get_genre_by_movie = graphene.Field(Genre, movie_id=graphene.Int(required=True))

    def resolve_movies(self, info):
        return db.session.execute(db.select(MovieModel)).scalars().all()

    def resolve_genres(self, info):
        return db.session.execute(db.select(GenreModel)).scalars().all()

    def resolve_get_movies_by_genre(self, info, genre_id):
        return db.session.execute(
            db.select(MovieModel).where(MovieModel.genre_id == genre_id)
        ).scalars().all()

    def resolve_get_genre_by_movie(self, info, movie_id):
        return db.session.execute(
            db.select(GenreModel).join(MovieModel).where(MovieModel.id == movie_id)
        ).scalars().first()

# Mutations
class AddGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, name):
        if len(name) > 100 or not name.strip():
            raise ValueError("Invalid genre name")
        with Session(db.engine) as session:
            with session.begin():
                genre = GenreModel(name=name)
                session.add(genre)
            session.refresh(genre)
            return AddGenre(genre=genre)

class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, id, name):
        if len(name) > 100 or not name.strip():
            raise ValueError("Invalid genre name")
        with Session(db.engine) as session:
            with session.begin():
                genre = session.execute(
                    db.select(GenreModel).where(GenreModel.id == id)
                ).scalars().first()
                if not genre:
                    raise ValueError("Genre not found")
                genre.name = name
            session.refresh(genre)
            return UpdateGenre(genre=genre)

class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        with Session(db.engine) as session:
            with session.begin():
                genre = session.execute(
                    db.select(GenreModel).where(GenreModel.id == id)
                ).scalars().first()
                if not genre:
                    return DeleteGenre(success=False)
                session.delete(genre)
            return DeleteGenre(success=True)

class AddMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=False)
        year = graphene.Int(required=True)
        genre_id = graphene.Int(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, title, description, year, genre_id):
        with Session(db.engine) as session:
            with session.begin():
                genre = session.execute(
                    db.select(GenreModel).where(GenreModel.id == genre_id)
                ).scalars().first()
                if not genre:
                    raise ValueError("Genre not found")
                movie = MovieModel(
                    title=title, description=description, year=year, genre_id=genre_id
                )
                session.add(movie)
            session.refresh(movie)
            return AddMovie(movie=movie)

class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=False)
        description = graphene.String(required=False)
        year = graphene.Int(required=False)
        genre_id = graphene.Int(required=False)

    movie = graphene.Field(Movie)

    def mutate(self, info, id, title=None, description=None, year=None, genre_id=None):
        with Session(db.engine) as session:
            with session.begin():
                movie = session.execute(
                    db.select(MovieModel).where(MovieModel.id == id)
                ).scalars().first()
                if not movie:
                    raise ValueError("Movie not found")
                if title:
                    movie.title = title
                if description:
                    movie.description = description
                if year:
                    movie.year = year
                if genre_id:
                    movie.genre_id = genre_id
            session.refresh(movie)
            return UpdateMovie(movie=movie)

class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        with Session(db.engine) as session:
            with session.begin():
                movie = session.execute(
                    db.select(MovieModel).where(MovieModel.id == id)
                ).scalars().first()
                if not movie:
                    return DeleteMovie(success=False)
                session.delete(movie)
            return DeleteMovie(success=True)

class Mutation(graphene.ObjectType):
    create_genre = AddGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()
    create_movie = AddMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
