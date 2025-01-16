# M14_Mini_Project_movie_db

# Movie and Genre Management API

This project is a Flask-based GraphQL API for managing movies and genres. The API provides CRUD operations for movies and genres, allowing users to create, read, update, and delete records. It uses SQLAlchemy for database interactions and GraphQL for data querying.

## Features

- Create, read, update, and delete genres.
- Create, read, update, and delete movies.
- GraphQL API interface for flexible querying.
- Uses Flask-SQLAlchemy and Graphene for ORM and GraphQL integration.
- Includes data validation and error handling.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Ensure you have MySQL installed and running.
   - Create a database named `movie_db`:
     ```sql
     CREATE DATABASE movie_db;
     ```
   - Update the `password` variable in the `confidential.py` file with your MySQL root password.

5. Initialize the database:
   ```bash
   flask shell
   >>> from models import db
   >>> db.create_all()
   >>> exit()
   ```

6. Start the application:
   ```bash
   python app.py
   ```

7. Access the GraphQL interface:
   Open your browser and navigate to `http://localhost:5000/graphql`.

## GraphQL Queries and Mutations

### Queries

- **Retrieve all movies:**
  ```graphql
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
  ```

- **Retrieve all genres:**
  ```graphql
  query {
    genres {
      id
      name
    }
  }
  ```

- **Get movies by genre:**
  ```graphql
  query {
    getMoviesByGenre(genreId: 1) {
      id
      title
      year
    }
  }
  ```

- **Get genre by movie:**
  ```graphql
  query {
    getGenreByMovie(movieId: 1) {
      id
      name
    }
  }
  ```

### Mutations

- **Add a new genre:**
  ```graphql
  mutation {
    createGenre(name: "Comedy") {
      genre {
        id
        name
      }
    }
  }
  ```

- **Update an existing genre:**
  ```graphql
  mutation {
    updateGenre(id: 1, name: "Drama") {
      genre {
        id
        name
      }
    }
  }
  ```

- **Delete a genre:**
  ```graphql
  mutation {
    deleteGenre(id: 1) {
      success
    }
  }
  ```

- **Add a new movie:**
  ```graphql
  mutation {
    createMovie(title: "Inception", description: "A sci-fi thriller", year: 2010, genreId: 1) {
      movie {
        id
        title
      }
    }
  }
  ```

- **Update an existing movie:**
  ```graphql
  mutation {
    updateMovie(id: 1, title: "Interstellar", year: 2014) {
      movie {
        id
        title
      }
    }
  }
  ```

- **Delete a movie:**
  ```graphql
  mutation {
    deleteMovie(id: 1) {
      success
    }
  }
  ```

## Project Structure

- `app.py`: Main application entry point.
- `models.py`: Database models for Movie and Genre.
- `schemas.py`: GraphQL schema and resolver definitions.
- `confidential.py`: Stores sensitive data like database passwords.
- `requirements.txt`: Lists Python dependencies.

## Requirements

- Python 3.8+
- MySQL
- Flask
- Flask-SQLAlchemy
- Graphene
- Flask-GraphQL
- PyMySQL

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For further questions or issues, feel free to contact the project maintainer.

