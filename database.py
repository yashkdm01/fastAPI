from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHEMY_DATABSE_URL, connect_args={'check_same_thread':False})

Base= declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()