# Channel Management
import time
import random
from epg_ky import connection_pool_instance

def generate_unique_channel_id():
    # Generate a unique channel ID using timestamp and random number
    timestamp_part = int(time.time() * 1000)  # Convert current timestamp to milliseconds
    random_part = random.randint(1000, 9999)  # Generate a random 4-digit number

    # Combine timestamp and random number to create a unique channel ID
    channel_id = f"{timestamp_part}-{random_part}"

    return channel_id

class Channel:
    def __init__(self, channel_id, name, description):
        self.channel_id = channel_id
        self.name = name
        self.description = description

# Channel Management Logic



class ChannelManager:
    def __init__(self):
        self.channels = []  # Assume channels are predefined

    def create_channel(self, name, description):
        # In a real system, generate a unique channel ID and store channel data in a database
        channel_id = generate_unique_channel_id()
        channel = Channel(channel_id=channel_id, name=name, description=description)
        self.channels.append(channel)
        return channel

    def update_channel(self, channel_id, new_name, new_description):
        # In a real system, update channel data in a database
        channel = self.get_channel_by_id(channel_id)
        if channel:
            channel.name = new_name
            channel.description = new_description
            return channel
        else:
            return None

    def delete_channel(self, channel_id):
        # In a real system, delete channel data from a database
        channel = self.get_channel_by_id(channel_id)
        if channel:
            self.channels.remove(channel)
            return True
        else:
            return False

    def get_channel_by_id(self, channel_id):
        # In a real system, fetch channel data from a database
        for channel in self.channels:
            if channel.channel_id == channel_id:
                return channel
        return None

    def list_all_channels(self):
        # In a real system, fetch and return all channels from a database
        return self.channels

# Example Usage

channel_manager = ChannelManager()

# Example of creating a channel
new_channel = channel_manager.create_channel(name="Channel 1", description="Description of Channel 1")
print(f"Channel created: {new_channel.name}, ID: {new_channel.channel_id}")

# Example of updating a channel
updated_channel = channel_manager.update_channel(channel_id=new_channel.channel_id, new_name="Updated Channel 1", new_description="Updated Description")
if updated_channel:
    print(f"Channel updated: {updated_channel.name}, ID: {updated_channel.channel_id}")

# Example of deleting a channel
deleted_channel_id = new_channel.channel_id
if channel_manager.delete_channel(channel_id=deleted_channel_id):
    print(f"Channel deleted: ID {deleted_channel_id}")
else:
    print(f"Channel with ID {deleted_channel_id} not found.")

# Example of listing all channels
all_channels = channel_manager.list_all_channels()
print("All Channels:")
for channel in all_channels:
    print(f"{channel.name} - ID: {channel.channel_id}")
