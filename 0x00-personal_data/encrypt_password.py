#!/usr/bin/env python3
"""Contains password hashing algorithm"""
import bcrypt
from typing import Union


def hash_password(password: str) -> Union[bytes | None]:
    """Hashes a password"""
    if type(password) is not str:
        return None
    pw: bytes = password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()
    hashed_pw: bytes = bcrypt.hashpw(pw, salt)

    return hashed_pw
