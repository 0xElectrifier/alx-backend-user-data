#!/usr/bin/env python3
"""Contains password hashing algorithm"""
import bcrypt
from typing import Union


def hash_password(password: str) -> bytes:
    """Hashes a password
    Args:
        password (str): password to be hashed
    """
    pw: bytes = password.encode('utf-8')
    hashed_pw: bytes = bcrypt.hashpw(pw, bcrypt.gensalt())

    return hashed_pw
