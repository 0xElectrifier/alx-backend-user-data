#!/usr/bin/env python3
"""Module for Session Authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for user with ID, @user_id"""
        if user_id is None or type(user_id) is not str:
            return None
        session_id = uuid.uuid4()
        user_id_by_session_id[session_id] = user_id
        return session_id
