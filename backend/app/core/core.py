import os
from mysql.connector import connect, Error
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except Error as e:
        print("Error al conectar a MySQL:", e)
        return None