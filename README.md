# FastAPI Blog Application

A blog API built with FastAPI, SQLAlchemy, and SQLite with JWT auth, refresh tokens, validation, ownership authorization, migrations, tests, Docker support, and CI.

## Key Improvements

- Environment-based config for DB and JWT settings
- Access + refresh token authentication flow
- User schema split (input/output) to avoid password leakage
- Field validation for user and blog payloads
- Ownership checks for blog update/delete
- Standardized API error payloads
- Service layer added between routes and repositories
- Alembic migrations for schema management
- Pytest test suite and GitHub Actions CI
- Dockerfile and docker-compose for local container runs

## Setup

### 1. Install dependencies

```bash
pip install -r blog11/requirements.txt
```

### 2. Configure environment variables

```bash
export APP_NAME="FastAPI Blog Application"
export DATABASE_URL="sqlite:///./blog.db"
export JWT_SECRET_KEY="replace-with-a-strong-secret"
export JWT_ALGORITHM="HS256"
export ACCESS_TOKEN_EXPIRE_MINUTES="30"
export REFRESH_TOKEN_EXPIRE_MINUTES="10080"
export AUTO_CREATE_TABLES="false"
```

### 3. Run migrations

```bash
alembic upgrade head
```

### 4. Run app

```bash
uvicorn src.main2:app --reload
```

## API Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

### Authentication
- `POST /login` → returns `access_token` + `refresh_token`
- `POST /refresh` → returns refreshed access token

### Users
- `POST /user/` → create user (password never returned)
- `GET /user/{id}` → fetch user and blog previews

### Blogs (auth required)
- `GET /blog/`
- `POST /blog/`
- `GET /blog/{id}`
- `PUT /blog/{id}` (owner only)
- `DELETE /blog/{id}` (owner only)

## Tests

```bash
pytest -q
python -m compileall src
```

## Docker

```bash
docker compose up --build
```
