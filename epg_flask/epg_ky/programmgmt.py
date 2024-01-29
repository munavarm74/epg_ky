# Program Information Management

import time
import random
from epg_ky import connection_pool_instance

def generate_unique_program_id():
    # Generate a unique channel ID using timestamp and random number
    timestamp_part = int(time.time() * 1000)  # Convert current timestamp to milliseconds
    random_part = random.randint(1000, 9999)  # Generate a random 4-digit number

    # Combine timestamp and random number to create a unique channel ID
    channel_id = f"{timestamp_part}-{random_part}"

    return channel_id


class Program:
    def __init__(self, program_id, channel_id, name, description, duration, genre):
        self.program_id = program_id
        self.channel_id = channel_id
        self.name = name
        self.description = description
        self.duration = duration
        self.genre = genre

    def to_dict(self):
        return {
            'program_id': self.program_id,
            'channel_id': self.channel_id,
            'name': self.name,
            'description': self.description,
            'duration': self.duration,
            'genre': self.genre
        }


# Program Information Management Logic

class ProgramManager:
    def __init__(self, connection):
        self.programs = []
        self.connection = connection_pool_instance.pool.connection()


    # Add a new program to the list of programs
    # Store data in database if the data is not yet avialble.
    # Return the newly added program.

    def add_program(self, channel_id, name, description, duration, genre):
        print( " Into Add Program")
        program_id = generate_unique_program_id()
        # program = Program(
        #     program_id=program_id,
        #     channel_id=channel_id,
        #     name=name,
        #     description=description,
        #     duration=duration,
        #     genre=genre
        # )
        # Store program data in a database if needed
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO programs ( channel_id, title, description, duration, genre) VALUES ( %s, %s, %s, %s, %s)",
                       (channel_id, name, description, duration, genre))
        self.connection.commit()
        self.connection.close()
        # self.programs.append(program)
        return 'success'

    def get_program_by_id(self, program_id):
        # Use a SQL SELECT statement to fetch program data from the database
        query = "SELECT * FROM programs WHERE program_id = %s"

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (program_id,))
            program_data = cursor.fetchone()

            if program_data:
                # Assuming program_data is a tuple or dictionary representing the program
                return program_data
            else:
                return None
        finally:
            cursor.close()

    def update_program(self, program_id, name, description, duration, genre, channel_id):
        # Use a SQL UPDATE statement to update program data in the database
        query = "UPDATE programs SET title = %s, description = %s, duration = %s, genre = %s, channel_id=%s WHERE program_id = %s"
        print( " Query : ", query )
        print( " Program ID : ", program_id )
        print("chan", channel_id)
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (name, description, duration, genre,  channel_id,program_id))
            self.connection.commit()  # Commit the changes to the database

            # Check if any rows were affected (updated)
            if cursor.rowcount > 0:
                return True
            else:
                return False
        finally:
            cursor.close()


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
