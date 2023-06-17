#!/usr/bin/env python3
"""User model"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """An SQLAlchemy Database schema named 'users'"""

    __tablename__ = "users"
    id = Column("id", primary_key=True)
    email = Column("email", nullable=False)
    hashed_password = Column("hashed_password", nullable=False)
    session_id = Column("session_id")
    reset_token = Column("reset_token")
