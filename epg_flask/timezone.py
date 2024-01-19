# Timezone Support
import time, random


def generate_unique_user_id():
    # Generate a unique channel ID using timestamp and random number
    timestamp_part = int(time.time() * 1000)  # Convert current timestamp to milliseconds
    random_part = random.randint(1000, 9999)  # Generate a random 4-digit number

    # Combine timestamp and random number to create a unique channel ID
    channel_id = f"{timestamp_part}-{random_part}"

    return channel_id

class User:
    def __init__(self, user_id, username, preferred_timezone):
        self.user_id = user_id
        self.username = username
        self.preferred_timezone = preferred_timezone

# Timezone Support Logic

class TimezoneManager:
    def __init__(self):
        self.supported_timezones = ["UTC", "America/New_York", "Europe/London", "Asia/Tokyo"]  # Add more timezones as needed

    def get_supported_timezones(self):
        return self.supported_timezones

# User Profile Management

class UserProfileManager:
    def __init__(self):
        self.users = []

    def create_user(self, username, preferred_timezone):
        # In a real system, validate the timezone and store user data in a database
        if preferred_timezone in TimezoneManager().get_supported_timezones():
            user_id = generate_unique_user_id()
            user = User(user_id=user_id, username=username, preferred_timezone=preferred_timezone)
            self.users.append(user)
            return user
        else:
            return None

    def update_user_timezone(self, user_id, new_preferred_timezone):
        # In a real system, update user data in a database
        user = self.get_user_by_id(user_id)
        if user and new_preferred_timezone in TimezoneManager().get_supported_timezones():
            user.preferred_timezone = new_preferred_timezone
            return user
        else:
            return None

    def get_user_by_id(self, user_id):
        # In a real system, fetch user data from a database
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

# Example Usage

timezone_manager = TimezoneManager()
user_profile_manager = UserProfileManager()

# Example of creating a user with a preferred timezone
new_user = user_profile_manager.create_user(username="user123", preferred_timezone="America/New_York")
if new_user:
    print(f"User created: {new_user.username}, ID: {new_user.user_id}, Preferred Timezone: {new_user.preferred_timezone}")

# Example of updating user timezone
updated_user = user_profile_manager.update_user_timezone(user_id=new_user.user_id, new_preferred_timezone="Europe/London")
if updated_user:
    print(f"User updated: {updated_user.username}, ID: {updated_user.user_id}, Preferred Timezone: {updated_user.preferred_timezone}")
