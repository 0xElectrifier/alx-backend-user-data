#!/usr/bin/env python3
""" Module for Authenticaton
"""
from flask import request
from typing import (List, TypeVar)


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False
        """
        if (path is None or
                excluded_paths is None or
                type(excluded_paths) is list and len(excluded_paths) == 0):
            return True

        slash_ends_path = path[len(path) - 1:] == '/'
        if slash_ends_path:
            slashed_path = path
        else:
            slashed_path = path + '/'

        if slashed_path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None
        """
        return None
