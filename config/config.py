import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

env_type = os.getenv('TYPE', 'development').lower()

env_mapping = {
    'development': {
        'DB_HOST': os.getenv('DEV_DB_HOST'),
        'DB_PORT': int(os.getenv('DEV_PORT', 3306)),
        'DB_USER': os.getenv('DEV_DB_USER'),
        'DB_NAME': os.getenv('DEV_DB_NAME'),
        'DB_PASS': os.getenv('DEV_DB_PASS'),
        'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY_DEV'),
    },
    'production': {
        'DB_HOST': os.getenv('PROD_DB_HOST'),
        'DB_PORT': int(os.getenv('PROD_PORT', 3306)),
        'DB_USER': os.getenv('PROD_DB_USER'),
        'DB_NAME': os.getenv('PROD_DB_NAME'),
        'DB_PASS': os.getenv('PROD_DB_PASS'),
        'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY_PROD'),
    },
    'test': {
        'DB_HOST': os.getenv('TEST_DB_HOST'),
        'DB_PORT': int(os.getenv('TEST_PORT', 3306)),
        'DB_USER': os.getenv('TEST_DB_USER'),
        'DB_NAME': os.getenv('TEST_DB_NAME'),
        'DB_PASS': os.getenv('TEST_DB_PASS'),
        'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY_TEST'),
    }
}

config = env_mapping.get(env_type, env_mapping['development'])

def getConnection():
    try:
        connection = mysql.connector.connect(
            host=config['DB_HOST'],
            port=config['DB_PORT'],
            user=config['DB_USER'],
            password=config['DB_PASS'],
            database=config['DB_NAME']
        )
        if connection.is_connected():
            print(f"Successfully connected to the {env_type} database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL in {env_type} environment: {e}")
        raise e

def closeConnection(connection):
    if connection and connection.is_connected():
        connection.close()
        print(f"MySQL connection is closed for {env_type} environment")




# connection = get_mysql_connection()
# print(connection)


