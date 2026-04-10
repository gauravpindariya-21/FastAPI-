# FastAPI Blog Application

A simple blog application built with FastAPI, SQLAlchemy, and SQLite. This application supports user authentication, blog creation, and management.

## Features

- **User Management**: Create users and retrieve user details with their associated blogs.
- **Authentication**: Secure login using OAuth2 with JWT tokens.
- **Blog Management**: CRUD operations (Create, Read, Update, Delete) for blogs.
- **Database**: Uses SQLAlchemy ORM with SQLite for data storage.
- **Security**: Password hashing using Passlib (bcrypt).

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLite](https://www.sqlite.org/)
- [Passlib](https://passlib.readthedocs.io/)
- [Python-jose](https://python-jose.readthedocs.io/)

## Project Structure

```text
.
├── blog11/
│   └── requirements.txt     # Project dependencies
├── src/
│   ├── blog1/               # Core application logic
│   │   ├── Routes/          # API route definitions (blog, user, auth)
│   │   ├── repository/      # Database interaction logic
│   │   ├── blog_models.py   # SQLAlchemy models
│   │   ├── blog_schemas.py  # Pydantic schemas
│   │   ├── token.py         # JWT token handling
│   │   └── ...
│   ├── utils/               # Utility functions (DB connection, hashing)
│   └── main2.py             # Application entry point
├── blog.db                  # SQLite database file
└── README.md                # Project documentation
```

## Getting Started

### 1. Install Dependencies

It is recommended to use a virtual environment. Install the required packages using:

```bash
pip install -r blog11/requirements.txt
```

*Note: You may also need to install `python-jose[cryptography]` for JWT support.*

### 2. Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn src.main2:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### 3. API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Authentication
- `POST /login`: Authenticate a user and receive an access token.

### Users
- `POST /user/`: Register a new user.
- `GET /user/{id}`: Get details of a specific user.

### Blogs
- `GET /blog/`: Get all blogs (requires authentication).
- `POST /blog/`: Create a new blog (requires authentication).
- `GET /blog/{id}`: Get details of a specific blog (requires authentication).
- `PUT /blog/{id}`: Update a blog (requires authentication).
- `DELETE /blog/{id}`: Delete a blog (requires authentication).
