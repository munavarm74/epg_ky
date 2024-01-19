# User Authentication and Authorization
import bcrypt
import time
import random

def hash_password(password):
    # Hash a password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def check_password(input_password, stored_hashed_password):
    # Check if the provided password matches the stored hash
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password)

def generate_unique_user_id():
    # Generate a unique channel ID using timestamp and random number
    timestamp_part = int(time.time() * 1000)  # Convert current timestamp to milliseconds
    random_part = random.randint(1000, 9999)  # Generate a random 4-digit number

    # Combine timestamp and random number to create a unique channel ID
    channel_id = f"{timestamp_part}-{random_part}"

    return channel_id
class User:
    def __init__(self, user_id, username, password_hash, role, preferred_timezone):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.role = role
        self.preferred_timezone = preferred_timezone

# User Authentication and Authorization Logic

class UserManager:
    def __init__(self):
        self.users = []  # Assume users are predefined

    def register_user(self, username, password, role, preferred_timezone):
        # In a real system, hash the password and store user data in a database
        user_id = generate_unique_user_id()
        password_hash = hash_password(password)
        user = User(user_id=user_id, username=username, password_hash=password_hash, role=role, preferred_timezone=preferred_timezone)
        self.users.append(user)
        return user

    def login_user(self, username, password):
        # In a real system, validate the username and password against stored user data
        user = self.get_user_by_username(username)
        if user and check_password(password, user.password_hash):
            return user
        else:
            return None

    def get_user_by_username(self, username):
        # In a real system, fetch user data from a database
        for user in self.users:
            if user.username == username:
                return user
        return None

    def authorize_user(self, user, required_role):
        # Check if the user has the required role for authorization
        return user.role == required_role

# Example Usage

user_manager = UserManager()

# Example of user registration
registered_user = user_manager.register_user(username="user123", password="password123", role="user", preferred_timezone="UTC")
print(f"User registered: {registered_user.username}, ID: {registered_user.user_id}")

# Example of user login
logged_in_user = user_manager.login_user(username="user123", password="password123")
if logged_in_user:
    print(f"User logged in: {logged_in_user.username}, ID: {logged_in_user.user_id}, Role: {logged_in_user.role}")
else:
    print("Login failed. Invalid credentials.")

# Example of authorization check
if user_manager.authorize_user(user=logged_in_user, required_role="admin"):
    print("User is authorized as an admin.")
else:
    print("User is not authorized as an admin.")
