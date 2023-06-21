#!/usr/bin/env python3
"""Basic Flask app"""
from flask import abort, Flask, jsonify, redirect, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def get_root():
    """Returns a simple json message"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Endpoint to register a new user"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        new_user = AUTH.register_user(email, pwd)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": new_user.email,
                    "message": "user created"}), 200


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Log in function"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    is_valid_cred = AUTH.valid_login(email, pwd)
    if is_valid_cred is False:
        abort(401)
    else:
        sess_id = AUTH.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", sess_id)

    return resp


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """Log out function"""
    from sqlalchemy.orm.exc import NoResultFound

    sess_id = request.cookies.get("session_id")
    try:
        if sess_id:
            AUTH.destroy_session(sess_id)
            redirect("/")
    except NoResultFound:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
