#!/usr/bin/env python3
"""Module for Hashed Password"""
from bcrypt import checkpw, hashpw, gensalt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User


def _hash_password(password: str) -> bytes:
    """Returns the salted hash of @password, hashed with bcrypt.hashpw
    """
    salt = gensalt()
    h_pw = hashpw(password.encode(), salt)
    return h_pw


def _generate_uuid() -> str:
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

    def create_session(self, email: str) -> str:
        """Creates a session ID and stores it in the DB with
        the corresponding user with the email, @email
        """
        try:
            user_by_email = self._db.find_user_by(email=email)
            user_id = user_by_email.id
            s_id = _generate_uuid()
            self._db.update_user(user_id, session_id=s_id)

            return s_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[None, User]:
        """
        Takes a session_id and returns the corresponding user, if one exists,
        else returns None
        Args:
            session_id (str): session id for user
        Return:
            user object if found, else None

        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user
    """

    def get_user_from_session_id(self, session_id: str) -> Union[User | None]:
        """Returns the 'User' object with the corresponding @session_id"""
        if session_id is None:
            return None
        try:
            user_by_sess_id = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user_by_sess_id
