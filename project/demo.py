import os
import sqlite3
from datetime import datetime
import json

def create_db(db_name):
    if not os.path.exists(db_name):
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS person(ID INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT,
                            last_name TEXT, birthday DATE,weight REAL);""")
            print('Table created')
    else:
        print('Database exists.')

def insert_data(db_name, first_name, last_name, birthday, weight):
    if not os.path.exists(db_name):
        print("Database does not exist. Please create the database first.")
        return

    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        insert_query = "INSERT INTO person (first_name, last_name, birthday, weight) VALUES (?, ?, ?, ?);"
        values = (first_name, last_name, birthday, weight)
        cursor.execute(insert_query, values)

        print('Data inserted')

    convert_to_json('last.db', 'user_data.json')
def calculate_age(birthday_str):
    birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
    today = datetime.today().date()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def show_data(db_name):
    if not os.path.exists(db_name):
        print("Database does not exist. Please create the database first.")
        return None

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM person;")
        tables = cursor.fetchall()
        list_of_users_data = []

        for table in tables:
            table = list(table)
            table[3] = calculate_age(table[3])
            list_of_users_data.append(table)

    return list_of_users_data

def convert_to_json(db_file, json_file):
    with open(json_file, 'w') as file:
        for inner_list in show_data(db_file):
            json_data = json.dumps(inner_list, ensure_ascii=False, indent=4)
            file.write(json_data + '\n')

if __name__ == '__main__':
    #for example
    print('this is the main file.')
