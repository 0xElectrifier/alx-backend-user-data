#!/usr/bin/env python3
"""Module for Hashed Password"""
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Returns the salted hash of @password, hashed with bcrypt.hashpw
    """
    from bcrypt import hashpw, gensalt
    salt = gensalt()
    h_pw = hashpw(password.encode(), salt)
    return h_pw


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Creates a 'User' instance and saves it to the database"""
        from sqlalchemy.orm.exc import NoResultFound
        try:
            user_by_email = self._db.find_user_by(email=email)
            if user_by_email:
                raise ValueError("User {} already exists".format(
                    user_by_email.email))
        except NoResultFound:
            h_pwd = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=h_pwd)
            return new_user
