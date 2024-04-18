import os
import sqlite3


def create_db(db_name):
    if not os.path.exists(db_name):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS person(ID INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT,
        last_name TEXT, birthday INTEGER,weight REAL);""")
        connection.commit()
        connection.close()
        print('table created')
        return connection

    print('Database exist.')


def insert_data(db_name):
    if not os.path.exists(db_name):
        print("Database does not exist. Please create the database first.")
        return None
    else:
        # Connect to your SQLite database
        connection = sqlite3.connect(db_name)

        cursor = connection.cursor()

        insert_query = "INSERT INTO person (first_name, last_name,birthday,weight) VALUES (?, ?, ?, ?);"

        firs_name = input('Firs Name: ')
        last_name = input('Last Name: ')
        birthday = int(input('Birthday: '))
        weight = float(input('Weight: '))

        values = (firs_name, last_name, birthday, weight)

        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        print('data insert')


def show_data(db_name):
    if not os.path.exists(db_name):
        print("Database does not exist. Please create the database first.")
        return None

    # Connect to your SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Execute a query to get a list of tables
    cursor.execute("SELECT * FROM person;")

    # Fetch all the results
    tables = cursor.fetchall()

    # Print the list of tables
    for table in tables:
        print(table)

    cursor.close()
    conn.close()
