from fastapi import FastAPI
from time import perf_counter
import logging
from uuid import uuid4

from src.blog1 import blog_models
import uvicorn

# ! Database
from src.utils.db import engine
from src.core.config import settings
from src.core.errors import register_exception_handlers

#? routers
from src.blog1.Routes.authentication import authentication_router
from src.blog1.Routes.blog_routers import blog_router
from src.blog1.Routes.user_routers import user_router

logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
logger = logging.getLogger("app")
app = FastAPI(title=settings.app_name)

if settings.auto_create_tables:
    blog_models.Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def add_request_context(request, call_next):
    request_id = str(uuid4())
    started_at = perf_counter()
    response = await call_next(request)
    duration_ms = (perf_counter() - started_at) * 1000
    response.headers["X-Request-ID"] = request_id
    logger.info(
        "request.completed method=%s path=%s status=%s duration_ms=%.2f request_id=%s",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
        request_id,
    )
    return response


register_exception_handlers(app)

# ? include routers
app.include_router(authentication_router)
app.include_router(blog_router)
app.include_router(user_router)