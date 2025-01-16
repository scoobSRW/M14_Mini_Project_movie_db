from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Genre(Base):
    __tablename__ = 'genres'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False, unique=True)
    movies: Mapped[list["Movie"]] = relationship('Movie', back_populates='genre')

class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    description: Mapped[str] = mapped_column(db.Text, nullable=True)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    genre_id: Mapped[int] = mapped_column(db.ForeignKey('genres.id'), nullable=False)
    genre: Mapped[Genre] = relationship('Genre', back_populates='movies')
