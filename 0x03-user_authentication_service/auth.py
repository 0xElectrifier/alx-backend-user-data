#!/usr/bin/env python3
"""Module for Hashed Password"""
from bcrypt import checkpw, hashpw, gensalt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Returns the salted hash of @password, hashed with bcrypt.hashpw
    """
    salt = gensalt()
    h_pw = hashpw(password.encode(), salt)
    return h_pw


def _generate_uuid():
    """Returns a string representation of a new UUID"""
    from uuid import uuid4
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Creates a 'User' instance and saves it to the database"""
        try:
            user_by_email = self._db.find_user_by(email=email)
            if user_by_email:
                raise ValueError("User {} already exists".format(
                    user_by_email.email))
        except NoResultFound:
            h_pwd = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=h_pwd)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Queries the database to check if @email and @password passed
        matches existing data
        """
        if type(email) is not str or type(password) is not str:
            return False
        e_pwd = password.encode()
        try:
            user_by_email = self._db.find_user_by(email=email)
            is_valid = checkpw(e_pwd, user_by_email.hashed_password)
            return is_valid
        except NoResultFound:
            return False
