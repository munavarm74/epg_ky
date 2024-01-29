from flask import Blueprint,jsonify

from epg_ky import connection_pool_instance
from epg_ky.programmgmt import ProgramManager

programs_bp = Blueprint('programs', __name__)

@programs_bp.route('/listall')
def index():
    # Use the connection pool
    connection = connection_pool_instance.pool.connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Perform database operations
        # ...
        # execute the statement using cursor
        cursor.execute("SELECT * FROM programs where program_id > 10")
        # fetch the results
        programs = cursor.fetchall()
        program_list = [dict(program) for program in programs]
        #jsonify the results
        # pgm = ProgramManager(connection)
        # pgm.add_program(1,'test','test',30,'sport')
        cursor.close()

        print ( program_list )
        return jsonify(program_list)
    finally:
        cursor.close()
        connection.close()  # Return the connection to the pool

from flask import request

@programs_bp.route('/add', methods=['POST'])
def add():
    # Use the connection pool
    connection = connection_pool_instance.pool.connection()
    cursor = connection.cursor()
    try:
        # Get data from the form
        title = request.form.get('title')
        description = request.form.get('description')
        duration = int(request.form.get('duration'))
        genre = request.form.get('genre')
        channel_id = request.form.get('channelid')

        # Use ProgramManager to add the program
        pgm = ProgramManager(connection)
        pgm.add_program(channel_id=channel_id, name=title, duration=duration, genre=genre, description=description)

        # cursor.execute("INSERT INTO programs (title, description, duration, genre) VALUES (%s, %s, %s, %s)", (title, description, duration, genre))
        # connection.commit()

        return 'Added successfully'
    except Exception as e:
        return f'Error: {str(e)}'
    finally:
        cursor.close()
        connection.close()  # Return the connection to the pool

#
@programs_bp.route('/update',methods=['POST'])
def update():
    # Use the connection pool
    connection = connection_pool_instance.pool.connection()
    cursor = connection.cursor()
    try:
        # Perform database operations
        # ...
        #jsonify the results
        title = request.form.get('title')
        description = request.form.get('description')
        duration = int(request.form.get('duration'))
        genre = request.form.get('genre')
        channel_id = request.form.get('channel_id')
        program_id = request.form.get('program_id')

        pgm = ProgramManager(connection)
        pgm.update_program(program_id,title,description,duration,genre,channel_id)
        return 'success'
    finally:
        cursor.close()
        connection.close()  # Return the connection to the pool

# @programs_bp.route('/delete')
# def delete():
#     # Use the connection pool
#     connection = connection_pool_instance.pool.connection()
#     cursor = connection.cursor()
#     try:
#         # Perform database operations
#         # ...
#         # execute the statement using cursor
#         cursor.execute("SELECT * FROM programs")
#         # fetch the results
#         results = cursor.fetchall()
#         #jsonify the results
#         pgm = ProgramManager(connection)
#         pgm.add_program(1,'test','test',30,'sport')
#         return results
#     finally:
#         cursor.close()
#         connection.close()  # Return the connection to the pool
#
@programs_bp.route('/<int:program_id>')
def get_program_by_id(program_id):
        # Use a SQL SELECT statement to fetch program data from the database
        query = "SELECT * FROM programs WHERE program_id = %s"
        connection = connection_pool_instance.pool.connection()
        cursor = connection.cursor(dictionary=True)  # Set dictionary=True to return results as dictionaries
        try:
            cursor.execute(query, (program_id,))
            program_data = cursor.fetchone()

            if program_data:
                return program_data
            else:
                return None
        finally:
            cursor.close()


@programs_bp.route('/delete/<int:program_id>', methods=['DELETE'])
def delete(program_id):
    # Use a SQL DELETE statement to remove the program from the database
    query = "DELETE FROM programs WHERE program_id = %s"

    try:
        connection = connection_pool_instance.pool.connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (program_id,))
        connection.commit()

        return jsonify({'message': 'Program deleted successfully'}), 200

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error deleting program with ID {program_id}: {e}")
        return jsonify({'error': 'Failed to delete program'}), 500