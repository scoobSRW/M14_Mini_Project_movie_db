﻿# M14_Mini_Project_movie_db

Movie and Genre Management API

This project is a Flask-based GraphQL API for managing movies and genres. The API provides CRUD operations for movies and genres, allowing users to create, read, update, and delete records. It uses SQLAlchemy for database interactions and GraphQL for data querying.

Features

Create, read, update, and delete genres.

Create, read, update, and delete movies.

GraphQL API interface for flexible querying.

Uses Flask-SQLAlchemy and Graphene for ORM and GraphQL integration.

Includes data validation and error handling.

Installation

Clone the repository:

git clone <repository-url>
cd <repository-folder>

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure the database:

Ensure you have MySQL installed and running.

Create a database named movie_db:

CREATE DATABASE movie_db;

Update the password variable in the confidential.py file with your MySQL root password.

Initialize the database:

flask shell
>>> from models import db
>>> db.create_all()
>>> exit()

Start the application:

python app.py

Access the GraphQL interface:
Open your browser and navigate to http://localhost:5000/graphql.

GraphQL Queries and Mutations

Queries

Retrieve all movies:

query {
  movies {
    id
    title
    description
    year
    genre {
      id
      name
    }
  }
}

Retrieve all genres:

query {
  genres {
    id
    name
  }
}

Get movies by genre:

query {
  getMoviesByGenre(genreId: 1) {
    id
    title
    year
  }
}

Get genre by movie:

query {
  getGenreByMovie(movieId: 1) {
    id
    name
  }
}

Mutations

Add a new genre:

mutation {
  createGenre(name: "Comedy") {
    genre {
      id
      name
    }
  }
}

Update an existing genre:

mutation {
  updateGenre(id: 1, name: "Drama") {
    genre {
      id
      name
    }
  }
}

Delete a genre:

mutation {
  deleteGenre(id: 1) {
    success
  }
}

Add a new movie:

mutation {
  createMovie(title: "Inception", description: "A sci-fi thriller", year: 2010, genreId: 1) {
    movie {
      id
      title
    }
  }
}

Update an existing movie:

mutation {
  updateMovie(id: 1, title: "Interstellar", year: 2014) {
    movie {
      id
      title
    }
  }
}

Delete a movie:

mutation {
  deleteMovie(id: 1) {
    success
  }
}

Project Structure

app.py: Main application entry point.

models.py: Database models for Movie and Genre.

schemas.py: GraphQL schema and resolver definitions.

confidential.py: Stores sensitive data like database passwords.

requirements.txt: Lists Python dependencies.

Requirements

Python 3.8+

MySQL

Flask

Flask-SQLAlchemy

Graphene

Flask-GraphQL

PyMySQL

License

This project is licensed under the MIT License. See the LICENSE file for details.

For further questions or issues, feel free to contact the project maintainer.
