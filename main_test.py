import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='mysql',
            user='root',  # username
            password='password',  # password
            database='test_db'  # database name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

if __name__ == "__main__":
    create_connection()