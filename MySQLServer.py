import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (without specifying database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="+233Ghana"  # Replace with your actual password
    )

    cursor = connection.cursor()

    # Try to create database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL Server: {err}")

finally:
    # Clean up
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
