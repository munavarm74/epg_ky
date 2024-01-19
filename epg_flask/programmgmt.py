# Program Information Management

import time
import random
def generate_unique_program_id():
    # Generate a unique channel ID using timestamp and random number
    timestamp_part = int(time.time() * 1000)  # Convert current timestamp to milliseconds
    random_part = random.randint(1000, 9999)  # Generate a random 4-digit number

    # Combine timestamp and random number to create a unique channel ID
    channel_id = f"{timestamp_part}-{random_part}"

    return channel_id

class Program:
    def __init__(self, program_id, title, description, start_time, end_time, genre):
        self.program_id = program_id
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.genre = genre

# Program Information Management Logic

class ProgramManager:
    def __init__(self):
        self.programs = []

    def add_program(self, title, description, start_time, end_time, genre):
        # In a real system, generate a unique program ID and store the program in a database
        program_id = generate_unique_program_id()
        program = Program(program_id=program_id, title=title, description=description, start_time=start_time, end_time=end_time, genre=genre)
        self.programs.append(program)
        return program

    def get_program_by_id(self, program_id):
        # In a real system, fetch program data from a database
        # This is a placeholder method, and you should implement a proper data retrieval mechanism
        for program in self.programs:
            if program.program_id == program_id:
                return program
        return None

    def update_program(self, program_id, title, description, start_time, end_time, genre):
        # In a real system, update program data in a database
        program = self.get_program_by_id(program_id)
        if program:
            program.title = title
            program.description = description
            program.start_time = start_time
            program.end_time = end_time
            program.genre = genre
            return program
        return None

    def delete_program(self, program_id):
        # In a real system, delete program data from a database
        program = self.get_program_by_id(program_id)
        if program:
            self.programs.remove(program)
            return True
        return False

    def get_all_programs_for_channel(self, channel_id):
        # In a real system, fetch all programs for a channel from a database
        # This is a placeholder method, and you should implement a proper data retrieval mechanism
        channel_programs = [program for program in self.programs if program.channel_id == channel_id]
        return channel_programs

# Example Usage

program_manager = ProgramManager()

# Example of adding a program
new_program = program_manager.add_program(title="Program 1", description="Description of Program 1", start_time="2024-01-12 08:00", end_time="2024-01-12 09:00", genre="Drama")
print(f"Program added: {new_program.title}, ID: {new_program.program_id}")

# Example of updating a program
updated_program = program_manager.update_program(program_id=new_program.program_id, title="Updated Program 1", description="Updated Description", start_time="2024-01-12 09:00", end_time="2024-01-12 10:00", genre="Comedy")
if updated_program:
    print(f"Program updated: {updated_program.title}, ID: {updated_program.program_id}")

# Example of deleting a program
deleted_program_id = new_program.program_id
if program_manager.delete_program(program_id=deleted_program_id):
    print(f"Program deleted: ID {deleted_program_id}")
else:
    print(f"Program with ID {deleted_program_id} not found.")

# Example of fetching all programs for a channel
channel_programs = program_manager.get_all_programs_for_channel(channel_id="channel_123")
print(f"All programs for Channel ID channel_123: {channel_programs}")
