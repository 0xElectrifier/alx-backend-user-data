#!/usr/bin/env python3
"""Module for Hashed Password"""


def _hash_password(password: str) -> bytes:
    """Returns the salted hash of @password, hashed with bcrypt.hashpw
    """
    from bcrypt import hashpw, gensalt
    salt = gensalt()
    h_pw = hashpw(password.encode(), salt)
    return h_pw
