# File: application.py (Application Layer)

# A simple in-memory user database for demonstration purposes
users = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"}
}

def auntenticacion(username, password):
    if not username or not password:
        return False

    if username not in users or users[username]["password"] != password:
        return False

    return True
