#user.py
import hashlib
from .database import execute_query, fetch_query

def create_user(username, password):
    """
    Creates a new user in the users table in the database.

    Args:
        username: The username of the new user.
        password: The password of the new user.

    Returns:
        bool: True if the user is created successfully, False if the username already exists.
    """
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    existing_user = get_user_by_username(username)
    if existing_user:
        return False
    query = ''' INSERT INTO users(username, password_hash) VALUES(?,?) '''
    execute_query(query, (username, password_hash))
    return True


def get_user_by_username(username):
    """
    Retrieves a user from the users table in the database by username.

    Args:
        username: The username of the user.

    Returns:
        dict: A dictionary containing user information if the user is found, otherwise None.
    """
    query = ''' SELECT * FROM users WHERE username = ? '''
    rows = fetch_query(query, (username,))
    return rows[0] if rows else None

def verify_user(username, password):
    """
    Verifies if the provided username and password match
    an existing user in the users table in the database.

    Args:
        username: The username of the user.
        password: The password of the user.

    Returns:
        bool: True if the provided username and password match an existing user, otherwise False.
    """
    user = get_user_by_username(username)
    if user:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return user[2] == password_hash # pylint: disable=unsubscriptable-object
    return False
