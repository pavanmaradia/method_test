"""
Temperature Tracker application settings
"""

from os import getenv

DATABASE = {
    'username': getenv('db_username'),
    'password': getenv('db_password'),
    'db': getenv('db_host'),
    'db_name': getenv('db_name'),
    'db_port': getenv('db_port')
}
