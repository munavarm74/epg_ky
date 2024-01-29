import mysql.connector
from dbutils.pooled_db import PooledDB

# pip install mysql-connector-python


# Database configuration
DB_HOST = "localhost"
DB_PORT = 3308
DB_USER = "munavar"
DB_PASSWORD = "Munavar2@23"
DB_NAME = "epg_schema"

# Connection pool configuration
POOL_SIZE = 5

# Singleton pattern for the connection pool
class ConnectionPool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConnectionPool, cls).__new__(cls)
            cls._instance.pool = cls._create_connection_pool()
        return cls._instance

    @staticmethod
    def _create_connection_pool():
        return PooledDB(
            creator=ConnectionPool._create_connection,
            mincached=POOL_SIZE,
            maxcached=POOL_SIZE,
            maxconnections=POOL_SIZE,
            blocking=True,
            setsession=[],
        )

    @staticmethod
    def _create_connection():
        return mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

# Create a single instance of the connection pool
connection_pool_instance = ConnectionPool()
