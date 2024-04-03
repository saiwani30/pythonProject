# # This is a sample Python script.
# import mysql.connector
# from flask import Flask, render_template
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# # import mysql.connector
# #
# # # Connect to MySQL
# # try:
# #     connection = mysql.connector.connect(
# #         host="localhost",  # Change this to your MySQL host
# #         user="username",   # Change this to your MySQL username
# #         password="password",  # Change this to your MySQL password
# #         database="dbname"   # Change this to your MySQL database name
# #     )
# #
# #     if connection.is_connected():
# #         print("Connected to MySQL")
# #
# #         # Perform database operations here
# #
# # except mysql.connector.Error as e:
# #     print("Error connecting to MySQL:", e)
# #
# # finally:
# #     # Close the connection
# #     if 'connection' in locals() and connection.is_connected():
# #         connection.close()
# #         print("MySQL connection closed")
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#     connect_to_database()
#     insert_values_into_table()
#     queries()
# def connect_to_database():
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="root123",
#             database="pycharm"
#         )
#
#         if connection.is_connected():
#             print("Connected to MySQL")
#             return connection
#
#     except mysql.connector.Error as e:
#         print("Error connecting to MySQL:", e)
#
#     return None
#
# def queries():
#     connection = connect_to_database()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM demo")
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#         cursor.close()
#         connection.close()
#
#
# def insert_values_into_table():
#     # Establish connection
#     connection = connect_to_database()
#     if connection:
#         try:
#             # Create cursor
#             cursor = connection.cursor()
#
#             # SQL INSERT query
#             sql_insert_query = """
#             INSERT INTO demo (iddemo,name)
#             VALUES (%s, %s)
#             """
#
#             # Example values to insert
#             values = ('101', 'aparna')
#
#             # Execute query
#             cursor.execute(sql_insert_query, values)
#
#             # Commit changes
#             connection.commit()
#             print("Values inserted successfully.")
#
#         except mysql.connector.Error as e:
#             print("Error inserting values:", e)
#
#         finally:
#             # Close cursor and connection
#             if 'cursor' in locals():
#                 cursor.close()
#             connection.close()
#
#
# # Call the function to insert values into the table
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('saee wani')
#     app.run(debug=True)
#
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="pycharm"
        )

        if connection.is_connected():
            print("Connected to MySQL")
            return connection

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

    return None

@app.route('/')
def index():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM demo")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('index.html', rows=rows)
    else:
        return "Error connecting to database"

if __name__ == '__main__':
    app.run(debug=True)


#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
