# Schedule Management
from programmgmt import ProgramManager


class Schedule:
    def __init__(self, channel_id, programs):
        self.channel_id = channel_id
        self.programs = programs

# Schedule Management Logic

class ScheduleManager:
    def __init__(self):
        self.schedules = []

    def create_schedule(self, channel_id, programs):
        # In a real system, validate the schedule and store it in a database
        if self.validate_schedule(programs):
            schedule = Schedule(channel_id=channel_id, programs=programs)
            self.schedules.append(schedule)
            return schedule
        else:
            return None

    def update_schedule(self, channel_id, new_programs):
        # In a real system, update the schedule in a database
        existing_schedule = self.get_schedule_by_channel_id(channel_id)
        if existing_schedule and self.validate_schedule(new_programs):
            existing_schedule.programs = new_programs
            return existing_schedule
        else:
            return None

    def delete_schedule(self, channel_id):
        # In a real system, delete the schedule from a database
        schedule = self.get_schedule_by_channel_id(channel_id)
        if schedule:
            self.schedules.remove(schedule)
            return True
        return False

    def get_schedule_by_channel_id(self, channel_id):
        # In a real system, fetch the schedule data from a database
        for schedule in self.schedules:
            if schedule.channel_id == channel_id:
                return schedule
        return None

    def view_schedule(self, channel_id):
        # In a real system, fetch and display the schedule for a channel
        schedule = self.get_schedule_by_channel_id(channel_id)
        if schedule:
            print(f"Schedule for Channel ID {channel_id}:")
            for program in schedule.programs:
                print(f"{program.title} - Start Time: {program.start_time} - End Time: {program.end_time}")
        else:
            print(f"Schedule for Channel ID {channel_id} not found.")

    def validate_schedule(self, programs):
        # In a real system, perform validation checks on the schedule
        # This is a placeholder method, and you should implement proper validation logic
        return not self.has_overlapping_programs(programs)

    def has_overlapping_programs(self, programs):
        # Check if there are overlapping programs in the schedule
        sorted_programs = sorted(programs, key=lambda x: x.start_time)
        for i in range(len(sorted_programs) - 1):
            if sorted_programs[i + 1].start_time < sorted_programs[i].end_time:
                return True
        return False

# Example Usage

schedule_manager = ScheduleManager()
program_manager = ProgramManager()

# Example of adding a program
program1 = program_manager.add_program(title="Program 1", description="Description of Program 1", start_time="2024-01-12 08:00", end_time="2024-01-12 09:00", genre="Drama")
program2 = program_manager.add_program(title="Program 2", description="Description of Program 2", start_time="2024-01-12 08:00", end_time="2024-01-12 09:00", genre="Drama")
program3 = program_manager.add_program(title="Program 3", description="Description of Program 3", start_time="2024-01-12 08:00", end_time="2024-01-12 09:00", genre="Drama")
program4 = program_manager.add_program(title="Program 4", description="Description of Program 1", start_time="2024-01-12 08:00", end_time="2024-01-12 09:00", genre="Drama")
program5 = program_manager.add_program(title="Program 5", description="Description of Program 1", start_time="2024-01-12 08:00", end_time="2024-01-12 09:00", genre="Drama")



# Example of creating a schedule
programs_for_schedule = [program1, program2, program3]  # Assume programs are predefined
created_schedule = schedule_manager.create_schedule(channel_id="channel_123", programs=programs_for_schedule)
if created_schedule:
    print(f"Schedule created for Channel ID {created_schedule.channel_id}")

# Example of updating a schedule
new_programs_for_schedule = [program4, program5]  # Assume new programs are predefined
updated_schedule = schedule_manager.update_schedule(channel_id="channel_123", new_programs=new_programs_for_schedule)
if updated_schedule:
    print(f"Schedule updated for Channel ID {updated_schedule.channel_id}")

# Example of deleting a schedule
deleted_channel_id = "channel_123"
