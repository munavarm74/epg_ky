





# ===========================================

# Search and Filter

class Program:
    def __init__(self, title, description, start_time, genre):
        self.title = title
        self.description = description
        self.start_time = start_time
        self.genre = genre

# Search and Filter Logic

class ProgramManager:
    def __init__(self):
        self.programs = []  # Assume programs are predefined

    def search_programs(self, query):
        # In a real system, search programs in a database
        # This is a placeholder method, and you should implement a proper search mechanism
        return [program for program in self.programs if query.lower() in program.title.lower() or query.lower() in program.description.lower()]

    def filter_programs_by_genre(self, genres):
        # In a real system, filter programs in a database based on genres
        # This is a placeholder method, and you should implement a proper filtering mechanism
        return [program for program in self.programs if program.genre in genres]

    def filter_programs_by_date_range(self, start_date, end_date):
        # In a real system, filter programs in a database based on date range
        # This is a placeholder method, and you should implement a proper filtering mechanism
        return [program for program in self.programs if start_date <= program.start_time <= end_date]

# Example Usage

program_manager = ProgramManager()

# Example of searching programs
search_query = "Drama"
search_results = program_manager.search_programs(query=search_query)
print(f"Search results for '{search_query}': {search_results}")

# Example of filtering programs by genre
selected_genres = ["Action", "Adventure"]
filtered_by_genre = program_manager.filter_programs_by_genre(genres=selected_genres)
print(f"Programs filtered by genre: {filtered_by_genre}")

# Example of filtering programs by date range
start_date = "2024-01-12 08:00"
end_date = "2024-01-12 12:00"
filtered_by_date_range = program_manager.filter_programs_by_date_range(start_date=start_date, end_date=end_date)
print(f"Programs filtered by date range: {filtered_by_date_range}")
