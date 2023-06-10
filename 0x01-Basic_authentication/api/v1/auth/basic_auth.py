#!/usr/bin/env python3
"""Module for Basic Auth"""
from api.v1.auth.auth import Auth
import base64
import re


class BasicAuth(Auth):
    """Basic Authentication Class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of @authorization_header for
        a Basic Authentication
        """
        if (authorization_header is None or
                type(authorization_header) is not str):
            return None
        auth_type = re.match("^(Basic )(.*)", authorization_header)
        if auth_type is None:
            return None
        auth_type = auth_type.groups()
        if auth_type[0] != "Basic ":
            return None

        return auth_type[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of @base64_authorization_header string
        """
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None
        try:
            decoded_auth = base64.b64decode(base64_authorization_header)
        except Exception as e:
            return None
        return decoded_auth.decode('utf-8')
