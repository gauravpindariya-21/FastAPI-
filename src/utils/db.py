from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import settings


#delcareing a path
SQLALCHEMY_DATABASE_URL = settings.database_url

#creating a engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#mapping
Base = declarative_base()

#creating a session
sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()