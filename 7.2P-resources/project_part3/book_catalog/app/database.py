from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://book_catalog_t2ro_user:TVRn302kn5EBTwzA5swVLKsVi4iVrOQr@dpg-crkskd8gph6c73dka360-a.oregon-postgres.render.com/book_catalog_t2ro" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
