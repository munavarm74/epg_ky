import mysql.connector

# Replace with your MySQL connection details
mysql_config = {
    'host': 'localhost',
    'port':'3308',
    'user': 'munavar',
    'password': '', #replace with correct password
    'database': 'epg_schema'
}

try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(**mysql_config)

    if connection.is_connected():
        print(f"Connected to MySQL Server: {connection.get_server_info()}")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example: Execute a simple query
        cursor.execute("SELECT * FROM channels")
        result = cursor.fetchall()
        print("Query Result:", result)

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")
