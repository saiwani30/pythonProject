import mysql.connector

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",  # Change this to your MySQL host
        user="username",   # Change this to your MySQL username
        password="password",  # Change this to your MySQL password
        database="dbname"   # Change this to your MySQL database name
    )

    if connection.is_connected():
        print("Connected to MySQL")

        # Perform database operations here

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
