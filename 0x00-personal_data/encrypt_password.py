#!/usr/bin/env python3
"""Contains password hashing algorithm"""
import bcrypt
from typing import Union


def hash_password(password: str) -> Union[bytes | None]:
    """Hashes a password"""
    if type(password) is not str:
        return None
    pw = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(pw, salt)

    return hashed_pw
