import click
import mysql.connector
from mysql.connector import pooling
from contextlib import contextmanager
from flask import current_app, g
from flask.cli import with_appcontext

def init_db():
    """
    Initialize the database connection pool.
    """
    db_params = current_app.config['DATABASE']
    g.db_pool = pooling.MySQLConnectionPool(
        pool_name="mysql_pool",
        pool_size=db_params['pool_size'],
        **db_params['connection_args']
    )

@contextmanager
def get_db():
    """
    Get a database connection from the pool.
    """
    connection = g.db_pool.get_connection()
    try:
        yield connection
    finally:
        connection.close()

def close_db():
    """
    Close the database connection pool.
    """
    if hasattr(g, 'db_pool'):
        g.db_pool.close()

def init_app(app):
    """
    Initialize the app to work with the database.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    CLI command to initialize the database connection pool.
    """
    init_db()
    click.echo('Initialized the database connection pool.')
