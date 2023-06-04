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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates @hashed_password with the provided @password"""
    if type(hashed_password) is not bytes or type(password) is not str:
        return False
    dec_pw = password.encode()
    return bcrypt.checkpw(dec_pw, hashed_password)
