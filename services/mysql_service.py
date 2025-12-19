import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "Libertad.636",
    "database": "proyecto_python"
}

def get_connection():
    return mysql.connector.connect(**config)

def fetch_all(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()