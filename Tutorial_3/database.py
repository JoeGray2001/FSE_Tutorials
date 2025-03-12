import sqlite3

with sqlite3.connect("my_database.db") as connection:
    cursor = connection.cursor()

    print("Database created and opened successfully")

    
    connection.close