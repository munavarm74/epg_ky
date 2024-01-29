from flask import Blueprint,jsonify

from epg_ky import connection_pool_instance

channels_bp = Blueprint('channels', __name__)


@channels_bp.route('/')
@channels_bp.route('/listall')
def index():
    # Use the connection pool
    connection = connection_pool_instance.pool.connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Perform database operations
        # ...
        # execute the statement using cursor
        cursor.execute("SELECT * FROM channels")
        # fetch the results
        channels = cursor.fetchall()
        channels_list = [dict(channel) for channel in channels]
        #jsonify the results
        # pgm = ProgramManager(connection)
        # pgm.add_program(1,'test','test',30,'sport')
        cursor.close()

        # print ( program_list )
        return jsonify(channels_list)
    finally:
        cursor.close()
        connection.close()  # Return the connection to the pool

@channels_bp.route('/add')
def add():
    # Use the connection pool
    connection = connection_pool_instance.pool.connection()
    cursor = connection.cursor()
    try:
        # Perform database operations
        # ...
        # execute the statement using cursor
        cursor.execute("insert into channels ( channel_id, name , description)  values ( 3, 'movies', 'movies')")
        # fetch the results
        connection.commit()
        cursor.close()
        # print ( program_list )
        return jsonify('success')
    finally:
        cursor.close()
        connection.close()  # Return the connection to the pool