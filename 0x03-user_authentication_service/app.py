#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def get_root():
    """Returns a simple json message"""
    return jsonify({"message": "Bienvenue"}), 200

@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Endpoint to register a new user"""
    from auth import Auth
    AUTH = Auth()
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        new_user = AUTH.register_user(email, pwd)
        return jsonify({"email": new_user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
