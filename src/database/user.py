import hashlib
from .database import execute_query, fetch_query

def create_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    existing_user = get_user_by_username(username)
    if existing_user:
        print(f"User with username '{username}' already exists")
        return
    query = ''' INSERT INTO users(username, password_hash) VALUES(?,?) '''
    execute_query(query, (username, password_hash))



def get_user_by_username(username):
    query = ''' SELECT * FROM users WHERE username = ? '''
    rows = fetch_query(query, (username,))
    return rows[0] if rows else None

def verify_user(username, password):
    user = get_user_by_username(username)
    if user:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        print(f'user: {user}')
        print(f'password_hash: {password_hash}')
        return user[2] == password_hash
    return False